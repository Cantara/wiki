# Cloud Home

> 📝 Work in progress, feel free to add/complete information

### **Definition of Cloud Computing:**

Cloud computing is a pay-per-use model for enabling available, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, services) that can be rapidly provisioned and released with minimal management effort or service provider interaction. This cloud model promotes availability and is comprised of five key characteristics, three delivery models, and four deployment models.

Ref: 
- [NIST Cloud definition](http://csrc.nist.gov/groups/SNS/cloud-computing/index.html)
- [Working group drafts of NIST Reference Architecture and Taxonomy](http://bit.ly/eHsIHF)

### Key Characteristics:
- On-demand self-service. A consumer can unilaterally provision computing capabilities, such as server time and network storage, as needed without requiring human interaction with each service's provider. 
- Ubiquitous network access. Capabilities are available over the network and accessed through standard mechanisms that promote use by heterogeneous thin or thick client platforms (e.g., mobile phones, laptops, and PDAs).
- Location independent resource pooling. The provider's computing resources are pooled to serve all consumers using a multi-tenant model, with different physical and virtual resources dynamically assigned and reassigned according to consumer demand. The customer generally has no control or knowledge over the exact location of the provided resources. Examples of resources include storage, processing, memory, network bandwidth, and virtual machines.
- Rapid elasticity. Capabilities can be rapidly and elastically provisioned to quickly scale up and rapidly released to quickly scale down. To the consumer, the capabilities available for rent often appear to be infinite and can be purchased in any quantity at any time.
- Pay per use. Capabilities are charged using a metered, fee-for-service, or advertising based billing model to promote optimization of resource use. Examples are measuring the storage, bandwidth, and computing resources consumed and charging for the number of active user accounts per month. Clouds within an organization accrue cost between business units and may or may not use actual currency.

Note: Cloud software takes full advantage of the cloud paradigm by being service oriented with a focus on statelessness, low coupling, modularity, and semantic interoperability.

### Delivery Models:
- Cloud Software as a Service (SaaS). The capability provided to the consumer is to use the provider's applications running on a cloud infrastructure and accessible from various client devices through a thin client interface such as a Web browser (e.g., web-based email). The consumer does not manage or control the underlying cloud infrastructure, network, servers, operating systems, storage, or even individual application capabilities, with the possible exception of limited user-specific application configuration settings.
- Cloud Platform as a Service (PaaS). The capability provided to the consumer is to deploy onto the cloud infrastructure consumer-created applications using programming languages and tools supported by the provider (e.g., java, python, .Net). The consumer does not manage or control the underlying cloud infrastructure, network, servers, operating systems, or storage, but the consumer has control over the deployed applications and possibly application hosting environment configurations.
- Cloud Infrastructure as a Service (IaaS). The capability provided to the consumer is to rent processing, storage, networks, and other fundamental computing resources where the consumer is able to deploy and run arbitrary software, which can include operating systems and applications. The consumer does not manage or control the underlying cloud infrastructure but has control over operating systems, storage, deployed applications, and possibly select networking components (e.g., firewalls, load balancers).

### Deployment Models:
- Private cloud. The cloud infrastructure is owned or leased by a single organization and is operated solely for that organization.
- Community cloud. The cloud infrastructure is shared by several organizations and supports a specific community that has shared concerns (e.g., mission, security requirements, policy, and compliance considerations). 
- Public cloud. The cloud infrastructure is owned by an organization selling cloud services to the general public or to a large industry group.
- Hybrid cloud. The cloud infrastructure is a composition of two or more clouds (internal, community, or public) that remain unique entities but are bound together by standardized or proprietary technology that enables data and application portability (e.g., cloud bursting).

Each deployment model instance has one of two types: internal or external. Internal clouds reside within an organizations network security perimeter and external clouds reside outside the same perimeter. 

#### Standards and protocols 

- [Open Cloud Manifesto](http://www.opencloudmanifesto.org/) 

#### Cloud definitions and Categorisation

**Diagram: CloudCategories**

- Infrastructure as a Service (IaaS)
- Platform as a Service (PaaS)
- Cloud-backed Software as a Service (SaaS)

#### Features / Feature set

- Infrastructure
- Scalable infrastructure
- Provisioning infrastructure
- 

#### Usages of cloud technology

- Continuous deploy infrastructure

#### Implementations 

- [Google App Engine](http://code.google.com/appengine/) 
- [Amazon Elastic Compute Cloud aka. EC2](http://en.wikipedia.org/wiki/Amazon_EC2)
- [Amazon Simple Storage Service S3](http://aws.amazon.com/s3/)
- [MS Windows Azure](http://en.wikipedia.org/wiki/Azure_Services_Platform)
- [VMware vSphere](http://www.vmware.com/products/vsphere/) 

#### Attachments

#### Resources 

[Do clouds require redundancy?](http://service-architecture.blogspot.com/2009/05/do-clouds-require-redundancy.html)
