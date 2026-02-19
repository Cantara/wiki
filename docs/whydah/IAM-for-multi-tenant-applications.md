# IAM for multi-tenant applications

- All data belongs to a single organization. The isolation between organizations is enforced in all applications.

- An application defines one or more roles. The interpretation, i.e. what privileges this role gives, is only known in the scope of the application.

- We use the term *AccessControlEntry* (aka. *UserApplicationRoleEntry*) to denote the concept of an "entry"/row which defines access. An ACEntry contains the following:
  - organizationId
  - applicationId
  - roleId/roleName
  - rolevalue

- A group contains 0-n persons and a person can be member of 0-m groups. The purpose of the group is to simplify administration of authorization.

- A policy can be attached to a group or user. The user is always the primary entity for authentication and authorization. If groups are used to simplify administration, AccessControlEntries needs to be resolved from group memberships.

## Brainstorming

1. Does it makes sense to expose http-endpoints in all applications which expose all possible roleId/roleName and roleValues used in the application?
   1. Yes, that might be useful. However, probably more robust if the information is *pushed to* Whydah instead of Whydah requesting the information from all applications.
2. Some kind of "OrganizationService" which expose available organizations.
   1. Same as above. Not in Whydah's scope. Push the information to Whydah (UAS).
