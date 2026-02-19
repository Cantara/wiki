# Scalability Axiom no 2 - CAP theorem

_What goals might you want from a shared-data system?_

- Strong Consistency: all clients see the same view, even in presence of updates
- High Availability: all clients can find some replica of the data, even in the presence of failures
- Partition-tolerance: the system properties hold even when the system is partitioned

The theorem states that you can always have only two of the three CAP properties at the same time. The first property, Consistency, has to do with ACID systems, usually implemented through the two-phase commit protocol (XA transactions).

**References**
- [http://camelcase.blogspot.com/2007/08/cap-theorem.html](http://camelcase.blogspot.com/2007/08/cap-theorem.html)
- [http://highscalability.com/paper-brewers-conjecture-and-feasibility-consistent-available-partition-tolerant-web-services](http://highscalability.com/paper-brewers-conjecture-and-feasibility-consistent-available-partition-tolerant-web-services)
- [http://www.cs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf](http://www.cs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf)
- [http://codahale.com/you-cant-sacrifice-partition-tolerance](http://codahale.com/you-cant-sacrifice-partition-tolerance)
