# Planning and modelling access strategies

In order to be successful with an IAM strategy, it is essential to have a concious relation to the roles used for different applications.
We have seen many chaotic situations over the years. For example Active Directories with more than 1000 security groups but only 400 users using only 10 applications.
It is common to leave definition of roles to the application, whydah allows to keep this practice but also regain some control. You also store and gather all roles in one place on a single identity.

This method take into consideration that you have a legacy of users to migrate. If that is not the case and you are starting from scratch (Lucky you), skip the action items related to migration.
#### How do you get started?
We suggest creating a detailed plan on how you want to aproach this. Here is a suggested list of activities to get you started.
1. Create a best effort list of applications
1. Create a field map that documents the source of the role fields. Go through the top priority applications that need to be SSO enabled and identify their roles and properties needed for these roles.
1. Create a field map that documents the source of the user fields. Pay special attention to the **CustomerRef** field. \\This field may be used for a common external reference for all applications. \\This field may come from for example CRM-system, AD or membership systems.

Whydah is fundamentally agnostic to how you map your roles and identities.
You may do it any way that gives meaning. The fundamental structure in whydah is illustrated below.
![WhydahStructure](../images/gliffy/38437012-WhydahStructure.png)
#### Examples
###### User
| User field | Sample data | Comment |
| --- | --- | --- |
| Username | Donaldduck | Avoid using e-mail adresses as they will change! |
| FirstName | Donald | The users first name, useful to Welcome the user |
| LastName | Duck | The users last name |
| E-mail | donald@duckburg.com | Necessary for the user to be able to reset his PW |
| Phone number | 99 99 99 99 | Necessary for two factor autentication (If used) |
| Customer ref | 313 | Customer ref common for all applications |

###### Userroles
 || App ID || App name|| Org ID || Org name || Role name || Properties || Comment ||
| 1 | ScroogeVault | 1 | MoneyBin | **Employee** | donald@ducksburg.com | E-mail as prop may be useful in for example cross domain situations or in order to map multiple users to the same user in your application |
| 1 | ScroogeVault | 1 | MoneyBin | **Manager** | no | Property "no" indicates that poor Donald is definitely not a manager in the Scrooge Vault |
| 34 | LeafApp | 314 | Nissan | **CarUser** | 313 | Gives the user access to administer his Leaf with reg nr 313 |
| 314 | JudgeDirectory | 1234 | Junior Woodchucks, Ducksburg | **Organizer** | `{"orgid": "1234", "orgname": "Junior Woodchucks, Ducksburg"}` | JSON stored as property for ease of integration |
| 314 | JudgeDirectory | 1235 | Junior Woodchucks, Warszaw | **Organizer** | `{"orgid": "1235", "orgname": "Junior Woodchucks, Warszaw"}` | Another organisation with access to JudgeDirectory |
| 314 | JudgeDirectory | 2 | Junior Woodchucks Foundation | **JudgeAdministrator** | Poland | Admin access to JudgeDirectory for Poland |
| 314 | JudgeDirectory | 2 | Junior Woodchucks Foundation | **JudgeAdministrator** | Norway | Admin access to JudgeDirectory for Norway |

###### Alternative to JudgeAdministrator with multiple values in same role
| App ID | App name | Org ID | Org name | Role name | Properties | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| 314 | JudgeDirectory | 2 | Junior Woodchucks Foundation | **JudgeAdministrator** | NO,PL | Admin access to JudgeDirectory for both Norway and Poland using language codes |

#### How do you continue to migrate into Whydah?
It is possible to use whydah as a login handler without changing the user experience by having your login form use Security Token Service Directly. 
However, we recommend using the default Whydah-SSOLoginWebApp and inform your users about the change.
Here is a suggested list of activities to get you started.
1. Import users to Whydah & test that the import was successful using useradmin web app.
1. Change the application to authenticate using whydah (See the test app that includes examples using different technologies)
1. Test this thouroughly with all different roles in your test environment
1. Communicate to existing users that you plan to change login method and that they may experience a new UC on login.
1. Reimport users if changes has occurred since you test-imported
1. Put changes in production
1. Follow up users that need help
