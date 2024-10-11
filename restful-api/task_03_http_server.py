#!/usr/bin/python3
import http.server
import json


class Server(http.server.BaseHTTPRequestHandler):
    """
    Server to manage GET requests.
    Handles the following endpoints:
    - '/' : returns a greeting message.
    - '/data' : returns a sample JSON response.
    - '/status' : returns 'OK' to check the status of the API.
    For any other undefined endpoints, it returns a 404 error.
    """

    def do_GET(self):
        """
        Handle GET requests.
        Responds based on the requested path:
        - For '/' : returns a plain text greeting message.
        - For '/data' : returns a JSON object.
        - For '/status' : returns a plain text 'OK'.
        - For any other path, returns a 404 Not Found response.
        """
        if self.path == '/':
            # Root endpoint: returns a simple greeting message
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == '/data':
            # /data endpoint: returns a JSON response
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.wfile.write(json.dumps(response).encode())
        
        elif self.path == '/status':
            # /status endpoint: returns "OK"
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        
        else:
            # Undefined endpoints: return a 404 Not Found
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found: Endpoint not found")


# Configure the server
server_address = ('', 8000)  # Listen on port 8000
httpd = http.server.HTTPServer(server_address, Server)

# Start the server
httpd.serve_forever()
