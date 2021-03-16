## Challenge 01

Given a port number.

Create a simple UDP server which listen on that port. Send back any incoming message following the its length.

Note: use IP address 0.0.0.0

## Test

There are several ways to emulate client. One possible solution is using netcat. Assuming port is 8080

```
nc -u 127.0.0.1 8080
```