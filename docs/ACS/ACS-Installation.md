# ACS Installation

- [Prereq](#ACSInstallation-Prereq)
- [Install Apache](#ACSInstallation-InstallApache)
- [Installing mod\_wsgi](#ACSInstallation-Installingmodwsgi)
- [Installing Django on server](#ACSInstallation-InstallingDjangoonserver)
- [Install Database](#ACSInstallation-InstallDatabase)
- [Install GIT](#ACSInstallation-InstallGIT)
- [Install Java](#ACSInstallation-InstallJava)
- [Install Solr](#ACSInstallation-InstallSolr)
- [Install ProxyPass](#ACSInstallation-InstallProxyPass)
- [Install Libreoffice for converting .doc and .pdf](#ACSInstallation-InstallLibreofficeforconverting.docand.pdf)
- [Install postfix to send nag-mails](#ACSInstallation-Installpostfixtosendnagmails)

**Todo**

- TODO automatic redeployment
- TODO sikkerhet på solr lenke i apache.conf/proxy
- TODO enable wsgi in apache
- TODO setup django admin console <https://docs.djangoproject.com/en/1.5/howto/deployment/wsgi/modwsgi/>

### Prereq

- Ubuntu installed and updated.
- User has sudo access.

### Install Apache

- Based on info from <http://www.howtoforge.com/installing-apache2-with-php5-and-mysql-support-on-ubuntu-12.10-lamp>

**Commands**

**Fix ssl**

1. restart apache

|  | **Apache Conf**   - default document root is /var/www on Ubuntu, - configuration file /etc/apache2/apache2.conf. - Additional configurations are stored in subdirectories of the /etc/apache2 directory such as /etc/apache2/mods-enabled (for Apache modules), /etc/apache2/sites-enabled (for virtual hosts), and /etc/apache2/conf.d. |

### Installing mod\_wsgi

1. See <https://www.digitalocean.com/community/articles/installing-mod_wsgi-on-ubuntu-12-04>

   restart apache

### Installing Django on server

**ACS-User**

**ACS Source code**  
git clone <https://github.com/altran/Awesome-Competence-System.git> /home/acs-user/acs

**Django**

- <https://docs.djangoproject.com/en/1.4/howto/deployment/wsgi/modwsgi/>

**/etc/apache2/sites-available/acs.conf**  
**Note: This configuration is outdated!!**

1. Opprett bruker i .htaccess

### Install Database

TODO: more config needed to document.

### Install GIT

sudo apt-get install git

### Install Java

### Install Solr

### Install ProxyPass

See [cantaraadm:Webproxy - OpenSolaris]

Add symbolic links to /etc/apache2/mods-enabled  
lrwxrwxrwx 1 root root 28 Feb 21 11:42 proxy.conf -> ../mods-available/proxy.conf  
lrwxrwxrwx 1 root root 28 Feb 21 11:42 proxy.load -> ../mods-available/proxy.load

In /etc/apache2/sites-available/default

Verify: <http://altubuntu01.cloudapp.net/solr/#/>

### Install Libreoffice for converting .doc and .pdf

sudo apt-get install libreoffice

Run:

### Install postfix to send nag-mails

Choose "No configuration" upon prompt

Start postfix with command
