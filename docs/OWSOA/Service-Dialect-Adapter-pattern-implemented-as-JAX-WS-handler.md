# Service Dialect Adapter pattern implemented as JAX-WS handler

> ℹ️ 

## Evolving Service Endpoint versioning

The main idea of the Evolving Service Endpoint (ESE) pattern is to be able to modify web service endpoints without necessarily disturbing clients. It should be possible to modify a WSDL without forcing all existing clients to adapt to a new API at once. The only way to achieve this is to implement web service endpoints which can accept client requests in different formats. These should also respond to clients in the same format used by the client in the request.

The proposed solution demonstrates one possible way to achieve this. Its main strengths are:
- Different versions of WSDLs differ only in type definitions (different xsd mappings).
- All clients must use one or another WSDL. Although clients can choose which WSDLs they will use, they can not send an arbitrary request to endpoint. This enables strong typing.
- At each time there is only one official WSDL. All new clients will only see it.
- Heavy reuse of xsd files. If two WSDL versions have common parts, they will not be duplicated.

> ℹ️ Please note that this is an endpoint<sub>~bound solution to the ESE/ESA pattern, which does make sense in many circumstances, but which is not true to the OW SOA service manifest which dictates a service</sub>~bound solution (and thus being able to support a greater varity of endpoint strategies :)

## Technical notes

Although it should be theoretically possible to implement the proposed solution with any WS framework, our choice was JAX-WS RI 2.1 and the following discussion will rely on its concepts and capabilities.

## Service dialect adapter 

Web service endpoints should provide the same piece of functionality to all their clients. However, we want to allow different clients to use different message formats to request this functionality. This implies that response message formats may also differ for different clients. We define a **service dialect** as a combination of request message format and the corresponding response message format which is understandable by a web service endpoint. A web service endpoint may support one or more service dialects.

A **service dialect adapter** can be seen as a special web service endpoint designed to serve one particular service dialect. An ESE will have at least one service dialect adapter.

Service dialects need to be loosely associated with the different message formats that are understandable by a web service endpoint. This association may be achieved in different ways and there is nothing in the proposed solution that dictates one approach or another. ServiceDialectAdapter is an interface and developers are free to choose appropriate implementations.

However, we believe that the best solution is to define service dialects in terms of xsd. There are basically two approaches:
- A unique namespace for each service dialect - provides clearer separation between dialects
- A shared namespace for multiple dialects - can be less xml because of no xsd imports

The main advantages of xsd-based approach are:
- All message formats are formally defined and it's much harder for clients to do something stupid
- Its very easy for the ESE to determine which dialect a client wants to use. The only thing we must do is to check the fully qualified name of the first element of the clients request.

