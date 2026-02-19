# Whydah 2.5 - Release Log

### Whydah 2.5 - Release log

**Release log**

| Version | Date | Main changes | Comment(s) |
| --- | --- | --- | --- |
| 2.5.70 | 2020-09 | SSOLWA - support for pre-configured users/personas to simplify service-development and testing of SSO solutions where processes spans several users. OAUTH2 some minor adjustment to support more logout scenarios. Monthly dependency (JavaZone edition) and security patch update |  |
| 2.5.60 | 2020-08 | monthly dependency and security patch update |  |
| 2.5.57 | 2020-07 | monthly dependency and security patch update |  |
| 2.5.55 | 2020-06 | Pre-July 2021 Security release including full Open ID Connect Support in the OAUTH2 service |  |
| 2.5.43 | 2020-06 | OAuth2Service - A transitive last-minute vuln dependency snuk in, thus fast-patching OAuth2Service out-of-cycle |  |
| 2.5.42 | 2020-06 | June 2020 security release. Added OpenID Connect provider support to OAuth2Service |  |
| 2.5.41 | 2020-05 | May 2020 security release and minor tweaks on health endpoint reporting to align with Visuale |  |
| 2.5.37 | 2020-04 | monthly dependency and security patch update |  |
| 2.5.36 | 2020-04 | UIB only patch to fix haelth-check constantly missing admin-user lookup loping, and a workaround for re-syncing large LDAP databases to index |  |
| 2.5.35 | 2020-03 | monthly dependency and security patch update |  |
| 2.5.34 | 2020-02 | monthly dependency and security patch update |  |
| 2.5.33 | 2020-01 | spring framework vuln hotfix - security patch update |  |
| 2.5.31 | 2020-01 | monthly dependency and security patch update |  |
| 2.5.30 | 2019-12 | monthly dependency and security patch update |  |
| 2.5.27 | 2019-11 | some fixes and cleanup in SSOLWA, monthly dependency and security patch update |  |
| 2.5.25 | 2019-10 | monthly security patch update |  |
| 2.5.24 | 2019-08 | added support for paging LDAP queries to support connecting and indexing large LDAP directories/organizations and some minor hazelcast dependency updates |  |
| 2.5.22 | 2019-08 | monthly security patch update and stabillity fixes on UAWA user export with strange data in roles |  |
| 2.5.15 | 2019-07 | monthly security patch update and java 11+ updates |  |
| 2.5.13 | 2019-06 | monthly security patch update and minor UI updates in UAWA for user searches for large installations |  |
| 2.5.12 | 2019-05 | monthly security patch update |  |
| 2.5.11 | 2019-04 | security patching of dependencies |  |
| 2.5.10 | 2019-03 | security patching of dependencies |  |
| 2.5.9 | 2019-01 | security patching of dependencies |  |
| 2.5.8 | 2018-11 | security patching of dependencies |  |
| 2.5.7 | 2018-10 | security patching of dependencies |  |
| 2.5.6 | 2018-10 | security patching of dependencies |  |
| 2.5.3 | 2018-10 | Minor fixes to log configuration |  |
| 2.5.1 | 2018-09 | UIB Bugfix, avoiding application copies in the application search index |  |
| 2.5 | 2018-08 | Promoted to 2.5 release |  |
| 2.5-rc-3 | 2018-08 | Typelib - patch to handle more semantic Tags |  |
| 2.5-rc-2 | 2018-08 | SSOLWA - bug discovered in signup fixed,  STS - smarter handling of large threat signal maps for mis-configured environments and environments under attack,  CRMService - fixed a hazelcast initialization issue and some refactoring |  |
| 2.5-rc-1 | 2018-08 | Initial release candidate |  |
| 2.4.19 | 2018-08 | Minor security dependency bump and some small corner-case bugfixes and optimizations |  |
| 2.4.18 | 2018-08 | Dependency bump for spring and fixed a mysql issue in statisticsservice introduced in 2.4.16 |  |
| 2.4.16 | 2018-08 | Sync release of a few minor fixes including better usage statistics for users and applications in UAWA and CRM-info previews |  |
| 2.4.11 | 2018-07 | Fix for broken "New Application" function in UAWA |  |
| 2.4.10 | 2018-07 | Replaced old dependencies in UAWA with Admin SDK commands. Whitelisting more special characters for Firstname, LastName++ |  |
| 2.4.9 | 2018-07 | Minor patches |  |
| 2.4.8 | 2018-06 | UIB - support for re-creating user-index from LDAP added, refactoring of the timestamp baseclass implementations |  |
| 2.4.7 | 2018-06 | STS/Typelib bug preventing user sessions over 27h fixed, UIB thread bug which might cause double application in application index fixed |  |
| 2.4.6 | 2018-06 | Patched jackson dependency, fixed a bug in UserTokenLifespan handling preventing long SSO sessions | STS tokenmap need to be reset |
| 2.4.5 | 2018-05 | Hardening STS handling of session lifespan config parameters, minor code cleanup/refactoring's, synchronized release |  |
| 2.4.1 | 20180503 | Minor bugfix to application session lifespan handling, and security patching of UIB |  |

### Key focus/features (planned)

- OAUTH2 provider - release
- Support for Single-Page Applications, with SPAProxyService and Whydah Single Page Application javascript library

**Planned ideas and tasks**

| Version | Main changes | Comment(s) |
| --- | --- | --- |
| 2.5 | Encrypted user tokens | encrypted JWTtokens in SPAProxyService |
| 2.5 | JWT provider support | part of SPAProxyService |
| 2.5 | Single-page Application support | part of SPAProxyService |

#### Non-coordinated/matured modules

| Module | Version | Date | Comment |
| --- | --- | --- | --- |
| Whydah-OAuth2Service | 0.13 | August, 2018 | Working Early Beta - will be production stabilised/versioned after more real-world integration testing |
| Whydah-SPAProxyService | 1.2.0 | February, 2019 | Working Early Beta Release - will be production versioned after more real-world integration testing |
