# Helper Libraries

The purpose of this page is to describe a few _helpers_ that are often useful for service and system tests. The same helpers are also the basis for a [SysAdmin Production Toolbox](SysAdmin<sub>~Production</sub>~Toolbox.md). 

_RestoreDefaultState_ - bring the system back to a known, "empty" state. 

Each test insert their own test data and use helpers to clean up afterwards. 

#### Process helper 

- Spawn an instance of an application in a new process. 

- Verify process state (alive, dead) 

See also https://akuma.dev.java.net/

#### SQL Helper 

- drop, create schema, insert _product_ data 

- convenience methods to insert test data 

- clean - delete test data 

#### JMS helper 

- create Destinations (Queues and Topics)

- purge Destination 

- count number of messages on a Destination

- Tool to verify that all destinations work (functional test) 

- Tool to test performance of JMS server (non-functional) 

#### SOAP helper
