## Challenge 05

Given three different port numbers: `A`, `B`, `C`.

Create a server which listen on three of them.

Port `C` is restricted, refusing or closing incoming connection from non-whitelisted IP address. While `A` and `B` are available.

If series of connection made from a single IP address to `A` and `B` in specific order, whitelist the address so `C` can accept only connection from that address.

The connection can be in any order and not requiring any message. For example: `A - B - A - A - B`.

Optionally, you can set `C` listen only when series of connection had been made.

## Remarks

This is an imitation of `Port Knocking`.

Port knocking is a method of externally opening ports on firewall by generating a connection attempt on a set of prespecified closed ports.

In our case, we are creating a server that open port when a connection attempt had been made to a set of ports.