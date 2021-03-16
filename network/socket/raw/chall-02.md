## Challenge 02

Given a port number.

Create a raw socket and listen to the port. Receive a packet and extract source and destination MAC address from Ethernet header.

## Remarks

Layer 2 or Data Link Layer is responsible for data transfer at adjacent network nodes.

Using raw socket on layer 2 gives flexibility on modifying ethernet header and payload. The payload include modification of transport layer or any layer on top of it.