# Pythonidae Challenge

Learn Python for Cyber Security by completing challenges.

#### Network

This is `Network Technology Set`. This set involve any network interactions, from lower level (sockets) to higher level (protocol specific communication).

## Contents

This set consists of:

- [Socket](socket) programming (client/server/raw)

#### Socket Programming

Client

0. receive message sent by server (TCP).
1. send message and receive the response (TCP).
2. receive message sent by server (UDP).
3. send message and receive the response (UDP).
4. given IP and list of port, connect to each port and mark the status.

Server

0. Send back any incoming message (TCP).
1. Only respond message from certain IP address.
2. Listen on two different ports, each will send unique message for incoming connection.
3. Only respond when peer send some messages in correct order.
4. Liten on two different port, if peer connect with certain order, a new port will be available for that peer.
5. Create a TCP proxy.
6. Create a thread to handle each connection.

Raw

0. Create raw socket.
1. Extract IP addresses from IP header.
2. Extract MAC addresses from ethernet header. 
3. Send packet with SYN flag activated.