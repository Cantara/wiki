# STS

## SecurityTokenService (STS)

#### Responsibility

The scalable secure session control

###### Details

- Session state
- Usertoken generation
- Usertoken / UserTicket / user credential verification
- Application credential verification
- Application token generation

#### Integration endpoints

**UserToken API**

---

**ApplicationToken API**

---

### Configuration properties

The STS Artefact contains default properties for the different [IAM\_MODE](/web/20210121042813/https://wiki.cantara.no/display/whydah/IAM_MODE "IAM_MODE")'s being used.  
<- Indicates same value as the one to the right.

| Property | Example values PROD  Use external config  Exists as embedded - not recommended | Default values TEST | Default values DEV | Comment |
| --- | --- | --- | --- | --- |
| **myuri** | http://myserver.net/tokenservice/ | <http://localhost:9998/tokenservice/> | <http://localhost:9998/tokenservice/> | The URI to this instance of STS |
| **service.port** | 9998 | <- | <- | Port for this service |
| **useridbackendUri** | <http://myservice/uib/> | <http://localhost:9995/uib/> | <http://localhost:9995/uib/> | URL to useridentity backend |
| **testpage** | disabled | enabled | enabled | Whether or not to enable the testpage. The url is printed when you start the service with it enabled. |
| **logourl** | http://stocklogos.com/somelogo.png | <- | <- | A logo to display for the kicks of it |

### Additional info

- HazelCast + Apache mod\_balance to share state.
