# Cookie handling

###### SSOLoginWebapp

- SSOLoginWebapp will
    - create user token cookie on successful authentication. 
    - clear user token cookie if user token verification fails. 
    - clear user token cookie if logout is called. 

- Configurable property, _cookiedomain_, to set cookie domain. Should be set to the domain SSOLoginWebapp is deployed on, e.g. .ssologin.yourdomain.no. 

###### Clients 

- Clients should set a cookie with the user token id. 
    - Cookie domain should be set to something _different: than the domain in SSOLoginWebapp. 

###### UserAdminWebapp (a special client) 

- UserAdminWebapp, if deployed on the same (sub)domain as SSOLoginWebapp, can reuse the cookies set by SSOLoginWebapp. However, separate cookies have been chosen also for UserAdminWebapp. 
- When user logs out of UserAdminWebapp, the user should also be logged out from SSOLoginService. 

- UserAdminWebapp redirects to the _logout_ endpoint (not logoutaction). 

- Configurable property, _cookiedomain_, to set cookie domain. Should be set to the domain UserAdminWebapp is deployed on, e.g. .useradmin.yourdomain.no. 

###### Read more 

[httpCookie.setDomain](http://docs.oracle.com/javase/8/docs/api/java/net/HttpCookie.html#setDomain-java.lang.String-)
