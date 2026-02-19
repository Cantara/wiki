# JigZaw Introduction

#### Introduction
The [V-model](http://en.wikipedia.org/wiki/V-Model_(software_development)) is a popular approach to testing in a  typical [waterfall](http://en.wikipedia.org/wiki/Waterfall_model) project. With the rising popularity of agile development methodologies like XP and Scrum, the V-model is no longer sufficient. We realized the shortcomings of the V-model while working on a rather complex project in the autumn 2007. Keywords that illustrate the complexity of the project: remoting, integration with multiple external systems, JMS, workflow engine, webstart for deployment, multiple programming languages (C, C++, Java), multiple operating platforms (Solaris, Linux, OSX, Windows) and performance critical data processing. To handle the complexity of this system and make it testable, we developed a new test model more suitable for agile work patterns. A tabular comparison can be found in [V-model vs JigZaw](V-model-vs-JigZaw.md). 

#### Motivation 

We often see 
- enormous unit tests 
- too few integration tests 
- many broken integration tests 
- integration tests are run too seldom
- difficult to determine the problem when a test fails 
- people clinging to their silver-bullet instead of realizing that there actually are more than one type of problem also in testing.  

#### Goals 

What we want 
- a clear separation between the responsibilities of each tests
- multiple simple/cheaper tests than a few big/complex/expensive tests
- to test as much of the system as possible, as often as possible 
- to maximize the value from our testing efforts

[< Back](JigZaw.md) to JigZaw home  [Next >](JigZaw-Design-Principles-and-Drivers.md) Design Principles and Drivers
