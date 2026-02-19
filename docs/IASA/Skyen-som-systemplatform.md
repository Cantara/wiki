# Skyen som systemplatform

2009.05.28- Totto

> 💡 
> 💡 "Making the best of the cloud requires that we take an architectural view, something that we've proven remarkably bad at over and over. Simply deploying an application unchanged to the cloud is unlikely to deliver much benefit."
> 💡 
> 💡 * distributed system (on IaaS)
> 💡 ** redundancy in software
> 💡 ** security in software
> 💡 ** cloud-scaling as peek strategy
> 💡 * single responsibility principle (services)
> 💡 ** continuously integration (automatic, EMI)
> 💡 ** continuously deploy (automatic, EMI)
> 💡  
> 💡 remember: **There are no Silver Bullets**

### 5 Key Cloud Characteristics

- On<sub>~demand self</sub>~service 
- Ubiquitous network access
- Location independent resource pooling
- Rapid elasticity
- Pay per use

### 3 Cloud Delivery Models

- Cloud Software as a Service (SaaS)
    - Use provider's applications over a network 
- Cloud Platform as a Service (PaaS)
    - Deploy customer-created applications to a cloud 
- Cloud Infrastructure as a Service (IaaS)
    - Rent processing, storage, network capacity, and other fundamental computing resources

To be considered "cloud" they must be deployed on top of cloud infrastructure that has the key characteristics

### 4 Cloud Deployment Models

- Private cloud 
    - enterprise owned or leased
- Community cloud
    - shared infrastructure for specific community
- Public cloud
    - Sold to the public, mega-scale infrastructure
- Hybrid cloud
    - composition of two or more clouds

Two types: internal and external

### Common Cloud Characteristics

Cloud computing often leverages:
- Massive scale
- Virtualization
- Free software
- Autonomic computing
- Multi-tenancy
- Geographically distributed systems
- Advanced security technologies
- Service oriented software

### The Fallacies of Distributed Computing

"a set of common but flawed assumptions made by programmers when first developing distributed applications. The fallacies are summarized as follows:"

1. The network is reliable.
1. Latency is zero.
1. Bandwidth is infinite.
1. The network is secure.
1. Topology doesn't change.
1. There is one administrator.
1. Transport cost is zero.
1. The network is homogeneous.

### Efficient cloud requires

- They don't require masses of administrator intervention when they go wrong.
- They can be installed with minimal administrator effort because there's no need to worry about tweaking URLs, IP addresses, database connections etc.
- They readily support horizontal scaling e.g. because they contain an abstraction that can support sharding of data-storage.
