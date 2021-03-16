## Challenge 12

Given a DNS server host `H` (can be IP address or domain), and list of string `L`.

Create a simple client which connect to `H`. For each string (subdomain) in the list `L`, send DNS query to `H` and check the response if the host exists.

Note: `L` is list of subdomain not in `FQDN (Full-Qualified Domain Name)`. 