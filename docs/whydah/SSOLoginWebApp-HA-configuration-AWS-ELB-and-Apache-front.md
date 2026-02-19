# SSOLoginWebApp HA configuration (AWS ELB and Apache front)

**more /etc/httpd/conf.d/whydah.conf**

|  | - We use port 80 for https-redirect, terminate https/ssl in ELB and forward 443 SSL terminated to port 9999 on our *cluster* - We deploy this configuration on all cluster members (possibly without the test WebApp) - We only deploy one instance of useradmin, to emulate it in a more secure deployment - The UIB DNS/IP is provisioned in the services property files - If interested, we have ansible-provisioning scripts to quickly set-up a similar configuration |
