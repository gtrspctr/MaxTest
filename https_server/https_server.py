#!/usr/bin/env python

"""
**FIGURE OUT WHAT TO PUT HERE**
Docstrings??
Sources-

This application was written by Al Robison.
Last Modified:  2023/01/20
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from os import path

# Define the host IP and port number
# An IP of 0.0.0.0 will broadcast on all local NICs
# 443 is the standard port for HTTPS
host_addr = "0.0.0.0"
port = 443

# Get HTML content
server_path = path.dirname(__file__)
html_source = path.join(server_path, "main_page.html")
print("Path: " + server_path)
print("HTML: " + html_source)

#
class AlsServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		# Website body
		# self.wfile.write(bytes("", "utf-8"))
		self.wfile.write(bytes(html, "utf-8"))

try:
	with open(html_source, "r") as reader:
		html = reader.read()
except FileNotFoundError as fnfe:
	print("HTML source file is not present")
	exit(1)
except:
	print("Something went wrong.")
	exit(1)

server = HTTPServer((host_addr, port), AlsServer)
try:
	server.serve_forever()
except KeyboardInterrupt:
	server.server_close()

print()
print("Server connection terminated.")
