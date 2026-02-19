# Qi4J, EDR, AOP resources

### Recommended reading

#### Qi4j
_I picked Qi4j because it allows me (or it will allow me once I work out the kinks in integrating it with the specific things I want to use like Struts) to focus on the domain and providing a rich environment for the users. I've done the whole Hibernate/Spring/(WebWork|JSF|Struts) thing in the past and the thing that always bothered me is the redundancy and the amount of time I spent on the Hibernate mappings and wiring up Spring properly._

_But what I really liked was the idea of getting rid of the inheritance mess that usually comes with typical OO programming and using Mixins to implement behavior. I see that as probably one of the biggest wins with Qi4j. Then there is the redundancy of defining properties and also having to map them to the backend in a separate metadata file and then also having to worry about constraints and invariants all over the application and not having any reasonable way of putting them all on the entity itself and allowing higher level layers, like the UI, to discover them and provide additional validation controls at that level if that's what they wish._

_I could probably go on and on for quite a while. To put it bluntly, I just really really like a lot of the fundamental principles Qi4j is based on._

- [Introduction to Qi4j](http://www.qi4j.org/introduction.html)
- [JFokus - Presentation: Composite Oriented Programming with Qi4j](http://www.jfokus.se/jfokus08/pres/jf08-CompositeOrientedProgrammingWithQi4j.pdf)

#### EDR
Most enterprises have several systems which own parts of a domain object.The data from these systems might be disjoint, as well as overlapping. The data quality and SLA requirements for each system are often of diversified quality. We need a standardized way to handle multi<sub>~source domain objects, and to extend the Domain repository to handle the real</sub>~world CRUD of todays enterprises.

There seems to be some kind of consensus that one type of SOA services are services that are responsible for the core business objects - and vendors are monitoring and releasing their SOA Data Server products to close the gap. By pioneering the SOA space with EDR, we have gained lots of valuable of experiences of how to solve the Master Data challenges in SOA.

- [EDR](http://wiki.community.objectware.no/display/EDR/Enterprise+Domain+Repository+-+Home)
- [EDR - MDS](http://wiki.community.objectware.no/pages/viewpage.action?pageId=131099)
- [EDR - MDS a less is more approach to MDM (ppt)](http://wiki.community.objectware.no/download/attachments/131099/EDR-MDS+a+less+is+more+approach+to+MDM.ppt)

### Additional reading 

**Enterprise Pojos**
- Link 1
- Link 2

**Qi4J**
- [Rickards Blog](http://www.jroller.com/rickard/)

**EDR**
- [EDR in community wiki](http://wiki.community.objectware.no/display/EDR/Enterprise+Domain+Repository+-+Home)
- [EDR podcast on java.net](http://today.java.net/pub/a/today/2008/06/13/j1<sub>~2k8</sub>~mtT12.html)
- [EDR<sub>~MDS podcast on java.net](http://today.java.net/pub/a/today/2008/06/18/j1</sub>~2k8-mtT13.html)

**Other**

- [Generics, Inversion of Control and Repository<T>](http://andersnoras.com/blogs/anoras/archive/2008/04/03/generics<sub>~inversion</sub><sub>of</sub><sub>control</sub><sub>and</sub><sub>repository</sub>~t.aspx) 
- [More on generics and Inversion of Control](http://andersnoras.com/blogs/anoras/archive/2008/04/06/more<sub>~on</sub><sub>generics</sub><sub>and</sub><sub>inversion</sub><sub>of</sub>~control.aspx)

- [Composite oriented programming to the rescue?](http://hedemark.net/blog/?p=10) 
- [Evolving domain models and processes](http://hedemark.net/blog/?p=23) 

- [AOP](http://en.wikipedia.org/wiki/Aspect-oriented_programming)
