from Phidget22.Phidget import *
from Phidget22.Net import *
from Phidget22.Devices.RFID import *

def onTag(self, tag, protocol):
	print("Tag: " + str(tag))
	print("Protocol: " + RFIDProtocol.getName(protocol) + " from script 1")
	print("----------")

def onTagLost(self, tag, protocol):
	print("Tag: " + str(tag))
	print("Protocol: " + RFIDProtocol.getName(protocol) + " from script 1")
	print("----------")

def main():
	Net.addServer("PHIDGET", "localhost", 5661, "", 0);

	rfid0 = RFID()

	rfid0.setIsRemote(True)

	rfid0.setOnTagHandler(onTag)
	rfid0.setOnTagLostHandler(onTagLost)

	rfid0.openWaitForAttachment(20000)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	rfid0.close()

main()
