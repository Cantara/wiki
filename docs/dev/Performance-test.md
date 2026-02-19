# Performance test

See [Wikipedia: Software performance testing](http://en.wikipedia.org/wiki/Software_performance_testing) for an introduction to the subject. 

This page is about discussing different strategies and their pros and cons. 

#### Run a browser, Selenium 2

Selenium 2 (with webdriver) + The grinder can be used for both functional and non-functional testing. 

One of the drawbacks using this approach for performance testing is the browser dependency. I.e., 

1. the application under test must support a browser which the test clients can run. E.g. if the test clients run Firefox on Linux, the application under test must support firefox. 
1. Running multiple browsers are resource intensive. This adds cost, but may be mitigated by using e.g. [grinder in the cloud](http://www.jk-itberatung.de/grinder/GrinderInTheCloud-linux.pdf) or [Xvfb](http://en.wikipedia.org/wiki/Xvfb). 

#### Tool approach (JMeter, LoadRunner, etc)

+ Can hire professional testers 
+ Short ramp-up time 

\- Recording strategy: Often necessary to record anew for every tiny change to the user interface 
\- Recording strategy: Often difficult to add custom data providers or logic 
\- Ajax support? (Meter does not execute the Javascript found in HTML pages.)
\- Often difficult to debug when something is not working as expected. 
\- The commercial tools require licenses and training 
\- the GUI clients is resource intensive (JMeter has a non-GUI mode)

#### Custom (only http requests) 

+ Resource efficient, really low test clients hardware requirements 
+ Not restricted by client-side validation code (can be utilized for security testing)
+ Excellent support for custom logging, tracing and debugging information 
+ Can automate statics and report creation 
+ Can implement any strategy 

\- No library or framework available, must write it yourself.
