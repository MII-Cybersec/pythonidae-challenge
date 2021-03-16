## Challenge 00

Given IP and port.

Create a simple TCP client which connect to the address. Receive some data sent by the server.

## Test

There are several ways to emulate target server. One possible solution is using netcat (nc):

```
echo "MII CyberSec" | nc -lvp 8080
```

once connecting to this server, a message "MII CyberSec" is immediately given.

## Remarks

TCP is a connection oriented protocol. Before communication happen, a connection should be established between two parties. Communication is two way, each side can send or receive.

The `Three-Way Handshake` mechanism is used to establish TCP connection. In this mechanism, the client and server acknowledge the presence of each other.

Some service will send a banner for every connection established. In some cases, banner can give some information such as version.