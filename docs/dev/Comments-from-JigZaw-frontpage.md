# Comments from JigZaw frontpage

Totto: 

http://en.wikipedia.org/wiki/Model-based_testing

---

Mads Nissen: 

On the subject of test project organization (folder/package structure) I've been experimenting with BDD-style syntax to provide a more fluent guide into test behaviour:

**Assembly/component:**
MyComponent.Tests
**Package/namespace:**
.In_MockedContext.Given_CustomerRepository
**TestFixture:**
Get_Should
**TestMethod:**
Return_One_For_GetById

In test reports this produces nice statements that describe the tests:
MyComponent.Tests.In_MockedContext.Given_CustomerRepository.Get_Should.Return_One_For_GetById
MyComponent.Tests.In_SAP_IntegrationContext.Given_CustomerRepository.Get_Should.Return_One_For_GetById
MyComponent.Tests.In_SQL_IntegrationContext.Given_CustomerRepository.Get_Should.Return_One_For_GetById
etc. etc.

However after a while of implementing various tests at different levels I find that this syntax works well for System tests (high-level black box), but that it renders as complete nonsense (so far) for low level tests.

1. Is "in_mocked_context" just rubbish because this is really just unittests?
1. Shouldn't tests in different contexts just be designed for wiring with some IoC container?
    1. If so; how to structure the tests that test the stuff that gets wired

wow. I just confused myself.

---

Erik D in reply to Mads: 

It is nice to read that there are others that are thinking about how to improve how we work in this area. 

While I'm not completely sure what you are asking here, I'll try to comment. 

Note on BDD: 
My experience with BDD-style naming is that often becomes too verbose. One trick is to multiple classes for the tests and put common context information into the name of the test class. I also prefer to use the BDD-syntax only on methods that map directly to the domain and not on "technical" tests. For example could _Should.Return_One_For_GetById_ be replaced with getCustomerByIdOK. 

1. In my implementations of JigZaw I try to reduce to use of mocks as much as possible. I find that the need for mocks can in many cases by eliminated by a different design and that the changes often lead to reduces coupling and improves cohesiveness. 

2. 

This subject is often easier to understand if we discuss concrete examples. According to JigZaw the different context part is only relevant when we are writing **service** and **system** tests (i.e. not unit tests).

There are multiple ways to implement the different context part depending on the actual problem. E.g. if data should be different in different contexts, the _dataprovider_ concept in TestNG can be used. Another example is to test with different DBMSs, which can be done with Maven profiles. 

I see now that there are to much to discuss here to efficiently communicate via comments. Give me a call or send me an email if you want to discuss these topics further. :)
