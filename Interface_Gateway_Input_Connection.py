import sys
import socket
import time

def connect(ipAddress, port, clientName, simName, simVersion, coreCodeVersion):

	#Method to create a TCP connection to a simsig server.
	#Returns the connection if succesfull
	#Or returns the error message if not

	#Define the basics of our connection
	TCP_IP = ipAddress
	TCP_PORT = port
	BUFFER_SIZE = 1024
	connectionMessage = "iA" + clientName + "C" + simVersion + "/" + coreCodeVersion + "/" + simName + "|"

	#Open up the connection
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(connectionMessage)

	#Create a variable to hold our connection state message

	messageOnServerConnect = "Connection Failed - Host did not accept"

	for x in range(0,3):
		print ("...")
		data = s.recv(BUFFER_SIZE)
		if (data[0:2] == "iG"):
			messageOnServerConnect = "Connection Failed Server Not Running Same Simulation or Version"
			s.close()
		elif (data[0:2] == "iF"):
			messageOnServerConnect = "Connection established"
			break
		elif (x == 3):
			s.close()

	#return the connection socket and the connection message
	return s, messageOnServerConnect
