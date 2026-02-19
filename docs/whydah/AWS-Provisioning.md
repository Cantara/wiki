# AWS Provisioning

#### Provisioning strategy

- The same [ansible](http://www.ansible.com/home) scripts are used by all environments. Differences between environments is handled by configuration.

- Limit flexibility and prioritize the recommended setup.

#### Infrastructure

- Create servers, Amazon Linux
  - Micro installation: 1 micro server (SSOLoginWebApp, SecurityTokenService, UserAdminService), 1 small server (UserIdentityBackend, UseradminWebApp)
  - Normal installation: 2 micro servers HA (SSOLoginWebApp, SecurityTokenService, UserAdminService), 1 small server (UserIdentityBackend),1 small server (UseradminWebApp)
  - Normal On-premise admin installation: 2 micro servers HA (SSOLoginWebApp, SecurityTokenService, UserAdminService), 1 small server (UserIdentityBackend),On premise server (UseradminWebApp)

- Set up firewalls
  - DMZ sone (SSOLoginWebApp, SecurityTokenService, UserAdminService)
  - Secure Vault (UserIdentityBackend, UseradminWebApp)

- [Install OpenLDAP for UIB](/web/20210731175506/https://wiki.cantara.no/display/whydah/Install+OpenLDAP+for+UIB "Install OpenLDAP for UIB") on Ubuntu

- [Amazon RDS for PostgreSQL](http://aws.amazon.com/rds/postgresql/)

#### Whydah core

- Properties, config\_override

- HTTPS only, Certificates

- HA, HazelCast

- Import from CSV

#### TODO

1. Remove import.enabled
   1. Always run import functionality. Add missing data, never overwrite or remove.
   2. Do not delete anything by default
