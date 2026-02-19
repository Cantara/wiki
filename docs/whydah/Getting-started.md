# Getting started

|  |  |  |  |
| --- | --- | --- | --- |
| For the security officer  - Whydah provides a secure and relatively quick way to make dousins of custom made aplications adhere to a reasonable secure SSO policy. - By firewall configuration, proxy settings and URIs it is possible to put UserIdentityBackend in a "vault" to enforce role authenticity. - Audit logging log evry change being made to roles and users.   Read more about the [Security](/web/20221204051257/https://wiki.cantara.no/display/whydah/Security "Security") in Whydah. | For the operations department  - Set up Whydah by installing a typical production environment.   See the [Whydah for production](/web/20221204051257/https://wiki.cantara.no/display/whydah/Whydah+production+setup "Whydah production setup") page. [Try whydah](https://registry.hub.docker.com/u/totto/whydah/) on your machine.  Also see [Whydah for demo/test](/web/20221204051257/https://wiki.cantara.no/display/whydah/Contributing+to+Whydah+-+demo+and+test+installation "Contributing to Whydah - demo and test installation") | For the app developer See the [Integrating with Whydah](/web/20221204051257/https://wiki.cantara.no/display/whydah/Integrating+with+Whydah "Integrating with Whydah").   [Try whydah](https://registry.hub.docker.com/u/totto/whydah/) on your machine. | For the java developer If you want to enhance Whydah, you should first verify that you understand how Whydah work by using one of the examples provided in the integration guide.  [Try whydah and trace](https://registry.hub.docker.com/u/totto/whydah/) on your machine. Then it is time to install [Whydah development environment](/web/20221204051257/https://wiki.cantara.no/display/whydah/Whydah+development+environment+installation "Whydah development environment installation") |

## Quick set-up (Using Docker on local machine)

- [Install docker](https://docs.docker.com/installation/)
- Start Whydah, ready for Integration

  Unknown macro: {code}

  sudo docker run -it -p 80:9999 -p 9990:9990 -p 9995:9995 -p 9996:9996 -p 9997:9997 -p 9998:9998 totto/whydah /usr/bin/supervisord
- Go to Whydah <http://localhost/sso/welcome>

### Client code example

- (Example using Apache HTTP Components Fluent API and jOOX Fluent API)

  Unknown macro: {code}

  // Execute a POST to authenticate my application  
  String appToken = Request.Post("https://sso.whydah.net/sso/logon")  
  .bodyForm(Form.form().add("applicationcredential", myAppCredential).build())  
  .execute().returnContent().asBytes();

  // authenticate with username and password (user credential)  
  String usertoken = Request.Post("https://sso.whydah.net/sso/user/"appTokenID"/"new UserTicket(UUID.randomUUID()).toString()"/usertoken/")  
  .bodyForm(Form.form().add("apptoken", appToken)  
  .add("usercredential", new UserCredential(username,password).asXML()).build())  
  .execute().returnContent().asBytes();

  // Execute a POST to SecurityTokenService with userticket to get usertoken  
  String usertoken = Request.Post("https://sso.whydah.net/sso/user/"appTokenID"/get\_usertoken\_by\_userticket/")  
  .bodyForm(Form.form().add("apptoken", appToken)  
  .add("userticket", userTicket).build())  
  .execute().returnContent().asBytes();

  // That's all you need to get a full user database, IAM/SSO, Facebook/OAUTH support ++  
  boolean hasEmployeeRoleInMyApp = $(usertoken).xpath("/usertoken/application[@ID="+myAppId+"]/role[@name=\"Employee\"");
