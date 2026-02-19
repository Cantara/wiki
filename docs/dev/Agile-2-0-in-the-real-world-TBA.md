# Agile 2.0 in the real world (TBA)

#### Title 
One idea: _How we successfully rewrote the entire core of a big distributed system_ - an experience report from the real world

#### Highlight Summary

Project mandate: Complete rewrite of major parts of a big, distributed system. 
Necessary? Yes. 
Difficult? Very. 
Costly? Extremely.  
The result? **Priceless!** 

#### Abstract 

In 2006 Telenor Cinclus initiated the largest GPRS-based _Automatic Meter System_ (AMS) project in Europe with over one million meters. The meters are located in Sweden, while the central system is located in Norway. Each meter reports their power consumption for the last 24 hours every night. The result is a distributed system with high performance and stability requirements. 

The original solution had several disadvantages:
- A central component was developed and maintained by an external third party. 
- The solution did not scale according to the increasing number of installed terminals.
- A huge number of servers was required to achieve the necessary performance.
- The solution required too much manual work and interaction, leading to poor testing, data quality etc.
- The solution was too complex to test and deploy, resulting in infrequent system releases.
- The solution took at least one man-week to deploy. 

The new platform was developed in parallel with continued development on the existing platform for an extended period. Change requests (CR) from the customer were implemented in both systems, increasing the total CR cost dramatically. The development team for the new platform was constantly being set to fix bugs in other projects. This made planning difficult. In addition, the system requirements were often changed back and forth, leading to frequent code changes.

This talk is about how Telenor Cinclus approached these challenges, and the experience gained about technical and organizational measures. And no, this is _not_ a textbook example, but yes it was a success! 

#### Language

English 

#### Level 
Intermediate 

#### Outline 

- **The problem**
    - Introduction to Telenor Cinclus and the problem domain 
    - Context: replace core, 3rd party components with in-house developed software
    - Goals and challenges 

- **The measures taken**
    - Scalable architecture (service oriented, asynchronous coupling between collection and validation+persistence, etc.) 
    - Build stability and traceability with Enterprise Maven Infrastructure 
    - More and better testing with test automation according to _JigZaw - Agile Testing done Right_
    - Automated deployment using unix<sub>~maven</sub>~plugin and RPM package management system. 

- **Experiences**
    - Took a long time and cost a lot (avoid parallel development if possible) 
    - Achieved both functional and non-functional goals 
    - Success factors  
        - Good architectural solutions are critical 
        - Good technical solutions are important
        - Organizational changes are required 

#### Equipment

Whiteboard? 

#### Expected audience

Developers and managers who have some experience with projects in the real world and want to get some tips on how to address some common problems. 

#### Speakers 

Ole-Gunnar Westgaard
Role(s) in Telenor Cinclus: Manager Development

Åsmund Sand
Role(s) in Telenor Cinclus: Project manager and team manager
Certified Java 2 Programmer.
PhD in Electrical Engineering from NTNU.

Erik Drolshammer
Role(s) in Telenor Cinclus: Competence Manager Quality Assurance and developer (consultant from Objectware AS)  
Specialization and interests: Advanced continuous integration, automated tests and lightweight architecture.  
Codehaus Mojo Commiter
Master in Computer Science from NTNU.
