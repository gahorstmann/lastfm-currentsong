import json

class HTTPResponse:
    def __init__(self, status_code=200, json=None):
        self.status_code = status_code
        self.json = json
        
    def json(self):
        return json.loads(self.text)