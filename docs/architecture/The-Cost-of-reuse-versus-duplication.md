# The Cost of reuse versus duplication

> When should developers try to make re-usable components that can be used by other IT projects? And who should pay for the development of these components?

The **cost** of making a component **reusable** can be split into

1. maintaining a separate project structure
2. maintaining a separate release cycle
3. writing more generic code than the current project actually needs (remember reuse != framework)
4. more QA
5. risk of changes made for one project affecting another project adversely (see above)
6. refactoring across non-snapshot dependencies (in Maven) require more work (but in a TDD-world, this ensures better quality

The **cost of duplication** can be split into

1. maintaining test-suites of all the duplicated code
2. maintenance and verification of consistency and correctness and QA between the duplicated code
3. risk of bugs having to be fixed many times
4. larger total code base
5. change ability and evolve ability of the duplicated code
6. lack of good tool support for refactoring
7. design and architecture degradation

In the article [The Hidden Cost of Reuse](http://www.informationweek.com/708/08iuhid.htm) in InformationWeek, Allan Radding points to studies that indicate that reusable code is about three times as expensive to develop (and probably to maintain) as one-off code. In [Facts and Fallacies of Software Engineering](http://www.amazon.com/exec/obidos/ASIN/0321117425/), Robert Glass makes the same assessment.