> 💡 A good [article](http://msdn.microsoft.com/en-us/library/ms954726.aspx) on MSDN discusses possible strategies for versioning schemas and Web services and summarizes some best practices:
> 💡 
> 💡 * Use **targetNamespace** to communicate major version releases.
> 💡 * Judicious use of unambiguous wildcards can minimize service versioning.
> 💡 * Extensions must not use the **targetNamespace** value.
> 💡 * When adding new data structures, make them optional and add them to the end of service request messages.
> 💡 * Changing service response messages (other than type restrictions) are breaking changes that will require a new version of the service.
> 💡 * Adopt a one<sub>~to</sub>~one relationship between interface versions and UDDI tModels.

As an illustration of different dialects consider the following two requests to an imaginary Customer Service. Both requests are asking for the same data but do it in different ways:
```title
<dialect:findCustomer xmlns:dialect="http://.../customerService/v1">
    <customerId>123</customerId>
</dialect:findCustomer>
```
```title
<dialect:getCustomer xmlns:dialect="http://.../customerService/v2">
    <socialSecurityNumber>321</socialSecurityNumber>
</dialect:getCustomer>
```
The following drawing illustrates an ESE which supports two dialects. Each of them is based on a separate xsd with a unique namespace. When a clients request arrives at the ESE, the service adapter just delegates processing to an appropriate service dialect adapter. Later we will see how and when the service dialect adapter is chosen. For now assume that the service adapter (Java class annotated as a WS endpoint) just happens to know the clients dialect for each incoming request.
![ESE_versioning.jpg](ESE_versioning-jpg.md)(ESE_versioning.jpg)

## How and when to determine dialect?

A service endpoint may have a set of policies associated with it. Examples of policies are authorization, logging, etc. Typically a policy defines some preprocessing of incoming messages and postprocessing of outgoing messages. It is effectively an interceptor around a service endpoint. Since policy implementations usually use the contents of incoming and outgoing messages, they should be able to understand clients dialects in the same way as service adapters do.

JAX<sub>~WS allows policy functionality by means of WS Handlers which execute before and after invocations of service endpoints. For each policy we can define a set of handlers and organize them in handler chain. Since each policy handler will need to know the clients dialect we must determine it before the first handler in the handler chain is called. The most obvious solution is to create a special handler which will always be called first in the handler chain and whose only responsibility will be to determine the correct service dialect adapter for the incoming request and put it in some place where all other handlers and service adapter can access. In JAX</sub>~WS the MessageContext is exactly such a place.
![ESE_ServiceDialectHandler.jpg](ESE_ServiceDialectHandler-jpg.md)(ESE_ServiceDialectHandler.jpg)

## ESE and JBI

When a web service is deployed in a JBI environment it becomes a Service Unit(SU) which can be configured to interact with any number of other Service Units in the same JBI runtime. A SU interacts with other SUs in two ways:
- A SU can consume messages emitted by other SUs
- A SU can provide messages to other SUs

It follows that any two SUs communicating with each other either directly or indirectly (via a chain of SUs) may need to agree on the message format. The message format which a SU understands is defined in WSDL descriptor which accompanies the SU. The degree of such coupling varies in different arrangements of SUs. On one extreme, the communicating SUs might be completely unaware of the message format. On the other extreme, the communicating SUs might need to know the exact format of the messages. The fact that a web service with ESE does not have a fixed message format may complicate the arrangement of SUs.

The message format coupling between a provider SU and a consumer SU arises when a consumer SUs makes certain assumptions about the message format. In other words, the provider SU must be sure that the message that it sends will be understood by the consumer SU. With ESE in mind, we can think of 4 different arrangements of message<sub>~format</sub>~aware SUs and the corresponding message definitions in WSDL descriptors:
|  | Provider WSDL | Consumer WSDL |
| --- | --- | --- |
| None of SUs support ESE | Strong/weak type definitions | Strong type definitions |
| Only consumer SU supports ESE | Strong/weak type definitions | Weak type definitions |
| Both provider SU and consumer SU support ESE | Weak type definitions | Weak type definitions |
| Only provider SU supports ESE | Weak type definitions | ? |
The strong type definition means the exact message format. The weak type definition means 'any' message format. The strong/weak type definition means that both alternatives are possible. However, the weak type definition should be preferred unless the SU must understand the message. For example, if the provider SU is a Binding Component which just forwards messages to other SUs, then it doesn't need to know very much about the message formats. Using weak type definitions reduces message format couplings between provider SUs and consumer SUs. Note that for SUs supporting ESE it is impossible to have strong type definitions because with ESE a SU can have many formats for the same message.

The most complicated case is when only provider SU supports ESE. In this case the provider SU can emit messages in different formats while the consumer SU can only understand one specific message format. The possible solutions are:
- Implement ESE at consumer SU (the preferable solution)
- Create special-purpose version of provider SU without ESE

Consider a simple case where a web service supporting ESE is exposed via a File BC in OpenESB. We have two SUs. One provider SU implemented with File BC and one consumer SU implemented with Sun JavaEE SE. The consumer SU can accept messages in different formats because of implementation of the web service. The WSDL descriptor of the provider SU must therefore use weak types.
```title
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
            version="1.0"
            xmlns="http://www.objectware.no/frontend/policy/types"
            targetNamespace="http://www.objectware.no/frontend/policy/types">

    <xsd:element name="findPolicy">
        <xsd:complexType>
            <xsd:sequence>
              <xsd:any minOccurs="0"/>
            </xsd:sequence>
        </xsd:complexType>
    </xsd:element>

    <xsd:element name="findPolicyResponse">
        <xsd:complexType>
            <xsd:sequence>
              <xsd:any minOccurs="0"/>
            </xsd:sequence>
        </xsd:complexType>
    </xsd:element>
</xsd:schema>
```
![ese_jbi.PNG](ese_jbi-PNG.md)(ese_jbi.PNG)
