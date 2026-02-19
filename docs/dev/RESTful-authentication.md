# RESTful authentication

RESTful web service is stateless, do not use HTTP sessions and will therefore re-authenticate on every request.
Authentication should only be done by a request to the correct URI and all other requests should simply fail with a 401 UNAUTHORIZED status code if the client is not authenticated.

###### Alternatives 

[HTTP Basic authentication](http://en.wikipedia.org/wiki/HTTP_basic_authentication) + SSL, application level 

[Digest access authentication](http://en.wikipedia.org/wiki/Digest_access_authentication), application level 

[TLS client Authentication](http://www.ibm.com/developerworks/lotus/library/ls<sub>~SSL_client_authentication/), Network</sub>~level

###### How to transfer 

1. HTTP Authorization headers 
1. URI query parameters
1. URI path param /\/some/path
    1. Makes authentication more explicit -> builds awareness. 

###### Frameworks and libraries 

- Spring Security (support basic + digest using servlet filters)

- https://github.com/hueniverse/hawk (implementations https://github.com/hueniverse/hawk/issues?labels=port&state=closed)

- https://github.com/hueniverse/oz

- OAth 

###### Resources 

http://mark<sub>~kirby.co.uk/2013/how</sub><sub>to</sub><sub>authenticate</sub><sub>apis</sub><sub>http</sub><sub>basic</sub><sub>vs</sub>~http-digest/

http://stackoverflow.com/questions/14043397/http<sub>~basic</sub><sub>authentication</sub><sub>instead</sub><sub>of</sub><sub>tls</sub>~client-certificaiton
