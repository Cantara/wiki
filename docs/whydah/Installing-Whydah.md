# Installing Whydah

|  | The Readme.MD file of the Whydah github repos contains detailed installation information and start-up scripts |

### Release notes

- [Whydah Releases](/web/20221204054059/https://wiki.cantara.no/display/whydah/Whydah+Releases "Whydah Releases")

### A typical production installation of Whydah:

Unknown macro: {gliffy}

Using DNS & mod\_balance load-balancing

### More configuration documentation

- [SSOLoginWebApp HA configuration (AWS ELB and Apache front)](/web/20221204054059/https://wiki.cantara.no/display/whydah/SSOLoginWebApp+HA+configuration+%28AWS+ELB+and+Apache+front%29 "SSOLoginWebApp HA configuration (AWS ELB and Apache front)")
- [SecurityTokenService HA configuration (AWS EC2 Hazelcast)](/web/20221204054059/https://wiki.cantara.no/display/whydah/SecurityTokenService+HA+configuration+%28AWS+EC2+Hazelcast%29 "SecurityTokenService HA configuration (AWS EC2 Hazelcast)")

### Load-balancing

- Amazon's [Elastic Load Balancing](http://aws.amazon.com/elasticloadbalancing/)  (We use this for AWS deployments)
- [Round-robin\_DNS](http://en.wikipedia.org/wiki/Round-robin_DNS) and Apache mod\_balance (We use this for on-premise deployments)
- Apache only load-balancer: [How To Set Up A Loadbalanced High-Availability Apache Cluster](http://www.howtoforge.com/high_availability_loadbalanced_apache_cluster)

#### Installation guides

See [Whydah infrastructure recommendations](/web/20221204054059/https://wiki.cantara.no/display/whydah/Whydah+infrastructure+recommendations "Whydah infrastructure recommendations") for particular tips on infrastructure setup.

###### Linux

- [Install SSOLoginWebApp on Ubuntu]
- [Install SecurityTokenService on Ubuntu]
- [Install UserIdentityBackend](/web/20221204054059/https://wiki.cantara.no/display/whydah/Install+UserIdentityBackend "Install UserIdentityBackend")
- [Install UserAdminWebApp on Ubuntu]
- [Install apache web proxy on Ubuntu]

#### Integration setups

- [Integrating with Whydah](/web/20221204054059/https://wiki.cantara.no/display/whydah/Integrating+with+Whydah "Integrating with Whydah")

See [TestWebApp](/web/20221204054059/https://wiki.cantara.no/display/whydah/TestWebApp "TestWebApp") for an example on how to integrate your application with Whydah. The github repository includes examples in Java, JavaScript,  
Django, Microsoft Sharepoint App and Spring Security.

### Default ports for the whydah services

| Whydah Module | Default Port |
| --- | --- |
| UserIdentityBackend | 9995 |
| SecurityTokenService | 9998 |
| UserAdminService | 9992 |
| UserAdminWebapp | 9996 |
| SSOLoginWebApp | 9997 |
| CRMService | 12121 |
| SPAProxyService | 9898 |
| OAUTH2Service | 8086 |

### IAM\_MODE

[IAM\_MODE](/web/20221204054059/https://wiki.cantara.no/display/whydah/IAM_MODE "IAM_MODE") is used to run the modules in different mode

### IAM\_CONFIG

IAM\_CONFIG is used to define your own config-file for Whydah. File-names are relative to current directory. Example:

Unknown macro: {code}

java -jar -DIAM\_CONFIG=useridentitybackend.TEST.properties UserIdentityBackend.jar
