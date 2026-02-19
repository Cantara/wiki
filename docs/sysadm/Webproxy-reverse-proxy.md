# Webproxy (reverse proxy)

For http-based services a webproxy can be used in combination to dns to simplify switching between which implementation a logical service name points to. The general idea behind webproxy is that it is easier to switch implementations by changing the webserver config file and reloading the config, than it is to do the switch in DNS. A setup based on Apache httpd looks something like: 

```
<VirtualHost *:80>
        #m2repo, for reference in pom.xml
        ProxyPreserveHost OFF
        #ProxyPass / http://193.19.64.142:8081/artifactory/
        #ProxyPassReverse / http://193.19.64.142:8081/artifactory/
        ProxyPass / http://193.19.64.155:8081/artifactory/
        ProxyPassReverse / http://193.19.64.155:8081/artifactory/
        ServerName m2repo.company.com
</VirtualHost>
<VirtualHost *:80>
        # repo, for access to the webapp
        ProxyPreserveHost OFF
        #ProxyPass /artifactory/ http://193.19.64.142:8081/artifactory/
        #ProxyPassReverse /artifactory/ http://193.19.64.142:8081/artifactory/
        ProxyPass /artifactory/ http://193.19.64.155:8081/artifactory/
        ProxyPassReverse /artifactory/ http://193.19.64.155:8081/artifactory/
        ServerName repo.company.com
</VirtualHost>
```

Note the setup above has omitted the recommended middle level of using machine-names, but shows the concept of setting up CNAME records to point to the webproxy: 

```
dig m2repo.company.com

;; ANSWER SECTION:
m2repo.company.com.   3600    IN      CNAME   webproxy.company.com.
webproxy.company.com. 421     IN      A       193.19.64.148
```
