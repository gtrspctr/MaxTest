#!/usr/bin/env python

"""
This is an http server.
Its GET request handler will server various web pages.
Unfortunately I never got the POST request handler working.

This application was written by Al Robison.
Last Modified:  2023/01/26
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
from os import path
import json
import cgi

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
files_source = path.join(content_repo,		# File upload HTML content
						  "files.html")
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
		elif self.path == "/files":
			self.send_header("Content-type", "text/html")
			self.end_headers()

			self.wfile.write(bytes(files_output, "utf-8"))
		"""
		else:
			self.send_header("Content-type", "text/html")
			self.end_headers()

			self.wfile.write(bytes(unkn_output, "utf-8"))
		"""

	def do_POST(self):
		self.send_response(201)
		if self.path == "/upload":
			self.wfile.write(bytes("Hello!!!!", "utf-8"))
			target_path = file_repo
			filename = path.basename(self.path)
			self.wfile.write(bytes("Target:" + target_path, "utf-8"))
			self.wfile.write(bytes("Filename:" + filename, "utf-8"))
			"""file_length = int(self.headers["Content-Length"])
			with open(filename, "wb") as output_file:
				output_file.write(self.rfile.read(file_length))
			self.end_headers()
			reply_body = "Saved '%s'\n" % filename
			self.wfile.write(bytes(reply_body, "utf-8"))"""

			ctype, pdict = cgi.parse_header(self.headers['Content-Type'])
			print("CTYPE: " + str(ctype))
			print("PDICT: " + str(pdict))
			if ctype == 'multipart/form-data':
				cgi.parse_multipart(self.rfile, pdict)
			elif ctype == 'application/x-www-form-urlencoded':
				lenth = int(self.headers['content-length'])
				parse_qs(self.rfile.read(length), keep_blank_values=1)

			"""
			ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
			if ctype == "multipart/form-data":
				fields = cgi.parse_multipart(self.rfile, pdict)
			"""
		"""
		self.send_header("Content-type", "application/json")
		self.end_headers()
		self.wfile.write(bytes(str(json_obj), "utf-8"))
		"""

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
files_output = ""
index_output = readFiles(index_source, index_output)
json_output = readFiles(json_source, json_output)
unkn_output = readFiles(unknown_source, unkn_output)
files_output = readFiles(files_source, files_output)

# Get JSON data as an object
#json_obj = json.loads(json_output)

# Create HTTPSServer object, passing in the addr/port 
# and request handler object.
server = HTTPServer((host_addr, port), AlsRequestHandler)

# Create SSL Context.
# This basically wraps the HTTPSServer object in
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
