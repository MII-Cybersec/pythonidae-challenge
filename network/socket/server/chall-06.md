## Challenge 06

Given an IP address `A`, two port numbers `P` and `Q`. 

Create a server which listen on port `Q`. When there is an incoming message on `Q`, connect to address `A` and port `P` then send the same message to `P`. Once `P` response, relay it back to the original peer (connecting to `Q`).

## Remarks

This is an imitation of proxy, which relays request and response. As an entity on middle of communication, proxy can inspect data exchange and even modify it.

Analysis of network protocol especially in binary format might require a custom TCP proxy. Inspection not only limited to print out all byte sequence, but also to parse and display the content based on hypothetical format.