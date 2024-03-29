var arguments = process.argv.splice(2);
var port = arguments[0]
var httpProxy = require('http-proxy');
var http = require('http');

var servers = [
{ target : 'http://127.0.0.1:8001'},
//{ target : 'http://127.0.0.1:8002'},
{ target : 'http://52.10.123.178:8000'},
];

var pending = [0,0]
var proxy = httpProxy.createProxyServer();

var load_balancer = http.createServer(function (req, res) {
	var server = 0;
	if(pending[0] > pending[1])
		server = 1
	pending[server]+=1
	console.log("Sending request to server " + server);
	proxy.web(req, res, servers[server]);
	proxy.on('error', function (err, req, res) {
		res.writeHead(500, {'Content-Type': 'text/plain'});
		res.end('Something went wrong. That\'s all we know');
	});
	res.on('finish', function() {
		pending[server]-=1
	});
});

load_balancer.listen(port || 8000, '0.0.0.0');
console.log("Load Balancer Started");
