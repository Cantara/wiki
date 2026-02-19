# Whydah 2.1 - ApplicationModel and Administration APIs - Release log

| Version | Main changes | Comment(s) |
| --- | --- | --- |
| 2.0.23-SNAPSHOT | UAS - Initial API complete version. | All UIB references in all modules property-files changed to UAS references |  |
| 2.0-29-SNAPSHOT | STS - Implemented UserToken filterinng for all non fulltoken applications | fulltokenid= in propertyfiles for applications which should have no filter |  |
| 2.0.26-SNAPSHOT | SSOLWA - Implemented application links in sso/welcome controlled by property file settings and layout enhancements | (to be from new ApplicationData structure) |  |
| 2.0-29-SNAPSHOT | STS - Receiving app-filter on UserTokens #12 | New property **fulltokenapplications**= _11,12,15,19_ to list applications who should receive full UserTokens |
|
| 2.0-29-SNAPSHOT | STS - Implemented lastSeen map in STS  #9 | Not persisted yet |  |

 Totto vil prioritere etablering av UAS med alle STS og SSOLogin kall først...  så UAWA kallene..    så nye Import eller AppModel API-er 

---

### Planned milestone modules

- SSOLoginWebApp: [https://github.com/altran/Whydah-SSOLoginWebApp/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs](https://github.com/altran/Whydah-SSOLoginWebApp/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs)
- STS: [https://github.com/altran/Whydah-SecurityTokenService/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs](https://github.com/altran/Whydah-SecurityTokenService/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs)
- UAS: [https://github.com/altran/Whydah-UserAdminService/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs](https://github.com/altran/Whydah-UserAdminService/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs)
- UIB: [https://github.com/altran/Whydah-UserIdentityBackend/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs](https://github.com/altran/Whydah-UserIdentityBackend/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs)
- UAWA: [https://github.com/altran/Whydah-UserAdminWebApp/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs](https://github.com/altran/Whydah-UserAdminWebApp/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs)
- TestWebApp: [https://github.com/altran/Whydah-TestWebApp/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs](https://github.com/altran/Whydah-TestWebApp/milestones/2.1%20-%20ApplicationModel%20and%20Administration%20APIs)
