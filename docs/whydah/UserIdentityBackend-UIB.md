# UserIdentityBackend - UIB

## UserIdentityBackend (UIB)

#### Responsibility

The vault of users and applications

###### Details

- Responsible for maintaining a single consistent view for identity and roles for all users and applications.

- **Users**
- **Role storage**
- *applications and application secrets/access info*

- Can integrate with several repositories for identity and role data.
  - User and application identity is typically stored in LDAP or Active Directory.
  - Roles are typically stored in a RDBMS.

- *Import users functionality?*

- HTTP ([level 2](http://martinfowler.com/articles/richardsonMaturityModel.html#level2)) endpoint for integration.

- [Integration with 3rd party identity providers](/web/20221204061157/https://wiki.cantara.no/display/whydah/User+Authentication "User Authentication")

## API overview

#### Security considerations

- See [Whydah production setup](/web/20221204061157/https://wiki.cantara.no/display/whydah/Whydah+production+setup "Whydah production setup") for a graphical overview for a Whydah installation.

- It is recommended to secure UIB as good as possible.
  - Run UIB as non-root user
  - Expose only a single HTTPS endpoint.
  - Borderline security: limit access to only port 443 in firewalls and only allow access from IPaddresses of services that need access(SecurityTokenService IPadress(es) and UserAdminService IP address)
  - Lock down RDBMS, LDAP and AD servers which store the actual data.
    - E.g. Only allow direct connection from localhost.
  - TODO More?

#### Configuration properties

The UIB Artefact contains default properties for the different [IAM\_MODE](/web/20221204061157/https://wiki.cantara.no/display/whydah/IAM_MODE "IAM_MODE")'s being used.

- <- \* Indicates same value as the one to the right.

| Property | Example values PROD  Use external config  Exists as embedded - not recommended | Default values TEST | Default values DEV | Comment |
| --- | --- | --- | --- | --- |
| **prop.type** | PROD | TEST | DEV | [IAM\_MODE](/web/20221204061157/https://wiki.cantara.no/display/whydah/IAM_MODE "IAM_MODE") for this property file |
| **ldap.embedded** | false | true | true | Whether to use the artefact embedded LDAP or not. Typically being used to test. Note that enabled/disabled should not be used. |
| **ldap.embedded.directory** | ~~Not used~~ | bootstrapdata/ldap | target/bootstrapdata/ldap | Directory to store data when using embedded LDAP |
| **ldap.embedded.port** | 10389 | 10389 | 10389 (11389 in template) | The port for embedded LDAP |
| **ldap.primary.url** | ldap://servername:10389/dc=external,dc=WHYDAH,dc=no | ldap://localhost:10389/dc=external,dc=WHYDAH,dc=no | ldap://localhost:10389/dc=external,dc=WHYDAH,dc=no | Primary URL to LDAP server |
| **ldap.primary.admin.principal** | uid=admin,ou=system | <- | <- | ? |
| **ldap.primary.admin.credentials** | secret | <- | <- | ? |
| **ldap.primary.usernameattribute** | initials | <- | <- | ? |
| **ldap.primary.readonly** | false | <- | <- | Enable this if you only want to read information from the ldap server. NOT RECOMENDED |
| **roledb.directory** | ~~Not used~~ | bootstrapdata/hsqldb | bootstrapdata/hsqldb | Folder for bootstrapdata (Using embedded HSQL DB) |
| **roledb.jdbc.driver** | com.mysql.jdbc.Driver | org.hsqldb.jdbc.JDBCDriver | <- | The jdbc driver to use to fetch and store roledata. MySQL or PostgreSQL in prod environment, embedded HSQL in test and dev normally. |
| **roledb.jdbc.url** | jdbc:mysql://datbaseserverurl:3306/databasename | jdbc:hsqldb: <file:bootstrapdata/hsqldb/roles> | <- | The path to the role database being used |
| **roledb.jdbc.user** | sa | <- | <- | The username for the role database |
| **roledb.jdbc.password** |  | <- | <- | The password for the role database |
| **import.enabled** | false | true | true | If enabled, UIB will upon starting, import users and roles specified in the files below. |
| **import.usersource** | prodInitData/users.csv | testdata/users.csv | <- | Users to be imported upon starting UIB |
| **import.rolemappingsource** | prodInitData/rolemappings.csv | testdata/rolemappings.csv | <- | Roles to be imported upon starting UIB |
| **import.applicationssource** | prodInitData/applications.csv | testdata/applications.csv | <- | Applications to be imported upon starting UIB |
| **import.organizationssource** | prodInitData/organizations.csv | testdata/organizations.csv | <- | Organizations to be imported upon starting UIB |
| **useradmin.requiredrolename** | WhydahUserAdmin | <- | <- | Requiered role name in order to use UserAdmin |
| **adduser.defaultrole.facebook.name** | FBData | <- | <- | Default role to be set on a user from Facebook  (Is deprecated, to be set in UserAdminWebApp) |
| **adduser.defaultrole.netiq.name** | Employee | <- | <- | Default role to be set on a user from NetIQ  (Is deprecated, to be set in UserAdminWebApp) |
| **adduser.defaultrole.name** | Employee | <- | <- | Default role name to be set on all new users  (Is deprecated, to be set in UserAdminWebApp) |
| **adduser.defaultrole.value** | 1 | <- | <- | Default value to be set on all new users  (Is deprecated, to be set in UserAdminWebApp) |
| **adduser.defaultapplication.name** | Whydah | <- | <- | Default application name to be added to new users  (Is deprecated, to be set in UserAdminWebApp) |
| **adduser.defaultapplication.id** | 3 | <- | <- | Default application id to be set on new users  (Is deprecated, to be set in UserAdminWebApp) |
| **adduser.defaultorganization.name** | Altran | <- | <- | Default organization name to be set on new users |
| **ssologinservice** | http://myservice.net/sso/ | <http://localhost:9997/sso/> | <http://localhost:9997/sso/> | URI to loginservice |
| **securitytokenservice** | http://myservice.net/tokenservice/ | <http://localhost:9998/tokenservice/> | <http://localhost:9998/tokenservice/> | URI to Tokenservice |
| **myuri** | http://myservice.net/uib | <http://localhost:9995/> | <http://localhost:9995/> | URI to UIB itself |
| **service.port** | 9995 | <- | <- | The port UIB runs on |
| **lucene.directory** | bootstrapdata/lucene | bootstrapdata/lucene | bootstrapdata/lucene | Lucene is used for quick indexing of users |
| **gmail.username** | 123@gmail.com |  |  | Username to gmail account for sending forgot password messages, including @gmail.com |
| **gmail.password** | pw |  |  | Password to gmail account for sending forgot password messages |

#### TODO

1. What RDBMS have been used in production? Which versions? -> Update list above.
   1. MS SQL server
2. What about AD? Used for users only or also roles?
   1. Both as to reflect typical internal uesre and their roles
   2. What is the state of the integration with AD now? Has it been tested lately?
      1. Probably barely working as an LDAP alternative, not used for a long time
3. Design decision: How should be support different RDBMSs?
   1. Bundle supported RDBMSs in the shaded jar? (This is done now.) <-- probably enough for now
   2. Add JDBC drivers to classpath from a known location? (A bit more hassle for installations, possibly less secure)
4. What is the purpose of [UserAdminService - UAS](/web/20221204061157/https://wiki.cantara.no/display/whydah/UserAdminService+-+UAS "UserAdminService - UAS")?
   1. To control and allow some back-office user self-administration features for whydah applications.
   2. Why is [UserAdminWebApp - UAWA](/web/20221204061157/https://wiki.cantara.no/display/whydah/UserAdminWebApp+-+UAWA "UserAdminWebApp - UAWA") allowed to integrate directly with UIB? Why not SSOLoginService and TokenService?
      1. Tokenservice are allowed access, SSOLoginService should not need direct contact to UIB
5. Create issue on github to clean up code (add more tests) to ensure the code reflects the features and decisions described above.
