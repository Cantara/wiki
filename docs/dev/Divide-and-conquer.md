# Divide and conquer

#### Divide et impera - architecture, implementation and tests 

In JigZaw context, "_Divide and conquer_" is the concept of dividing a problem into sub<sub>~problems until we know how to solve them. This is a well</sub>~known technique for handling something complex and/or complicated. This principle is the cornerstone of the test strategy and is the origin for the name JigZaw. _Jigsav puzzles_ got their name from a painting divided into small pieces with a jigsaw. The same as we do to a complicated test problem; we split it into multiple smaller problems. 

Divide and conquer can be applied the test code, but also on the architecture and the actual implementation code. A typical example of applying this principle is to refactor a [God object](http://en.wikipedia.org/wiki/God_object) and write separate tests for each of the concerns the God object was split into. 

JigZaw promotes the concept of using _tests to drive the development_, but the recommended process is more sophisticated than the [test<sub>~first](http://www.extremeprogramming.org/rules/testfirst.html) principle recommended by eXtreme Programming and TDD. The first part of David Heinemeier Hansson's blogpost [TDD is dead. Long live testing.](http://david.heinemeierhansson.com/2014/tdd</sub><sub>is</sub><sub>dead</sub><sub>long</sub><sub>live</sub>~testing.html) explains some of our objections to the test-first approach. 

###### How small? 
The size of a problem can be measured in many ways and no general rule will be appropriate for every context. However, the following concepts may be useful: 

- [architecture:Clear and consistent responsibility power all great architectures](../architecture/Clear<sub>~and</sub><sub>consistent</sub><sub>responsibility</sub><sub>power</sub><sub>all</sub>~great-architectures.md)
- [Single<sub>~responsibility principle](Single</sub>~responsibility-principle.md)
- Intention Revealing Interface, see Domain-driven Design: Tackling Complexity in the Heart of Software by Eric Evans. 

###### Maven multi-module antipattern? 

For maven users, it is useful to reflect over how _maven multi<sub>~module_ break the concept by allowing several pieces in the puzzle to be altered simultaneously. Unfortunately, the world is not perfect, so you can't have complete freedom and self</sub>~standing quality modules at the same time (the truth holds both for development and in the real world).

#### Historical references and quotes 

The divide and conquer tactic is perhaps best known from [Divide and conquer algorithms](http://en.wikipedia.org/wiki/Divide_and_conquer_algorithm) or the political [Divide and rule](http://en.wikipedia.org/wiki/Divide_and_rule) - _divide et impera_ - strategy. 

###### Quotes on Complexity

---
Back to [JigZaw Design Principles and Drivers](JigZaw<sub>~Design</sub><sub>Principles</sub><sub>and</sub>~Drivers.md)
