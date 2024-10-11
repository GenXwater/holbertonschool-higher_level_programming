#!/usr/bin/env python3


import http.server
import json


PORT = 8000
Handler = http.server.BaseHTTPRequestHandler

class Server(Handler):
    """
    CustomRequestHandler is a class to handle incoming GET requests
    and respond based on the requested endpoint.
    """

    def do_GET(self):
        """
        Handle GET requests and respond based on the requested path.
        - '/' : Returns a plain text message.
        - '/data' : Returns a JSON object with user data.
        - '/status' : Returns 'OK' in plain text.
        - '/info' : Returns a JSON object with API version and description.
        If the path is not defined, a 404 Not Found response is returned.
        """

        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
                }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found: Endpoint not found")


if __name__ == "__main__":
    with http.server.HTTPServer(("", PORT), Server) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
