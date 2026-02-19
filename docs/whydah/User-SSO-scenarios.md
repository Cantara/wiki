# User SSO scenarios

### Typical Applications SSO Scenarios

1. **Web-Application log-in**
1. **Application  log-in (mobile app or other native application)**

### Application log.in (mobile app or other native application  )

1. App -> authApplication ([ApplicationCredential](ApplicationCredential.md)) -> SecurityTokenService (return:  [ApplicationToken](ApplicationToken.md))
1. App - > show username and password form -> get field values
1. App -> authUser ([UserCredential](UserCredential.md)) -> SecurityTokenService (return:  [UserToken](UserToken.md))

### Web-Application log-in

Public websites caan chose to use the scenario described above, or they can opt for an connom sso-login form authrentication as described below.

!SSO scenario.png|border=1!
