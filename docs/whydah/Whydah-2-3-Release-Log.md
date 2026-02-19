# Whydah 2.3 - Release Log

### Key focus/features

- Whydah application to application sessions (to be enhanced in Whydah 2.4 \* with adaptive end-to-end payload encryption)
- Resilience (fallacies of distributed computing)  
  \*UAWA Applications
- ApplicationModel enhancements
- UAWA Import/Export of Users and Applications
- UAWA TAG filters
- UAWA CRM and activity view
- OAUTH2 provider - early release
- DEFCON readiness
- Threat signaling readyness (to be enhanced in Whydah 2.4 with countermeasures)
- Enhanced accessibility of "inner workings" of the platform to simplify monitoring and mainternance

### Whydah 2.3 - Release log

| Version | Main changes | Comment(s) |
| --- | --- | --- |
| 2.3.94 | Fixed bug in anynomous usertoken creation and removed false positive validation errors in logs |  |
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
| 2.3 | Promoted to final 2.3 release |  |
| 2.3.0-rc-7 | Updated more 3rd party dependencies for all modules. More initializing corner cases (NPEs) provoked and handled |  |
| 2.3.0-rc-7 | Upgraded 3rd party dependencies |  |
| 2.3.0-rc-5 | Work on ensuring that the DEFCON is distributed on all cornercases of UserToken distribution |  |
| 2.3.0-rc-4 | more work on corner cases and optimizing the internal whydah session handling (SD and SDK integration) myuri added to UserAdminService properties |  |
| 2.3.0-rc-3 | minor fortifying in SDK mainly |  |
| 2.3.0-rc-2 | Weeded out a was startup snafu in SDK causing slower discovery/was connect |  |
| 2.3.0-rc-1 | Promoted to rc-1 |  |
| 2.3.0-beta-5 | Refactoring and cleanup in SDK systemtests |  |
| 2.3.0-beta-4 | Some enhancements in status/handling of MFA/PIN processes in STS. Added supported userSessionSecurityLevel to Application Model (TypeLib) |  |
| 2.3.0-beta-1 | Promoted to beta-1 release |  |
| 2.3.0-alpha-24 | Minor cleanup and module synchronization with SDK implementation, and smarter backoff/handling of was in modules preventing catch-22 in bootstrapping corner cases |  |
| 2.3.0-alpha-19 | Tweaking the UAS securityfilter with was sessions + security model. Fixed /applications/find/applicationID in UIB |  |
| 2.3.0-alpha-17 | Bugs in UAS "/applications/find" fixed,   "/applications" cache in UAS added   refactoring and cleanup in the SDK vs Admin SDK |  |
| 2.3.0-alpha-11 | Synchronized early preparation to a whydah 2.3 release |  |
| 2.3.0-alpha-9 | Enhanced /health endpoints in modules |  |
| 2.3.0-alpha-8 | Wired securityfilter failures for UIB to threat signals |  |
| 2.3.0-alpha-7 | Minor work on threat signals in SDK and STS |  |
| 2.3.0-alpha-6 | Synchronized early preparation to a whydah 2.3 release |  |
| 2.2.27 | OAuth2 API provider module (simplified API) | https://github.com/Cantara/Whydah-OAuth2Servicehttps://wiki.cantara.no/display/whydah/OAuth2Service |
| 2.2.26 | STS - ThreatSignal view expose the threatsignal log to build understanding of threshhold levels and mappings to DEFCON change actions |  |
| 2.2.25 | Enhanced GUI for application administration in UAWA. |  |
| 2.2.26 | UAWA - new ApplicationDetail admin view |  |
| 2.2.25 | UIB - added async bolk queueing of UserIdentity to lucene index... 3x in throughput for import of users |  |
| 2.2.24 | UIB - LDAP search timeout (1s) could prevent adding new users to large userdatabases (<50k users) fixed |  |
| 2.2.23 | Some sync of STS and UAWA |  |
| 2.2.22 | Typelib completely retrofitted into UIB | New UIB property: ldap.primary.alwayslookupinexternaldirectory=false // set to true if other application is updating the AD/LDAP server |
| 2.2.18 | Performance work on large userdatasets in UAWA, UAS and UIB |  |
| 2.2.14 | UAWA, UAS and UIB enhancement for paginated user-aggregate searches and user import/export enhancements |  |
| 2.2.11 | UAWA remote user search reintroduced to support huge user >1 mill installations | Synced full release. |
| 2.2.10 | UAWA bugfixes | Partially released. |
| 2.2.9 | TAG-filtering in UAWA GUI. | Partially released. |
| 2.2.7 | UAWA User CRM data view (for instances with CRMService). Fixes some special cornercases in user searches. | Must add crmservice property in UAWA to enable displaying crm-data. Partially released. |
| 2.2.6 | UAWA User Activity Log (for instances with StatisticsService) | Partially released. |
| 2.2.5 | Better application tag support in UAWA++, UAWA Application Activity Log (for instances with StatisticsService) Must add statisticsservice property in UAWA to enable application activity log feature. |  |
| 2.2.3 | UAWA - Export and Import Users, corner-case of uawa useraggregate.json mapping found and fixed, mysql support in statisticsservice |  |
| 2.2.2 | Some minor tweaking on ACL for UAWA and 3rd party applications. Signalling STS on userchange/delete to updated active UserTokens |  |
| 2.2.1 | Updating content of active UserTokens if changed through UAS |  |

[Whydah 2.2 - Release Log](/web/20220811081124/https://wiki.cantara.no/display/whydah/Whydah+2.2+-+Release+Log "Whydah 2.2 - Release Log")
