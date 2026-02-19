# Prod setup in sso.altrancloud.com

###### Install services 
| # Ubuntu server | (/) |  |
| # Firewall rules....  source limitations of UIB access | (x) |
1. JDK 7 (OpenJDK)
1. Apache or NginX as webproxy 
1. [ApacheDS](http://directory.apache.org/apacheds/download/download<sub>~linux</sub>~deb.html)
    1. http://opendesignarch.blogspot.no/2012/12/download<sub>~and</sub><sub>install</sub><sub>ldap</sub>~on-ubuntu.html 
1. PostgreSQL
    1. [How To Install and Use PostgreSQL on Ubuntu 12.04](https://www.digitalocean.com/community/articles/how<sub>~to</sub><sub>install</sub><sub>and</sub><sub>use</sub><sub>postgresql</sub><sub>on</sub><sub>ubuntu</sub>~12-04)
    1. [cantaraadm:Setup Postgres database for Confluence](../cantaraadm/Setup<sub>~Postgres</sub><sub>database</sub><sub>for</sub>~Confluence.md)

###### Configuration 

###### Install UIB 

###### Security 

UIB, webproxy 
postgres, apacheds 

All services run as separate, non-root users. 

Suggest require SSH tunnel to access database and LDAP. Only allow direct connection from localhost.
