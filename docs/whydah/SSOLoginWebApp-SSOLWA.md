# SSOLoginWebApp - SSOLWA

#### Responsibility

*Web SSO made easy*

#### Features

- Provide the user one, common, recognizable login interface
- Provide FB authentication
- Provide NetIQ auth and other 3rd party identities

#### Configuration properties

The LWA Artefact contains default properties for the different [IAM\_MODE](/web/20221204054025/https://wiki.cantara.no/display/whydah/IAM_MODE "IAM_MODE")'s being used.  
<- Indicates same value as the one to the right.

| Property | Example values PROD  Use external config  Exists as embedded - not recommended | Default values TEST | Default values DEV | Comment |
| --- | --- | --- | --- | --- |
| **securitytokenservice** | <http://yourdomain.com/tokenservice/> | <http://localhost:9998/tokenservice/> | <- | The URL to STS |
| **useridentitybackend** | <http://yourdomain.com/tokenservice/> | <http://localhost:9995/uib/> | <- | The URL to UIB |
| **myuri** | <https://sso.yourdomain.com/sso/> | <http://localhost:9997/sso/> | <- | STS own uri |
| **cookiedomain** | .whydah.net | <- | <- | Domain to set on the cookie that LWA sets on logged in users cookie |
| **logintype.facebook** | enabled | <- | <- | Whether or not to enable Facebook as an identity provider (remember to configure FACEBOOK-specific config |
| **logintype.openid** | enabled | <- | <- | Whether or not to enable OpenID as an identity provider |
| **logintype.omni** | disabled | <- | <- | Whether or not to enable Omni as an identity provider, see more at <http://www.omniidentity.com/> |
| **logintype.userpassword** | enabled | <- | <- | Whether or not to allow direct login with username and pw |
| **logintype.netiq** | enabled | <- | <- | Whether or not to display a NetIQ Login Button |
| **logintype.netiq.text** | NetIQ | <- | <- | Text to display on the netIQ-login button |
| **logintype.netiq.logo** | images/netiqlogo.png |  |  | Logo to display on the netIQ-login button |
| **signupEnabled** | true |  |  | Whether it should be allowed to sign up, signup-link will appear |
| **netIQauthURL** | <https://netiq.novel.com/netiqauth> |  |  | The path to the NetIQ Auth server, see more at [https://netiq.novel.com](https://netiq.novel.com/) |
| **FACEBOOK\_APP\_SECRET** | 2124234234234 |  |  | The app secret for the Facebook app with |
| **FACEBOOK\_APP\_ID** | 23423252452442 |  |  | The app ID for the Facebook app you auth with |
| **logourl** | <http://domain.com/somepicture.png> |  |  | Picture to be displayed on top of login page |

#### Whydah User Session Discovery Flow

Unknown macro: {gliffy}
