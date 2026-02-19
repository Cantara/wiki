# Whydah Key Features

|  | Whydah is a light-weight, modular, open source Single Sign-on and Identity and Access Management (IdM, IAM) |

### Key Unique Selling Points

- **Agile, flexible and extendible.** aka. *Developer friendly*
- **Modern micro-service design** (Since Whydah 1.0)\*
- **Support web, apps and desktop applications**, including session handover(s) (Since Whydah 1.3)
- **Easily integrated to project development and CI processes** - IAM/SSO from *day one* (simpler than bake your own)... (Since Whydah 1.0)
- **High scalability and High Availability built-in (Since Whydah 2.0)**
- **Application security model** (Since Whydah 1.0)
- **User-session security elevation** (Will be rewritten and completed in Whydah 2.2)
- **ApplicationManagement** including security *contraints*, routing, (Since Whydah 2.1)
- **Configurable high-security levels on authentication and tokens (Will be completed in Whydah 2.2)**
- **Real-time threat level coordination and responses (Will be completed in Whydah 2.3)**

See [Why choose Whydah?](/web/20210506190255/https://wiki.cantara.no/pages/viewpage.action?pageId=33292322 "Why choose Whydah?") for more about what differentiates Whydah from other alternatives.

---

#### System features

| Feature | Details | Ready for production |
| --- | --- | --- |
| [High Availability](/web/20210506190255/https://wiki.cantara.no/display/whydah/High+Availability+and+Scalability "High Availability and Scalability") | Designed to support a variety of HA configurations out of the box for free |  |
| [High Scalability](/web/20210506190255/https://wiki.cantara.no/display/whydah/High+Availability+and+Scalability "High Availability and Scalability") | Designed with modern micro-services architecture, Whydah will support successful businesses with million of users actively using their services |  |
| [Fallback to secondary identity provider](/web/20210506190255/https://wiki.cantara.no/display/whydah/Integration+with+LDAP+and+Active+Directory "Integration with LDAP and Active Directory") | Use cases vary, so expect to spend some time verifying the concrete setup required. |  |
| Threat level coordination | The registered system threat level is distributed to all Whydah applications so they can take action accordingly |  |
| [System threat mechanisms](../whydah/DEFCON---System-threat-mechanisms.md) | Under construction - planned for Whydah 2.3 |  |

---

#### User-level features

| Feature | Details | Ready for production |
| --- | --- | --- |
| [User Single Sign-On](/web/20210506190255/https://wiki.cantara.no/display/whydah/User+Single+Sign-On "User Single Sign-On") |  |  |
| [User authorization](/web/20210506190255/https://wiki.cantara.no/display/whydah/User+authorization "User authorization") | - Role-based access control - [On-behalf-of relations](/web/20210506190255/https://wiki.cantara.no/display/whydah/On-behalf-of+relations "On-behalf-of relations") |  |
| [User Authentication](/web/20210506190255/https://wiki.cantara.no/display/whydah/User+Authentication "User Authentication") | Supported:    - Whydah username and password - LDAP - AD - Facebook - NetIQ - ADFS (SSOLogin 2.1 or 2.2) - [OAuth 2.0 Google/OpenID](https://developers.google.com/accounts/docs/OAuth2Login)  (SSOLogin 2.1) - MFA/2-factor auth (customer extensions, SSO 2.1) |  |
| [User administration web application](/web/20210506190255/https://wiki.cantara.no/display/whydah/UserAdminWebApp+-+UAWA "UserAdminWebApp - UAWA") | Whydah ship with it's own Admiistration client for ease of use |  |
| [User self-service](/web/20210506190255/https://wiki.cantara.no/display/whydah/User+self-service "User self-service") | - User registration - Reset password |  |
| [UserAdministration API](/web/20210506190255/https://wiki.cantara.no/display/whydah/UIB+services+%28API%29 "UIB services (API)") |  | Enhanced ApplicationModel in Whydah 2.1 |
| Session (user and application) configurable timeout and renew support |  | Renew in Whydah 2.1 |
| Security levels in application sessions and user sessions |  | Whydah 3.0 add *super-secure* levels |

---

#### APPLICATION features

| Feature | Details | Ready for production |
| --- | --- | --- |
| Application Authentication | [UIB Data storage - persistence](/web/20210506190255/https://wiki.cantara.no/display/whydah/UIB+Data+storage+-+persistence "UIB Data storage - persistence") |  |
| Application Sessions | To participate in Whydah, the application must use the authenticated session |  |
| Application Authorization | Whydah have AccessControlList (ACL) on all invocations controlling which applications who can perform privileged operations | ApplicationModel is extended in Whydah 2.1 |
| Application Administration API | [UIB services (API)](/web/20210506190255/https://wiki.cantara.no/display/whydah/UIB+services+%28API%29 "UIB services (API)") -> [UAS services API] | Whydah 2.1 |
| Application Administration WebApplication | [UAS services API] [UserAdminWebApp - UAWA](/web/20210506190255/https://wiki.cantara.no/display/whydah/UserAdminWebApp+-+UAWA "UserAdminWebApp - UAWA") will include extensive administrative operations on Application Management in 2.1 | Extended in Whydah 2.1 |
| Configurable Application session timeout(s) |  |  |
| Configurable Application session security algorithms |  | Planned for Whydah 3,0 |
