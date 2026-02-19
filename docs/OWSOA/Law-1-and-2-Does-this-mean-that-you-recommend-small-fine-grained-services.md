# Law 1 and 2 - Does this mean that you recommend small, fine grained services?

Q: "Law 1, 2: Does this mean that you recommend small, fine grained services? Are these services usually distributed, or should they more often be local interfaces in the system? Should the "laws" say anything about this to make sure we're all on the same page re: what is a service?"

a: Have a look at Service Manifest, and yes - the services have the same characteristics as all reusable code - they focus on a single responsibility. Services which tries to do too much, gets bloated with environment and start to expose the characteristics of both their clients and their implementation, and provide horrible service. 

---
