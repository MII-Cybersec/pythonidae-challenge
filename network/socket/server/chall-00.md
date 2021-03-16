## Challenge 00

Given a port number.

Create a simple TCP server which listen on it. Send back any incoming message following the its length.

Note: use IP address 0.0.0.0

## Test

There are several ways to emulate client. One possible solution is using netcat. Assuming port is 8080

```
nc 127.0.0.1 8080
```