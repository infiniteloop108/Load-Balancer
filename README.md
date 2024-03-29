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
Click run. You can see a statistics graph in Response Time Graph. You can also save the graph by clicking 'Save graph'

You might run out of memory for jmeter. Run this `HEAP="-Xms512m -Xmx4096m"` to set your heap size to 4gb

## Some Results

We ran some tests.

1. Using no load balancer, sending requests on localhost - g1.png

2. Using no load balancer, sending requests on aws - g2.png

3. Using load balancer, with two servers on localhost - g3.png

4. Using load balancer, with one server locally, one on aws - g4.png
