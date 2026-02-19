# Core design requirements and Whydah support

| Design requirement | Details | Why it is important | Whydah support |
| --- | --- | --- | --- |
| Application security | All applications that should negotiate with Whydah services needs to be authenticated by SecurityTokenService, in addition to authentication of users. | Un-autenticated apps poses a severe security threat |  |
| Application security | SSOLoginWebApp needs to authenticate towards SecurityTokenService before it can authenticate a user. |  |  |
| Application security | UserAdminWebApp needs to authenticate towards SecurityTokenService and verify that the user has the correct UserAdminWebApp role before gaining access to user administration |  |  |
