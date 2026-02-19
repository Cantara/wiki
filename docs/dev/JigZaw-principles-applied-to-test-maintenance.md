# JigZaw principles applied to test maintenance

For the record; no problem is equal to another, there will always be multiple possible solutions to any problem and developers we always have different preferences with regards to how they write and maintain tests. (Yes, I assume you write tests since you have actually come to read this page. :) ) A one-size fits all solution is thus not possible, in my humble opinion. 

However, if you follow the principles of JigZaw, it is possible to give you some hints on how to think when maintaining and evolving your tests. Here goes! 

#### Overlap between unit and service tests 
You will always have (and should always have) overlapping tests, but you should not to test the same aspect more than once. You should also try to find a natural _ordering_ between tests that checks different aspects of some module or code block. (This ordering is often a good basis for mapping to build definitions on a Continuous Integration server.) 

**Example**: a developer will (hopefully) want to write a unit test to verify that a fancy algorithm he has just written works as intended. The algorithm is part of a complex sequence of operations and corresponds to a user requirement to the _service_ under development. The developer then writes a test to verify that this portion of the service works as expected. The two tests overlap, but this is not a bad thing, because their purpose is different. 
If the algorithm is faulty the service will probably not work properly either. The service test is in some way "related" or perhaps "dependent" on the technical unit test. This relationship differs from that between a database test that depends on testDBConnectionOK. The difference being that it makes sense to run the service test even though some unit tests fails. Since the unit test and the service test verifies different aspects the failures also provide different information with regards to what change caused the failure. 

Note! Is is **NOT** necessary to always write a unit test and a service test in this manner. If each unit is really simple, it is often a good idea to only maintain a service test. 

If the service test includes a really complex workflow it might be a good idea to write a simple (unit) test to verify the different branches. Use a mocking framework to create mocks for the commands/operations in each step (if such mocking is not possible, the sequence test should be omitted). Simple sequences/workflows can be verified directly in the service test.
> 📝 
> 📝 
> 📝 h4. Write test code iteratively 
> 📝 
> 📝 When writing code and tests we learn more about the domain, more about the problem and we get better at what we do. This indicates that a choice made six months ago perhaps will be evaluated differently today. The same is true about what tests to write and maintain. If a test gives little value; delete it! It does not matter if it sometime in the past was important. 
> 📝 
> 📝 Another angle on the same concepts is an answer to "when should I refactor my tests?". Refactor your tests when they need to be improved (due to something omitted earlier) or when the code evolve. This means that it is not important if you tests overlap or are sub-optimally structured if the code doesn't change. Improving test code for code that will not be developed further is just wasteful... 
> 📝 
> 📝
