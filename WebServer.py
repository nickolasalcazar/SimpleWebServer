from socket import *
import sys # In order to terminate the program

# http://localhost:5050/HelloWorld.html

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
#SERVER_HOST = "localhost"
SERVER_HOST = "127.0.0.1"	# Host address; localhost
SERVER_PORT = 5050			# Listening at

# Not sure how this line works exactly
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Bind the socket to address
# A pair (host, port) is used for the AF_INET address family
serverSocket.bind((SERVER_HOST, SERVER_PORT))

serverSocket.listen(1)

while True:
	# Establish the connection
	print('Ready to serve...')

	'''
		clientSocket is a new socket object usable to 
			send and receive data on the connection
		clientAddr is the address bound to the socket on
			the other end of the connection
	'''
	clientSocket, clientAddr = serverSocket.accept() #TODO
	
	try:
		message = "HelloWorld.html"
		#filename = message.split()[1]
		#f = open(filename[1:])
		f = open(message)
		#outputdata = #TODO
		
		# Client request
		#request = clientSocket.recv(1024).decode()

		# Send one HTTP header line into socket
		clientSocket.send('HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n'.encode())
		clientSocket.send("""<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Hello World</title></head><body><p>Hello world!</p></body></html>""".encode())


		'''
		# Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			clientSocket.send(outputdata[i].encode())
		clientSocket.send("\r\n".encode())
		'''

		#response = 'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n<html><body>Hello World</body></html>'
		#clientSocket.sendall(response.encode())
		clientSocket.close()

	except IOError:
		print('except IOError')
		# Send response message for file not found
		#TODO

		# Close client socket
		#TODO

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data 