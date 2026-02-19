# Issues på testserver

Endret artifact fra client til useradmin (pr. versjon 1.1-SNAPSHOT)

#### Test på testserver pr. -24.august-  30. august:
- Paginering i griden virker ikke (piler frem/tilbake). Den sier også side "0 av 1" 
- sortering virker ikke i tabellen 
- <sub>~funker ikke i firefox (finner ikke console)</sub>~
- <sub>~flytting av bruker virker ikke. GUI gir beskjed om flytting OK, men "commiter" ikke på LDAP</sub>~
- <sub>~noe encoding</sub>~problematikk en plass ser det ut som. ÆØÅ blir feil i ApacheDS etter endring i GUI (usikker på hva som er rett/feil)-
- <sub>~ikke mulig å endre passord på bruker (blir ikke commitet)</sub>~
- <sub>~mangler rolle for tilgang til logon på useradmin</sub>~appen-
