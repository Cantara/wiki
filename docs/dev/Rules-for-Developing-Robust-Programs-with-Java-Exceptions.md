# Rules for Developing Robust Programs with Java Exceptions

> ℹ️ Exceptions are designed for exceptional situations. 
> ℹ️ - Control of flow must be handled programmaticaly, prohibit your exceptions this luxury.

**Possible emergencies**
- For each module, identify possible emergencies. 
- Define how each module should respond to an undesired event. 

**Generic exception handling**
- Do not catch the generic exceptions. 
    - Let your framework do this for you. Though create nice pages that show good messages to the end user.
- Do not throw the generic exceptions.

**Spesific exception handling**
- Do not use exceptions for control flow. 
- Use exceptions in exceptional situations. 
- Ensure the object is in a stable state after throwing an exception. 
- Create abstract superclasses for related sets of exceptions. 
- Do not leave a catch clause empty. 
- Use separate try blocks for statements that throw the same exceptions. 

**Runtime vs checked expeptions**
- Use runtime exceptions to indicate programming errors. 
- Use checked exceptions for recoverable conditions. 

- Be careful when returning from a try clause with finally. 

*Standard vs custom exceptions
- When available, and suitable, use standard exceptions provided by Java. Do not design you own.
- Use custom exceptions when you have a intended purpose with this exception.

- Do not propagate implementation specific exceptions. 
- Use exception chaining when translating an exception. 
- Use exceptions when a constructor fails. 
- Document the exceptions well. 

- References
    - _Rules for developing robust programs with java exceptions_ by Hoa Dang Nguyen and Magnar Sveen
    - [Best Practice within Java Web Application Development page 60.](http://org.ntnu.no/feta/report.pdf) by Henning Jensen and Erik Drolshammer
