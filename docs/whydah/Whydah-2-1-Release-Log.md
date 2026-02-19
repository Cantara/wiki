# Whydah 2.1 - Release Log

### Whydah 2.1 - ApplicationModel and Administration APIs - Release log

| Version | Main changes | Comment(s) |
| --- | --- | --- |
| 2.1-beta-11 | UIB - Postgresql support |  |
| 2.1-beta-10 | complete sync with some small adjustments |  |
| 2.1-beta-8 | SSOLWA - fixed bug with text in action redirects for SessionCheck=true requests |  |
| 2.1-beta-7 | SDK - Enhanced WhydahUserSession with re-establish application session after unsuccessful renew session several times in a row and enhanced hasActiveSession in WUS and WAS |  |
| 2.1-beta-7 | STS - Minor enhancements to /health endpoint |  |
| 2.1-beta-7 | STS - hazelcast config now updated to hazelcast 3.5 | NB config changes |
| 2.1-beta-6 | STS - implemented application session renewal | Not using params from Application Model yet |
| 2.1-beta-6 | SSOLWA/SDK - integrated WhydahApplicationSession for automatic application session management |  |
| 2.1-beta-6 | SSOLWA - added resource guard on configurable features in login and signup |  |
| 2.1-beta-2 | SSOLWA/STS - Implemented /health endpoint |  |
| 2.1-beta-2 | UAWA - Shortening and mouseover for rolename and rolevalues to keep display tidy |  |
| 2.1-beta-2 | SSOLWA - Filter og TAGS=HIDDEN in welcome |  |
| 2.1-beta-2 | UAS - Implemented missing update role in UAS |  |
| 2.1-beta-2 | SSOLWA - CSRFtoken and fixed in signup form |  |
| 2.1-beta-1 | UAS - Signup password mail fixed |  |
| 2.1-ALPHA-20 | UAS - TypeLib integration completed |  |
| 2.1-ALPHA-20 | UAS - UserAggregate GET and POST |  |
| 2.1-ALPHA-18 | UAS/UIB - Fixed forgotten password |  |
| 2.1-ALPHA-17 | SDK - enhanced WhydahApplicationSession and WhydahUtil to use ApplicationCredential to keep the ApplicationName through the session (mostly for logging purposes) |  |
| 2.1-ALPHA-17 | UIB/UAS Application search against applications lucene index implemented |  |
| 2.1-ALPHA-13 | UAWA - editing of the fullTokenApplication parameter enabled in GUI |  |
| 2.1-ALPHA-13 | STS - lastSeen endpoint implemented, Command in SDK for use |  |
| 2.1-ALPHA-13 | STS - not\_in\_use stuff deleted |  |
| 2.1-ALPHA-13 | STS - removed last traces of UIB configuration and use |  |
| 2.1-ALPHA-12 | SSOLWA/STS - completed implementing coordinating securitylevel and DEFCON in UserToken |  |
| 2.1-ALPHA-11 | SSOLWA: fixed so signup return to login page | should probably end in a registration successful page, with info about password mail and info on Whydah and link to login after password reset action |
| 2.1-ALPHA-11 | Minor adjustment in bootstrap data |  |
| 2.1-ALPHA-10 | Minor bugfixes and code cleaning | handling of proxy installations which terminate tls |
| 2.1-ALPHA-9 | Minor bugfixes and code cleaning |  |
| 2.1-ALPHA-8 | UAS/UIB - Mailsending moved from UIB to UAS | Migration: provision mail config in UAS config/properties and not in UIB config/properties |
| 2.1-ALPHA-5 | ALL - New default application IDs for the Whydah components | A merge strategy is needed for upgrades. Easiest is to provision the old application IDs vy updateing in applications.json and import it in UIB |
| 2.1-ALPHA-5 | UAS/UIB - UAS-UIB filter implemented | Only UAS can now call UIB |
| 2.1-ALPHA-5 | UAS/UIB New implementation of Security Filter(s) | Note: STS properties need temporarily to have UIB appid and secret in property file - removed from propertyfile in ALPHA-11 |
| 2.1-ALPHA-5 | STS - Now using Applications mastered by UIB as well as provisioned applications | Provisioned applications (STS properties) is deprecated and will be removed |
| 2.1-ALPHA-5 | UIB - LDAP - ldap schema adjustments | Note that this release change the default domain for LDAP-users from external.WHYDAH.no to peolpe.whydah.no. To preserve backward compability the property ldap.primary.url must be set in useridentity.properties to f.eks ldap://localhost:11389/dc=external,dc=WHYDAH,dc=no |
| 2.1-ALPHA-5 | CoreLibs: ApplicationCredential updated with required applicationName |  |
| 2.1-ALPHA-4 | UAWA: New Application List, view application detail, edit and update application details. |  |
| 2.1-ALPHA-3 | SSOLWA, UAS: Use Whydah SDK for Hystrix Commands |  |
| 2.1-ALPHA-3 | All: Common Whydah TypeLib |  |
| 2.1-ALPHA-3 | New: Whydah TypeLib introduced |  |
| 2.1-ALPHA-3 | SSOLWA: CSRF implemented, more web security robustness changes |  |
| 2.1.ALPHA-2 | 1. UIB and UAS: CRUD for application (json) 2. UIB: Simplify storage of application data (only tested for HSQLDB!) 3. SDK: API implemented as Hystrix Commands with system tests and Util convenience and session manager threads for application and user sessions in SDK 4. UIB: Use DTO and json parsing logic from SDK for Application CRUD endpoint 5. UIB: new config strategy (using Constretto) 6. UIB: dependency upgrade (Jersey, replaced Guice with Spring, ++) 7. UAS: test and bugfix of user functions used bu UserAdminWebapp |  |
| 2.0.32-ALPHA | All Modules on same Release. Introduced Whydah-Java-SDK. | Ensuring that all modules are coordinated,and may be used for client installation.The SDK will, when stable be great benefit for client applications wanting to connect to Whydah. |
| 2.0-29-SNAPSHOT | STS - Implemented lastSeen map in STS #9 | Not persisted yet |
| 2.0-29-SNAPSHOT | STS - Receiving app-filter on UserTokens #12 | New property **fulltokenapplications**= *11,12,15,19* to list applications who should receive full UserTokens |
| 2.0.26-SNAPSHOT | SSOLWA - Implemented application links in sso/welcome controlled by property file settings and layout enhancements | (to be from new ApplicationData structure) |
| 2.0-29-SNAPSHOT | STS - Implemented UserToken filterinng for all non fulltoken applications | fulltokenid= in propertyfiles for applications which should have no filter |
| 2.0.23-SNAPSHOT | UAS - Initial API complete version. | All UIB references in all modules property-files changed to UAS references |
