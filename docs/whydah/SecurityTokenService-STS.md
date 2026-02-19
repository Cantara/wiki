# SecurityTokenService - STS

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

Unknown macro: {code}

@Path("/user")

@Path("/usertoken\_template")  
@GET  
@Produces(MediaType.APPLICATION\_XML)  
public Response getUserTokenTemplate()

Unknown macro: {
return Response.ok(new Viewable("/usertoken.ftl", new UserToken())).build();
}

/\*\*  
\*  
\*

- @param applicationtokenid the current application wanting to authenticate the user.
- @param appTokenXml the token representing the application the user want to access.
- @param userCredentialXml
- @return  
  \*/  
  @Path("/

  Unknown macro: {applicationtokenid}

  /usertoken")  
  @POST  
  @Consumes(MediaType.APPLICATION\_FORM\_URLENCODED)  
  @Produces(MediaType.APPLICATION\_XML)  
  return Response.ok(new Viewable("/usertoken.ftl", token)).build();

  /\*\*

  - Login in user by his/her usercredentials and register its ticket in the ticket-map for session handover  
    \*
  - @param applicationtokenid
  - @param userticket
  - @param appTokenXml
  - @param userCredentialXml
  - @return  
    \*/  
    @Path("/

  /

  Unknown macro: {userticket}

  /usertoken")  
  @POST  
  @Consumes(MediaType.APPLICATION\_FORM\_URLENCODED)  
  @Produces(MediaType.APPLICATION\_XML)  
  return Response.ok(new Viewable("/usertoken.ftl", usertoken)).build();

  /\*\*

  - Verify that a usertoken and a user session is still valid. Usually used for application re-entries and before allowing
  - a user important and critical processes like monetary transactions  
    \*  
    \*
  - @param applicationtokenid
  - @param userTokenXml
  - @return  
    \*/  
    @Path("/

    Unknown macro: {applicationtokenid}

    /validate\_usertoken")  
    @POST  
    @Consumes(MediaType.APPLICATION\_FORM\_URLENCODED)  
    return Response.ok().build();

    @Path("/

    /validate\_usertokenid/

    Unknown macro: {usertokenid}

    ")  
    @GET  
    return Response.ok().build();

  /\*\*

  - Used to create a userticket for a user to transfer a session between whydah SSO apps  
    \*
  - @param applicationtokenid
  - @param appTokenXml
  - @param userticket
  - @param userTokenId
  - @return  
    \*/  
    @Path("/

    Unknown macro: {applicationtokenid}

    /create\_userticket\_by\_usertokenid")  
    @POST  
    @Consumes(MediaType.APPLICATION\_FORM\_URLENCODED)  
    return Response.ok(new Viewable("/usertoken.ftl", userToken)).build();

    /\*\*

    - Used to get the usertoken from a usertokenid, which the application usually stores in its secure cookie  
      \*
    - @param applicationtokenid
    - @param appTokenXml
    - @param userTokenId
    - @return  
      \*/  
      @Path("/

    /get\_usertoken\_by\_usertokenid")  
    @POST  
    @Consumes(MediaType.APPLICATION\_FORM\_URLENCODED)  
    @Produces(MediaType.APPLICATION\_XML)  
    return Response.ok(new Viewable("/usertoken.ftl", userToken)).build();

  /\*\*

  - Lookup a user by a one-time userticket, usually the first thing we do after receiving a SSO redirect back to
  - an application from SSOLoginWebApplication  
    \*  
    \*
  - @param applicationtokenid
  - @param appTokenXml
  - @param userticket
  - @return  
    \*/  
    @Path("/

    Unknown macro: {applicationtokenid}

    /get\_usertoken\_by\_userticket")  
    @POST  
    @Consumes(MediaType.APPLICATION\_FORM\_URLENCODED)  
    return Response.ok(new Viewable("/usertoken.ftl", userToken)).build();

    /\*\*

    - Force cross-applications/SSO session logout. Use with extreme care as the user's hate the resulting user experience..  
      \*
    - @param applicationtokenid
    - @param userTokenID
    - @return  
      \*/  
      @Path("/

    /release\_usertoken")  
    @POST

  /\*\*

  - This method is for elevating user access to a higher level for the receiving end of a session handover between SSO applications  
    \*
  - @param applicationtokenid
  - @param userTokenXml
  - @param newAppToken
  - @return  
    \*/  
    @Path("/

    Unknown macro: {applicationtokenid}

    /transform\_usertoken")  
    @POST

    /\*\*

    - The SSOLoginWebApplication backend for 3rd party UserTokens. Receive a new user, create a Whydah UserIdentity with
    - the corresponding defaultroles (UAS|UIB) and create a new session with a one-time userticket for handover to receiving
    - SSO applications  
      \*
    - @param applicationtokenid
    - @param userticket
    - @param appTokenXml
    - @param userCredentialXml
    - @param thirdPartyUserTokenXml typically facebook user-token or other oauth2 usertoken
    - @return  
      \*/  
      @Path("/

    /

  /create\_user")  
  @POST

---

**ApplicationToken API**

Unknown macro: {code}

@Path("/")  
@GET  
@Produces(MediaType.TEXT\_HTML)  
if ("enabled".equals(appConfig.getProperty("testpage")))

Unknown macro: {
return Response.ok().entity(new Viewable("/testpage.html.ftl", model)).build();
}

else

Unknown macro: {
return Response.ok().entity(new Viewable("/html/prodwelcome.html")).build();
}

@Path("/applicationtokentemplate")  
@GET  
@Produces(MediaType.APPLICATION\_XML)  
return Response.ok().entity(template.toXML()).build();

@Path("/applicationcredentialtemplate")  
@GET  
@Produces(MediaType.APPLICATION\_XML)  
return Response.ok().entity(template.toXML()).build();

@Path("/usercredentialtemplate")  
@GET  
@Produces(MediaType.APPLICATION\_XML)  
return Response.ok().entity(template.toXML()).build();

@Path("/logon")  
@POST  
@Consumes(MediaType.APPLICATION\_FORM\_URLENCODED)  
@Produces(MediaType.APPLICATION\_XML)  
return Response.ok().entity(applicationTokenXml).build();

@Path("

Unknown macro: {applicationtokenid}

/validate")  
@POST  
@Consumes(MediaType.APPLICATION\_FORM\_URLENCODED)  
return Response.ok().build();

---

### Configuration properties

The STS Artefact contains default properties for the different [IAM\_MODE](/web/20230925121535/https://wiki.cantara.no/display/whydah/IAM_MODE "IAM_MODE")'s being used.  
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
