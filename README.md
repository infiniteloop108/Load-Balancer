# Load-Balancer

## Deploying servers

run `python server.py host port`
You'll need BaseHTTPServer python module to run the server

It is advised that you deploy 1 server on aws and 1 server locally

The server gives the functionality of adding two numbers. The http request should be of the form:
`/sum?a=123&b=456`

## Deploying load balancer

You need to install some node modules first

run `npm install http-proxy`
run `npm install http`

Put the server addresses in servers array in load-balancer.js 
run `node load-balancer.js port`
You can run the load balancer locally.

Now any request made to load balancer IP will be redirected to one of the above two mentioned servers depending on the load on them

## Testing the load balancer with jmeter

First install jmeter using `brew install jmeter` (use apt-get on linux)
Open the Test Load Balancer.jmx file in jmeter
Verify the address to which the request is sent (in HTTPRequest and HTTPRequestDefault)
Click run. You can see a statistics graph as stats.png

## Some Results

We ran some tests.
