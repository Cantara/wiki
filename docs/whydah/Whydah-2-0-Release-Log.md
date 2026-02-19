# Whydah 2.0 - Release Log

| Version | Main changes | Comment(s) |
| --- | --- | --- |
| 2.0.1.Final | BUGFIX/ADDON: Added property support to installations which had issues with special TLS/SSL certificates |  |
| 2.0.Final |  |  |
| 2.0-rc-5 | Some minor tuning of sso/welcome and install-id prefixing of hazelcast channels |  |
| 2.0-rc-4 | Fixed some references in UserToken, BugFix on personRef in UIB, fortification of provisioning scripts |  |
| 2.0-rc-3 | [UserToken](/web/20220811081314/https://wiki.cantara.no/display/whydah/UserToken "UserToken") rewrite in STS to restore support for multiple roles per application ref [STS #14](https://github.com/altran/Whydah-SecurityTokenService/issues/14). Tighter cookie handling in UAWa and SSOLoginWebApp |  |
| 2.0-rc-2 | Release\_usertoken/user session on logoutaction in SSOLogin. UAWA cookie handling and role verification. UAWA encoding issues fixed. Dependencies upgraded. |  |
| 2.0-rc-1 | BUG in UIB enabling duplicate users from 3rd party tokens fixed. Some GUI fixed in UAWA |  |
| 2.0-beta-1 | Facebook login fixed, deleted old unused code in UserAdmin, fixed cookie/SSO functionality in SSOLoginWebApp |  |
| 2.0-alpha-16 | High-Availability/cluster configuration (SSOLoginWebApp and SecurityTokenService) | see documentation   \* [SSOLoginWebApp HA configuration (AWS ELB and Apache front)](/web/20220811081314/https://wiki.cantara.no/display/whydah/SSOLoginWebApp+HA+configuration+%28AWS+ELB+and+Apache+front%29 "SSOLoginWebApp HA configuration (AWS ELB and Apache front)")   \* [SecurityTokenService HA configuration (AWS EC2 Hazelcast)](/web/20220811081314/https://wiki.cantara.no/display/whydah/SecurityTokenService+HA+configuration+%28AWS+EC2+Hazelcast%29 "SecurityTokenService HA configuration (AWS EC2 Hazelcast)") |
| 2.0-alpha-15 | consistent trailing slash on all URI paths in property files | Clients: Must update properties files locally. |
| 2.0-alpha-14 | Refactoring: Consistent naming of terms in tokens and UAWA naming cleanup | [ApplicationToken diff](https://wiki.cantara.no/pages/diffpages.action?pageId=38437471&originalId=38963284)   [UserToken diff](https://wiki.cantara.no/pages/diffpages.action?pageId=37388753&originalId=38963281) |
| 2.0-alpha-13 | DEFCON security awareness skeleton implemented | [DEFCON concept background](http://2014.javazone.no/presentation.html?id=b7ab616e) |
| 2.0-alpha-12 | SecurityTokenService internal structure refactoring, hazelcast in STS upgraded apacheds to 2.0m16 | [Embedded config](https://github.com/altran/Whydah-SecurityTokenService/blob/master/src/main/resources/hazelcast.xml) |
| 2.0-alpha-11 | Refactoring: snake\_case in public API to minimize misunderstandings | [API diff](https://wiki.altrancloud.com/pages/diffpages.action?pageId=33915690&originalId=38963189) |
| 2.0-alpha-10 | internal naming convension refactoring |  |
| 2.0-alpha-9 | refactoring: SecurityTokenService , from /token to /user in public API |  |
| 2.0-alpha-8 | Application ID and secret implementation | Clients: Must update properties files locally. |
| 2.0-alpha-4 | NetIQ redirect verification filter | [Property example](https://github.com/altran/Whydah-SSOLoginWebApp/blob/master/src/main/resources/ssologinwebapp.PROD.properties) |
| 2.0-alpha-3 | ticket => userticket refactoring |  |
| 2.0-alpha-2 | New UserAdminWebApp application |  |
