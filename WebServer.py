#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#TODO

while True:
	# Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = #TODO
	try:
		message = #TODO
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = #TODO

		# Send one HTTP header line into socket
		#TODO

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
		connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())

		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		#TODO

		 #Close client socket
		 #TODO

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data 