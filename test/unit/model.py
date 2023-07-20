import json

class HTTPResponse:
    def __init__(self, status_code=200, text=None):
        self.status_code = status_code
        self.text = text
        
    def get_text(self):
        return self.text
    
    def get_status_code(self):
        return self.status_code