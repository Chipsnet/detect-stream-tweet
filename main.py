import http.server
import socketserver
import json

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()

with socketserver.TCPServer(("", 80), MyHandler) as httpd:
    httpd.serve_forever()