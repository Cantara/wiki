# Enterprise POJO

Enterprise POJO is not really a term, but we have coined this term to have a starting point of a discussion on the topic of weather there are differences between application objects (POJO) and the objects we use in enterprise development.

Quite few of the objects in a typical application will be Enterprise POJOs. Most objects of will be private to one application. But the objects that are shared between two applications and the objects that are shared across a large number of applications in the enterprise must be treated differently. The fact that more systems depend on the same objects means we have to deal with a lot more problems. "Enterprise POJOs" is a term we use to discuss these issues. An "Enterprise POJO" is an object that is being used by (many systems? more than one system?) in the enterprise.

For Enterprise POJOs, dealing with change is the most important issue. Changes will affect many system, and the systems might want to adopt these changes at different times. Simplicity, understandability, etc will have to be sacrificed in order to support change across multiple system.

As enterprise systems are long lived, an important source of savings comes from identifying systems that can be taken out of commission and no longer maintained. The problem of many interoperating systems often means we need to introduce indirection layers. However, each layer of indirection will make it harder to identified information that is no longer needed.

| Prioritized feature | [POJO](http://en.wikipedia.org/wiki/POJO)  (Fowler et al) | Enterprise POJO (#GeekCruise) |
| --- | --- | --- |
| 1 | [Understandability](/web/20210124121444/https://wiki.cantara.no/display/EA/Understandability "Understandability") | [Modifiability](/web/20210124121444/https://wiki.cantara.no/display/EA/Modifiability "Modifiability") |
| 2 | [Simplicity](/web/20210124121444/https://wiki.cantara.no/display/EA/Simplicity "Simplicity") | [Understandability](/web/20210124121444/https://wiki.cantara.no/display/EA/Understandability "Understandability") |
| 3 | [Modifiability](/web/20210124121444/https://wiki.cantara.no/display/EA/Modifiability "Modifiability") | ~~[Simplicity](/web/20210124121444/https://wiki.cantara.no/display/EA/Simplicity "Simplicity")~~ *AsSimpleAsPossible* |

The reasons why we have a change in the prioritization for enterprise POJOs are

- They are by *default* remote (By this we mean that their common characteristics is that they are used across system boundaries, not that they necessary extends serializable or provide remote proxies)
- They have more **external dependencies**. (parts, systems, applications)
- They are exposed to extreme **frequent changes** in the requirements (world around them changes more frequently than the application itself.)
- They need to support non-deployment changes/updates (which has never been simple).

**So the enterprise POJO is a contradiction in terms, as an enterprise POJO will never be able to actually be implemented as an POJO**

### Some discussions

Q: Is really combining state and behavior (as in OO) a good idea for evolvabillity?  
A: As you change the behavior of an object, you explicitly introduce a data-migration process on the state of the object, and it does not seem as a sensible idea to move to a more loosely coupled strategy. What might be in sight for the future, is a mechanism to explicitly add the transition-of-state concept as a language feature.

Q: What about EJBs, Hibernate-objects, Domain-objects?
