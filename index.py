import socket

# Define the socket host and port 
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000 

# Creating the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is the IPv4 Address Family and SOCK_STREAM basically TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on Port %s ...' % SERVER_PORT)


while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)
    
    fin = open("pages/index.html")
    content = fin.read()
    fin.close()

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n %s' %content
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()
