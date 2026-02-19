# Whydah infrastructure recommendations

When setting up Whydah you have to consider how secure you want your installation.  
The security corresponds somewhat to the [IAM\_MODE](/web/20210616081034/https://wiki.cantara.no/display/whydah/IAM_MODE "IAM_MODE") as one would expect PROD to be more secure than DEV.

| Mode / security | What to setup | Server recommendation |
| --- | --- | --- |
| 1. Development mode | - Download the docker image and start rolling on your local computer or all components on one server | - None (your local comuter with Java 8 installed will do fine) |
| 2. Test mode | - Setup a separate UIB and LDAP behind firewall. - Download the docker image and change the user identity backend configuration to point to your UIB | - All in one server or with separate UIB and Front end |
| 3. Production mode | - Get a SSL certificate for the domain you wish to run whydah on, i.e. sso.whydah.net - Setup a separate UIB and LDAP behind firewall. - Setup a separate front-end server with UAS, UAWA and STS. | See [Installing Whydah](/web/20210616081034/https://wiki.cantara.no/display/whydah/Installing+Whydah "Installing Whydah") for deployment diagram.    - LDAP server: Amaxon Linux AMI m3.medium 8GB  (Or AD can be used, see [User directory strategy](/web/20210616081034/https://wiki.cantara.no/display/whydah/User+directory+strategy "User directory strategy")) - UIB server: Amazon Linux AMI t2.micro 8GB - Frontend server: 1-4 Amazon Linux AMI t2.micro 8GB - RoleDB: Mysql, db.m1.small, 10GB |

Note that installation can be provisioned using Ansible once you have the infrastructure setup.   
You'll find it at <https://github.com/altran/Whydah-Provisioning>.

### Whydah development Express-route for linux and osx/mac

|  | Pre-requisites: JDK 8, maven 3 and wget installed |

1. run bootstrapAndRunWhydah.sh (wget <https://raw.githubusercontent.com/Cantara/Whydah/master/dev-quickstart/bootstrapAndRunWhydah.sh>) which will do the following
   1. clone all main Whydah repositories
   2. build all modules on local machine
   3. start all built modules in a TEST\_LOCALHOST configuration
2. verify that it is working before starting to code (<http://localhost:9997/sso/welcome> u:useradmin pw:useradmin567)

## Notes when setting up new Server environment in Amazon AWS

- Apply "Protect against accidental termination"
- Keep instances as physically close to on another (Subnet)
- Set Naming strategy as quickly as possible to avoid confusion. Example:
  - MyCompany-PROD-UserIdentityBackend
  - MyCompany-PROD-SecurityTokenService
  - MyCompany-PROD-SSOLoginWebapp
  - MyCompany-PROD-UserAdmin
- Create new keys for PROD and don't reuse test-keys. They can't be changed afterwards.

#### Zone recommendation

Whydah-Vault  
Whydah-DMZ  
Whydah-admin

#### Key recommendation

Whydah-Vault.pem  
Whydah-DMZ.pem  
Whydah-AdminService.pem  
Whydah-AdminWebapp
