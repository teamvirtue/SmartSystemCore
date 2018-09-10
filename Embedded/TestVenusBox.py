from pyModbusTCP.client import ModbusClient
import sys


Server_Host = "192.168.1.125"
Server_Port = 502
unitID1 = 245
unitID2 = 243
reading = 100

while(reading > 0):
	print("Starting")
	print("Opened yeiiiii")
	reading = reading -1

sys.exit(0)

c = ModbusClient()
c.host(Server_Host)
c.port(Server_Port)
c.unit_id(unitID2)

if not c.is_open():
  if not c.open():
    print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
  else:
      print("Opened")

while(True):
	regs = c.read_holding_registers(259, 1)
	
	if regs:
    		print(str(regs))
	else:
    		print(str(regs) + "  read error")

#this script was created to test the communication addresses and protocol with VenusBox. 
