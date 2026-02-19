# Arkitektur og teknologivalg

# Overordnet

Vi ser for oss en LDAP-til-JSON-proxy, samt en web-klient.

## Proxy
Vi har undersøkt to teknologi-stacker og valgt det første alternativet pga fleksibilitet og enkelhet av å utvikle ny funksjonalitet. 

### Spring MVC og Spring LDAP
Spring MVC brukes her for å tilgjengeliggjøre tjenester med REST-api. Med spring mvc er det enkelt å eksponere tjenester vha urler og man la spring formattere retur-data som json  eller text eller det man måtte ønske.

[Spring LDAP](http://www.springsource.org/ldap) er et bibliotek for å gjøre det enklere å snakke med ldap-servere. Den har blant annet en klasse som heter ldapTemplate som i stor grad kan sammenlignes med simplejdbctemplate hvis man har jobbet med dette før. Man slipper plumber-kode og massiv exception-handling man ville ha måttet skrevet uten biblioteket. 

Spring mvc vil kun bli brukt for å tilby crud-operasjoner for klienten(e).

### Apache Sling
[Sling](http://sling.apache.org) er en OSGi-basert plattform for REST-baserte webapplikasjoner. I utgangspunktet bruker Sling et Java Content Repository som data-backend, men det er mulig å skrive adaptere for andre typer datastores, som LDAP. Fordelen er at Sling er bra tilpasset en hierarkisk datastore, som JCR og LDAP er.
For kommunikasjon mot LDAP brukes [Apache Directory LDAP API](http://directory.apache.org/api/).
Sling har veldig fleksible muligheter for å rendre data, men det er mulig det er overkill for dette formålet.

## Klient

### Teknologi: HTML og jQuery

For å holde utvikling på et enklest mulig nivå vil vi kun bruke ren html med javascript. Vi har valgt jquery pga fleksibilitet og hvor enkelt det er å komme i gang med det. 

### GWT
Vi har vurdert GWT, men tidligere erfaringer med lange byggetider og mye arbeid med å få det til med maven har vi droppet dette alternativet. 

# Oppsummering grafisk

**Diagram: Teknologistack**
