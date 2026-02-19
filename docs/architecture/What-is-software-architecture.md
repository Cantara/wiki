# What is software architecture?

First we need to define what "software architecture" means, and this is no easy task :-)

Martin Fowler discusses some definitions in his [Who needs an architect?](http://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf) article. One definition is the following:

The architecture of a software system (at a given point in time) is its organization or structure of significant components interacting through interfaces, those components being composed of successively smaller components and interfaces. 
--RUP/IEEE

Fowler seems to agree with [Ralph Johnson](http://en.wikipedia.org/wiki/Ralph_Johnson) (of GoF fame), that it is important to understand that there is also a social aspect to software architecture, as described below. Ralph Johnson provides 3 definitions of software architecture:

1) In most successful software projects, the expert developers working on that project have a shared understanding of the system design. This shared understanding is called 'architecture.' This understanding includes how the system is divided into components and how the components interact through interfaces. These components are usually composed of smaller components, but the architecture only includes the components and interfaces that are understood by all the developers.

2) Architecture are the decisions that you wish you could get right early in a project.

3) Architecture is about the important stuff. Whatever that is. 
--Ralph Johnson

###### What is good software architecture?

A good software architecture must ensure that the system is designed in such a way that both the functional and non-functional requirements of the system are met. [Grady Booch](http://en.wikipedia.org/wiki/Grady_Booch) coined the term **FURPS** as a mnemonic for the different categories of system requirements:

- **Functional** — features, capabilities, security. 
- **Usability** — human factors, help, documentation. 
- **Reliability** — frequency of failure, recoverability, predictability. 
- **Performance** — response times, throughput, accuracy, availability, resource usage. 
- **Supportability** — adaptability, maintainability, internationalization, configurability. 

In addition, there might be requirements such as:
- **Re<sub>~use</sub>~ability** - whether parts of the system should be designed to be re-used by other applications.
- **Operations support** - functionality and qualities that ensure that the application can be managed and monitored satisfactory in its operational setting.

The "goodness" of an architecture should always be measured against the requirements. A simple design with poor scalability qualities might be the correct architecture in one case, and a very wrong architecture in another. 

###### Architecture principle index

{contentbylabel:architecture_principle|maxResults=99|operator=AND|excerpt=true|showLabels=false|showSpace=false}
