# Pythonidae Challenge

Learn Python for Cyber Security by completing challenges.

#### Network

This is `Network Technology Set`. This set involve any network interactions, from lower level (sockets) to higher level (protocol specific communication).

## Contents

This set consists of:

- [Socket](socket) programming (client/server/raw)
- [Protocol](protocol) communication (client/server)

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

#### Protocol Communication

client

0. HTTP client for enumerating file and directory
1. FTP client for bruteforcing username and password.
2. FTP client for listing home directory.
3. SSH client for bruteforcing username and password.
4. SSH client for executing command on remote host.
5. SSH client for login with SSH key.
6. SMTP client for enumerating valid user with SMTP VRFY command.
7. SMTP client for enumerating valid user with SMTP RCPT TO command
8. POP client for bruteforcing username and password.
9. IMAP client for bruteforcing username and password.
10. SMB client for bruteforcing username and password.
11. Client for sending ICMP ECHO request with payload `MII Cyber Security`.
12. DNS client for mapping subdomain from DNS server.
13. SSH tunnelling.

server

0. HTTP server which send `Super Normal Web Server` as response.
1. DNS server which always response with IP 127.0.0.1
2. DNS server which provide TXT record with message `Command to execute`.
3. FTP server which logging all login attempt.
4. FTP server which responding directory listing command with static result.
5. SSH server which logging all login attempt.
6. SSH server which responding command with message `command not found` for every command.