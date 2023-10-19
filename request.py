"""
A valid Request structure

[verb] [dir] [http/version]\r\n
[Headers_Name]:[Headers_values]
[Blank Space]
[Body]
"""

class Request:
    def __init__(self, req):
        if (req is None or len(req) == 0):
            raise ValueError("A valid Request is not provided. Request: %s" %req)
        self.rawRequest = req
        split_lines = req.split("\r\n")
        if (len(split_lines) == 0):
            raise ValueError("Invalid Request. Unable to split the request.")

        # Getting the first first_line
        first_line = split_lines[0].split(" ")
        if (len(first_line) != 3):
            raise ValueError("Invalid Request. The first line is not formatted correctly. First Line: %s" %first_line)
        
        if (first_line[0].upper() not in self.valid_method):
            raise ValueError("Invalid Https Method. Method: %s" %first_line)
        
        self._http_method = first_line[0]
        self._http_request_directory = first_line[1]
        self._http_version = first_line[2]

        #        print(self._http_method, self._http_version, self._http_request_directory)
        # print(split_lines[1:])
        
        self._http_headers = {}

        if ("" in split_lines[1:]):
            empty_line_index = split_lines[1:].index("")
            for header in split_lines[1:empty_line_index-1]:
                current_header_split = header.split(":")
                self._http_headers[current_header_split[0]] = ":".join(current_header_split[1:]).strip()
            second_empty_line_index = split_lines[empty_line_index:].index("")
            self._http_body = "\r\n".join(split_lines[second_empty_line_index:-1])
        
    @property
    def http_method(self):
        return self._http_method

    @property
    def http_request_directory(self):
        return self._http_request_directory
    
    @http_request_directory.setter
    def http_request_directory(self, val):
        self._http_request_directory = val


    @property
    def http_version(self):
        return self._http_version

    @property
    def http_body(self):
        return self._http_body

    @property
    def http_headers(self):
        return self._http_headers

    @property
    def valid_method(self):
        return ["GET", "POST", "DELETE", "PUT", "PATCH"]

class Response:
    def __init__(self) -> None:
        self._status_code = 200
        self._status_text = "ok"
        self._http_version = "http/1.1"
        self._http_body = ""

    def format_to_send(self):
        return f"{self.http_version} {self.status_code} {self.status_text}\r\n\r\n{self.http_body}"

    @property
    def status_code(self):
        return self._status_code
    
    @status_code.setter
    def status_code(self, val):
        self._status_code = val

    @property
    def status_text(self):
        return self._status_text

    @status_text.setter
    def status_text(self, val):
        self._status_text = val

    @property
    def http_version(self):
        return self._http_version

    @http_version.setter
    def http_version(self, val):
        self.http_version = val

    @property
    def http_body(self):
        return self._http_body
    
    @http_body.setter
    def http_body(self, val):
        self._http_body = val


if __name__ == "__main__":
    req = Request("")

