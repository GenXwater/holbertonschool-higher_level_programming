#!/usr/bin/env python3


import http.server
import json


class RequestHandler(http.server.BaseHTTPRequestHandler):
    """
    RequestHandler is a custom handler to manage GET requests.
    It handles the following endpoints:
    - '/' : returns a simple greeting message.
    - '/data' : returns a sample JSON response.
    - '/status' : returns 'OK' to check the status of the API.
    For any other undefined endpoints, it returns a 404 Not Found error.
    """

    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response = {"name": "John", "age": 30, "city": "New York"}

            self.wfile.write(json.dumps(response).encode())

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found: Endpoint not found")


server_address = ("", 8000)
httpd = http.server.HTTPServer(server_address, RequestHandler)

httpd.serve_forever()
