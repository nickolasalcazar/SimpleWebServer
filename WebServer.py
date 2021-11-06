#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
#SERVER_HOST = "localhost"
SERVER_HOST = "127.0.0.1"	# Host address; localhost
SERVER_PORT = 8080			# Listening at

# Not sure how this line works exactly
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to address
# A pair (host, port) is used for the AF_INET address family
serverSocket.bind((SERVER_HOST, SERVER_PORT))

serverSocket.listen(1)

while True:
	# Establish the connection
	print('Ready to serve...')
	clientSocket, clientAddr = serverSocket.accept() #TODO
	
	try:
		message = "HelloWorld.html"
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = #TODO

		# Send one HTTP header line into socket
		#TODO

		# Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			clientSocket.send(outputdata[i].encode())
		clientSocket.send("\r\n".encode())

		connectionSocket.close()
	except IOError:
		# Send response message for file not found
		#TODO

		# Close client socket
		#TODO

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data 