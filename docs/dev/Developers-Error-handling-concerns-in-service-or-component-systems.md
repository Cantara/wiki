# Developers - Error handling concerns in service or component systems

The fact that error handling is often the lowest<sub>~priority concern is doubly weird if you consider that **cross</sub>~component error handling is the same concern as core functionality messaging**. In both cases there are the same sets of concerns, both with regards to communication with external components and interaction between the component's internal implementation and the communication layer. Some typical concerns that development teams have to deal with are:

#### Distributed Systems and remoting

**Integration Points**
    - Every integration point will eventually fail in some way, you need to be prepared 
    - Integration point failures take many forms, e.g.: 
        - Network error 
        - Sematic error 
        - Protocol violation 
        - Slow response 
        - Direct hang 
    - Program defensively to avoid cascading failures 
    - Integration points without timeouts is a surefire way to create cascading failures 
    - Safe resource pools always limit the time a thread can wait to check out a resource 

#### **Error message definition**

Just as SOA components require clear definitions of the messages that will be exchanged with client components for mainline communication, **clear definitions** must also be given of messages that carry error information.

#### **Error communication behaviour definition**

Just as mainline communication behaviour between SOA components must be clearly and formally defined, so must similar definitions be given for when a component can send an error message in response to a request for operation.

See [Error Categorization example](Error<sub>~Categorization</sub>~example.md)

#### **Projecting exception types from the domain language onto error types from the communication language**

In the case of error handling, this is one half of a problem that also exists for mainline communication. In mainline communication request messages must be projected onto domain model types and domain model types must be projected onto communication language types when the component returns a response. In the case of error handling of course there is no concept of request projection since nobody requests an error; however, the analog with projecting a domain model type onto a response communication message remains.

#### **Maintaining component independence**

This concern actually affects a component more as a consumer of other services than as a publisher of services. Maintaining component independence is related to avoiding domain models leaking over into foreign components (as Eric Evans puts it). In the case of messaging it means not building your domain model so that it is a mere copy of a foreign component's communication model. In the more specific case of error handling it relates to not linking error handling too closely to the definition of errors used by foreign components. Instead, as with mainline messages, **foreign component-generated errors should be projected onto the local domain**

Reference: [SOA component design: thinking about error handling](http://www.gridshore.nl/2008/07/26/soa<sub>~component</sub><sub>design</sub><sub>thinking</sub><sub>about</sub><sub>error</sub>~handling/)

---
