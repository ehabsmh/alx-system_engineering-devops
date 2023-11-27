# Some specifics about this infrastructure

## What is a server
A server is a powerful computer hardware or software that provides a service to other computers known as clients.

---

## What is the role of the domain name
To alias an IP Address so it can be recognizable, for example the domain name, www.facebook.com is easier to recognize than its IP Address which is 157.240.22.35

---

## What type of DNS record www is in www.foobar.com 
"A" record is used by www.foobar.com, since it maps the domain name with the right corresponding ipv4 address.

---

## What is the role of the web server
It plays a major role in HTTP protocol requests, it handles it by getting all the static content directly and dynamic content of www.foobar.com by route the request to the application server to respond with all business logic it has. the web server will make an HTTP response for the client.

---

## What is the role of the application server
It runs and handles the dynamic content such as database or server-side scripts.

---

## What is the role of the database
To maintain a collection of organized information that can easily be accessed, managed and updated.

---

## What is the server using to communicate with the computer of the user requesting the website
Communication between the client and the server occurs over the internet network through the TCP/IP protocol.

---

# issues with this infrastructure:

## SPOF
There are multiple of SPOF (Single Point Of Failure) in this infrastructure. For example,
If the MYSQL database server is down, the entire site would be down.

---

## Downtime when maintenance needed (like deploying new code web server needs to be restarted)
Since there's only one server, this will cause us to turn the server off for maintenance.

---

## Cannot scale if too much incoming traffic
It would be hard to scale this infrastructure, it only has one server, So the server can quickly run out of resources or gets slow down when it starts receiving a lot of requests

