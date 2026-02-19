# Whydah Administration Questions

### Huh?

Whydah is a Single Sign On provider that handles ACL ([Access Contol List](http://en.wikipedia.org/wiki/Access_control_list)) for any application that connects to it.  
It has a very easy role setup where a user may have access to an application and be given different roles and each role may hold a value that the application can use for granting access to protected resources.  
An example of such a user-role matrix is this one from [AwesomeCompetenceSystem] showing that the Manager role has some additional attributes:

| Application | Organization | Role | Value |
| --- | --- | --- | --- |
| MyApplication | \* | ReadOnly | \* |
| MyApplication | \* | Employee | <e-mail> |
| MyApplication | \* | Manager | \* *Eks: { role: 'Practice lead', location: 'Oslo', country: [ASE:'Norway', 'Sweden'] }* |
| MyApplication | \* | Administrator | \* |

### Components- separation of responsibility.

Whydah is separated in four main components:

| Component | What it does | Status |
| --- | --- | --- |
| [UserAdministration](https://github.com/altran/Whydah-UserAdministration) | The web front end to help project managers and Thomas Ingebretsen (for example...) add users and add roles to users | Has love, more features on its way |
| [SecurityTokenService](https://github.com/altran/Whydah-SecurityTokenService) | Provides a security token to the application when someone tries to log in | Has love (ie. works!) |
| [SSOLoginWebApp](https://github.com/altran/Whydah-SSOLoginService) | The web-frontend for the Whydag SSO services. It uses SecurityTokenService and UserIdentityBackend behind the scenes, where SecurityTokenService needs to be accessible from the same zone that your applications reside. | Has love (ie. works!) |
| [UserIdentityBackend](https://github.com/altran/Whydah-UserIdentityBackend) | Also known as UIB. Stores UserIdentities and their relation to Roles, Applications and Organizations. Requires SecurityTokenService if authorization is turned on. | Works |

### How do I add a new application to Whydah?

You add it in UserAdminWebApp
