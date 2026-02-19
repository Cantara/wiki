# Typical application architecture

Use case: Graphical web application using HTML5 and JavaScript. Needs to use services which expose REST APIs. 

#### Alternative 1: Communicate with backend which in turn fetch data from other services 

![rest-consumer](../images/gliffy/41878558-rest-consumer.png)

###### Pros 

- Do not need [CORS](CORS.md)
- May be easier and faster to implement logic in a language like for example Java than in Javascript. 
    - Authentication 
    - Aggregate data from different services 
    - Expose API tailored for the javascript client, which is not necessarily the same as the API exposed by the CRUD service. 

###### Cons 

- Seems like over-engineering if the endpoint used by the javascript client is identical to the endpoint exposed by the CRUD service. 

#### Alternative 2: Use CORS and communicate directly 

![cors-consumer](../images/gliffy/41878558-cors-consumer.png)

###### Pros 

- Only static resources needs to be served, so can use Apache/NginX instead of Jetty or similar web container. 

###### Cons 

- Need to set up [CORS](CORS.md) 
- Need to implement all logic on client side using javascript. 
- More difficult to build and maintain good, RESTful APIs for CRUD and CRUD2 services? 

###### Some thoughts 

- Most go for alternative 1, with good reason.
