import socket
class TCPServer:
    def __init__(self, host="127.0.0.1", port=8000):
        self.host = host
        self.port = port

    def start(self):
        # Creating the socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is the IPv4 Address Family and SOCK_STREAM basically TCP
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((SERVER_HOST, SERVER_PORT))
        self.server_socket.listen(1)
        print('Listening on Port %s ...' % SERVER_PORT)
        

        while True:
            # Wait for client connections
            client_connection, client_address = self.server_socket.accept()

            # Get the client request and only read 1024 byte
            request = client_connection.recv(1024).decode()
            print(request)
            
            response = self.handleRequest(request)
            fin = open("pages/index.html")
            content = fin.read()

            fin.close()
            # Send HTTP response
            response = 'HTTP/1.0 200 OK\n\n %s' %content
            client_connection.sendall(response.encode())
            client_connection.close()

    def parse_request(self, req):
        splitItems = req.split("\r\n")
        
    def handleRequest(self, req):
        import request
        reqClass = request.Request(req)
        print(reqClass.request_method)

    def close(self):
        self.server_socket.close()
        print("Socket close ...")


if __name__ == "__main__":
    # Define the socket host and port 
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8000 
    
    server = TCPServer()
    server.start()

