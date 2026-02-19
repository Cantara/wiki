# ACS Infrastructure recommendations

## Here is a suggested infrastructure to host ACS in AWS

#### EC2

- Ubuntu 12.10 (How about 14.04, see NB1) m3.large
- 8 GB Storage

#### Database

- 30 GB PostgreSQL database MultiAZ with automated daily backup

#### Authentication

- [Whydah infrastructure](/web/20210127011309/https://wiki.cantara.no/display/whydah/Whydah+infrastructure+recommendations "Whydah infrastructure recommendations") to Authenticate and log in

NB1) For the current time being ACS is dependant upon old version of Python-uno and old version of libreoffice.
