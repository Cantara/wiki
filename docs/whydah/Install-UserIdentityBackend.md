# Install UserIdentityBackend

UserIdentityBackend supports Windows and Linux, but Ubuntu or Amazon Linux is recommended.   
This page describes a typical production setup, see [Install UserIdentityBackend - devtest](/web/20210731184152/https://wiki.cantara.no/display/whydah/Install+UserIdentityBackend+-+devtest "Install UserIdentityBackend - devtest") for a easier, but not production ready installation.

#### Prerequisites

1. RDBMS: MySQL, MS SQL Server or HSQLDB
2. LDAP: [ApacheDS](http://directory.apache.org/apacheds/download/download-linux-deb.html) or OpenLDAP
   1. <http://opendesignarch.blogspot.no/2012/12/download-and-install-ldap-on-ubuntu.html>
   2. [Whydah OpenLDAP Docker image](/web/20210731184152/https://wiki.cantara.no/display/whydah/Whydah+OpenLDAP+Docker+image "Whydah OpenLDAP Docker image")
   3. [Install OpenLDAP for UIB](/web/20210731184152/https://wiki.cantara.no/display/whydah/Install+OpenLDAP+for+UIB "Install OpenLDAP for UIB")

#### Install UIB

Installation is automated using Ansible.

- Create AWS EC2 instance or similar
- git clone <https://github.com/Cantara/Whydah-Provisioning> Whydah-Provisioning-yourEnvName
- Set up configuration files for provisioning (ask Stig or Erik, not easily documented as of now)
- time ansible-playbook -vvv provision-whydah.yml --private-key=~/.ssh/altran\_whydah\_dev.pem --tags=uib

---

#### Docker strategy

- Database: Docker container or <http://aws.amazon.com/rds/>
- LDAP: OpenLDAP in separate Docker container
- Data volume container
  - useridentitybackend\_override.properties
  - prodInitData (csv fles for import)
  - logback.xml
  - lucene data
- UIB in Docker
