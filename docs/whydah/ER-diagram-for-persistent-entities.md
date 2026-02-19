# ER-diagram for persistent entities

|  | Diagram to facilitate a discussion, but necessarily how Whydah is implemented now or in the future |

A UserAggregate contains the *UserIdentity* (from LDAP) and a list of *UserApplicationRoleEntry*'s.  
UserApplicationRoleEntry: applicationId, orgName, roleId, userId, roleValue

*[Diagram: er-digram]*
