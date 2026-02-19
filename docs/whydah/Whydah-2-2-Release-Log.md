# Whydah 2.2 - Release Log

### Whydah 2.2 - Application admin support, CRMService and Statistics - Release log

| Version | Main changes | Comment(s) |
| --- | --- | --- |
|  | UAWA - Export and Import Users |  |
| 2.2.2 | Some minor tweaking on ACL for UAWA and 3rd party applications. Signalling STS on userchange/delete to updated active UserTokens |  |
| 2.2.1 | Updating content of active UserTokens if changed through UAS |  |
| **2.2.Final** | RELEASE - finally |  |
| 2.2-rc-27 | Added SSOLWA landing page for signup. UIB log tuning |  |
| 2.2-rc-26 | Enhanced GUI for application administration in UAWA. Added SSOLWA landing page for signup. UIB log tuning | (planned) |
| 2.2-rc-25 | Version sync of all modules. StatisticsService wrapping of valuereporter updated to be a real whydah module |  |
| 2.2-rc-23 | Import and Export of Applications in UserAdminWebApplication. Some fortifications in STS++ on UserCredential and logging |  |
| 2.2-rc-20 | Minor mapping fortification for application and module version sync |  |
| 2.2-rc-17 | Minor toString enhancenent for UserToken (TypeLib) |  |
| 2.2-rc-16 | Minor bug in setting defcon in UserToken (TypeLib) |  |
| 2.2-rc-15 | Tightening up the Application model with separation of 3rd party admin apps and whydah internal admin apps, and supporting anonymous tokens for new sites for an user | Check this section: "security": {   "minSecurityLevel": "0",   "minDEFCON": "DEFCON5",   ...  "userTokenFilter": "false",   "whydahUASAccess": true,   "whydahAdmin": true,  "secret": \*\*\*\* }, |
| 2.2-rc-14 | DEFCON state kept in WhydahApplicationSession. Simple start-implmentation of DEFCON level actions for applications |  |
| 2.2-rc-6 | Lot of small tweaks on application roles and UAS | Minor change in json for applications |
| 2.2-rc-1 | Voted rc1 ready by development team |  |
| 2.2-beta-16 | BugFix NPE in Application parsing in TypeLib |  |
| 2.2-beta-15 | Upgraded web-layer of STS |  |
| 2.2-beta-13 | Updated external dependencies and pom cleanup in TypeLib and SDK |  |
| 2.2-beta-12 | Bugfix in Typelib handling of UserAggregateXml |  |
| 2.2-beta-9 | Flowing DEFCON updates in WAS, wired in SSOLWA and displyed in /health - adjusted /health to json in most components |  |
| 2.2-beta-8 | Typelib - usertoken mapping bugfixes and enhancements, |  |
| 2.2-beta-5 | Typelib - useraggregate mapping bugfixes and enhancements, STS - replaced STS implementations with Typelib implementations |  |
| 2.2-beta-2 | Minor stability fixes in Typelib parsing |  |
| 2.2-alpha-41 | Fixed in whydah session handling (fortification, and added more production audit details to health and logging |  |
| 2.2-alpha-37 | STS - adjusted logging and health for sysadmin purposes and re-used stsToken session | <https://whydahdev.cantara.no/tokenservice/health> |
| 2.2-alpha-36 | sync for beta-readiness |  |
| 2.2-alpha-32 | STS - fixed some update usertoken cases, SDK more systemtests |  |
| 2.2-alpha-31 | STS - bugfixes on usersession time/validation/expiration control |  |
| 2.2-alpha-30 | UAS: property-overide of subject for defined template overrides | Config (useradminservice.properties): email.subject.NewUserPasswordResetEmail.ftl=Whydah - please complete registration |
| 2.2-alpha-29 | SDK: Patches to fix resetUserpassword command. UAS: Allow filesystem override on user email templates and API to pinpoint the email template | UAS template directory: ./tamplates.email |
| 2.2-alpha-24 | Initialization and stability and performance work mainly in SDK and version sync |  |
| 2.2-alpha-17 | Minor tweaks and version sync |  |
| 2.2-alpha-13 | Fixed bug in send delayed mail command and updated external dependencies in Typelib and SDK |  |
| 2.2-alpha-12 | CRMCustomer - added ability to use central whydah mailsending along with local mail client |  |
| 2.2-alpha-11 | UIB - DB - Extend UserRole - RoleValue | ALTER TABLE UserRoles ALTER COLUMN RoleValues TYPE varchar(4096); |
| 2.2-alpha-10 | Typelib - few fixed in mappers, particular for CRMCustomer |  |
| 2.2-alpha-7 | STS - hazelcast 3.6.2 - should fix hazelcast in eu-west-1 |  |
| 2.2-alpha-5 | UIB some bugs in the sesr has set password functionality fixed |  |
| 2.2-alpha-4 | Typelib - bug in parsing roles in UserToken fixed |  |
| 2.2-alpha-3 | SDK - Command to verify us UserTokenID is Whydah User Admin | Note: Tests against   <application ID="2212">  <applicationName>Whydah-UserAdminService</applicationName>  <organizationName>Whydah</organizationName>  <role name="WhydahUserAdmin" value="1"/>  </application> |
| 2.2-alpha-2 | All - added Whydah session status info and added missing /health endpoints to simplify troubleshooting and simplify mainternance of whydah installations |  |
| 2.2-alpha-1 | UAS/UIB - Added password\_login\_enabled |  |
| 2.2-alpha-1 | SDK - Added scheduled sms and mail commands |  |
| 2.2-alpha-1 | STS - Added refresh\_usertoken |  |
| 2.2-alpha-1 | STS - Added support for Anonymous UserTokens for 3rd party applications where the user has no roles | New property ANONYMOUSTOKEN=true to enable this, false by default |
| 2.2-alpha-1 | Java-SDK - Enhancements and bugfixed to WhydahApplicationSession | Now used by most Whydah components |
| 2.2-alpha-1 | Java-SDK - Removed Jersey dependency |  |
| 2.2-alpha-1 | STS - Fixed fallback parsing of ole uderidentity json structure |  |
| 2.2-alpha-1 | Typelib - Enhanced ApplicationCredential added with mappers |  |
| 2.2-alpha-1 | Typelib - CRMCustomer optional data structures added |  |
| 2.2-alpha-1 | STS - PIN-verified signup implemented |  |
| 2.2-alpha-1 | Java-SDK - SendSMSMessage to customer command added | New properties for [config of smsgw](/web/20220811081201/https://wiki.cantara.no/display/whydah/config+of+smsgw "config of smsgw") and template needed to instantiate the service |
| 2.2-alpha-1 | Java-SDK - CRMCustomer commands added |  |
| 2.2-alpha-1 | STS - StatisticsService signals - UserSession CRUD signals added and enhanced |  |
| 2.2-alpha-1 | STS - Valuereporter - Moved to HttpRequest, from Jersey-client |  |
| 2.2-alpha-1 | UAS - Valuereporter - Moved to HttpRequest, from Jersey-client |  |
| 2.2-alpha-1 | SSOLWA - CRMService and Statistics Service support, | New properties for [StatisticsService](/web/20220811081201/https://wiki.cantara.no/display/whydah/StatisticsService "StatisticsService") and [CRMService](/web/20220811081201/https://wiki.cantara.no/display/whydah/CRMService "CRMService") connection(s) |
| 2.2-alpha-1 | STS - StatisticsService signals - UserSession signal | New properties for [StatisticsService](/web/20220811081201/https://wiki.cantara.no/display/whydah/StatisticsService "StatisticsService") connection |
| 2.2-alpha-1 | UAS ~~StatisticsService signals~~ UserLogon signal | New properties for [StatisticsService](/web/20220811081201/https://wiki.cantara.no/display/whydah/StatisticsService "StatisticsService") connection |
| 2.2-alpha-1 | StatisticsService - new StatisticsService established | New optional Whydah module |
| 2.2-alpha-1 | CRMService - new CRMService established | New optional Whydah module |
| 2.2-alpha-1 | SSOLWA/SDK - Functionality for loading StartSSL certificates and enhanced noTLSCheck to sockets since jersey do some checks |  |

---
