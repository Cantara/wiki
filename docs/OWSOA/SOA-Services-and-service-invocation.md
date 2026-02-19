# SOA - Services and service invocation

|  | **Background** Most developers and architects I meet tend to define **service == protocol endpoint** which **is wrong**. I thought I might open up some eyes by describing the myriad of service invocation options we might have in a service oriented architecture |

work-in-progress...

**Remote invocation options**

- WS-\* (The one and only...)
- REST
- XML over HTTP
- JMS/Messaging

**In process service invocation options**

- stateless service instance (or state to client service instance strategy)
- statefull service instance with collaboration backbone (dist hashmaps, eventing, tuple-spaces...)
- statefull service instance with global state persistence (central DB)
- statefull vertical segmented service instance

**Example of remote service, with endpoint (WS or REST) deployed with the service in a container (typical JEE scenario)**

![service, endpoint and deployment unit](../images/gliffy/3146520-service,-endpoint-and-deployment-unit.png)
