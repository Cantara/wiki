# JigZaw TimeLine 2

### Shorter test phase 

Test-Driven Development tries to get us to integrate automated tests into the early parts of the project. However, since developers doing TDD often encounter problems keeping their tests running and well managed throughout a project, Agile projects often give up maintaining their tests, and spend their efforts in the good old test phase, usually spoiling the iteration rythm and pushing the project over budget.

TDD means that functionality and tests are written (and committed) together. All code is then accompanied by unit tests and service tests. We also recommend writing system tests iteratively, so for each added feature the corresponding system test suite is extended as well. This allows us to shorten the test phase and spend more time creating value for the customer. JigZaw enables TDD and keeps it going throughout the **entire** project by providing concepts and techniques for grouping and categorizing tests, as well as inspiring cleaner test code and better test architecture.

Ideally, the test phase could be omitted all together, but in practice we need some time to write and run additional system and acceptance test to stabilize everything before a major release. The time spent in each phase with the waterfall model and with JigZaw and agile development is shown below: 

![test.phase.timeline](test<sub>~phase</sub>~timeline.md)(../images/gliffy/16515318-test.phase.timeline.png)

### Conclusions 

A transition from waterfall to JigZaw as test strategy will give the following changes visible from "outside the box": 

- Less time spent in the acceptance test phase. 

- Testing is done iteratively (which reduces risk and total cost) 

- Test skills are needed through the whole project, not only before a release, so it is often a good idea to have at least one person on each team with good test skills.  

```

{section}
{column}
h4. Spend less time on integration testing.
{gliffy:name=JigZaw reasoning|size=S|align=left}
{column}
{column}
h4. Test categorization
{gliffy:space=dev|page=JigZaw Test Levels|name=test.aspects|size=M|align=left}
{column}
{section}

```
