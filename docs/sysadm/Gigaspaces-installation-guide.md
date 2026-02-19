# Gigaspaces installation guide

Start gigaspaces at boot and deploy spaces using upstart on Ubuntu 14.10. 

1. cd /opt 
1. Download [http://www.gigaspaces.com/xap-download](http://www.gigaspaces.com/xap-download) 
1. unzip gigaspaces-xap-lite-10.0.1-ga-b11800.zip
    1. unzip advanced_scripts.zip (in the bin folder) 
1. Edit gslicense.xml and add license. 
1. adduser space 
1. chown space:space /opt/gigaspaces-xap-premium-10.0.1-ga -R 
1. Add upstart conf files to /etc/init/ to start Gigaspaces and deploy spaces 
    1. cp [^gigaspaces.conf](gigaspaces-conf.md) /etc/init/ 
    1. cp [^gsspaces.conf](gsspaces-conf.md) /etc/init/

Note! 

Assuming that you are not mirroring / replicating any data to an external DB, using kill to shutdown gigaspaces should be fine.

###### Read more about start at boot 

- http://docs.gigaspaces.com/sbp/initd.html
- Default agent values: http://docs.gigaspaces.com/xap97adm/the-runtime-environment.html 

- https://github.com/patrickmay/gigaspaces-admin

- http://docs.gigaspaces.com/sbp/safe-grid-shutdown.html
