# Query

#### Hvordan vil du lagre data med følgende forutsetninger?

**Datastruktur**

- tre-struktur
  - typisk 3-5 nivå i treet
  - enkle parametre på hvert nivå
- tre-noder
  - enkle parametre
  - tre underliggende sett med referansepekere (Høy, Medium, Lav) kobblingskoeffisient -sett
  - et underliggende map med (referansepeker-koeffisient-teller) (bruksstatistikk)

**Aksessmønster**

- 99% query-basert read
  - vektet søk på referansepekerene i settene og mappet, resultatsettet som en prioritert liste av nodene basert på koblingskoeffisienter og statistikk
  - les medfører ikke oppdatering av statistikk
- 1 % write
  - hovedsaklig (99%) oppdatering av bruksstatistikken
  - resten, insert node, update parames, delete node

**Datavolum**

- Under 10.000 noder, men bør kunne skalere til en 100.000 noder

**Mulig kontekst**

- En kan se for seg at en lager et system som observerer brukeraksjoner for å kunne gi brukerene en prioritert liste av mulige aksjoner basert på nåsituasjonen og brukerens grovgrupperte historikk (høy, medium og lav sannsynlighet på tidligere aksjoner)
