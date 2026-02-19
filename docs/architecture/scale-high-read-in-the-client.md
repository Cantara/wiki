# scale high read in the client

Example: Map client, spotify, iTunes. 
We create one user system with a 1.tier client. 
Caching on client and/or server.
p2p if server wire is bottleneck. 
Movable code to fetch data async.
Streaming from server.

## Default / Enterprise 
- Caching
    - Most obvious solution. 
        - Can clients live with "old" data? 
- Movable code
    - Can use some sort of moveble code for fetching data async. 
- Streaming 
    - Everybody does it! 

## Bleading edge. 
- P2P
    - If you have very large datasets, the wire from the server can be the bottleneck. We can solve the problem by letting the clients share data p2p. Maps, videos, what ever heavy.  
    - Can create some sort of controlled network in order to get better latency. 

## Useless stuff:  
- Async writes
    - We do heavy reads. Async writes won´t help. 

- Static code
WTF
