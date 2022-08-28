import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, 'utils' )
sys.path.append( mymodule_dir )
from functions import get_environ_vars

def application(environ, start_response):
    response = Response(environ)

    start_response(response.status, response.response_headers)
    return response.get_output()
class Response:
    def __init__(self, environ):
        self.environ = environ

    status = '200 OK'

    response_headers = [('Content-type', 'text/plain')]
    
    def get_output(self):
        output = bytes(get_environ_vars(self.environ), "utf-8")
        return [output] 
