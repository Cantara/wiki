# Integration with LDAP and Active Directory

[UIB](/web/20210624220538/https://wiki.cantara.no/display/whydah/UserIdentityBackend+-+UIB "UserIdentityBackend - UIB") can treat an [Active Directory](http://en.wikipedia.org/wiki/Active_Directory) (AD) server as a standard LDAP server because [UIB] only use a small subset of the functionality in LDAP.

Two AD or LDAP servers are supported. The *primary* server is checked first and if the user is found, authentication is attempted. If authentication fails, access is denied.   
If the user is not found in the primary LDAP/AD server, authentication against the *secondary* LDAP/AD server is attempted.

It is possible to configure whether UIB can write or if the LDAP/AD server is read-only.

###### Single AD/LDAP with write permissions

This is the standard setup. AD integration is similar to LDAP, but the default schema in AD has no UID field. It is possible to add an extension (todo reference here) to AD to get UID and other LDAP fields, but otherwise UID is constructed from existing AD fields. I.e. Default AD configuration will work without any modifications.

###### Only AD read-only

**NotApplicable** / **NotSupported**, as it can't support a huge amount of Whydah functionality.

- Functionality requiring write permissions to AD/LDAP
  - Add new users (new [UserIdentity](/web/20210624220538/https://wiki.cantara.no/display/whydah/UserIdentity "UserIdentity")) (Create OAUTH2/Facebook/NetIQ user representations, sign-up functionality)
  - Update [UserIdentity](/web/20210624220538/https://wiki.cantara.no/display/whydah/UserIdentity "UserIdentity") (update 2-factor cell-phone number, update name/surname)
  - New Password (lost password functionality)

###### AD + Whydah LDAP (AD or LDAP is master)

- New users are added to master, but not to secondary
- Master is used first, secondary thereafter
- Write [UserIdentity](/web/20210624220538/https://wiki.cantara.no/display/whydah/UserIdentity "UserIdentity") updates to both

###### AD read-only + Whydah LDAP (LDAP is master)

- Use AD for auth
- Fallback on LDAP for auth
- Writes [UserIdentity](/web/20210624220538/https://wiki.cantara.no/display/whydah/UserIdentity "UserIdentity") to LDAP
  - User may have two passwords if they use Whydah to change passowrd
- Support usage during AD downtime/mainternance

#### Only AD - CLEANUP required

Works as standalone LDAP, with the following exception(s)

TODO: What rules defines the tranformation from an AD user to a Whydah user?

- Import all
- Whydah user = AD user
- First access
- Manual process?

Those decisions needs to be implemented to keep the UserDataIntex in Lucene "up-to-date"

###### Comments from ED to be merged into the text.

- Default AD LDAP schema does not have an *uid* field. Extensions are possible to add this. If no uid can be found, UIB use the *userprincipalname* field as uid. Example: userprincipalname=firstname.lastname@company.com.

- Import functionality is used to add applications, organizations and mapping between roles and users. It is possible to add mapping to roles without actually importing any users by referencing the uid expected to be found when looking up the user in AD.

- Login as usual with **username without domain**. E.g. *erikd*, not DOMAIN\erikd.

- Authentication and authorization of users thus not rely on any changes to LDAP/AD servers, only the role database is changed.

- NOTE! The lucene index is currently not updated on import. See todo in *RoleMappingImporter*. The UserAdminWebapp can thus not find the users, but they can login.

---

#### Field-mapping

Mapping is performed in *LdapUserIdentityDao*.

| UserIdentity field | LDAP field | LDAP schema | AD field |
| --- | --- | --- | --- |
| uid | [uid](http://www.zytrax.com/books/ldap/ape/core-schema.html#uid) | core.schema | [userPrincipalName](http://msdn.microsoft.com/en-us/library/ms680857%28v=vs.85%29.aspx) |
| username | [initials](http://www.zytrax.com/books/ldap/ape/core-schema.html#initials), non-standard use | core.schema | [sAMAccountName](http://msdn.microsoft.com/en-us/library/ms679635%28v=vs.85%29.aspx) |
| cn | [cn](http://www.zytrax.com/books/ldap/ape/core-schema.html#cn) | core.schema | [cn](http://msdn.microsoft.com/en-us/library/ms675449%28v=vs.85%29.aspx) |
| sn | [sn](http://www.zytrax.com/books/ldap/ape/core-schema.html#sn) | core.schema | [sn](http://msdn.microsoft.com/en-us/library/ms679872%28v=vs.85%29.aspx) |
| givenName | [givenName](http://www.zytrax.com/books/ldap/ape/core-schema.html#gn) | core.schema | [givenName](http://msdn.microsoft.com/en-us/library/ms675719%28v=vs.85%29.aspx) |
| mail | [mail](http://www.zytrax.com/books/ldap/ape/core-schema.html#mail) | core.schema | [mail](http://msdn.microsoft.com/en-us/library/ms676855%28v=vs.85%29.aspx) |
| mobile | [mobile](http://www.zytrax.com/books/ldap/ape/cosine.html#mobile) | cosine.schema | [mobile](http://msdn.microsoft.com/en-us/library/ms677119%28v=vs.85%29.aspx) |
| userpassword, case error, should be *userPassword*? | [userPassword](http://www.zytrax.com/books/ldap/ape/core-schema.html#userpassword) | core.schema | [userPassword](http://msdn.microsoft.com/en-us/library/ms680851%28v=vs.85%29.aspx) |
| personRef | [employeeNumber](http://www.zytrax.com/books/ldap/ape/inetorgperson.html#employeenumber) | inetorgperson | [employeeNumber](http://msdn.microsoft.com/en-us/library/ms675663%28v=vs.85%29.aspx) |

See [Table 8.3: Commonly Used Syntaxes](http://www.openldap.org/doc/admin23/schema.html) for readable syntax descriptions.

[Windows Active Directory LDAP Schema](https://fsuid.fsu.edu/admin/lib/WinADLDAPAttributes.html)

Default AD LDAP schema does not have an uid field. Extensions (Microsoft’s Services for UNIX?) are possible to add this. If no uid can be found, UIB use the *userprincipalname* field as uid. Example: userprincipalname=firstname.lastname@company.com.
