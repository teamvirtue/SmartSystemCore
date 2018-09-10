#!/usr/bin/python

import sys
import os.path
import serial
#default config
serialPort = "/dev/ttymxc2"
serialBaud = 19200

debug = 0
def enableDebugging():
    global debug
    debug = 1

def printDebug(text):
    if debug is 1:
        print '\033[1;33m',"DEBUG: ", text, '\033[0m'

def printError(text):
    print '\033[1;31m', "ERROR: ", text, '\033[0m'

def showMenuAndDie():
    print "usage: "
    print "-group [group_num] -on"
    print "-group [group_num] -off"
    print "-group [group_num] -fade [time_in_ms]"
    print "-group [group_num] -intensity [intensity in promille]"
    print "-broadcast [same as above]"
    sys.exit(1)

# serial stuff
# direction = 1 == write, 0 == read
def setSerialDDR(direction):
    with open('/sys/class/gpio/gpio146/value', 'w') as io_dir:
        io_dir.write(direction)

def SerialInit():
    printDebug("in SerialInit")
    #actum value specific code, set kernel stuff to prepare the rs485 bus
    if not os.path.isdir('/sys/class/gpio/gpio146'):
        printDebug("exporting serial bus in kernel")
        with open('/sys/class/gpio/export', 'w') as io_bus:
            io_bus.write('146')

    with open('/sys/class/gpio/gpio146/direction', 'w') as activate_bus:
        activate_bus.write('out')

    global daliSerial
    global serialPort
    global serialBaud
    # as according to http://www.foxtron.cz/images/ke_stazeni/pexprotocol.pdf
    daliSerial = serial.Serial(port=serialPort, baudrate=serialBaud, parity=serial.PARITY_EVEN, bytesize=8, stopbits=1, timeout=0.05)
    if daliSerial.isOpen() is False:
        daliSerial.open()

def SerialWrite(data):
    # RS485 is not async, set to write
    setSerialDDR('1')
    printDebug("in SerialWrite")
    printDebug("witing:")
    printDebug(data)
    daliSerial.write(data)
    daliSerial.flush()

def SerialRead(count):
    # RS485 is not async, set to read
    setSerialDDR('0')
    printDebug("in SerialRead")
    return serialPort.read(count)

# dali modes implementation
daliModeNames = ["-on", "-off", "-fade", "-intensity"]
daliModes = {}
daliModeArgument = None
daliIntensity = "0"
daliGroup = -1
daliSerial = None
daliFadeEnabled = False #becomes true in the fade functions, used for intensity command
daliFadeValue = "000"
daliData = [0x01, 0x66, 0x00, 0x00, 0x00, 0x02, 0x30, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x2F, 0x17, 0x03]

def DaliSetGroup(data, group, code):
    printDebug("In DaliSetGroup")
    if group < 0:
        for i in range(0, 10):
            data[7 + i] = code
    else:
        data[7 + int(group)] = code

def DaliGetData():
    printDebug("In getDebug")
    return daliData[:]

#argument is expected to be a string int between 0 and 999
def DaliSetArgument(data, argument):
    printDebug("In setArgument")
    if int(argument) < 0 or int(argument) > 999:
        printError("Argument out of range [0-999]")
    else:
        #prepend with zeroes if needed
        while len(argument) < 3:
            argument = "0" + argument
        #from decimal to ascii
        for i in range(0, len(argument)):
            data[2 + i] = int(argument[i]) + 0x30

def DaliFuncOff():
    printDebug("in DaliFuncOff")
    global daliIntensity
    daliIntensity = "000"
    DaliFuncIntensity()
def DaliFuncOn():
    printDebug("in DaliFuncOn")
    global daliIntensity
    daliIntensity = "999"
    DaliFuncIntensity()

def DaliFuncFade():
    printDebug("in DaliFuncFadeIn")
    printDebug("dali intensity: " + daliIntensity)
    data = DaliGetData()
    DaliSetGroup(data, daliGroup, 0x38) #set level at next fade
    DaliSetArgument(data, daliIntensity)
    SerialWrite(data)
    data = DaliGetData()
    DaliSetGroup(data, daliGroup, 0x32) #set level at next fade
    DaliSetArgument(data, daliFadeValue) #value measured in time
    SerialWrite(data)

def DaliFuncIntensity():
    printDebug("in DaliFuncIntensity")
    if daliFadeEnabled:
        printDebug("early exit DaliFuncIntensity, Fade is used, ignore intensity function since it is handled differently")
        return
    global daliIntensity
    data = DaliGetData()
    DaliSetGroup(data, daliGroup, 0x33) #direct set code
    DaliSetArgument(data, daliIntensity) #brightness
    SerialWrite(data)

daliModes["-on"]  = DaliFuncOn
daliModes["-off"] = DaliFuncOff
daliModes["-fade"]    = DaliFuncFade
daliModes["-intensity"] = DaliFuncIntensity


def main():
    DaliGetData()
    groupIndex = -1
    broadcastIndex = -1
    intensityIndex = -1
    fadeIndex = -1
    global daliGroup
    global daliIntensity
    global daliFadeEnabled
    global daliFadeValue

    #optional enable debugging
    try:
        sys.argv.index("-debug")
        enableDebugging()
    except:
        pass

    printDebug("Debugging enabled")

    #choosing between broadcasting and specific group addressing
    try:
        groupIndex = sys.argv.index("-group")
        daliGroup = sys.argv[groupIndex + 1]
    except:
        pass

    try:
        broadcastIndex = sys.argv.index("-broadcast")
    except:
        pass

    try:
        intensityIndex = sys.argv.index("-intensity")
        daliIntensity = sys.argv[intensityIndex+1]
        if int(daliIntensity) < 0 or int(daliIntensity) > 999:
            printError("dali intensity out of range[0-999]")
            sys.exit(1)
    except:
        pass

    try:
        fadeIndex = sys.argv.index("-fade")
        daliFadeValue = sys.argv[fadeIndex + 1]
        daliFadeEnabled = True
    except:
        pass

    if groupIndex < 0 and broadcastIndex < 0:
        showMenuAndDie()

    if groupIndex >= 0 and daliGroup < 0:
        showMenuAndDie()

    #choosing the mode
    SerialInit()
    done = 0
    for i in range (0, len(daliModeNames)):
        try:
            index = sys.argv.index(daliModeNames[i])
            try:
                global daliModeArgument
                daliModeArgument = sys.argv[index + 1]
            except IndexError:
                pass
            daliModes[daliModeNames[i]]()
            done = 1
        except ValueError:
            pass

    if not done:
        printDebug("show menu at end of program")
        showMenuAndDie()




main()
