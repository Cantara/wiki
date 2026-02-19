# Whydah 2.4 - Release Log

### Whydah 2.4 - Release log

### Key focus/features

- Maintenance release - lots of internal quality rework
- Replaced inner-workings with domain-driven security white-listing matched against the domain concepts
- Whydah application to application sessions with adaptive end-to-end payload encryption)
- OAUTH2 provider - enhancements
- JWT token support++ for SPA applications in SPAProxyService
- DEFCON change alerts with suggested actions (probably mail/sms) - to observe and verify/match the suggested actions to real-life situations

#### Non-coordinated/matured modules

| Module | Version | Date | Comment |
| --- | --- | --- | --- |
| Whydah-OAuth2Service | 0.11.10 | December 4th, 2017 | Working PoC - will be production stabilized after more real-world integration testing, planned Q2-2018 |
| Whydah-SPAProxyService | 0.3.10 | April 14th, 2018 | Working PoC/MVP - will be production stabilized after real-world integration testing, planned Q2-2018 |

### Release log

| Version | Main changes | Comment(s) |
| --- | --- | --- |
|  |  |  |
| 2.4.19 | Minor security dependency bump and some small corner-case bugfixes and optimizations |  |
| 2.4.18 | Dependency bump for spring and fixed a mysql issue in statisticsservice introduced in 2.4.16 |  |
| 2.4.16 | Sync release of a few minor fixes including better usage statistics for users and applications in UAWA and CRM-info previews |  |
| 2.4.11 | Fix for broken "New Application" function in UAWA |  |
| 2.4.10 | Replaced old dependencies in UAWA with Admin SDK commands. Whitelisting more special characters for Firstname, LastName++ |  |
| 2.4.9 | Minor patches |  |
| 2.4.8 | UIB - support for re-creating user-index from LDAP added, refactoring of the timestamp baseclass implementations |  |
| 2.4.7 | STS/Typelib bug preventing user sessions over 27h fixed, UIB thread bug which might cause double application in application index fixed |  |
| 2.4.6 | Patched jackson dependency, fixed a bug un UserTokenLifespan handling preventing long SSO sessions | STS tokenmap need to be reset |
| 2.4.5 | Hardening STS handling of session lifespan config parameters, minor code cleanup/refactoring's, synchronized release |  |
| 2.4.1 | Minor bugfix to application session lifespan handling, and security patching of UIB |  |
| 2.4 | Released |  |
| 2.4-rc-2 | Minor updates and dependency cleanup, tighter was thread handling |  |
| 2.4-rc-1 | First release candidate |  |
| 2.3.100 | Minor maintenance adjustments updated to get ready for 2.4 alpha |  |
| 2.3.94 | Fixed bug in anonymous usertoken creation and removed false positive validation errors in logs |  |
| 2.3.92 | Fixed bug if setting applicationsesstionexpires to high in property |  |
| 2.3.90 | Minor adjustments tp LastName and DefaultRolenames definitions |  |
| 2.3.84 | Internal bottom-up quality work |  |
| 2.3.75 | Tweaking the domain-driven security whitelisting |  |
| 2.3.68 | Replaced all inner-workings of Whydah with domain-driven security implementation, enforcing strict white-listing on all data matched against the domain concept | might be som corner-cases we've not discovered yet |
| 2.3.44 | Squashed a few bugs in cache invalidation in UAS and applied more domain-driven security to key parts | should be worth a go |
| 2.3.38 | Enhanced the time-fields in typelib to smart-fields to remove pain/failure points | released to simplify in-the-wild test/verifications |
| 2.3.37 | Initial work on domain-driven security for Whydah key objects in typelib | released to simplify in-the-wild test/verifications |
| 2.3.31 | Post-pentest patch-release |  |
| 2.3.27 | Synchronized maintenance release | - tweaking logs and health for easier maintenance |
| 2.3.23 | Synchronized maintenance release | - to be penetration tested by third party |
| 2.3.22 | Synchronized maintenance release with lots of minor fixes |  |
| 2.3.20 | completed the embedded crypto handling on receiving payload in all hystrix commands |  |
| 2.3.19 | resilience in unstable network situations for application session handling by fail fast on application auth between sts and uas... (same should be implemented between uas and uib) |  |
| 2.3.18 | now with initial crypto key per application session exchange and configuration of super-secure applications |  |
|  | STS - using the testpage=enabled flag to choose verbose info in health (so it won't show in production setups) testpage=enabled for verbose info in /health |  |
|  | SDK and STS - early work on payload encryption and cryptokey rotation |  |
| 2.3.11 | SDK work on smarter and non-blocking session resilience |  |
| 2.3.5 | STS - properties for default user and application sessions | Extra properties application.session.timeout=120, user.session.timeout=240 |
| 2.3.4 | STS - forced removal and cleanup of expired sessions | Partially released |
| 2.3.3 | UAS/STS - enhancments on false threatSignal positives and obfuscating the session id's | Partially released |
| 2.3.2 | UIB - enhanced application search index and UAS wiring | Partially released |
