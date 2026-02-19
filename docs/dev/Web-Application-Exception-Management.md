# Web Application Exception Management

- Catch exceptions where you can do something about them (or let them propagate all the way up to the top level handler). 

- Categorization 

- Catch ALL exceptions at the top level of the application 
    - nice message to the user 
    - log as much info as possible to the appropriate log. See [Web Application Logging](Web-Application-Logging.md)

### What kind of exceptions should you make yourself?

Here are some examples..

- ExternalServiceException (abstract) 
- One subclass of the above for each external service or system you integrate with.
- According to log levels 

- Wrap ugly exceptions (Spring and Hibernate, for instance, do this nicely for SQLException).

### Resources 

[Error Handling And Exception Management](Error-Handling-And-Exception-Management.md)

### A funny exception

While attempting to save this page and moving it between spaces at the same time, we got this javascript-error from Confluence after saving:

![wiki-exception.png](16515260-wiki-exception.png)

Is this a nice message to the user?  ;)

We can see here that Confluence does have a top-level exception handler for AJAX actions. This is important to remember, because your normal exception filter/interceptor probably doesn't handle this.
