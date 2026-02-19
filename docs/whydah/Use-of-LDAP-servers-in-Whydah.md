# Use of LDAP servers in Whydah

#### Spørsmål (svar på engelsk) 

1. Èn lokal LDAP-instans eller to? 

For Whydah-UIB one LDAP instance should be sufficiant, but possibly in a cluster/HA configuration for HA production environments

1. Èn eller flere partisions? 

This is probably a product-specific decition. As almost all authenntication trafic never HIT the LDAP instance and the amount of data stored for each user is extremely slow, and since Whydah does not do LDAP searches, we should not need more than one partition for Whydah.

1. Hvilke LDAP schemas for hhv. user og application? 

We use the simple standard standard schema for users. I have to look at some use-cases before I would say that it makes any sence of putting applications/services in LDAP.

1. Lage en interface for authprovidere slik at også andre stores kan støttes? (f.eks. bruke MS SQL server for å lagre brukere i stedet for ldap? 

Whydah does not want to open for common mistakes like storing clear-text userpasswords in databases and other datastrores

1. Fast rekkefølge på oppslag eller mulig å konfigurere rekkefølgen man prøver de ulike authproviderne? 

Local first is the currect strategy
