# Installation and configuration of ApacheDS for Whydah

## Example of setting up Whydah server infrastructure

Screenshotet er litt rotete. Bare servere med navn som begynner med "TEST" har blitt brukt til WHYDAH

## Setting upp ApacheDS - LDAP for WHYDAH

- Set up a new Medium AWS Server
- Open up inbound port 10389 in the security zone of the ldap server to the secure zone of the UIB.
- Install ApacheDS v 2.0.0 M16 - <http://directory.apache.org/apacheds/downloads.html>. RPM commands are located below.

- To connect Apache Directory Studio
- For å koble til med Apache Directory Studio, lenger nede trengs port 10389 å åpnes mot din egen IP for en kort tidsperiode for å kunne bruke verktøyet mot LDAP'en. Denne skal skrus av etter konfigurasjon.

For å confe opp problemet ERR\_268 Cannot find a partition for uid=thomas.pringle@altran.com,ou=users,dc=external,dc=WHYDAH,dc=no] - les: <http://directory.staging.apache.org/apacheds/basic-ug/1.4.3-adding-partition.html>  
Jeg har fikset problemet ved å laste ned [Apache Directory Studio](https://directory.apache.org/studio/), koble til connections, nede til venstre i app'en, til serverinstansen på port:10389. Bruker: uid=admin,ou=system, Passord: secret.  
Nederst til venstre i Apache Studio -> Høyreklikk -> Open Configuration. Tab'en nederst -> Partitions. Add -> suffix "dc=WHYDAH,dc=no". ID: WHYDAH. For å lagre -> ctrl+s når man står i skjermbildet Configuration.  
Etter at partisjonen er lagret må apacheds ldap-applikasjonen restartes!!

#### Import av ldap-struktur fra annen kilde

WHYDAH UserIdentityBackend, i nåværende versjon, krever et par brukere for å settes opp. Denne prosesen kan brukes på en annen brukerdatabase også.  
I ApacheDirectoryStudio -> høyreklikk på partisjonen "dc=WHYDAH,dc=no" -> import -> LDIF import  
"Ldif file:" skal være [WHYDAH-initielle-brukere.ldif](/web/20211026222334/https://wiki.cantara.no/download/attachments/38437070/WHYDAH-initielle-brukere.ldif?version=1&modificationDate=1396257209569) Evt kan passordene til brukerne byttes ut.  
Sluttresultatet skal se slik ut:

ApacheDS/LDAP er nå satt opp -> steng den åpne 10389 porten!

### Nyttige kommandoer på

- Install rpm pakke: rpm -ivh pakke.rpm
- Finne installert rpm pakke: rpm -qa | grep apacheds
- Avinstallere: rpm -e pakkenavn
- Start av ApacheDS: sudo /etc/init.d/apacheds-2.0.0\_M16-default restart
