#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import sys

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        request_path = self.path
	path = request_path[0:5];
	if path != "/sum?":
		self.send_response(400)
		return
	if request_path[5] != "a":
		self.send_response(400)
		return
	b_ind = request_path.find("b")
	if b_ind == -1:
		self.send_response(400)
		return
	
	try:
		a=int(request_path[7:b_ind-1])
		b=int(request_path[b_ind+2:])
		self.wfile.write(str(a+b) + "\r\n");
		self.send_response(200);
	except:
		self.send_response(500)


if len(sys.argv) != 3:
	print '\033[91m' + 'Usage python server.py hostname port' + '\033[0m'
	sys.exit(0)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

server = HTTPServer((HOST, PORT), RequestHandler)
print('Listening on '+  HOST + ':' +  str(PORT))
server.serve_forever()
