from rest_framework.response import Response

class StatusControl:
    def __init__(self, statusCode: int, menStatus: str, body):
        self.statusCode: int = statusCode
        self.menStatus: str = menStatus
        self.body = body

    def __str__(self):
        return self
    
    def to_response(self):
        return Response(self.to_json(), status=self.statusCode, content_type='application/json; charset=utf-8')

    def to_json(self):
        return {
            "statusCode": self.statusCode,
            "menStatus": self.menStatus,
            "body": self.body
        }
    
    def ok_body(self, body):
        self.statusCode = 200
        self.menStatus = 'OK'
        self.body = body
        return self
    
    def error_body(self, body):
        self.statusCode = 500
        self.menStatus = 'ERROR'
        self.body = body
        return self
    
    def ok_message(self, message):
        self.statusCode = 200
        self.menStatus = message
        self.body = None
        return self
    
    def error_message(self, message):
        self.statusCode = 500
        self.menStatus = message
        self.body = None
        return self