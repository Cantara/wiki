# On-behalf-of relations

The basic scenario for authorization is to give a user one or more roles in an application. The same user can of course ha a different set of roles in another application.

But what if the same user has different relations to the application?

Example: insurance company

- *Customer* - basic privileges to see and modify own insurances
- *Employee* - administration privileges
- *Board member* - access to top-secret financial statistics

The naive approach is to give the person the flat list of all roles and privileges needed.

To support such a use case some information is needed to differentiate for which relation ("hat") the person is given what set of roles.

Technically this looks like this:

| userId | applicationId | relationId/OrgId | roleName | roleValue |
| --- | --- | --- | --- | --- |
| erikUserId | someWebappId | customer | modify\_own\_account | true |
| erikUserId | someWebappId | employee | modify\_all\_accounts | true |
| erikUserId | someWebappId | board\_member | financial\_statistics | true |
| erikUserId | anotherWebappId | <notInUse> | admin | true |

roleValue can be true/false or contain data. The use of this field can be chosen for each application. Common usage is true/false to support use cases for disabling access.
