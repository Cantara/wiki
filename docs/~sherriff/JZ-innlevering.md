# JZ-innlevering

Presentation format: 60 min presentation

###### Title

1. **Jeg er møkk lei utviklere som ikke kan skrive ordentlige tester!**
1. Jeg er DRIT lei utviklere som ikke kan skrive ordentlige tester!  
1. Jeg er dritlei utviklere som ikke skriver tester! 
1. Jeg er dritlei utviklere som ikke gjør jobben sin! 
1. Jeg er dritlei utviklere som ikke kan teste! 
1. Hvordan utarbeide taktikker for utviklertesting tilpasset problemet?  
1. Konteksttilpasset utviklertesting - hvorfor og hvordan 

###### Abstract

"_Enhetstester er lett. Integrasjonstester er vanskelig._" er en vanlig holdning blant norske utviklere. Det reelle problemet er egentlig ikke hvorvidt man tester enheter eller integrasjoner, men at mange utviklere ikke har peiling på hvordan de skal gå frem for å skrive skikkelige tester.

Erfaringsmessig har det vist seg viktigere å bygge kompetanse på problemanalyse enn å pugge konkrete oppskrifter. Fremgangsmåte og prioriteringene som må gjøres for å skrive gode tester står derfor i sentrum, men også teknologi- og verktøyalternativer vil bli diskutert.

Foredraget vil være case-orientert, med utgangspunkt i testing av et større logistikksystem.

Language: Norsk 

Level: Intermediate 

###### Outline

1. Introdusere problemstillingen/kontekst - 5 min
    1. Stor (>240k LoC) og gammel (10<sub>~15år) kodebase , mange integrasjoner (50+), trelags</sub>~, database-orientert arkitektur basert på JSF, spring og hibernate
    1. Oracle database, mye logikk i både PL_SQL, plain JDBC og hibernate
    1. Lav testdekning generelt (~7% line coverage), ingen automatiserte integrasjonstester
1. Analyse av tidligere forsøk - 15 min 
    1. Rollbackstrategi basert på Spring TestContext Framework - fungerte ikke for funksjonalitet hvor det ble startet ny transaksjon (PROPAGATION_REQUIRES_NEW)
    1. Greenpepper - god på kommunikasjon med ikke-teknikere, ikke så god på tester for å støtte utvikling pga. høy roundtrip under utvikling, tett kobling til infrastruktur og vanskelig å debugge feil. 
    1. Standard JUnit<sub>~tester + sql</sub>~script - vanskelig å vedlikeholde sql-scriptene + lite robuste tester pga. avhengighet til ekstern database, ingen god måte å kategorisere ulike typer tester.  
    1. Flere forsøk basert på egenutviklede mocker og ulike mock-rammeverk
1. Gjennomgang av prosessen og valgene som ble tatt - 20 min 
    1. Fokus på fremgangsmåte og hvordan tenke
    1. Kartlegge og prioritere behov og drivere 
    1. Finne aktuelle biblioteker og rammeverk
    1. Utarbeide strategi spesialtilpasset denne konteksten. 
    1. Velge konkrete biblioteker, rammeverk og konfigurasjon ++ for å realisere strategien. 
    1. Skrive tester<sub>~refaktorere</sub><sub>skrive tester, raffinere oppskriften, skrive tester</sub><sub>refaktorere</sub>~skrive tester, raffinere oppskriften, osv. 
1. Demonstrasjon av softwarestack/konkret taktikk - 10 min
    1. dbmaintain for vedlikehold av tilstand i databasen
    1. unitils 4.0 (ikke releaset enda) for enklere vedlikehold av testdata
    1. testng for kategorisering av tester
    1. Spring til dependency injection 
    1. Stabil oppskrift for én type problemer -> Forklare hvorfor akkurat denne oppskriften passer i vår kontekst. Poengtere at fremgangsmåten gjerne kan gjenbrukes, men at konkret taktikk/oppskrift må tilpasses kontekst.
1. Spørsmål - 10 min 

###### h6. Highlight Summary (English only)

Want to improve your developer testing skills? This presentation will explain how to analyze a given problem and evaluate different approaches for writing automated tests. 

Want to improve your developer testing skills? This presentation will explain how to analyze a given problem and evaluate different approaches for writing automated tests. 

Additional equipment: 

###### Expected audience

Utviklere, arkitekter, testere 

###### Tags 
Experience report
Enterprise Java
Testing

###### Speaker 

Speaker name: Erik Drolshammer 

- Speaker's profile:
Erik jobber som seniorkonsulent i Webstep, er styremedlem i IASA Norge og aktiv bidragsyter til Cantara Community Wiki. Han har spesialistkompetanse på utviklertesting og byggemiljø i store prosjekter og har vært sentral i utviklingen av konseptene Enterprise Maven Infrastructure  og JigZaw (en testmodell for smidig utvikling). 

Email: erik.drolshammer@webstep.no
Profile picture (max 500KB). Supported types: jpg, jpeg, png, gif.
