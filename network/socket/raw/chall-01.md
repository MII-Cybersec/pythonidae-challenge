## Challenge 01

Given a port number.

Create a raw socket and listen to the port. Receive a packet and extract source and destination IP address from IP header.

## Remarks

Layer 3 or Network Layer is responsible for packet forwarding including routing through intermediate routers.

Using raw socket on layer 3 gives flexibility on modifying IP header and payload. The payload include modification of transport layer or any layer on top of it.
