# Contributing to Whydah - demo and test installation

### Whydah development Express-route for linux and osx/mac

|  | Pre-requisites: JDK 8, maven 3 and wget installed |

1. run bootstrapAndRunWhydah.sh (wget <https://raw.githubusercontent.com/Cantara/Whydah/master/dev-quickstart/bootstrapAndRunWhydah.sh>) which will do the following
   1. clone all main Whydah repositories
   2. build all modules on local machine
   3. start all built modules in a TEST\_LOCALHOST configuration
2. verify that it is working before starting to code (<http://localhost:9997/sso/welcome> u:useradmin pw:useradmin567)

### SecurityTokenService - A Quick glance

1. Download SecurityTokenService.jar [Download](http://mvnrepo.cantara.no/content/repositories/releases/net/whydah/token/SecurityTokenService/)
2. Download propertyfile [here](https://raw.githubusercontent.com/cantara/Whydah-SecurityTokenService/master/securitytokenservice.DEV.properties) to same location
3. Run **java -DIAM\_MODE=DEV -DIAM\_CONFIG=securitytokenservice.DEV.properties -jar SSOLoginService.jar**
4. Point you browser at <http://localhost:9998/tokenservice/>
5. Test the operations in the [GUI](https://wiki.altrancloud.com/download/attachments/37388812/STS-testweb.png) (test API driver)
   1. NOTE: in this mode, you can create and adjust test-data/users/usertokens by creating files in the same directory with naming convention *<my\_test\_username>.token* ( See [Example](https://raw.githubusercontent.com/altran/Whydah-SecurityTokenService/master/t_test@hotmail.com.token))

---

### Set up test environment in a cloud

*Tested on Ubuntu 13.04 on a virual machine in Azure and on Ubuntu 13.10 on a virtual machine in Amazon cloud services*

|  | This installs all Whydah components on the same machine.   Preferably you should run the services on different machines in a production environment.  See this documentation (link to be inserted) to understand why. |

Get yourself a linux server.  
Connect to the server, for windows users the [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) client is a suggestion.

**Installation of 3rd party software**

Unknown macro: {code}

sudo apt-get install openjdk-7-jdk  
sudo apt-get install openjdk-7-jre  
sudo apt-get install apache2

**Configure Apache HTTP Proxy**

Put the following code in a file called 'whydah.conf' at /etc/apache2/sites-available/

Unknown macro: {code}

<VirtualHost \*:80>  
ServerName "your uri".cloudapp.net  
ServerAlias "your uri"  
ProxyRequests Off  
<Proxy \*>  
Order deny,allow  
Allow from all  
</Proxy>  
ProxyPreserveHost on  
ProxyPa<Virtualss /sso <http://localhost:9997/sso>  
ProxyPass /uib <http://localhost:9995/uib>   
ProxyPass /tokenservice <http://localhost:9998/tokenservice>  
ProxyPass /useradmin <http://localhost:9996/useradmin>  
ProxyPass /test <http://localhost:9990/test/>  
</VirtualHost>

Install required mods:

Unknown macro: {code}

sudo a2enmod proxy  
sudo a2enmod proxy\_http

Disable default site:

Unknown macro: {code}

sudo a2dissite 000-default

Enable your configuration:

Unknown macro: {code}

sudo a2ensite whydah  
sudo service apache2 restart

**Create users for the different services**

Unknown macro: {code}

sudo adduser SSOLoginService  
sudo adduser SecurityTokenService  
sudo adduser UserIdentityBackend  
sudo adduser UserAdministration

**Install UserIdentityBackend** <https://github.com/Altran/Whydah-UserIdentityBackend> (For scripts)

Unknown macro: {code}

1. As the correct user  
   sudo su - UserIdentityBackend

1. Download and update configuration file  
   wget <https://raw.github.com/altran/Whydah-UserIdentityBackend/master/src/main/resources/useridentitybackend.PROD.properties>  
   nano useridentitybackend.PROD.properties

1. Download startup-script for the service  
   wget <https://raw.github.com/altran/Whydah-UserIdentityBackend/master/start-service.sh>  
   chmod 550 start\_service.sh

1. Start the service  
   ./start\_service.sh

1. verify the log  
   more nohup.out

**Install SecurityTokenService** <https://github.com/Altran/Whydah-SecurityTokenService> (For scripts)

Unknown macro: {code}

1. As the correct user  
   sudo su - SecurityTokenService

1. Download and update configuration file  
   wget <https://raw.github.com/altran/Whydah-SecurityTokenService/master/src/main/resources/securitytokenservice.PROD.properties>  
   nano securitytokenservice.PROD.properties

1. Download startup-script for the service  
   wget <https://raw.github.com/altran/Whydah-SecurityTokenService/master/start-service.sh>  
   chmod 550 start\_service.sh

1. Start the service  
   ./start\_service.sh

1. verify the log  
   more nohup.out

**Install SSOLoginService** <https://github.com/Altran/Whydah-SSOLoginService> (For scripts)

Unknown macro: {code}

1. As the correct user  
   sudo su - SSOLoginService

1. Download and update configuration file  
   wget <https://raw.github.com/altran/Whydah-SSOLoginService/master/src/main/resources/ssologinservice.PROD.properties>  
   nano ssologinservice.PROD.properties

1. Download startup-script for the service  
   wget <https://raw.github.com/altran/Whydah-SSOLoginService/master/start-service.sh>  
   chmod 550 start\_service.sh

1. Start the service  
   ./start\_service.sh

1. verify the log  
   more nohup.out

**Install UserAdministration** <https://github.com/Altran/Whydah-UserAdministration> (For scripts)

Unknown macro: {code}

1. As the correct user  
   sudo su - UserAdministration

1. Download and update configuration file  
   wget <https://raw.github.com/altran/Whydah-UserAdministration/master/src/main/resources/useradministration.PROD.properties>  
   nano useradministration.PROD.properties

1. Download startup-script for the service  
   wget <https://raw.github.com/altran/Whydah-UserAdministration/master/start-service.sh>  
   chmod 550 start\_service.sh

1. Start the service  
   ./start\_service.sh

1. verify the log  
   more nohup.out

---

**Test webapp**  
There is a project named Whydah-TestWebApp that shows an implementation of a website secured by Whydah.  
The project can be downloaded at: <http://mvnrepo.cantara.no/service/local/artifact/maven/redirect?r=altran-snapshots&g=net.whydah.sso.web&a=Whydah-TestWebApp&v=LATEST&p=jar>

Unknown macro: {code}

wget -O TestWebApp.jar "http://mvnrepo.cantara.no/service/local/artifact/maven/redirect?r=altran-snapshots&g=net.whydah.sso.web&a=Whydah-TestWebApp&v=LATEST&p=jar"
