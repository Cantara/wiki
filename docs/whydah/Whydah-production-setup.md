# Whydah production setup

### A typical production installation of Whydah:

|  |  |
| --- | --- |
| [Full Size](/web/20210613133903/https://wiki.cantara.no/plugins/gliffy/viewlargediagram.action?name=Whydah infrastructure&ceoid=37388694&key=whydah&pageId=37388694)  |  | |

Using DNS & mod\_balance load-balancing

### More configuration documentation

- [SSOLoginWebApp HA configuration (AWS ELB and Apache front)](/web/20210613133903/https://wiki.cantara.no/display/whydah/SSOLoginWebApp+HA+configuration+%28AWS+ELB+and+Apache+front%29 "SSOLoginWebApp HA configuration (AWS ELB and Apache front)")
- [SecurityTokenService HA configuration (AWS EC2 Hazelcast)](/web/20210613133903/https://wiki.cantara.no/display/whydah/SecurityTokenService+HA+configuration+%28AWS+EC2+Hazelcast%29 "SecurityTokenService HA configuration (AWS EC2 Hazelcast)")

### Load-balancing

- Amazon's [Elastic Load Balancing](http://aws.amazon.com/elasticloadbalancing/)  (We use this for AWS deployments)
- [Round-robin\_DNS](http://en.wikipedia.org/wiki/Round-robin_DNS) and Apache mod\_balance (We use this for on-premise deployments)
- Apache only load-balancer: [How To Set Up A Loadbalanced High-Availability Apache Cluster](http://www.howtoforge.com/high_availability_loadbalanced_apache_cluster)
