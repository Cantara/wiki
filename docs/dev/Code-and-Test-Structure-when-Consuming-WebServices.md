# Code and Test Structure when Consuming WebServices

DRAFT/brainstorming quality  

### Introduction and problem description

**Scenario**: 
An application that _consume_ a WebService. How to efficiently test our code given the WSDL? 

Isolate the code that use the WebService and write tests for the conversion to our application's domain objects. To verify that our conversion code works as intended we need responses that reflect the responses the WebService would give. We have identified the following approaches:  

1. Record and playback approaches would give the best test coverage, but this approach is fragile. 

2. Automatically generated mocks might be more robust, but how realistic are they really? 

Let's start with the mock approach. 

### Mock approach 

Creating mock responses seem simple enough, but there are some challenges we need to address: 

- How to reduce the pain of WSDL changes? 
    - WSDL changes will always be pain, but can be reduced by following the [OWSOA:Evolving Service Endpoint Pattern](../OWSOA/Evolving<sub>~Service</sub>~Endpoint-Pattern.md). In our scenario we have no control over when or how the WSDL can change, but we need to keep it in mind that it _can_ change and how much pain it will give us when it does. 

- Should we generate the responses or write them ourselves?  
- How to reduce the pain of maintaining the mock responses? 

Given that we can achieve _good enough_ test coverage by generated response mocks, this seems the best solution as it is easier to maintain and cheaper. The problem is then how to generate good mock responses? 

Let's see how [soapUI](http://www.soapui.org) measures up. 

### Record and playback aka. Canned data 

\\
The rest of the code should now be unaffected by the fact that data is fetched from a WebService and unit and service tests can be written as usual. 

### Resources 

[soapUI - Web Service Mocking](http://www.soapui.org/userguide/mock/index.html)
