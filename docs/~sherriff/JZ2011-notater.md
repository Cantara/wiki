# JZ2011 - notater

## 1. Introdusere problemstillingen - 5 min

I dag skal vi se på hvordan man lager en testtaktikk og velger verktøy som passer til et konkret testproblem. 
Veien frem og valgene som blir gjort underveis er det viktigste, ikke selve løsningen. <bilde: vei, veien er målet, skill> 

For å gjøre dette litt mer håndfast skal vi ta utgangspunkt i et større logistikksystem. 

Beskrive systemet 

trelags-, basert på JSF, spring og hibernate med en Oracle database i bunn. Ganske standard. 
 <JSF, spring, hibernate logo> 

Mye kode og funksjonalitet implementert i databasen OG i java. En herlig blanding - som vanlig. 
1.1. Oracle database, mye logikk i både PL_SQL, plain JDBC og hibernate
Integrasjon via database 
<oracle db, PL_SQL>

Mange integrasjoner 

Stor (>240k LoC) og gammel (10-15år) kodebase, 
Generelt lav testdekning  (~7% line coverage), _ingen_ automatiserte integrasjonstester.

Jeg håper dette er en kontekst mange kjenner seg igjen i. 

## 2. Analyse av tidligere forsøk - 10 min

#### Rollbackstrategi (basert på Spring TestContext Framework)

\- fungerte ikke for funksjonalitet hvor det ble startet ny transaksjon (PROPAGATION_REQUIRES_NEW)

#### Greenpepper - executable specifications and automated functional testing
+ god på kommunikasjon med ikke-teknikere
\- ikke så god på utviklertester pga. høy roundtrip under utvikling
\- tett kobling til infrastruktur - avhengighet til drift
\- vanskelig å debugge feil - avhengighet til drift, funksjonalitet spredt på flere maskiner 

#### Standard JUnit<sub>~tester + custom sql</sub>~script 
+ fungerer for én utvikler 
\- vanskelig å vedlikeholde sql-scriptene
\- tidkrevende oppsett
\- lite robuste tester pga. avhengighet til _delt_, ekstern database
\- ingen god måte å kategorisere ulike typer tester.

#### Flere forsøk basert på egenutviklede mocker og ulike mock-rammeverk

\- trenger å teste mot reell database, mocking løser ikke det problemet. 

Jmock<sub>~, junit</sub>~oppsett

## 3. Gjennomgang av prosessen og valgene som ble tatt - 25 min

- Fokus på fremgangsmåte og hvordan tenke

Ok, da har vi sett på tre mulig tilnærminger til testing i denne konteksten. Hver med ulike styrker og svakheter. Hvilken er best? 
...

Det kommer an på.

Det kommer selvsagt an på hva som er behovet og målet. Så hva er faktisk _behovet_? 

#### 3.1 Hva er behovet? 
3.2. Kartlegge og prioritere behov og drivere

- Utviklersynspunkter 
    - Vil, men får det ikke til 
    - Vil ikke, kjedelig å skrive tester. 
    - Går ikke, problemet er altfor komplisert til å lage automatiserte tester.  
    - Får ikke tid til å sette oss ned å finne en god løsning.  

- Manager 
    - Færre feil! Just make it work! 

- Test manager 
    - Ikke nok tid til å test alt. 

- Stor kodebase og lav testdekning

- Lite oppsett for å skrive en ny test 

- Få/ingen avhengigheter til drift eller andre avdelinger - utvikler bør kunne sette opp, kjøre og debugge selv. 

- Sette seg inn i arkitekturen og design/kodevalg 
    - Må ha taktikk for PL_SQL, plain JDBC og hibernate-kode, helst samme løsning for å redusere opplæringsbehov for forenkle vedlikehold. 

3.3. Gjennomgå kort aktuelle biblioteker og rammeverk

- GreenPepper / FitNesse 

- JUnit 

- TestNG 

- Spring Testcontext Framework 

- dbUnit 

- Testaco 

- Unitils 

- dbMaintain 

- [Oracle TimesTen In-Memory Database](http://www.oracle.com/technetwork/database/timesten/overview/index.html)

- HsqlDB 

3.4. Utarbeide strategi spesialtilpasset denne konteksten.

- Skrive til ekstern Oracle database
    - Finnes allerede
    - Mye kompetanse på dette, mange som kjenner denne måten å jobbe på. 

- Verifisere data i databasen 

3.5. Forklare valg av konkrete biblioteker, rammeverk og konfigurasjon ++ for å realisere strategien.

- dbmaintain 

- unitils 

- Spring 

- TestNG 

- Ekstern Oracle db-server 

- Egne schema for utviklere og CI-server

3.6. Feedback-loop 

Beskrive iterativ forbedring: Skrive tester<sub>~refaktorere</sub><sub>skrive tester, raffinere oppskriften, skrive tester</sub><sub>refaktorere</sub>~skrive tester, raffinere oppskriften, osv.

Hvilke justeringer har vi gjort underveis? 

- assertDataset 
- 1 database schema per kodebase -> 1<sub>~2 database schema per utvikler og en per branch for CI</sub>~server 
- Deling vs duplisering av dataset mellom tester 

## 4. Demonstrasjon av softwarestack/konkret taktikk - 10 min

4.1. dbmaintain for vedlikehold av tilstand i databasen

4.2. unitils 4.0 (ikke releaset enda) for enklere vedlikehold av testdata

4.3. testng for kategorisering av tester

4.4. Spring til dependency injection

4.5. Stabil oppskrift for én type problemer -> Forklare hvorfor akkurat denne oppskriften passer i vår kontekst. Poengtere at fremgangsmåten gjerne kan gjenbrukes, men at konkret taktikk/oppskrift må tilpasses kontekst.

## 5. Spørsmål - 10 min
