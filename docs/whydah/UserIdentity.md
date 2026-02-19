# UserIdentity

User data. Mastered by [UserIdentityBackend - UIB](/web/20200806163837/https://wiki.cantara.no/display/whydah/UserIdentityBackend+-+UIB "UserIdentityBackend - UIB")

|  | This is the user as stored in LDAP and **NOT** the accesses and roles, which is derived from the user-company **contract(s)** (employee, member, buyer etc.) |

###### Minimal UserIdentity object

| Property | Nullable | Minimum length | Other |
| --- | --- | --- | --- |
| uid | no | 2 | unique |
| email | no | 5 | unique |
| username | no | 3 | unique |
| firstName | no | 2 |  |
| lastName | no | 2 |  |

**UserIdentityXml**

**UserIdentityJson**
