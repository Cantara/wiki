# Tips and tricks when building simple HTTP CRUD services

- Jackson eller Gson for JSON-mapping. 

- DTO / Representation objects to be used when converting to and from JSON. 

- Domain objects and objects related to persistence should not be polluted with JSON or XML mapping. 

- POST 
    - 201 created 
    - URI in the location header 
    - Entity representation in response body (including resource id) 
    - http://stackoverflow.com/questions/1860645/create<sub>~request</sub><sub>with</sub><sub>post</sub><sub>which</sub><sub>response</sub><sub>codes</sub><sub>200</sub><sub>or</sub><sub>201</sub>~and-content
    - http://programmers.stackexchange.com/questions/171122/proper<sub>~response</sub><sub>for</sub><sub>a</sub><sub>rest</sub><sub>insert</sub><sub>full</sub><sub>new</sub><sub>record</sub><sub>or</sub><sub>just</sub><sub>the</sub><sub>record</sub><sub>id</sub>~value
