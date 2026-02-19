# Tools and implementation

#### Basic implementation requirements

The purpose of this page is to give an overview of the technology that can be employed to implement the JigZaw test strategy. We need support for the following: 

- Support for organizing tests in groups og run code before and after a group of tests  
    - [How to use TestNG groups to implement JigZaw](How<sub>~to</sub><sub>use</sub><sub>TestNG</sub><sub>groups</sub><sub>to</sub>~implement-JigZaw.md)
    - [How to use JUnit Categories to implement JigZaw](How<sub>~to</sub><sub>use</sub><sub>JUnit</sub><sub>Categories</sub><sub>to</sub>~implement-JigZaw.md)
- [CI server](../sysadm/Continuous<sub>~Integration</sub>~Server-Overview.md)
    - [CI recommendations](CI-recommendations.md) 
    - [Organizing Maven projects](Organizing<sub>~Maven</sub>~projects.md)
- [Control State](Control-State.md) for all stateful systems/service
- [Lightweight alternatives to heavyweight technologies](Lightweight<sub>~alternatives</sub><sub>to</sub><sub>heavyweight</sub>~technologies.md)

#### Different types of tests 

- [Endpoint tests](Endpoint-tests.md) (Soap, JMS, Rest)

- [Database tests](Database-tests.md)

- [Sequence, flow or dispatcher test](Sequence<sub>~flow</sub><sub>or</sub><sub>dispatcher</sub>~test.md) 

- [Data<sub>~driven testing](Data</sub>~driven-testing.md)

- [Excel spreadsheet creation](Excel<sub>~spreadsheet</sub>~creation.md)

- [Spring IoC wiring test](Spring<sub>~IoC</sub>~wiring-test.md)

- [Web testing](Web-testing.md) 

- [Record<sub>~and</sub><sub>playback test automation](Record</sub><sub>and</sub><sub>playback</sub><sub>test</sub>~automation.md)
    - [Skyggedrift](Skyggedrift.md)
