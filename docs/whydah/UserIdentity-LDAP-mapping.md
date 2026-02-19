# UserIdentity LDAP mapping

Mapping is performed in _LdapUserIdentityDao_. 

| UserIdentity field | LDAP field | LDAP schema | AD field |  |
| --- | --- | --- | --- | --- |
| uid | [uid | http://www.zytrax.com/books/ldap/ape/core-schema.html#uid] | core.schema | [userPrincipalName | http://msdn.microsoft.com/en-us/library/ms680857%28v=vs.85%29.aspx] |
| username | [initials | http://www.zytrax.com/books/ldap/ape/core<sub>~schema.html#initials], non</sub>~standard use | core.schema | [sAMAccountName | http://msdn.microsoft.com/en-us/library/ms679635%28v=vs.85%29.aspx] |
| cn | [cn | http://www.zytrax.com/books/ldap/ape/core-schema.html#cn] | core.schema | [cn | http://msdn.microsoft.com/en-us/library/ms675449%28v=vs.85%29.aspx] |
| sn | [sn | http://www.zytrax.com/books/ldap/ape/core-schema.html#sn] | core.schema | [sn | http://msdn.microsoft.com/en-us/library/ms679872%28v=vs.85%29.aspx] |
| givenName | [givenName | http://www.zytrax.com/books/ldap/ape/core-schema.html#gn] | core.schema | [givenName | http://msdn.microsoft.com/en-us/library/ms675719%28v=vs.85%29.aspx] |
| mail | [mail | http://www.zytrax.com/books/ldap/ape/core-schema.html#mail] | core.schema | [mail | http://msdn.microsoft.com/en-us/library/ms676855%28v=vs.85%29.aspx] |
| mobile | [mobile | http://www.zytrax.com/books/ldap/ape/cosine.html#mobile] | cosine.schema | [mobile | http://msdn.microsoft.com/en-us/library/ms677119%28v=vs.85%29.aspx] |
| userpassword, case error, should be _userPassword_? | [userPassword | http://www.zytrax.com/books/ldap/ape/core-schema.html#userpassword] | core.schema | [userPassword | http://msdn.microsoft.com/en-us/library/ms680851%28v=vs.85%29.aspx] |
| personRef | [employeeNumber | http://www.zytrax.com/books/ldap/ape/inetorgperson.html#employeenumber] | inetorgperson | [employeeNumber | http://msdn.microsoft.com/en-us/library/ms675663%28v=vs.85%29.aspx] |

See [Table 8.3: Commonly Used Syntaxes](http://www.openldap.org/doc/admin23/schema.html) for readable syntax descriptions. 

[Windows Active Directory LDAP Schema](https://fsuid.fsu.edu/admin/lib/WinADLDAPAttributes.html)

Default AD LDAP schema does not have an uid field. Extensions (Microsoft’s Services for UNIX?) are possible to add this. If no uid can be found, UIB use the _userprincipalname_ field as uid. Example: userprincipalname=firstname.lastname@company.com.
