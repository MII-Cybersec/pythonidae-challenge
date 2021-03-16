## Challenge 07

Given a port `P`.

Create a simple server which listen on `P`.

When a connection come, spawn a thread and let it handle the communication to peer. The port should be able to accept next connection without waiting the current connection to cease.

## Remarks

For any real-world server, the ability to serve multiple request at once is essentials. Thread is one of solution where a pool of thread usually use (and reuse) to handle connection. Each thread will handle one client.