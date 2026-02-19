# Tools and implementation

#### Basic implementation requirements

The purpose of this page is to give an overview of the technology that can be employed to implement the JigZaw test strategy. We need support for the following: 

- Support for organizing tests in groups og run code before and after a group of tests  
    - [How to use TestNG groups to implement JigZaw](How-to-use-TestNG-groups-to-implement-JigZaw.md)
    - [How to use JUnit Categories to implement JigZaw](How-to-use-JUnit-Categories-to-implement-JigZaw.md)
- [CI server](../sysadm/Continuous-Integration-Server-Overview.md)
    - [CI recommendations](CI-recommendations.md) 
    - [Organizing Maven projects](Organizing-Maven-projects.md)
- [Control State](Control-State.md) for all stateful systems/service
- [Lightweight alternatives to heavyweight technologies](Lightweight-alternatives-to-heavyweight-technologies.md)

#### Different types of tests 

- [Endpoint tests](Endpoint-tests.md) (Soap, JMS, Rest)

- [Database tests](Database-tests.md)

- [Sequence, flow or dispatcher test](Sequence-flow-or-dispatcher-test.md) 

- [Data-driven testing](Data-driven-testing.md)

- [Excel spreadsheet creation](Excel-spreadsheet-creation.md)

- [Spring IoC wiring test](Spring-IoC-wiring-test.md)

- [Web testing](Web-testing.md) 

- [Record-and-playback test automation](Record-and-playback-test-automation.md)
    - [Skyggedrift](Skyggedrift.md)
