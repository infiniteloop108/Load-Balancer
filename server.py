#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import sys

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        request_path = self.path
	path = request_path[0:5];
	if path != "/sum?":
		self.send_response(404)
		self.end_headers()
		return
	if request_path[5] != "a":
		self.send_response(404)
		self.end_headers()
		return
	b_ind = request_path.find("b")
	if b_ind == -1:
		self.send_response(404)
		self.end_headers()
		return
	
	try:
		a=int(request_path[7:b_ind-1])
		b=int(request_path[b_ind+2:])
		body = str(a+b);
		self.send_response(200);
		self.send_header('Content-type', 'text/plaintext');
		self.send_header('Content-length', str(len(body)) )
		self.end_headers();
		self.wfile.write(body);
	except:
		self.send_response(500)
		self.end_headers()


if len(sys.argv) != 3:
	print '\033[91m' + 'Usage python server.py hostname port' + '\033[0m'
	sys.exit(0)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

server = HTTPServer((HOST, PORT), RequestHandler)
print('Listening on '+  HOST + ':' +  str(PORT))
server.serve_forever()
