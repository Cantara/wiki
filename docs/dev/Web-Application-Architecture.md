# Web Application Architecture

### Some classic patterns of web applications

These are fairly well documented in some [Excellent Books](Excellent-Books.md). We recommend that you make yourself familiar with the basic patterns, then follow through by using an existing [Java Web Framework](Java-Web-Frameworks.md). Do NOT attempt to create your own web framework before you really really know what you are doing.

- MVC 
    - Model 
    - View 
    - Controller - Input Controller 

- Front Controller 
    - Command Pattern 
    - Intercepting Filters (filter chain) 

- Application Controller 

- Template view 

### Layers

Web applications tend to follow the pattern of Marinescu layers (with some naming from Fowler): 

Presentation 
Presentation(Application Controller) 
Service Layer 
Domain Model 
Persistence / data source 

##### Maven modules 

Maven modules are used to separate according to _dependencies_. Java packages are used to group according to _function_ (see [Structuring packages and contexts](Structuring-packages-and-contexts.md)). 

**Essence: Use packages to seperate function. Use modules to seperate layers AND domains.**

- domainImpl, domainAPI
- repository (API) 
- daoImpl
- daoMock 
- controller 
- web (web.xml, jsp, _js which calls java code_)
- taglib 
- resources (images, html, javascript, css, velocity, freemarker - use filter) 
- jsp-fragments (JSP-files must use war overlay, see [Web Application Fragments](Web-Application-Fragments.md)) 

_Click the diagram to view full size_
**[Diagram: Maven](../Diagram/Maven.md)**

### Use of Session

#### Some clear advice
Do not allow the use of the HttpSession to trickle down beyond your web layer (see [Structuring packages and contexts](Structuring-packages-and-contexts.md)).

#### Some questions you should ask yourself

We advise that the application is architectured with a clear policy on how to manage session. Here are some questions you should consider:

- where should it be available? 
- what parameters to send in the session 
- session hijacking? 
- Use of cookies.
- How much state do you allow in the session, and what are the consequences of having too much?
- How do you manage the session (transparent, actively, do you use a SessionContainer object?)
- Is it possible to do conversation scoping/bijection?

### Use of intermediary objects and form backing objects

What are the ups and downs of using them as opposed to using domain objects directly in the web layer?

### Mapping patterns to Struts2 notes

We took a look at some classical patterns from MVC and Fowler..

- MVC 
    - Model - domain 
    - View - results (jsp, freemarker) backed by formBean (action) 
    - Controller (actions)
        - Input Controller - implemented with Interceptors and/or in Actions 

- Front Controller - FilterDispatcher; configured in struts.xml
    - Web handler 
    - Command Pattern  
- Intercepting Filters (filter chain) is called Interceptor _stack_ 
- Application Controller - FilterDispatcher; configured in struts.xml
- Template view - results 

Input controllers and app controlls should be stricly held in the web module/presentation layer.

Features:
-navigation
-command mapping
-result mapping
-type conversion

The reason is that they often depend on things that are web-specific (urls, string values, etc).

The Commands are strictly held in the controller module/application layer.

Features on this leve.
-validation
-execution

Keeping web-awareness out of your controller layer is a Good Thing.
