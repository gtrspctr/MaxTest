#!/usr/bin/env python

"""
**FIGURE OUT WHAT TO PUT HERE**
Docstrings??
Sources-

This application was written by Al Robison.
Last Modified:  2023/01/20
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import os

# Define the host IP and port number
# An IP of 0.0.0.0 will broadcast on all local NICs
# 443 is the standard port for HTTPS
host_addr = "0.0.0.0"
port = 443

# Define filepaths
server_path = os.path.dirname(__file__)		# Main directory
html_source = os.path.join(server_path,
						"index.html")		# HTML content
json_source = os.path.join(server_path,
						"todo_list.json")	# JSON content
file_repo = os.path.join(server_path,
					  "file_repository")	# Repository for file uploads
#cert_repo = os.path.abspath(os.path.join(server_path,
#					  					 os.pardir,
#					 					 "cert_repository"))	# Repository for certificates
cert_file = os.path.abspath("/etc/letsencrypt/live/alrobison.com/fullchain.pem")
key_file = os.path.abspath("/etc/letsencrypt/live/alrobison.com/privkey.pem")

# This class is the request handler.
# do_GET sends a response of 200 when
# successful. It also specifies that the
# content type is html, and displays html
# content to the browser.
class AlsRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		# Website body
		# self.wfile.write(bytes("", "utf-8"))
		self.wfile.write(bytes(html, "utf-8"))

	def do_POST(self):
		self.send_response(200)
		self.send_header("Content-type", "application/json")
		self.end_headers()
		self.wfile.write(bytes(json, "utf-8"))

def readFiles(source, output):
	try:
		with open(source, "r") as reader:
			output = reader.read()
		return output
	except FileNotFoundError as fnfe:
		print("HTML source file is not present")
		exit(1)
	except:
		print("Something went wrong.")
		exit(1)

html = ""
json = ""
html = readFiles(html_source, html)
json = readFiles(json_source, json)

server = HTTPServer((host_addr, port), AlsRequestHandler)
#cert_file = os.path.join(cert_repo, "public.pem")
#key_file = os.path.join(cert_repo, "private.key")
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)			# 7.
ssl_context.check_hostname = False
ssl_context.load_cert_chain(certfile=cert_file, keyfile=key_file)
server.socket = ssl_context.wrap_socket(server.socket,
										server_side=True)

try:
	server.serve_forever()
except KeyboardInterrupt:
	server.server_close()

print()
print("Server connection terminated.")
