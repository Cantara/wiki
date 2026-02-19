# Contributing to Whydah

### Whydah development Express-route for linux and osx/mac

|  | Pre-requisites: JDK 8, maven 3 and wget installed |

1. run bootstrapAndRunWhydah.sh (wget <https://raw.githubusercontent.com/Cantara/Whydah/master/dev-quickstart/bootstrapAndRunWhydah.sh>) which will do the following
   1. clone all main Whydah repositories
   2. build all modules on local machine
   3. start all built modules in a TEST\_LOCALHOST configuration
2. verify that it is working before starting to code (<http://localhost:9997/sso/welcome> u:useradmin pw:useradmin567)

|  |  |
| --- | --- |
| Whydah modules  - [SSOLoginWebApp - SSOLWA](/web/20230928103921/https://wiki.cantara.no/display/whydah/SSOLoginWebApp+-+SSOLWA "SSOLoginWebApp - SSOLWA") - [SecurityTokenService - STS](/web/20230928103921/https://wiki.cantara.no/display/whydah/SecurityTokenService+-+STS "SecurityTokenService - STS") - [UserIdentityBackend - UIB](/web/20230928103921/https://wiki.cantara.no/display/whydah/UserIdentityBackend+-+UIB "UserIdentityBackend - UIB") - [UserAdminService - UAS](/web/20230928103921/https://wiki.cantara.no/display/whydah/UserAdminService+-+UAS "UserAdminService - UAS") - [UserAdminWebApp - UAWA](/web/20230928103921/https://wiki.cantara.no/display/whydah/UserAdminWebApp+-+UAWA "UserAdminWebApp - UAWA") - [TestWebApp](/web/20230928103921/https://wiki.cantara.no/display/whydah/TestWebApp "TestWebApp") - [Whydah Typelib](/web/20230928103921/https://wiki.cantara.no/display/whydah/Whydah+Typelib "Whydah Typelib") - [Whydah Client SDK](/web/20230928103921/https://wiki.cantara.no/display/whydah/Whydah+Client+SDK "Whydah Client SDK") - [StatisticsService](/web/20230928103921/https://wiki.cantara.no/display/whydah/StatisticsService "StatisticsService") - [CRMService](/web/20230928103921/https://wiki.cantara.no/display/whydah/CRMService "CRMService") - [Whydah deployment alternatives](/web/20230928103921/https://wiki.cantara.no/display/whydah/Whydah+deployment+alternatives "Whydah deployment alternatives") | Key Whydah Data Structures  - [User Data Structures](/web/20230928103921/https://wiki.cantara.no/display/whydah/User+Data+Structures "User Data Structures") - [Application Data Structures](/web/20230928103921/https://wiki.cantara.no/display/whydah/Application+Data+Structures "Application Data Structures") |

|  | **Whydah development 911** If you have trouble getting Whydah to run locally, it is usually one or more of the following problems  1. You have inconsistent applicationID and applicationSecret between the modules - check this first 2. You have inconsistency/error in the URL links between the components 3. You have error in how you start the modules, leaving you running on a different set of properties/configuration than you expected   Watch the module logs to figure out where the problem is located. |

### The source code and issue trackers

|  | Source Code | Issue Tracking | Maturity |
| --- | --- | --- | --- |
| Super-module | <https://github.com/cantara/Whydah> | <https://github.com/cantara/Whydah/issues> |  |
| [SSOLoginWebApp - SSOLWA](/web/20230928103921/https://wiki.cantara.no/display/whydah/SSOLoginWebApp+-+SSOLWA "SSOLoginWebApp - SSOLWA") | <https://github.com/cantara/Whydah-SSOWebApplication> | <https://github.com/cantara/Whydah-SSOWebApplication/issues> |  |
| [SecurityTokenService - STS](/web/20230928103921/https://wiki.cantara.no/display/whydah/SecurityTokenService+-+STS "SecurityTokenService - STS") | <https://github.com/cantara/Whydah-SecurityTokenService> | <https://github.com/cantara/Whydah-SecurityTokenService/issues> |  |
| [UserIdentityBackend - UIB](/web/20230928103921/https://wiki.cantara.no/display/whydah/UserIdentityBackend+-+UIB "UserIdentityBackend - UIB") | <https://github.com/cantara/Whydah-UserIdentityBackend> | <https://github.com/cantara/Whydah-UserIdentityBackend/issues> |  |
| [UserAdminService - UAS](/web/20230928103921/https://wiki.cantara.no/display/whydah/UserAdminService+-+UAS "UserAdminService - UAS") | <https://github.com/cantara/Whydah-UserAdminService> | <https://github.com/cantara/Whydah-UserAdminService/issues> |  |
| [UserAdminWebApp - UAWA](/web/20230928103921/https://wiki.cantara.no/display/whydah/UserAdminWebApp+-+UAWA "UserAdminWebApp - UAWA") | <https://github.com/cantara/Whydah-UserAdminWebapp> | <https://github.com/cantara/Whydah-UserAdminWebapp/issues> |  |
| [Java-SDK - SDK] | <https://github.com/cantara/Whydah-Java-SDK> | <https://github.com/cantara/Whydah-Java-SDK/issues> |  |
| [TypeLib - TypeLib] | <https://github.com/cantara/Whydah-TypeLib> | <https://github.com/cantara/Whydah-TypeLib/issues> |  |
| [TestWebApp](/web/20230928103921/https://wiki.cantara.no/display/whydah/TestWebApp "TestWebApp") | <https://github.com/cantara/Whydah-TestWebApp> | <https://github.com/cantara/Whydah-TestWebApp/issues> |  |

###### Maven

<http://mvnrepo.cantara.no/content/repositories/releases/net/whydah/>

Example:

Unknown macro: {code}

<dependency>  
<groupId>net.whydah.identity</groupId>  
<artifactId>UserIdentityBackend</artifactId>  
<version>X.Y.Z</version>  
</dependency>

**[Versions](/web/20230928103921/https://wiki.cantara.no/display/whydah/Whydah+Releases "Whydah Releases")**

###### Example applications which integrate with Whydah

- [Whydah-TestWebApp](https://github.com/cantara/Whydah-TestWebApp) (java, spring, javascript, django and SharePoint app example integrations)
- [Awesome Competence System](https://github.com/cantara/Awesome-Competence-System)

**See [Integrating with Whydah](/web/20230928103921/https://wiki.cantara.no/display/whydah/Integrating+with+Whydah "Integrating with Whydah")**
