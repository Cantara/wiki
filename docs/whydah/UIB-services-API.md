# UIB services (API)

### UIB Services

UserIdentityBackend have two type of available services

1. Authenticate applications and users
2. Administration of resources:
   - user(s)
   - application(s)

Details of the API is documented below

---

### Authenticate applications and users

Authentication and authorization are XML over HTTP/HTTPS endpoints. (RPC oriented, not resource oriented.)

1. **Authenticate application** will return an *application* entity if authentication is successful.

- Input: [ApplicationCredential](/web/20210619223228/https://wiki.cantara.no/display/whydah/ApplicationCredential "ApplicationCredential")
- Output: [Application - configuration data for whydah applications](/web/20210619223228/https://wiki.cantara.no/display/whydah/Application+-+configuration+data+for+whydah+applications "Application - configuration data for whydah applications")

2. **Authenticate user** will return a *user* entity if authentication is successful. This operation requires a valid [applicationTokenID](/web/20210619223228/https://wiki.cantara.no/display/whydah/applicationTokenID "applicationTokenID") (application must be authenticated).

- Input: Currently POST is used with [UserCredential](/web/20210619223228/https://wiki.cantara.no/display/whydah/UserCredential "UserCredential") as xml inputstream in the body. Can/should be changed to a GET operation.
- Output: [-UserData-](/web/20210619223228/https://wiki.cantara.no/display/whydah/-UserData- "-UserData-")

|  | [ApplicationToken](/web/20210619223228/https://wiki.cantara.no/display/whydah/ApplicationToken "ApplicationToken") and [UserToken](/web/20210619223228/https://wiki.cantara.no/display/whydah/UserToken "UserToken") is created and managed by [SecurityTokenService] which is the **session controller** in Whydah. |

### Manage user/application credentials

---

### Administration of resources (Resources available for [UserAdminWebApp - UAWA](/web/20210619223228/https://wiki.cantara.no/display/whydah/UserAdminWebApp+-+UAWA "UserAdminWebApp - UAWA") and [UserAdminService - UAS](/web/20210619223228/https://wiki.cantara.no/display/whydah/UserAdminService+-+UAS "UserAdminService - UAS") only

There are four resources available: *user*, *users* (collection of users), *application* and *applications* (collection of applications).   
All require valid applicationToken and valid userToken. For applications without logged in users, an application specific *system* *user* should be used.

UIB will validate the tokens on every request, but is allowed to keep a cache of tokens to reduce number of round-trips to [SecurityTokenService - STS](/web/20210619223228/https://wiki.cantara.no/display/whydah/SecurityTokenService+-+STS "SecurityTokenService - STS"). Caching respects the token timeout values.

###### User

###### Users

###### Application

###### Applications

- List all:

Return [Applications\_json](/web/20210619223228/https://wiki.cantara.no/display/whydah/Applications_json "Applications_json")

- Search for applications. Add when needed

### Health check

- HTTP endpoint available, db, ldap and lucene available.

  - 204 - ok, no content
  - 5xx Server Error - if db, ldap or lucene is not working.

- STS separate test
