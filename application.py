import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, 'utils' )
sys.path.append( mymodule_dir )
from functions import get_environ_vars

"""
The application interface is a callable object

It accepts two arguments:
    * environ points to a dictionary containing CGI like environment
    variables which is populated by the server for each received request from the client
    * start_response is a callback function supplied by the server
    which takes the HTTP status and headers as arguments
"""
def application(environ, start_response):
    response = Response(environ)
    
    start_response(response.status, response.response_headers)
    return response.get_body()

# this is my response object that consists of 
# status, response headers and a function 
# returning a response body according to the request method
class Response:
    def __init__(self, environ):
        self.environ = environ

    status = '200 OK'

    response_headers = [('Content-type', 'text/plain')]
    
    def get_body(self):
        # body = bytes(get_environ_vars(self.environ), "utf-8")
        body = bytes(request_method_handler(self.environ), "utf-8")
        return [body] 

def request_method_handler(environ):
    res = "empty response"
    if(environ["REQUEST_METHOD"] == "GET"):
        res = str(environ["QUERY_STRING"])
        if len(res) == 0:
            res = "no query"
    elif(environ["REQUEST_METHOD"] == "POST"):
        res = str(environ["wsgi.input"].read(int(environ["CONTENT_LENGTH"])))

    return res
