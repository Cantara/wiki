# Whydah UserAdmin for 3. party applications.

### Background

Some application have a legitimate need to handle and coordinate its own roles and thus a IAM system like Whydah should let the system owner delegate such privileges to certain applications. This self-administration will be limited to roles within the application (as identified with applicationid). Typical usages are

- Change role for a user in an organization (i.e. from Employee to Manager)
- Remove role and access to this application
- Search the Whydah directory, and add access to the application for a user which has not access already
- Change role parameters belonging to this application for one or several users

**Third party User Administration Application Use Cases**

- Role-Administration for my application
  - CRUD RoleNames
  - CRUD User-Roles-Values
  - CRUD Organizations
- User-Admninistration
  - add/remove access to application (Q: future support for application portfolios?)

Whydah have already these functions in its internal API,, which is used by Whydah UserAdministration to administer Whydah users.

### API ovewview

| UseCase | Service | method | url | public | for admin apps | internal | comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
