# JigZaw FAQ

#### What _is_ JigZaw? Is it a tool? Is a pattern? Is it Java-specific? 

No it is not a tool, nor a pattern, nor is it a one<sub>~size</sub><sub>fits</sub><sub>all solution. JigZaw is a test model and can be used as framework when designing and discussing tests. While the examples are mostly with Java</sub>~related technology, there is nothing in JigZaw that is limited to Java. 

#### I focus on the customer/users and write end<sub>~to</sub>~end tests for all functionality. When is this approach appropriate? 

One of the core principles of JigZaw is to use [Divide and conquer](Divide<sub>~and</sub><sub>conquer.md) to reduce complexity. Writing _one_ end</sub><sub>to</sub><sub>end test to check all aspects of a service will make the test complex and hard to maintain (see [Single</sub><sub>responsibility principle](Single</sub>~responsibility-principle.md))... Writing multiple service tests to verify different aspects of the service seems like a better idea. **=> One service test per aspect under test**

There is also the question of cost; the time it takes to write the test and to maintain it and the time it takes to run it. If your service in general requires a database, the end<sub>~to</sub>~end test needs (minimum) to set up a connection to a database. Why incur this time penalty if some part of the service can be tested with a simpler and faster unit test? Higher complexity means harder to write and harder to maintain. One big test is more complex than two smaller ones. Ergo, it makes sense to use many simple tests instead of one big. **=> Use the cheapest approach available**

Writing _only_ end<sub>~to</sub><sub>end service tests makes sense only if ALL the functionality **IS** end</sub><sub>to</sub><sub>end. This limits the approach to rather simple problems. Data</sub><sub>driven systems may be a good candidate for such a setup. If the service handles [CRUD](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete), and nothing but CRUD, verifying the state of the data before and after an operation makes very much sense. The test tool [Testaco](http://testaco.org/) was created to support such a use case. Another example can be found in [appassembler</sub><sub>maven</sub><sub>plugin](http://mojo.codehaus.org/appassembler/appassembler</sub><sub>maven</sub><sub>plugin/source</sub>~repository.html). One service in this plugin is to generate start scripts. There is no in-between here; either is the generated script correct or it is not. Verifying the end result, and only the end result, is thus OK. 
**=> Appropriate if data-driven and not too complex**

#### I don't need any fancy test model. If something is too complex I fix my architecture. 

Great! Simplicity is underrated. If you can simplify the architecture or the domain, that is by far the most attractive solution. JigZaw do _not_ advocate designing complex test setups if it can be avoided. JigZaw aims to help you _handle_ complexity in a structured manner. 

#### Should I get rid of all testers and only hire programmers then? 

No! The fact that the test phase before a major release is shorter and less resources is spent in that phase does not mean that you do not need testers. Testers have valuable test expertise and domain knowledge that should be used throughout the whole project, not only in the test phase. 

As a digression, we would like to note that the segregation between **testers** and **developers** is unfortunate. An agile development team needs test and programming expertise and expert domain knowledge to have success. The segregation often leads to the conclusion that only "testers" should do testing and only "programmers" can write functional code. This is wrong and is a obstacle to effective agile development. 

As explained in [Scrum and XP from the Trenches](http://www.infoq.com/minibooks/scrum<sub>~xp</sub><sub>from</sub><sub>the</sub>~trenches) (chapter 14), we suggest that each team should have a team member with expert test skills. An organization with separate departments for test and development might achieve this by putting one tester in each team.
