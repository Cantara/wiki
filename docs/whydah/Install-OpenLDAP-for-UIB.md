# Install OpenLDAP for UIB

#### Install and configure OpenLDAP

1. Install packages
2. Set up olcSuffix and admin user

   2. Add password hash to ldif file
   3. Run ldapmodify:  
      admin.ldif:
3. Set up admin user for UIB
   1. ldapadd -x -D cn=uibadmin,dc=yourdomain,dc=no -W -f uibadmin.ldif  
      uibadmin.ldif:
   2. Run ldapmodify to give uibadmin necessary permissions:  
      uibadmin-acl.ldif:

#### Ldap commands

###### Find all

###### Find specific user "useradmin"

Print 1 when *useradmin* is found:

###### Delete entry

## Working with MySQL from UIB with the command line

Examples taken from <http://www.cyberciti.biz/faq/mysql-command-to-show-list-of-databases-on-server/>

###### Install mysql client:

###### Connect to Mysql and navigate db
