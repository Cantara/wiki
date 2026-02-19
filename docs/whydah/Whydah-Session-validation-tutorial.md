# Whydah - Session validation tutorial

### Introduction

In this tutorial we'll explore some of the common UserSession validation scenarios and give some suggestion(s) of how your application should address them.

1. Resolving the returned userticket to a UserToken (user session)  
What we see quite common is applications which try to use the ticket more than one time. There are several way we see this happen, but the most common ones are a) user reload the page which have the userticket=value parameter in it and b) Single-Page Applications where several components try to solve the same task of getting the UserToken. The suggested approach to both is for the application to handle the situation by combining the applications own session-state (i.e. storing the usertokenid in there) and the ticket-redirect. So if the ticket result in a UserToken, store the usertokenid in the application session (providing support for changing user) and using the stored value for the usertokenid for a secondary request \_get\_usertoken\_from\_usertokenid as a fallback on already authenticated users).

2. Resolving invalid UserTokens (i.e. users without required roles or similar)  
Most applications will have the need for checking the roles for an authenticated user. In an SSO flow, you should expect to get requests for authenticated users which does not have sufficient rights to access your application. A common flow we see, is implementations which repeat the SSO redirect directly when they do not accept the returned UserToken. This will in many cases cause a redirect loop between the application and Whydah SSO. The reason for this is that the SSO component (by definition) pick up the users session, create a new ticket and return. The user will thus return to your application with the same or a very similar role without any chance of log in as a new user. If your application receive an userToken with insufficient rights, we advice you to present the user with this fact, and give the user the abillity to log out and log in as another user. This can be done in several ways, where a redirect to /sso/logout with the same redirectURI as in /sso/login is the simplest way.

### Security filter login flow

Register and login new user in "my application"

Most applications will have the need for checking the roles for an authenticated user. In an SSO flow, you should expect to get requests for authenticated users which does not have sufficient rights to access your application. A common flow we see, is implementations which repeat the SSO redirect directly when they do not accept the returned UserToken. This will in many cases cause a redirect loop between the application and Whydah SSO. The reason for this is that the SSO component (by definition) pick up the users session, create a new ticket and return. The user will thus return to your application with the same or a very similar role without any chance of log in as a new user. If your application receive an userToken with insufficient rights, we advice you to present the user with this fact, and give the user the abillity to log out and log in as another user. This can be done in several ways, where a redirect to /sso/logout with the same redirectURI as in /sso/login is the simplest way.

###### Register and login new user in "my application"
