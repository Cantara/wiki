# Advanced Spring configuration

## Drivers 

- The generated artifact should be the same regardless of the target environment. This means that any deployment configuration must be run<sub>~time, not build</sub>~time. 
- Keep configuration as close to the bean that needs it as possible. **Self-configuring** beans should be preferred. 
- Minimize the number of properties that _must_ be set in property files.
- Allow full flexibility to override parameters for tweaking the application. 
- **Staging**: Support switching implementations of a service to facilitate development, test and production environments.

## Challenges 

- Switch resources run-time (e.g. datasource) 
- Switch implementations (e.g. to facilitate staging) 
- Authentication and authorization (e.g. username and password to a database) 
- Let system administrators customize and tweak the application 
- Two or more beans share a property (code smell?)
- How to ensure that required properties are set correctly?  
- Readability: It should be easy to see 
    - a) which implementations are used and 
    - b) how these are configured. 

#### Extra Challenges

While out of scope; 
Does the different tactics make it easier or harder to implement a configuration management strategy? 
Distributed systems, robustness and reliability are keywords here. 

## Solutions 

There are two approaches currently available to solve these challenges; 
- Use a combination of PropertyPlaceholderConfigurer, PropertyOverrideConfigurer, Factory-bean and Maven profiles: 
    - [Classic Spring configuration tactics](Classic<sub>~Spring</sub>~configuration-tactics.md)
    - [Deploy to different environments - run<sub>~time](Deploy</sub><sub>to</sub><sub>different</sub><sub>environments</sub><sub>run</sub>~time.md)
- Use [Staged Spring](Staged-Spring.md)

Currently Staged Spring seem to be a much better solution than the classic tactics. There are however a couple of issues that must be addressed to make it enticing also for system administrators. See [ticket 1](http://trac.kaare<sub>~nilsen.com/staged</sub><sub>spring/ticket/1) and [ticket 3](http://trac.kaare</sub><sub>nilsen.com/staged</sub>~spring/report/3).
