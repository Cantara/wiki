# Clean code measure overview

The purpose of this page is to help people _achieve_ clean code. It is not primarily created as a means for learning, but as a means for teaching/coaching these concepts and as a basis for automation. 

#### In general 

> ℹ️ "You know are working on clean code when each routine turns out to be pretty much what you expected." Robert C. Martin quoted Ward Cunningham on JavaZone 2008. 

- **Boy scout rule**: Always leave a class/function cleaner than you found it. 

- High cohesion, low coupling 

- Don't Repeat Yourself - rule within an application, _guideline_ in a system
    - "_The cost of violating DRY decreases with the distance between the duplications_" quote from Aslak Hellesøy vi Johannes on twitter. 

#### Syntax, formatting guidelines 

- When in doubt, introduce an extra object 

- When in doubt, split the function into smaller functions 

- Max 100 lines per method 

- Max 120 characters per line 

#### Structure, naming and design 

- Let context and encapsulation be reflected in naming 
    - Assume that reader (developer) knows the scope and don't repeat it in all methods. This lets us us shorter names. This tip is useful when writing functional code, but it is perhaps even more useful when writing tests. 

- Single-Responsibility Principle 
    - Don't mix error handling with business logic 

- One level of abstraction per function
    - When reading code it is beneficial to read at one abstraction level at a time. 

- [_Intention revealing interfaces_](http://domaindrivendesign.org/discussion/messageboardarchive/IntentionRevealingInterfaces.html)

- Intention revealing names 
    - [architecture:Ubiquitous Language](../architecture/Ubiquitous-Language.md) 

- Let design decisions be reflected in the _code_. Comments and documentation will always be outdated compared to the code itself. Example: When using the [command pattern](http://en.wikipedia.org/wiki/Command_pattern), let the each command be named *Command. This makes it obvious to the reader how the pattern has been applied. This can dramatically reduce the amount of required documentation. 

- Function arguments - less is more 
    - zero is better than one 
    - one is better than two 
    - use three only as a last resort 
    - 4-n should never be necessary 
    - avoid flag arguments

- Side-effects - No thank you! 

- [CommandQuerySeparation](http://www.martinfowler.com/bliki/CommandQuerySeparation.html)

- Prefer exceptions to error codes 
- Avoid passing null

- [Flattening Arrow Code](http://www.codinghorror.com/blog/archives/000486.html) - Replace conditions with guard clauses, etc. 

- Polymorphism over case and if/else statements 

- Positive conditionals over negative conditionals 

#### Code for maintainability
Even though every 'piece of code' in a system is written 'correctly', the overall maintainability will suffer dramatically if similar problems/solutions are solved utililzing different techniques or technologies. This is particularly true if the code is maintained by someone other than the original authors...

- Do not mix annotations and xml inappropriately
    - SpringMVC: Action-classes through annotations OR xml, not mixed
    - 

- While frameworks may offer many ways of implementing similar problems/solutions, establish which are better and utilize those only (RationalRose: architectual patterns isch)
    - webframeworks: utilize the same mechanisms for validation even though several techniques available
    - 

#### How to work? 

- One change per commit. E.g. fixing indentation and restructuring a method should be two commits. 

- All tests must run always. 

#### Resources 
[Clean Code: A Handbook of Agile Software Craftsmanship](http://www.amazon.com/Clean<sub>~Code</sub><sub>Handbook</sub><sub>Software</sub>~Craftsmanship/dp/0132350882) - by Robert C. Martin

[Clean Code III: Functions](http://javazone.no/incogito/session/Clean+Code+III%3A+Functions.html) - Robert C. Martin at JavaZone 2008
