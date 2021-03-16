## Challenge 00

Create a raw socket.

Note: Raw socket must be initialized to freely craft packet without headers.

## Remarks

Raw socket is used to send and receive raw packets. It means packets received at Ethernet layer (or any Layer 2) will directly be pass to the raw socket. Raw socket bypass the normal TCP/IP processing.

Raw socket need a privilege access from kernel. All packet crafting activity should be done manually, without kernel help.