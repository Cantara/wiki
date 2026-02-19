# Stories - behov

# Bakgrunn

Kundeservice bruker i dag Apache Directory Studio for å administrere LDAP. Den egner seg greit til alt mulig rart, men er for komplisert når det blir daglig administrasjon av brukere og organisasjoner.

Brukere kan selv oppdatere navn, e<sub>~post og passord via web</sub>~applikasjonen de bruker.

## Behov/scope

Kundeservice ønsker seg en web-klient for å administrere brukere, organisasjoner og muligens organisatoriske roller. Detaljert administrasjon av applikasjoner/systemroller/rettigheter m.v. kan man fremdeles benytte ApacheDS til, da det er mer systemadmin enn kundeservice. 

LDAP-webklienten lages som egen applikasjon, pt. ikke behpv for SSO med den andre applikasjonen, men bør kunne implementeres på et senere tidspunkt.

Eksisterende applikasjon bruker spring mvc, struts 2, spring security, java 6. Kjører i tomcat6 på linux.

## 

- Som kundeservice ønsker jeg å kunne administrere brukere effektivt for å yte god service
    - Som kundeservice ønsker jeg å kunne legge til nye brukere i eksisterende organisasjon
    - Som kundeservice ønsker jeg å kunne sette nytt passord for en eksisterende bruker
    - Som kundeservice ønsker jeg å kunne endre navn og epost for en bruker
    - Som kundeservice ønsker jeg å kunne slette en bruker
    - Som kundeservice ønsker jeg å kunne finne en bruker og se hvilken organisasjon og roller/rettigheter vedkommende har

- Som kundeservice ønsker jeg å kunne administrere organisasjoner effektivt
    - 
    - 
    - 

- Som kundeservice ønsker jeg raskt å kunne finne informasjon om en bruker eller organisasjon for å betjene henvendelser og løse problemer raskt
