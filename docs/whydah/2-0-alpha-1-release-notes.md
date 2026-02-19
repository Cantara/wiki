# 2.0-alpha-1 release notes

Work has been going on to prepare for this release the last half year, we are therefor happy to finally present it.  
Release date: 22.08.2014

### Vision

The vision for this release was to re-create and vastly improve the API of UIB in such a way that it allow for easier integration and better maintenance of users and applications.   
User admin web app was also given a major upgrade.

### Highligts

##### New UIB API

- API re-factored, see the details of the [UIB services (API)](/web/20201126072928/https://wiki.cantara.no/display/whydah/UIB+services+%28API%29 "UIB services (API)")
- Application authentication early implementation
- Real applicationID, applicationName, orgName and roleNames throughout Whydah modukles

##### New user UserAdminWebApp

We rewrote the admin web app from scratch using Angular.js, in addition with the new API from UIB it is:

- Stable and more effective to work with
- More appealing look and feel
- Better protection towards finger trouble. I.e. list of available roles and organisations and prompt before deleting a role for a user.
- Better scalability in both number of users and number of roles per user.
- Bulk user password reset
- Bulk user add role
- Application administration, see highligh below

##### Application administration

- Get a list of approved applications

#### Other items

- Refactored netiq implementation
- Refactored UIB security filter
- Using HTTP Status codes as request feedback

#### Key knows issues

- Add and remove applications using the UserAdmin interface. (Scheduled for 2.1)
- Applications will be given an application id and an application secret. (Scheduled for 2.1)
- Add and remove Roles and Organizations for applications. (Scheduled for 2.1)
- UAS functionality still in UIB. (Scheduled for 2.1)

### Detailed issue list per component (Not complete)

- <https://github.com/altran/Whydah-UserIdentityBackend/issues?q=milestone%3A%222.0+Alfa%22+is%3Aclosed>
- <https://github.com/altran/Whydah-SecurityTokenService/issues?q=is%3Aissue+is%3Aclosed>
- <https://github.com/altran/Whydah-SSOLoginWebApp/issues?q=milestone%3A%222.0+Alfa%22+is%3Aclosed>
- <https://github.com/altran/Whydah-UserAdminWebApp/issues?q=milestone%3A%222.0+Alfa%22+is%3Aclosed>
- <https://github.com/altran/Whydah-Provisioning/issues?q=milestone%3A%222.0+Alfa%22+is%3Aclosed>
- <https://github.com/altran/Whydah-TestWebApp/milestones/2.0%20Alfa>
