# Apache DS-notater fra ICS

#### Setup
server.xml

    * Change values:
      allowAnonymousAccess="false"
      accessControlEnabled="true"

    * Comment out or remove example.com partition

    * Add partition:
      <jdbmPartition id="icspartner" suffix="dc=icspartner,dc=com" />

Restart apacheds

#### Backup, restore and copy LDAP data

Backup/restore/copy is done by export and import of LDIF format data. Two parts need to be exported/imported:

    * icspartnerschema (cn=icspartnerschema,ou=schema) (must be imported first)
    * icspartner area (dc=icspartner,dc=com)
