# Deploy to different environments

## Problem description 

Projects are often deployed to multiple different environments. By "deploy" we do not mean the process of publishing an artifacts to a repository, but deploying an application to for example a application<sub>~, portlet</sub>~, or servlet-container or just installing the application in the staging or production environment. Environments that need special treatment can be 

- **Different types**: dev, test/staging, prodtest, prod
- **Different operating systems** (OS): Windows XP, Windows Vista, OSX, Linux 1, Linux 2, Solaris
- **Different DBMS**: In-memory, Standalone, Clustered 
- **Different implementations of Java EE functionality**: in-memory, provided by a standalone product (requires Spring?), provided by an application server

## Solution drivers 

#### Separate environment dependent and environment independent code 

There is always a good idea to try to separate code that depend on a specific environment and code that do not. This makes it easier to isolate the differences between environments and makes it easier to choose and implement a deployment strategy. Always look for refactoring opportunities first, before implementing any of the other approaches! 

#### Test vs deployment

It is a common mistake to let a solution that supports _test_ in different environments transform into a solution for _deploy_ to different environments. These are separate concepts and should be treated as separate concepts! The main difference is that developers and the Continuous Integration (CI) server handles testing, while system administrators are responsible for deploy. Test is thus done at **build<sub>~time**, while deploy creates a **run</sub>~time** environment. (Even though it often is possible to test deploy to different environments with a CI server.) 

It is easy to mix these two concepts. E.g., what is is called when you want to test an application with a standalone database and JMS implementation instead of the in<sub>~memory solutions used during development? AFAIK, there is no straight answer to this question; a run</sub>~time approach, a build-time approach or a mix might be appropriate. 

Regardless of classification there are a couple of recommendations that you always should follow: 

- Never put authentication information to an external system into the VCS. 
- _mvn clean install_ should always build cleanly when java and maven are set up correctly.
- Developers are lazy. Always make it easier to "do the right thing" than do it quick<sub>~and</sub>~dirty. 
- System administrators are not developers and cannot be expected to understand your application. Try to make their job as simple as possible. 
 

IMHO, testing can utilize build<sub>~time approaches, while deployment should use the run</sub>~time approach. 

## Implementations 

We have identified the following approaches: 

[Deploy to different environments - run<sub>~time](Deploy</sub><sub>to</sub><sub>different</sub><sub>environments</sub><sub>run</sub>~time.md)

[Change environment at build<sub>~time using profiles](Change</sub><sub>environment</sub><sub>at</sub><sub>build</sub><sub>time</sub>~using-profiles.md)

[Per<sub>~deployment projects](Per</sub>~deployment-projects.md)

Run [Jetty with pre<sub>~populated local HSQLDB](Jetty</sub><sub>with</sub><sub>pre</sub><sub>populated</sub><sub>local</sub>~HSQLDB.md)
