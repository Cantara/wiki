# Integrating with Whydah

## Quick set-up (Using Docker on development machine)

- [Install docker](https://docs.docker.com/installation/)
- Start Whydah, ready for Integration

  Unknown macro: {code}

  sudo docker run -it -p 80:9999 -p 9990:9990 -p 9995:9995 -p 9996:9996 -p 9997:9997 -p 9998:9998 totto/whydah bin/bash  
  /usr/bin/supervisord &  
  ls -al /home/\*/log/
- Add your application to the Whydah componnets (in Whydah 2.0: add it in securitytykenservice.TEST\_LOCALHOST.properties)

## Client code example

- [Integration tutorials](/web/20220930163214/https://wiki.cantara.no/display/whydah/Integration+tutorials "Integration tutorials")

Unknown macro: {code}

// Execute a POST to authenticate my application  
String myApplicationToken = Request.Post("https://sso.whydah.net/sso/logon")  
.bodyForm(Form.form().add("applicationcredential", "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?> <applicationcredential>   
<params> <applicationID>234</applicationID> <applicationSecret>applicationsecret</applicationSecret> </params>  
</applicationcredential>").build())  
.execute().returnContent().asBytes();

// Find applicationtokenID from applicationToken  
String myApplicationTokenID = $(myApplicationToken).xpath("/applicationtoken/params/applicationtokenID[1]");

// Redirect user til SSO login web with my URL as redirect and get userticket back as URL param  
//@RequestMapping("/myapp")  
//public String myWebApplication(@QueryParam("userticket") String userticket, HttpServletRequest request)

// Execute a POST to SecurityTokenService with userticket to get usertoken  
String usertoken = Request.Post("https://sso.whydah.net/sso/user/"myApplicationTokenID"/get\_usertoken\_by\_userticket/")  
.bodyForm(Form.form().add("apptoken", myApplicationToken).add("userticket", userTicket).build())  
.execute().returnContent().asBytes();

// Thats all you need to get a full userdatabase, SSO, Facebook/OAUTH support ++

(Example using Apache HTTP Components Fluent API and jOOX Fluent API)

## 1. Getting started - SecurityTokenService and parsing of UserToken

|  |  |
| --- | --- |
| SecurityTokenService is created to give the application an [ApplicationToken](/web/20220930163214/https://wiki.cantara.no/display/whydah/ApplicationToken "ApplicationToken") and a [UserToken](/web/20220930163214/https://wiki.cantara.no/display/whydah/UserToken "UserToken").  The UserToken will contain the roles granted for the given user in the app.   It is where to start when you want to integrate your app.  **Prerequisties:**   Development environment Win or Linux with Java installed.   1. Download SecurityTokenService.jar [Download](http://mvnrepo.cantara.no/content/repositories/releases/net/whydah/token/SecurityTokenService/) 2. Download propertyfile [here](https://raw.githubusercontent.com/altran/Whydah-SecurityTokenService/master/securitytokenservice.DEV.properties) to same location 3. In command prompt, run **java -DIAM\_MODE=DEV -DIAM\_CONFIG=securitytokenservice.DEV.properties -jar SecurityTokenService.jar** 4. Point a browser at <http://localhost:9998/tokenservice/> 5. Test the operations in the [GUI](https://wiki.altrancloud.com/download/attachments/37388812/STS-testweb.png) (test API driver)   **NOTE:**   In DEV mode, you can create and adjust test-data/users/usertokens by creating files in the same directory with naming convension t\_*<my\_test\_username>.token* ( See [Example](https://raw.githubusercontent.com/altran/Whydah-SecurityTokenService/master/t_test@hotmail.com.token)) Some tips on parsing the UserToken to check roles **Xpath examples** (Hint: experiment [here](http://www.freeformatter.com/xpath-tester.html))  Unknown macro: {code} // Get some token values  String userTokenID = $(usertoken).xpath("/usertoken/@id");  NodeList applicationRoleList = $(usertoken).xpath("/usertoken/application");  boolean hasEmployeeRoleInMyApp = $(usertoken).xpath("/usertoken/application[@ID=\"234\"]/role[@name=\"Employee\"");   1. find my applicationtokeID from returned ApplicationToken     /token/params/applicationtokenID  1. check UserToken if the user has the role Employee for the application with a given applicationID     /token/application[@ID="<myApplicationID>"]/role[@name="Employee"]  **Typical datastructures:**  [ApplicationCredential](/web/20220930163214/https://wiki.cantara.no/display/whydah/ApplicationCredential "ApplicationCredential"), [ApplicationToken](/web/20220930163214/https://wiki.cantara.no/display/whydah/ApplicationToken "ApplicationToken"), [UserCredential](/web/20220930163214/https://wiki.cantara.no/display/whydah/UserCredential "UserCredential"), [UserToken](/web/20220930163214/https://wiki.cantara.no/display/whydah/UserToken "UserToken") Integration examples We have provided a few integration examples for a set of different programming languages.   See links below.   - Java web-app example <https://github.com/altran/Whydah-TestWebApp> - Spring Security example <https://github.com/altran/Whydah-TestWebApp/tree/master/ImplementationExamples/spring-security> - Django example <https://github.com/altran/Whydah-TestWebApp/tree/master/ImplementationExamples/Django> - JavaScript example <https://github.com/altran/Whydah-TestWebApp/tree/master/ImplementationExamples/Javascript> - SharePoint 2013 (.NET) example <https://github.com/altran/Whydah-TestWebApp/tree/master/ImplementationExamples/SharePoint> | Unknown macro: {gliffy} |

## 2. Expand with a login GUI - Introduce SSOLoginWebApplication

|  |  |
| --- | --- |
| SSOLoginWebApplication is created to present a basic configurable login GUI, reset password GUI and user registration.   1. Download SSOLoginwebApp.jar [Download](http://mvnrepo.cantara.no/content/repositories/releases/net/whydah/sso/SSOLoginWebApp/) 2. Download propertyfile [here](https://raw.githubusercontent.com/altran/Whydah-SSOLoginWebApp/master/ssologinwebapp.TEST.properties) to same location. 3. Adjust properties and insert reference to a proper logo for your app/company. 4. In command prompt, run **java -DIAM\_MODE=TEST -DIAM\_CONFIG=ssologinwebapp.TEST.properties -jar SSOLoginwebApp.jar** 5. Point your browser to see the login GUI: <http://localhost:9997/sso/> 6. Configure your application to redirct to <http://localhost:9997/sso/> if no valid UserToken is presented.    - PS: Make this a configurable property in your app, since you might want to change it in PROD-environment | Unknown macro: {gliffy} |

## 3. Store users and roles - Introduce UserIdentityBackend

|  |  |
| --- | --- |
| UserIdentityBackend is created to store user identities, store user roles and integrate with 3rd party IDP's.  It may run locally in DEV mode with embedded LDAP for user storage and HSSQL db for role storage.  It should be set up to provide default roles to users from different 3rd party identities.   1. Download UserIdentityBackend.jar [Download](http://mvnrepo.cantara.no/content/repositories/releases/net/whydah/identity/UserIdentityBackend/) 2. Download propertyfile [here](https://raw.githubusercontent.com/altran/Whydah-UserIdentityBackend/master/useridentitybackend.DEV.properties) to same location. 3. Adjust properties if needed.    1. If you want to import test users, create a folder called testdata, [download these files](https://github.com/altran/Whydah-UserIdentityBackend/tree/master/src/main/resources/testdata) and adjust them if needed. Set **import.enabled=true**  1. In command prompt, run **java -DIAM\_MODE=DEV -DIAM\_CONFIG=useridentitybackend.DEV.properties -jar UserIdentityBacnend.jar** 2. If you have SecurityTokenService running from point 1. above, you need to change it's mode from DEV to TEST for it to talk with UIB:    1. Stop it by pressing CTRL+C in the command line window    2. Copy securitytokenservice.DEV.properties to securitytokenservice.TEST.properties (Or download [securitytokenservice.TEST.properties](https://github.com/altran/Whydah-SecurityTokenService/blob/master/securitytokenservice.TEST.properties))    3. Adjust TEST properties to point at the newly installed UIB om <http://localhost:9995/uib/>    4. Start by running **java -DIAM\_MODE=TEST -DIAM\_CONFIG=securitytokenservice.TEST.properties -jar SecurityTokenService.jar** | Unknown macro: {gliffy} |

## 4. User administration for administrators - Introduce UserAdminWebApp

You might want to have a look at the registered users and change them.  
For that you might want to run [UserAdminWebApp - UAWA](/web/20220930163214/https://wiki.cantara.no/display/whydah/UserAdminWebApp+-+UAWA "UserAdminWebApp - UAWA").  
Whydah 2.1+ introduces administration of collaborating applications

## 5. User administration self service - Introduce UserAdminService

You might want to include some simple self service features in your application, like adding roles to certain users or self registration.  
UserAdminService is created to allow for exactly that.  
It is however still in an early release.

---

### Whydah development Express-route for linux and osx/mac

|  | Pre-requisites: JDK 8, maven 3 and wget installed |

1. run bootstrapAndRunWhydah.sh (wget <https://raw.githubusercontent.com/Cantara/Whydah/master/dev-quickstart/bootstrapAndRunWhydah.sh>) which will do the following
   1. clone all main Whydah repositories
   2. build all modules on local machine
   3. start all built modules in a TEST\_LOCALHOST configuration
2. verify that it is working before starting to code (<http://localhost:9997/sso/welcome> u:useradmin pw:useradmin567)
