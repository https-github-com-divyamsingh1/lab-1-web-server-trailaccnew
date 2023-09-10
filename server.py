# Import the socket module
from socket import *
import sys  # In order to terminate the program

# Create a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare the server socket
serverPort = 8080  # You can change this port number if needed
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)

print('The server is ready to receive requests...')

while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()

    try:
        # Receive the request from the client
        message = connectionSocket.recv(1024).decode()

        # Parse the request to get the filename
        filename = message.split()[1]

        # Try to open the requested file
        try:
            f = open(filename[1:], 'rb')  # Open in binary mode
            outputdata = f.read()
            f.close()

            # Send the HTTP response header
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i:i+1])

        except FileNotFoundError:
            # Send a "404 Not Found" response if the file is not found
            connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
            connectionSocket.send('<html><head></head><body><h1>404 Not Found</h1></body></html>'.encode())

        # Close the client socket
        connectionSocket.close()

    except KeyboardInterrupt:
        # Handle Ctrl+C to gracefully exit the server
        serverSocket.close()
        sys.exit()

# Terminate the program
serverSocket.close()
