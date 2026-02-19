# Roles in agile testing

The purpose of this page is to describe different roles and responsibilities in JigZaw. This may or may not be appropriate for agile development in general. Note that we describe _roles_ and responsibilities, not positions or titles. 

**The _team_ is responsible for producing working software.**

It is as simple as that. How and who does not really matter. In practice different people have different skills and experience, so this is an attempt to ease the transition from a traditional (waterfall and V-model) setup to a more agile process and organization. 

#### Outside the team 

###### Product Owner (PO) 

- Prioritize all functional and non-functional requirements. 
- The architect should be involved in evaluating and formulating all requirements, but especially important for non-functional requirements. 

#### Within the team 

###### Developer 

- Write working software. 
- It is expected that automated tests verify that the functionality works as the developer intend it to work. What type of tests to write and what to test is in practice a programmer decision, but must adhere to non-functional requirements and guidelines from Product Owner and the architect. 

###### Tester 

- Peer program with developers to create good tests.
- Ask the question _how is this requirement verified?_. 
- May consider maintaining a mapping between how a group of automated tests ensure that a certain requirement is fulfilled. (There are ways to implement this in the code and generate a report.) 
- Examples of traditional test work that still makes sense
    - Exploratory testing 
    - User interface testing 
    - TODO Have a session with a "test person" to create a more extensive list of tasks. 

###### Architect 

- Create an architecture with testability attributes suitable to the problem at hand. 
- Help the team choose good designs, tools and test patterns. 
- Manage the balance between cost and risk reduction (writing test is a risk reduction activity). . 
- Avoid micro-managing developers. Mentor and enable developers to ensure their code works as intended. 
- Avoid creating policies and rules that limit developer effectiveness and reduce software quality. 
    - E.g. General rules like "all modules should have 90% test coverage" is not a good idea. A typical consequence of such a rule is tests for trivial functionality like getters and setters. 

#### Project context vs after project delivery 

It may or may not make sense to have a verification phase/step before a final project delivery. Both the team and the customer can decide to do extra quality assurance to reduce risk. This is really a cost vs risk decision. 
The goal of agile development is to minimize and remove this step completely because it is cheaper and more efficient to spend the effort _during_ the project than after.
