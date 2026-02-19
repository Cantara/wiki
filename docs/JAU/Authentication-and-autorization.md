# Authentication and autorization

## Problem

All clients share the same username and password. Given these credentials client1 can see configuration for client2. This affects */client/registration* and */client/{clientId}/sync*.   
This becomes a problem if clients are preregistered and simple/natural clientIds are used. An attacker with access to the shared username/password can then guess the clientId and get access to another party's ApplicationConfig.

## Roles and access control

| Path | Access | Comment |
| --- | --- | --- |
| /health | Anonymous |  |
| /client/registration | Shared client registration/sign-up credentials | [ConfigService Client API](/web/20210228123831/https://wiki.cantara.no/display/JAU/ConfigService+Client+API "ConfigService Client API"), login.user/login.password |
| /client/{clientId}/sync | client credentials | [ConfigService Client API](/web/20210228123831/https://wiki.cantara.no/display/JAU/ConfigService+Client+API "ConfigService Client API"), clientId/clientSecret |
| All other paths | admin | [ConfigService Admin API](/web/20210228123831/https://wiki.cantara.no/display/JAU/ConfigService+Admin+API "ConfigService Admin API"), login.admin.user/login.admin.password |
|  |  |  |

TODO: CS Dashboard should be possible to set up CS Dashboard with a user which cannot change any data OR a user with rw privileges to enable admin features from CS dashboard.

## How does it work

1. When a new Client is created, a clientSecret string is set using UUID.randomUUID().
   1. /client//registration, the clientSecret is returned to the client and persisted using *ConfigServiceClient.saveApplicationState*. The clientSecret is afterwards included whenever the client *checkForUpdate* (client/{clientId}/sync).
   2. PUT /client/{clientId}
2. The clientSecret is validated when a client calls client/{clientId}/sync. This validation is off by default, but can be enabled with the property *client.secret.validation.enabled*.

## Implementation notes

1. Backward compatible: It should be possible to continue to support the existing behavior. I.e.,
   1. Read login.admin.user and login.admin.password from configservice.properties and create or update these credentials in the database. All permissions for all paths.
   2. Read login.user and login.password from configservice.properties and create or update these credentials in the database. Access to /client.
2. Extend [Preregister Client with specific ApplicationConfig](/web/20210228123831/https://wiki.cantara.no/display/JAU/Preregister+Client+with+specific+ApplicationConfig "Preregister Client with specific ApplicationConfig") to also create a user with username=*clientId* and generate a password if password is omitted?

1. Write clientSecret
   1. ClientResource.registerClient (ClientService.registerClient)
   2. ClientAdminResource.putClient
2. Read
   1. ClientResource.sync
3. Perstence client side
   1. clientSecret is returned from ClientResource.registerClient (in ClientConfig) and persisted by ClientService.saveApplicationState
4. Client secret validation check is feature-toggled using property client.secret.validation.enabled

## Suggestion

Note! Current implementation does not use Spring Security or SQL db.

- Spring security, HTTP Basic authentication
  - <http://docs.spring.io/spring-security/site/docs/current/reference/html/jc.html#abstractsecuritywebapplicationinitializer-with-spring-mvc>
- ~~[JDBC Authentication](http://docs.spring.io/spring-security/site/docs/4.2.2.RELEASE/reference/html/jc.html#jc-authentication-jdbc), PostgreSQL (and H2 for tests)~~

- clientPassword must be set on the client side and provided with every request to /client/{clientId}/sync. Password should be stored on each [Client](/web/20210228123831/https://wiki.cantara.no/display/JAU/Client "Client").

#### Dependencies
