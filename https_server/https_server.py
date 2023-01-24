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
from os import path
import json

# Define the host IP and port number
# An IP of 0.0.0.0 will broadcast on all local NICs
# 443 is the standard port for HTTPS
host_addr = "0.0.0.0"
port = 443

# Define filepaths
server_path = path.dirname(__file__)		# Main directory
content_repo = path.join(server_path,		# Web page data directory
						 "content_repository")
index_source = path.join(content_repo,		# Index HTML content
						 "index.html")
unknown_source = path.join(content_repo,	# Unknown page HTML content
						   "unknown.html")
json_source = path.join(content_repo,		# JSON content
						"users.json")
file_repo = path.join(server_path,
					  "file_repository")	# Repository for file uploads
cert_file = path.abspath("/etc/letsencrypt/live/alrobison.com/fullchain.pem")
key_file = path.abspath("/etc/letsencrypt/live/alrobison.com/privkey.pem")

# This class is the request handler.
# do_GET sends a response of 200 when
# successful. It also specifies that the
# content type is html, and displays html
# content to the browser.
class AlsRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		if self.path == "/":
			self.path = "/index.html"

			self.send_header("Content-type", "text/html")
			self.end_headers()

			# Website body
			# self.wfile.write(bytes("", "utf-8"))
			self.wfile.write(bytes(index_output, "utf-8"))

		elif self.path == "/users":
			self.send_header("Content-type", "application/json")
			self.end_headers()

			self.wfile.write(bytes(json_output, "utf-8"))
		"""
		else:
			self.send_header("Content-type", "text/html")
			self.end_headers()

			self.wfile.write(bytes(unkn_output, "utf-8"))
		"""
	def do_POST(self):
		self.send_response(201)
		self.send_header("Content-type", "application/json")
		self.end_headers()
		self.wfile.write(bytes(str(json_obj), "utf-8"))

	def post_request_value(self):
		pass

	def post_request_all_content(self):
		return json_obj

	def post_update_value(self):
		pass

	def post_delete_dict(self):
		pass

	def post_delete_dict_structure(self):
		pass

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

index_output = ""
json_output = ""
unkn_output = ""
index_output = readFiles(index_source, index_output)
json_output = readFiles(json_source, json_output)
unkn_output = readFiles(unknown_source, unkn_output)

# Get JSON data as an object
json_obj = json.loads(json_output)
print(type(json_obj))

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
