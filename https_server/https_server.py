#!/usr/bin/env python

"""
**FIGURE OUT WHAT TO PUT HERE**
Docstrings??
Sources-

This application was written by Al Robison.
Last Modified:  2023/01/20
"""

from https.server import HTTPServer, BaseHTTPRequestHandler

# Define the host IP and port number
# An IP of 0.0.0.0 will broadcast on all local NICs
# 443 is the standard port for HTTPS
host_addr = "0.0.0.0"
port = 443

#
class HttpsServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(bytes("Hello!", "utf-8"))

server = HTTPServer((host_addr, port), HttpsServer)

try:
	server.serve_forever()
except KeyboardInterrupt:
	server.server_close()

print()
print("Server connection terminated.")
