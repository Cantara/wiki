# Scalability Axiom no 2 - CAP theorem

_What goals might you want from a shared-data system?_

- Strong Consistency: all clients see the same view, even in presence of updates
- High Availability: all clients can find some replica of the data, even in the presence of failures
- Partition-tolerance: the system properties hold even when the system is partitioned

The theorem states that you can always have only two of the three CAP properties at the same time. The first property, Consistency, has to do with ACID systems, usually implemented through the two-phase commit protocol (XA transactions).

**References**
- [http://camelcase.blogspot.com/2007/08/cap<sub>~theorem.html](http://camelcase.blogspot.com/2007/08/cap</sub>~theorem.html)
- [http://highscalability.com/paper<sub>~brewers</sub><sub>conjecture</sub><sub>and</sub><sub>feasibility</sub><sub>consistent</sub><sub>available</sub><sub>partition</sub><sub>tolerant</sub><sub>web</sub><sub>services](http://highscalability.com/paper</sub><sub>brewers</sub><sub>conjecture</sub><sub>and</sub><sub>feasibility</sub><sub>consistent</sub><sub>available</sub><sub>partition</sub><sub>tolerant</sub><sub>web</sub>~services)
- [http://www.cs.berkeley.edu/<sub>brewer/cs262b</sub><sub>2004/PODC</sub><sub>keynote.pdf](http://www.cs.berkeley.edu/</sub>brewer/cs262b<sub>~2004/PODC</sub>~keynote.pdf)
- [http://codahale.com/you<sub>~cant</sub><sub>sacrifice</sub><sub>partition</sub><sub>tolerance](http://codahale.com/you</sub><sub>cant</sub><sub>sacrifice</sub><sub>partition</sub>~tolerance)
