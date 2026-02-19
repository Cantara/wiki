# Whydah FAQ

#### I get returned to my application after an successful Whydah SSO login, but the application show no data

There are two typical scenarios which can produce this result. a) The application fail the application-logon, usually due to error in applicationid or application secret in the applicationcredential. This results in no valid application session, and then the application can not convert the userticket to a usertoken and thus we have no valid user session. b) the user which log on does not have the correct role that the application expect, and thus will not grant access to data.

#### No users showing in UserAdminWebApplication

If UIB is reinstalled or the Solr lucene index is emptied, the list of users in the AdminApp may lack users, even though they can still log in. To get the users back: search for them with a trailing "/", and the system will search for them in LDAP/DB and reintroduce them.

#### I get errors authentication in SSOLoginWebApp

This happens most frequently due to one of two reasone. a) UIB has (for some reasons) lost its connection to its internal LDAP server. If the LDAP server is not running, restart the LDAP server. Then restart UIB. b) UIB has lost connection to SecurityTokenService. Restart STS.

#### I get an authentication loop when trying to log in from UAWA (or some external application)

This happens when the application fail to connect to SecurityTokenService to get the UserToken form the provided UserTicket. Verify thet the calling application has a solid session-handling on its SecurityTokenService connection. If not, you might have to restart the calling application/UAWA.
