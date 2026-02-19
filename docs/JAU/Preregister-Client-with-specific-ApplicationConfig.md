# Preregister Client with specific ApplicationConfig

#### Example use case

Rolling out a new application where clients cannot all use the same configuration. The clientId must be decided before rolling out and the clients will have to send that id in the registerClient request.

#### How

###### Create new ApplicationConfig (see [Create Application and ApplicationConfig](/web/20210228125839/https://wiki.cantara.no/display/JAU/Create+Application+and+ApplicationConfig "Create Application and ApplicationConfig")).

|  | Note that when you POST it to /application/{applicationId}/config that new config will be used by any new clients calling registerClient for that artifactId. |

###### Create client

Create a client json file with clientId and a reference to the ApplicationConfig that should be used. Example file hello-world-client-1.json:

PUT to /client/{clientId}:

###### Add clientId to client distribution

This can vary per application, but for JAU clients add a property configservice.clientid to jau.properties.
