# Whydah - API authentication tutorial

### A quick API guide for using Whydah as Web SSO

The simplest form of WebSSO consist of the following steps

- Authenticate your app to Whydah SSO, by sending appId and appSecret. Successful authentication will return an appToken
- From your web application - use a http-redirect for the login-action. Successful login to Whydah SSO will user to your app with a userTicket
- Use the userTicket and appToken to get the user token / user data
- Use the SSO session or map the session to you web application user/session
- So, let us explore the steps in a bit more detail.

### Authenticate your app to Whydah SSO

Unknown macro: {code}

// Execute a POST to authenticate my application  
String myApplicationToken = Request.Post("https://sso.whydah.net/sso/logon")  
.bodyForm(Form.form().add("applicationcredential", "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?> <applicationcredential>   
<params> <applicationID>234</applicationID> <applicationSecret>applicationsecret</applicationSecret> </params>  
</applicationcredential>").build())  
.execute().returnContent().asBytes();

**Some code comments to the code**

Unknown macro: {code}

URI: https/my\_whydah\_installation/sso/logon  
HTTP-POST  
Form content ApplicationCredential  
Returns: ApplicationToken

From the ApplicationToken you will need to extract the application session id, which yopu might do with the XPATH expression **"/applicationtoken/params/applicationtokenID1"**

**From your web application - use a http-redirect for the login-action**

Unknown macro: {code}

URI: http://<ssologinwebapp>/login?redirectURI=<myApp>"  
RETURN: The Web SSO return the user to the URL defined in the redirectURI with a userticket=value in URL parameter

1. Use the ticket you get on the user return from Whydah SSO to get the user token / user data
