# Potensiale

#### Test 

- Skrive tester for funksjonalitet som brukes fra web og pocket. Hittil har det vært mye fokus på jobber. John Peter har identifisert noen prioriterte områder å starte med: 
    - [NGF<sub>~1547@JIRA](NGF</sub>~1547-JIRA.md) Skrive jiraissues for automatiserte tester av funksjonalitet i pocket 
    - [NGF<sub>~1548@JIRA](NGF</sub>~1548-JIRA.md) Skrive jiraissues for automatiserte tester av funksjonalitet i Web 

- Lære bort noen flere konkrete "slik tester du scenario X"
    - teste exceptionhåndtering 
    - eksempler på fornuftig (f.eks. logikk relatert til workflow) og ikke<sub>~fornuftig bruk (junit4mockery</sub>~testene) av mocking/mockerammeverk  
    - teste integrasjon med JMS
    - teste filbehandling (ligger vel en test som kan brukes som eksempel)
    - teste servlets og facelets. 

- Legge en konkret plan for å få slettet gammel kode som ikke vedlikeholdes 
    - I utgangspunktet venter vi på at nyeAN skal skrive adminfunksjonalitet så vi kan begynne å slette/rydde i "gamleAN"

- Formalisere og automatisere systemtester 
    - Hittil har vi brukt all tid på å skrive tester som verifiserer at koden fungerer slik vi mener den skal fungere. Dette er den mest kost<sub>~effektive måten å redusere antall feil på. Når dette begynner å komme på plass bør man starte å se på automatisering av systemtest og andre tester som utføres manuelt av SA</sub>~er og 2. linje. 
    - Definere et sett med tester som må være grønne for å kunne sette en ny versjon i produksjon. Dette sitter i dag i hodet til John Peter, Connie og Elisabeth. 
    - Refaktorere og skrive automatiserte, in-process tester der det er hensiktsmessig. Det er vanligvis hensiktsmessig å beholde en del av testene som manuelle tester. 

- Vurdere behov for jevnlig ytelsestest og andre ikke-funksjonelle tester. Måten vi jobber på i dag med "cachetesten" til nyeAN tar mye tid og tester ikke responstid i særlig grad f.eks. 

- Out<sub>~process, men in</sub>~men integrasjonstest fra dao i AN til BM. 
    - [NGF<sub>~1537@JIRA](NGF</sub>~1537-JIRA.md) - Skrive tester som verifiserer at TryggmatService og VaretellingService (BM) starter og er tilgjengelig

#### Arkitekturforbedringer 

- Etablere målbilde for arkitektur AN/NGF-systemet

- Identifisere overlappende funksjonalitet i nyeAN og NGF og vurdere hvorvidt koden skal samles i en felles modul/tjeneste eller hvorvidt vi skal forsette å duplisere. Det er antagelig mest nærliggende å starte med integrasjoner mot eksterne systemer da man der per definisjon har overlappende funksjonalitet. Ordre er allerede identifisert som et slikt område, se neste punkt. 

- Forbedre integrasjon og samhandling med eksterne ordresystemer
    - VI har stor teknisk og arkitekturmessig gjeld spesielt i integrasjonen med IMI. Det resulterer i at vi må leve med en del kjente feil, det er vanskelig å videreutvikle og vanskelig å debugge/teste når noe er feil. 
    - [ANARK<sub>~104@JIRA](ANARK</sub><sub>104</sub><sub>JIRA.md), [ANARK</sub><sub>72@JIRA](ANARK</sub><sub>72</sub><sub>JIRA.md), [NGF</sub><sub>1728@JIRA](NGF</sub>~1728-JIRA.md)

- Forbedre ruter og planer (Ole Henrik er på ballen)
    - LastTOSRuter - [NGF<sub>~903@JIRA](NGF</sub>~903-JIRA.md)

- Endre arkitektur for "jobber" som kjører svært ofte. Vi har i dag en del jobber som kjører f.ek.s hvert 2 minutt. I BM har man som et første trinn flyttet disse til en kontinuerlig prosess (BongMottaket) og trigger "jobber" fra Autosys via RMI. Dette sparer lasting av en stor appcontext som sparer mye ressurser ++. Det samme kan antagelig være et godt første trinn for Asko Netthandel. 

- Varelinking 

- Gjennomgang av ordregruppekonseptet og se på muligheter for en generalisering/rydding for å legge til rette for utvidet bruk. Hensikten er å legge til rette for å utnytte et antatt potensiale ved optimalisering av vareflyt fra lager. 

#### Prosess og hvordan vi jobber 

- [ANARK<sub>~109@JIRA](ANARK</sub>~109-JIRA.md) - Standardisere og strømlinjeforme prodsettingsplan

- Innføre konseptet og mulighet for rollback ved prodsetting. Et første trinn er antagelig å skrive script for å rulle tilbake databaseendringer for hver release. 

- Sette opp konfigurasjonsstyring

- Gjøre skikkelig opplæring og handover av oppgaver og ansvar til drift 

- Gjøre skikkelig opplæring og handover av oppgaver til 1. og 2. linje (spesielt John Peter bruker verdifull tid på ting som andre kan gjøre) 

- Heve kompetansenivået innenfor Clean Code og refactoring. Lese et par bøker og ha noen foredrag/studiegrupper er muligens nødvendig. 
    - [NGF<sub>~1565@JIRA](NGF</sub>~1565-JIRA.md) - Lage huskeliste ved endring av kode 
    - Se forøvrig https://wiki.cantara.no/display/dev/Excellent+Books
    - [Clean Code: A Handbook of Agile Software Craftsmanship](http://www.amazon.co.uk/Clean<sub>~Code</sub><sub>Handbook</sub><sub>Software</sub>~Craftsmanship/dp/0132350882/ref=sr_1_1?ie=UTF8&s=books&qid=1225918786&sr=8-1) by Robert C. Martin
    - [Refactoring databases](http://www.amazon.com/Refactoring<sub>~Databases</sub><sub>Evolutionary</sub><sub>Addison</sub><sub>Wesley</sub><sub>Signature/dp/0321293533/ref=sr_1_1?ie=UTF8&s=books&qid=1226673918&sr=1</sub>~1) by Scott Ambler
    - [Refactoring: Improving the Design of Existing Code](http://www.amazon.com/Refactoring<sub>~Improving</sub><sub>Existing</sub><sub>Addison</sub><sub>Wesley</sub><sub>Technology/dp/0201485672/ref=sr_1_1?ie=UTF8&s=books&qid=1226673663&sr=1</sub>~1) by Martin Fowler

- Heve kompetansenivå innenfor hvordan JVM-en fungerer og hvordan applikasjoner driftes på Linux plattform. 
    - Vi har gjort noen stunt her, se [FL:Driftsdokumentasjon](../FL/Driftsdokumentasjon.md)

#### Test og prodmiljø

- Innføre personlige brukere og ta vekk fellesbrukerne "oracle" og "jetty". 

- Få kontroll på ressurser og nettverk  i de ulike miljøene. 
    - Ta i bruk Cisco ACE som ny webproxy 
    - [NGF<sub>~1168@JIRA](NGF</sub><sub>1168</sub><sub>JIRA.md) - Samkjøre så alle HH</sub>~klienter bruker samme URL

- Skille utviklingsmiljøer for "leking" og ALT (som skal speile prod). 

- Definere en "eier" av ALT-miljøet. 

Kunne skrevet veldig mye her, men har snakket mye med Connie og Linn i lengre tid, så tror ikke det er stort mer jeg kan bidra med før man finner ut hvordan man vil gjøre disse tingene.
