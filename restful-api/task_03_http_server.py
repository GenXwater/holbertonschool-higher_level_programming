import http.server
import json


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

server_address = ('', 8000)
httpd = http.server.HTTPServer(server_address, RequestHandler)

httpd.serve_forever()
