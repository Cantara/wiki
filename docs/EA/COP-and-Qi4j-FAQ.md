# COP and Qi4j FAQ

## COP

###### Q: What is the differences between multiple inheritance and composite?

A: Multiple inheritance (MI) lacks the ability to resolve conflicts, a.k.a the diamond problem. Furthermore, COP incorporates "around aspects", known in our world as "Concerns" as well as "SideEffects" (executed after the completion of the method). COP allows generic (InvocationHandler) implementation of methods, which MI has no way to deal with. And few languages that supports MI has strong "interface" support, which blurs the role interface from the additional methods of more private nature.

## Qi4j

###### Q: In what scenarios are Qi4j especially well suited?

A: The initial goal of Qi4j was to support DDD to a great extent. A lot of inspiration was received from Eric Evans' book. Persistence is central in Qi4j, and is built-in, top-down and a strong model to support it. Another crucial aspect of Qi4j is tool support. Qi4j is done on top of Java to leverage the many tools available, IDEs with good refactoring being the most obvious one, but everything from a capable JVM to various classloading strategies to application servers were part of that picture. Refactoring support is a critical one, as we do modeling directly in code (i.e. by context dependent role interfaces) and models need to be flexible and easily changeable, hence the critical dependency on refactoring support. That is also a main reason for staying away from XML at all levels. It is too early to say exactly where Qi4j will shine and where it will not be a good choice (well, operating systems and its components is pretty bad

Totto says: OW SOA strategies
