## Challenge 00

Given IP and port.

Create a simple UDP client and connect to the server. Receiver some data sent by the server.

## Test

There are several ways to emulate target server. One possible solution is using netcat (nc):

```
echo "MII CyberSec" | nc -ulvp 8080
```
once connecting to this server, a message "MII CyberSec" is immediately given.

## Remarks

UDP is a connection-less protocol. No setup prior communication. No trace to order of packet. Any missing packet or out of order packet won't be detected by default.

