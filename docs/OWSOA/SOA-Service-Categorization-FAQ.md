# SOA - Service Categorization FAQ

### How does this service categorization relate to OW SOA?

This categorization is rooted in the OW SOA service categorization and extended from feedback from multiple sources and projects. It tried to communicate the fine lines somewhat more explicit to make it easier to understand and adopt. (OW SOA is documented in detail on [http://wiki.community.objectware.no](http://wiki.community.objectware.no)

### I miss discussion of each box and layer - definition, purpose, properties, constraints, examples, etc. 

Work in progress...   noted and will be detailed rsn :)

### What types of services can directly interact with other service types ?

It is not a strict layered model, so a Human 2 Application service can call a Core Service. But a Core Service can not interact with services in layers above.

### Is the categorization static, or can a service belong to several categories depending on its use ? 

A service can not belong more than one category. If you are seeing your services mapped to several categories, you are probably breaking most of the SOA Design Rules, as your service is doing way more than it should.

### And in that context, what about legacy systems acting as services ?

Legacy system services are embedded as A2A integration services or embedded within a ACS/CS for unified data access and query implementation.
