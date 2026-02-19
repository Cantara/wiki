# Example Whydah 2.1 installation Cantara QA

|  |  |
| --- | --- |
| Hosting environment | Cantara Whydah QA (AWS) |
| Purpose | QA Environment for testing Whydah 2.1 |
| Set up date | 2015-11-22 |
| Set up by | Stig Lau |
| My uri | sso.cantara.org |
| ELB | not configured |

#### Servers

| Server | Type | Public DNS | security group | ssh key | ports used |
| --- | --- | --- | --- | --- | --- |
| C-QA-W-2.1-STS-SSOLWA 1/1 |  | ? | QA-Whydah-DMZ | Cantara\_Whydah\_Frankfurt.pem | 9997,9998,9999 |
| C-QA-W-2.1-UAWA |  | ? | PROD-Whydah-DMZ | Cantara\_Whydah\_Frankfurt.pem | 9996 |
| C-QA-W-2.1-UAS |  | ? | PROD-Whydah-DMZ | Cantara\_Whydah\_Frankfurt.pem |  |
| C-QA-W-2.1-UIB |  | ? | QA-Whydah-Vault | Cantara\_Whydah\_Frankfurt.pem | 9995 |
| C-QA-W-UIB-DB |  | ? | Whydah Secure  Whydah-Datastorage | N/A | 3306 |
| C-QA-W-UIB-LDAP |  | ? | Whydah Secure Whydah-Datastorage | Cantara\_Whydah\_Frankfurt.pem | 10389 |

#### Applications

#### Role database

Endpoint: ?:3306  
DB Name: uibdbmysql  
Engine: mysql(5.6.23) ???  
Username: uibuser  
Master User Password: \*\*\*\*\*\*\*\*  
Option Group(s):default:mysql-5-6 ??  
Availability Zone: ??????  
VPC ID: ???  
Security Security Groups:Whydah Secure (??)  
Storage:10GB  
Instance Class:db.m1.small

#### LDAP - TODO Update config

Runs on: ??  
user: ec2-user  
run command: docker run -d -p 10389:389 ldap  
check whether container is running: docker ps  
check that ldap is working: ldapsearch -D cn=admin,dc=external,dc=WHYDAH,dc=no -w secret -p 10389 -h localhost -b "dc=external,dc=WHYDAH,dc=no" -s sub "(objectclass=\*)"

## How to set up Whydah from scratch on AWS

- Create Security groups
- Provision up a set of AWS AMI instances to install whydah on
- Set up the DB storage
- Git clone <https://github.com/Cantara/Whydah-Provisioning>
- Create internal project for storing sensitive environment specific configuration for Ansible provisioning
- Provision
