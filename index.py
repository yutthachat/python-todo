import socket
import request


class TCPServer:
    def __init__(self, host="127.0.0.1", port=8000, dir="./pages/"):
        self.host = host
        self.port = port
        self.dir = dir

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
            #print(f"request: {request}")
            response = self.handleRequest(request)
            
            # Send HTTP response
            client_connection.sendall(response.format_to_send().encode())
            client_connection.close()

    def handleRequest(self, req_string):
        req = request.Request(req_string)
        res = request.Response()

        if (req.http_method == "GET"):
            self.handle_get_request(req, res)
        elif (req.http_method == "POST"):
            self.handle_post_request(req, res)
        elif (req.http_method == "PUT"):
            self.handle_post_request(req, res)
        elif (req.http_method == "DELETE"):
            self.handle_post_request(req, res)
        
        return res
    
    def handle_get_request(self, req, res):
        print("Handling Get Request")

        # prevent the user accessing other directory than the intented one
        if (".." in req.http_request_directory or "~" in req.http_request_directory): 
            res.http_code = "400"
            res.http_status = "Bad Request"
            return
       
        #print(req.http_request_directory.split('/'))
        # The request uri does not have a file extension, so we are going
        # to get the html file
        dir_path = req.http_request_directory.split('/')
        if (dir_path[-1] == ''):
            req.http_request_directory = req.http_request_directory + "index.html"
        elif ('.' not in dir_path[-1]):
            req.http_request_directory = req.http_request_directory + ".html"

        try:
            fin = open(self.dir + req.http_request_directory)
            content = fin.read()
            res.http_body = content
            fin.close()
        except FileNotFoundError:
            res.http_code = 404
            res.http_status = "File not found"
            res.http_body = "<h1>File not found<h1>"
        return

    def handle_post_request(self, req, res):
        print("Handling post Request")
        print(req.http_body)
        if (req.http_request_directory == "/create"):
            item = self.string_to_object(req.http_body)
            print("inside the create dire")
            if ("f_item" in item):
                db = open("./db.txt", "a")
                db.write(item["f_item"])
                db.close()
                res.http_body = f"<h2>Successfully added {item['f_item']}</h2>"
                return res
            res.http_code = 400
            res.http_status = "Bad Request"
            res.http_body = f"<h2>Unable to add the item<h2>"

    def string_to_object(self, val):
        all_items = val.split('\r\n')
        obj = {}

        for item in all_items:
            if ("=" in item):
                equal_index = item.index("=")
                obj[item[:equal_index]] = item[equal_index + 1:]

        return obj

    def handle_put_request(self, req, res):
        print("Handling put Request")

    def handle_delete_request(self, req, res):
        print("Handling delete Request")

    def close(self):
        self.server_socket.close()
        print("Socket close ...")

# Run the program
if __name__ == "__main__":
    # Define the socket host and port 
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8000 
    WEB_DIRECTORY = "./pages/"
    server = TCPServer()
    server.start()

