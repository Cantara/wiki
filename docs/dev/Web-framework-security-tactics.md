# Web framework security tactics

### Possible pitfalls of Web Application Frameworks

Webapp security should take into consideration the different frameworks that are used to develop the application. The frameworks influence the application not only with preexisting code and design, but also by changing the mindset of developers. Developers can be mislead into thinking their application is secure and that the framework will e.g. hinder SQL-injection.

### Efforts that mitigate pitfalls

In order for some level of assurance to be acheived it is necessary to conduct a security evaluation of the framework prior to usage. This evaluation should consider the design and implementation of security measures and whether or not they are easy to use. A well defined API interface is important if it is to be used by developers with little or no knowledge of security lingo. When security measures are easy to use and are "self explainatory" they leave little room for error. There should be a clear connection between what is expected and what is actually provided.

### Sources of information

Paper that evaluates different frameworks according to Common Criteria, highlights whether or not the measures are easy to use and if configuration is required for the measures to function:

[Mandatory Security Measures In Web Applications](http://org.ntnu.no/websec/project.pdf) - Thomas Pronstad and Vegar Westerlund

[Web Application Exception Management](Web<sub>~Application</sub>~Exception-Management.md). How you handle exceptions and what information you expose it tightly coupled to security.

[OWASP](http://www.owasp.org). The Open Web Application Security Project; lists common vulnerabilities and projects that implements best practices security measures.

[Common Criteria](http://www.commoncriteriaportal.org/). A specification framework which gives best practices in how to handle assurance and security. _Warning, this is heavy reading_

http://searchsoftwarequality.techtarget.com/news/article/0%2c289142%2csid92_gci1321417%2c00.html 

[Security recommendations for web application frameworks](Security<sub>~recommendations</sub><sub>for</sub><sub>web</sub>~application-frameworks.md)
