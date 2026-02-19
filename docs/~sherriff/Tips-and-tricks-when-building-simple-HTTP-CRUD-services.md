# Tips and tricks when building simple HTTP CRUD services

- Jackson eller Gson for JSON-mapping. 

- DTO / Representation objects to be used when converting to and from JSON. 

- Domain objects and objects related to persistence should not be polluted with JSON or XML mapping. 

- POST 
    - 201 created 
    - URI in the location header 
    - Entity representation in response body (including resource id) 
    - http://stackoverflow.com/questions/1860645/create-request-with-post-which-response-codes-200-or-201-and-content
    - http://programmers.stackexchange.com/questions/171122/proper-response-for-a-rest-insert-full-new-record-or-just-the-record-id-value
