from pyModbusTCP.client import ModbusClient
import sys


Server_Host = "192.168.117.1"
Server_Port = 502
unitID1 = 103
unitID2 = 120
unitID3 = 1

reading = 5

while(reading > 0):
	print("Starting")
	print("Opened yeiiiii")
	reading = reading -1

#sys.exit(0)

c = ModbusClient()	
c.host(Server_Host)
c.port(Server_Port)
c.unit_id(unitID1)

if not c.is_open():
  if not c.open():
    print("unable to connect to "+ SERVER_HOST + ":" + str(SERVER_PORT))
  else:
      print("Opened")

while(True):
	regs = c.read_holding_registers(40070, 60)
	regs1 = c.read_holding_registers(40130, 60)
	
	if regs:
    		print(str(regs))
    		print(str(regs1))
	else:
    		print(str(regs) + "  read error")

