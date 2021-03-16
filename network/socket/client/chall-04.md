## Challenge 04

Given an IP address and a list of ports.

Connect to each port by TCP connection. If connection is successful, mark it as `alive`. Otherwise, mark it as `filtered`.

Optional: filter the port, only valid ports will be processed. Valid port is non zero, positive integer in the range of 1-65535.

# Remarks

A simple port scanning will do TCP handshake. If the connection established, it can be concluded port is alive and some service might listen on it.