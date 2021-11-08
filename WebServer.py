from socket import *
import sys # In order to terminate the program

# http://localhost:5050/HelloWorld.html

# Prepare a server socket
#SERVER_HOST = "localhost"
SERVER_HOST = "127.0.0.1"	# Host address; localhost
SERVER_PORT = 5050			# Listening at

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((SERVER_HOST, SERVER_PORT)) # Bind the socket to address/port
serverSocket.listen(1)

while True:
	print('Ready to serve...')
	'''
		clientSocket is a new socket object usable to 
			send and receive data on the connection
		clientAddr is the address bound to the socket on
			the other end of the connection
	'''
	clientSocket, clientAddr = serverSocket.accept() #TODO
	
	try:
		request = clientSocket.recv(1024).decode()
		print(request)

		# Obtain requested filename from 
		headers = request.split('\n')
		print(headers)
		filename = headers[0].split()[1]

		# if requesting HelloWorld.html
		if "HelloWorld.html" in request:
			# return content of HelloWorld.html
			file = open("HelloWorld.html")
			htmlContent = file.read()
			file.close()
			response = 'HTTP/1.0 200 OK\n\n' + htmlContent
		else:
			# return error 404
			response = 'HTTP/1.0 200 OK\n\nError 404'
		
		clientSocket.sendall(response.encode())
		clientSocket.close()

	except IOError:
		# return error 404
		response = 'HTTP/1.0 200 OK\n\nError 404'
		client_connection.sendall(response.encode())
		client_connection.close()

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data
