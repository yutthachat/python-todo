class Request:
    def __init__(self, req):
        self.rawRequest = req
        splitItems = req.split("\r\n")
        self._request_method = splitItems[0].split(" ")[0]
        
        
    @property
    def request_method(self):
        return self._request_method
