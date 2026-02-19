# New provisioning and deployment strategy

#### Spørsmål og diskusjon 
- Kontinuerlig produksjon
    - Which technology?
    - When/how often is the docker image replaced/updated?
    - Which service will trigger deployment to environment?
    - What's the strategy for deployment without down-time? Or is down-time acceptable?
    - What about user sessions?
    - How to roll-back if a change breaks the system?
- Post install tester
    - Health check end points?  
- Automatisert provisjonering av LDAP
- Easy to use SSL certificates
- Erfaringer med AWS lastbalanserer og utprøving av Apache Load balancer
- Docker

#### Mulige tiltak 

1. [Improve property loading to support config_override from file #50](https://github.com/altran/Whydah-UserIdentityBackend/issues/50)
1. Use Docker
