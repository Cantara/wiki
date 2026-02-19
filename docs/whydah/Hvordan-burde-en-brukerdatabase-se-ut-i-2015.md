# Hvordan burde en brukerdatabase se ut i 2015

###### Krav 

- Hvilke krav er viktige? 
    - SSO 
    - Enkelt å integrere med 
    - Kurrant å administrere 
    - Integrasjon over http 
    - Kryptert transport 
    - Reset password 
    - Støtte for flere autentiseringsmekanismer (Google, facebook, osv.) 
    - Grafisk, webbasert klient for administrasjon 
    - HTTP API for brukeradministrasjon fra andre applikasjoner/script 
    - Enkelt å sette opp og drifte 
    - Enkelt å sperre alle tilganger for en bruker eller til en applikasjon 

- Andre krav 
    - HA 
    - Interoperabilitet med eksisterende protokoller eller produkter? 

 
###### Design og implementasjonsstikkord man forventer/ønsker seg  

- Ryddig kode, god testdekning, ikke for mange (og gamle dependencies) 
- Tjenesteorientert, micro service-arkitektur 
- Security token 
- Engangs-ticket 
- Hvordan ser klientkommunikasjonen ut? 
- En database hvor det er mulig å gjøre spørringer, eksport/import, osv. 
- Ingen applikasjonsservere og ikke bygget i et språk som gjør det ekstra vanskelig å lage sikker kode. 
- Flernivå sikring hvor mulig 

- Docker? 

###### Hvorfor ikke produktX eller bygge selv? 

###### Hvilke valg (i Whydah)  påvirker sikkerhetsnivået direkte eller indirekte? 

- Hvilke tiltak er viktige for å oppnå et minimumsnivå av sikkerhet? 
- Hvilke kompromisser er gjort for å oppnå akseptabel brukervennlighet? 

---

###### Hvordan bør et IAM-system se ut i 2017? 

- Application authentication and authorization 
- Security levels
- Threat level coordination 
- System threat mechanisms
