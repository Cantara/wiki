# The holy grail of software integration

|  | This is an early and incomplete draft |

|  | The intent of this document is to establish common software integration ground. The purpose is to be able to deliver better services and better service quality. Common ground ensure good and enlightened decisions leading to reduced cost and better service quality. |

|  |  |
| --- | --- |
| Business value, risk and consequences  - The closer to the company's aorta the integration is, the higher value, risk and consequence the will be. This should be clearly identifiable in the SLA for the integration. - As we move further and further away from the heart of the company, we will hit a limit where the cost/value ratio turn negative. Business discussions are needed to address those processes before any integration. (Each integration add to the total system complexity)  Service-level agreement (SLA) and service quality The four key quality elements of a service. The cost is typically exponential so we need to select the correct level.   - **Availability:** Mission critical HA, Business critical HA, 99.95%, 99.95% 0600-1900, 95% - **Latency:** 95% of request within 10ms, 300 ms, 1 s, 5 s - **Load:** 100.000 reqs/s, 100 reqs/s, 5 reqs/s, 10 reqs/min - **Data-volume:** 10 GB/s 100 MB/s, 10MB/s, 1MB/s - **Other constraints:** SOX, privacy, Basel III  Information, Data and Domain-objects  - Integration data-sets which span more than one Enterprise Information Object should be kept at a minimum - Integration-loops for the sole purpose of having enough data for a decision should be replaced with a higher-level aggregated function  Data quality  - Each integration should explicit document the data quality clients should expect from the integration, including data-integration issues |  |

### Integration architecture

- Peer-to-peer (P2P) (From file-based ftp/samba to REST)
- Bus/Middleware (one size fits all or more than one?)
- Messaging and Pub/sub (might simplify application landscape)

> I've increasingly come to the view that integration through asynchronous messaging is one of the most effective ways to integrate disparate enterprise applications. [Enterprise Integration Patterns](http://www.enterpriseintegrationpatterns.com/) is a foundation collection of patterns for this approach. - M. Fowler

### Integration types

- Data-level integration
  - divide and conquer
- Application-level integration
  - overlapping functionality/responsibilities
- Method-level integration
  - monitoring the volume of integration's

### Protocols

| Protocol | Smartness | Discussion |
| --- | --- | --- |
| ftp |  | Not good: a) No notification (sender/receiver), b) No integrity of file c) not secure transfer d) not I/O resilient |
| shared disk (samba) |  | a) shared disk protocols like windows/samba require a very tight and open network architecture b) No notification (sender/receiver), c) No integrity of file d) I/O performance dependencies including performance and file-locking |

### Formats

Files vs records

- The larger the file, the more likely that the transfer og disk-io will experience errors causing erroneous data being accepted or re-transmit data

### Techniques

- Anti-corruption layer
- [At-least once semantics](../architecture/At-least-once-semantics.md) preferred over guaranteed delivery for looser coupling giving higher service levels

|  | **Rule-of-thumb**  You wont be very wrong if you go for asynchronous messaging with [at-least once semantics](../architecture/At-least-once-semantics.md) |

---

### Some pointers

> A **data-centric architecture** provides strong governance over data. It is so called because it organizes  
> the interactions among applications in terms of stateful data rather than in terms of operations to  
> be performed. Data structure and QoS are explicit and discoverable. The operations that act on that  
> state are uniform1. As a result, the integration infrastructure is able to enforce the data structure and  
> QoS contracts on behalf of the applications, such that applications are not permitted to communicate  
> malformed data or to change data in inappropriate ways. Applications are easier to develop, less  
> dependent on each other, and more fault-tolerant. Such architectures are therefore involving multiple  
> teams.
>
> Example implementation technologies: SQL databases [4] (data at rest only), RESTful web services [6] (data  
> at rest only), and OMG DDS [2] (data in motion).

<http://www.rti.com/whitepapers/System_Architecture_for_Integration.pdf>

> Systems integration- the integration between applications. Principles:
>
> - Achieve connection while at the same time maintaining the separation between applications.
> - Decouple applications, so that each application knows nothing of the internal data, processing, technology or schedules of any other.
> - Have well-defined system boundaries.
> - Send data in lumps that are meaningful in business terms.
> - Establish tool-independent standards for the technology and format of data sent between applications.
> - Consider each application as an equal peer, rather than arranging applications in layers.

<http://it.toolbox.com/blogs/minimalit/principles-of-intraapplication-integration-38296>

> **Data-level**  
> At this level, backend data stores are integrated to enable the movement of data between  
> them. Put simply, information can be extracted from one database, processed as needed,  
> and then updating it in another database. In an EAI enterprise, this could mean drawing  
> data from as many as hundreds of databases and thousands of tables. For this reason,  
> keeping the integrated application's data intact is a problem. For example, one table might  
> have dependencies to others, and the integrated application may be the sole enforcer of  
> those dependencies.  
> Data-level integration can be push- or pull-based. Push-based integration is when one  
> application makes SQL queries on another application's database; data is pushed into  
> another application's database. In contrast, pull-based integration is used when an  
> application requires passive notification of changes within another application's data.
>
> Cost benefits of data-level integration give it its advantage over other approaches. This is  
> because on the whole, the application is not altered; code is not changed and so the  
> expense of changing, testing, and deploying the application is not incurred.
>
> Data-level integration should be used when the application up for integration does not  
> provide any APIs or client interfaces. This is typically represented as the only option with  
> custom applications lacking application APIs.
>
> **Application-level**  
> This refers to making use of interfaces contained within custom or packaged applications  
> such as SAP, Peoplesoft or Baan. These interfaces are leveraged to provide access to  
> business processes and information. This approach is probably the best way to integrate  
> applications as it allows you to invoke business logic to preserve data integrity. Developers  
> are able to bundle many applications together so that business logic and information can  
> be shared. This approach is more widely used and is preferred since it is transparent to  
> the integrated application and the application's data integrity is preserved.
>
> **Method-level**  
> In effect, this is a more complicated form of application-level integration and is used less  
> frequently. Common operations on multiple applications are aggregated into a single front  
> application. For example, the method for updating a customer record can be accessed  
> from numerous applications without having to rewrite each method within the respective  
> application. Since all applications that interact with the integrated applications do so via  
> this front application, method-level integration requires the integrated applications to  
> support a RPC (remote procedure call) or distributed component technology.  
> The disadvantage lies in the fact that changing the integrated application API will break  
> the front application components and the applications that rely on them. Given this then, it  
> is usually more appropriate to opt for application-level integration using middleware.

<http://www0.cs.ucl.ac.uk/staff/ucacwxe/lectures/3C05-04-05/EAI-Essay.pdf>
