# Scalability - where, what and how to scale

**For details and process behind this, see**
- [Geek Cruise III 2009 - Scalability in 2009](http://wiki.cantara.no/display/PE/Geek+Cruise+III+2009+-+Scalability+in+2009)

**Legend**

- H = high probability for successful scaling
- M = Medium probability for successful scaling
- L = Low probability for successful scaling

|  | [complex data](complex-data.md) | [KM:large data](../KM/large-data.md) | [high reads](high-reads.md) | [high writes](high-writes.md) | [KM:compute-process](../KM/compute-process.md) |
| --- | --- | --- | --- | --- | --- |
| [KM:infrastructure](../KM/infrastructure.md) | *[L | scale complex data in the infrastructure layer]*  | *[H | scale large data in the infrastructure layer]*  | *[L | scale high read in the integration layer]*  | *[M | scale high write in the infrastructure layer]*  | *[H | scale high processing or high computational in the infrastructure layer]*  |
| [KM:os-cloud](../KM/os-cloud.md) | *[L | scale complex data in the os & cloud layer]*  | *[L | scale large data in the os & cloud layer]*  | *[L | scale high read in the os & cloud layer]*  | *[L | scale high write in the os & cloud layer]*  | *[L | scale high processing or high computational in the os & cloud layer]*  |
| [KM:database](../KM/database.md) | *[H | scale complex data in the database layer]*  | *[H | scale large data in the database layer]*  | *[M | scale high read in the database layer]*  | *[H | scale high write in the database layer]*  | *[L | scale high processing or high computational in database layer]*  |
| [middleware](middleware.md) | *[L | scale complex data in the middleware layer]*  | *[L | scale large data in the middleware layer]*  | *[H | High reads in the middleware]*  | *[M | scale high write in the middleware layer]*  | *[H | Scaling high computation load wrt. the middleware]*  |
| [KM:server code](../KM/server-code.md) | *[H | scale complex data in the server code layer]*  | *[H | scale large data in the server code layer]*  | *[L | scale high read in the server code layer]*  | *[H | scale high write in the server code layer]*  | *[H | scale high processing or high computational in the server code layer]*  |
| [client](client.md) | *[L | scale complex data in the client]*  | *[L | scale large data in the client]*  | *[H | scale high read in the client]*  | *[M | scale high write in the client]*  | *[H | scale high processing or high computational in the client]*  |
