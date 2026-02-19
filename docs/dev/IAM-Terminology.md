# IAM Terminology

### General terms

| Term | Definition | Comment |
| --- | --- | --- |
| IAM | Identity and access management | [Gartner's definition](http://www.gartner.com/it-glossary/identity-and-access-management-iam/) |
| IdM | Identity management (IdM) describes the management of individual principals, their authentication, authorization,[1] and privileges within or across system and enterprise boundaries with the goal of increasing security and productivity while decreasing cost, downtime and repetitive tasks. | [IdM on Wikipedia](http://en.wikipedia.org/wiki/Identity_management) |
| AM | Access management describes management of individuals authorization and privileges |  |
| SSO | Single Sign on - The user logs on once for multiple applications.   Also includes autentication of users towards backend services. |  |

### SSO terms

| Term | Definition | Comment |
| --- | --- | --- |
| [UserIdentity](/web/20210123074033/https://wiki.cantara.no/display/whydah/UserIdentity "UserIdentity") | This is the user as stored in LDAP and NOT the accesses and roles, which is derived from the user-company contract(s) (employee, member, buyer etc.) [UserIdentityBackend - UIB](/web/20210123074033/https://wiki.cantara.no/display/whydah/UserIdentityBackend+-+UIB "UserIdentityBackend - UIB") |  |
| [UserCredential](/web/20210123074033/https://wiki.cantara.no/display/whydah/UserCredential "UserCredential") | Used for logging on, i.e. username and password |  |
| [UserToken](/web/20210123074033/https://wiki.cantara.no/display/whydah/UserToken "UserToken") | A key given to the applicatin on behalf of the logged on user. | What is the diff between Security token and user token? [Security token on Wikipedia](http://en.wikipedia.org/wiki/Security_token) |
| [UserTokenID](/web/20210123074033/https://wiki.cantara.no/display/whydah/UserTokenID "UserTokenID") | The session-representation for a user-session in Whydah SSO |  |
| [ApplicationCredential](/web/20210123074033/https://wiki.cantara.no/display/whydah/ApplicationCredential "ApplicationCredential") |  |  |
| [ApplicationToken](/web/20210123074033/https://wiki.cantara.no/display/whydah/ApplicationToken "ApplicationToken") |  |  |
| [applicationTokenID](/web/20210123074033/https://wiki.cantara.no/display/whydah/applicationTokenID "applicationTokenID") | The session-token for an application collaborating in the Whydah SSO |  |
| [SSOTicket](/web/20210123074033/https://wiki.cantara.no/display/dev/SSOTicket "SSOTicket") | A one-time handover-token from one application to another to pass along a logged-on user between applications SSO | Also called UserTicket or just Ticket in SSO terminology |

#### External resources

<http://cs.uwsa.edu/IAM/glossary.aspx>
