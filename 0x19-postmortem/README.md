# website requests failure report
On previous month, it was reported that our website platform was returning 500 Error on all requests made on the platform routes, all the services were down.  most of the users were affected. The root cause was the failure of our master server web-01.

## Timeline
The error was realized on monday 11th January 2024 at 9:30 PM (EAT) when our server administrator saw the master server lagging in speed. After the situation happened, Our sytem technicians were on  call and  disconnected the master server web-01 for further system analysis and channelled all requests to web server web-02. They solved the problem by 12th January 2024  at 09:30 AM  (EAT).

## Root cause of The problem and resolution
The Website platform is served by 2 ubuntu cloud servers. technically our team belives that  HTTP 500 errors aren't problems with your computer, browser, or internet connection. Instead, they're a generic response that catches any unexplainable server error. You'll see the HyperText Transfer Protocol (HTTP) 500 Internal Server Error when your server issue doesn't fit another error code. Therefore , the team observed that the master server web-01 was connected to serve all requests, and it stopped functioning due to memory outage as a results of so many requests because during a previous test, the client server web-02 was disconnected temporarily for testing and was not connected to the load balancer afterwards. 


The issue was fixed when the master server was temporarily disconnected for memory clean-up then connected back to the loadbalancer and round-robin algorithm was configured so that both the master and client servers can handle equal amount of requests.

## Measures against such problem in future
- Choose the best loadbalancing algorithm for your programs
- Always keep an eye on your servers to ensure they are running properly
- Have extra back-up servers to prevent your program from completely going offline during an issue

##
Troubleshooting an HTTP 500 internal server error is like solving a mystery.
