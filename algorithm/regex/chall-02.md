## Challenge 02

Given a possible long text, find and extract domain names.

Domain name consists of several string, separated by dots. The right most string is top-level domain, which value is defined (i.e. com, net, id, org). The rest are defining hostnames, which can be any arbitrary string.

## Remarks

Some malware use communication with Command and Control server over DNS. The message is transported as DNS request/reply. To ensure communication, a random subdomain is generated using Domain Generation Algorithm.