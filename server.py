#!/usr/bin/python
# coding=utf-8


from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import os
from os import curdir, sep
import json
import re
import db_init
import db
import codecs
import cgi
import urlparse

if not os.path.isfile('db.sqlite3'):
    db_init.init()

PORT = 3000

class Handler (BaseHTTPRequestHandler) :

    def do_GET(self) :

        # Look for main page
        if self.path=="/":
            self.path="/index.html"

        if self.path == "/products" :
            #send response code:
            self.send_response(200)
            #send headers:
            self.send_header("Content-type:", "application/json")
            # send a blank line to end headers:
            self.wfile.write("\n")
            #send response:
            json.dump(db.getAll(), self.wfile)
        if re.match(r'\/product\/\d+', self.path): # match "/product/{ID}"
            #send response code:
            self.send_response(200)
            #send headers:
            self.send_header("Content-type:", "application/json")
            # send a blank line to end headers:
            self.wfile.write("\n")
            #send response:
            json.dump(db.getOne(re.search(r'[^/]*$', self.path).group(0)), self.wfile) # regex to get everything after the last slash

        try:
			#Check the file extension required and
            #set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".woff"):
				mimetype='font/opentype'
				sendReply = True
			if self.path.endswith(".ttf"):
				mimetype='font/opentype'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
                #Open the static file requested and send it
				f = open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()

			return

        except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

    def do_POST(self):

        # Look for POST request
        if self.path == "/product":
            length = int(self.headers.getheader('content-length'))
            # Get form data
            postvars = urlparse.parse_qs(self.rfile.read(length), keep_blank_values=1)

            # Init data
            name = postvars.get('name')[0]
            desc = postvars.get('description')[0]
            price = float(postvars.get('price')[0])

            # Send request to DB
            db.putOne(name, desc, price)

            # Send code 200
            self.send_response(200)
            self.end_headers()

    def do_PUT(self):

        # Look for PUT request
        if re.match(r'\/product\/\d+', self.path):
            length = int(self.headers.getheader('content-length'))
            # Get form data
            postvars = urlparse.parse_qs(self.rfile.read(length), keep_blank_values=1)

            # Init data
            name = postvars.get('name')[0]
            desc = postvars.get('description')[0]
            price = float(postvars.get('price')[0])

            # Send request to DB
            db.updateOne(re.search(r'[^/]*$', self.path).group(0), name, desc, price)

            # Send code 200
            self.send_response(200)
            self.end_headers()

    def do_DELETE(self):
        if re.match(r'\/product\/\d+', self.path): # match "/product/{ID}"
            #send response code:
            self.send_response(200)
            #send headers:
            self.send_header("Content-type:", "application/json")
            # send a blank line to end headers:
            self.wfile.write("\n")
            #send response:
            db.delete(re.search(r'[^/]*$', self.path).group(0)), self.wfile
            return


server = HTTPServer(("localhost", PORT), Handler)
print "serving at port", PORT
server.serve_forever()
