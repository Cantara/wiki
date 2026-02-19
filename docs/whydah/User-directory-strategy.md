# User directory strategy

|  | Contrary to other IAM Products that try to sync or provision users from one respository to another,   Whydah's aproach is to keep the users in one central repository (LDAP) and allow all associated apps to securely authenticate the user when needed. |

## User directory strategies

When UIB is running in dev and test mode it will use an embedded directory service, but when scaling your installation it is good practice to use an external Directory service.

We hve tried Apache DS, but has now migrated to OpenLDAP as that seem to give less hazzle.  
See [Integration with LDAP and Active Directory](/web/20210616075005/https://wiki.cantara.no/display/whydah/Integration+with+LDAP+and+Active+Directory "Integration with LDAP and Active Directory") and [Install OpenLDAP for UIB](/web/20210616075005/https://wiki.cantara.no/display/whydah/Install+OpenLDAP+for+UIB "Install OpenLDAP for UIB")

It is also possible to use AD directly without OpenLDAP, or AD together with NetIQ Access Manager and ADFS.
