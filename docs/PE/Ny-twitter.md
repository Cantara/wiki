# Ny twitter

- CASE - Lage TWITTER API *

Tipper litt på tall:
Registrerte brukere: 30 mill brukere.
Aktive brukere pr uke: 6 mill brukere.
Meldinger pr dag: 60 mill meldinger.

På datalaget:
Query-intensivt
Scalability
Availability

Ikke store krav til latency.

Hovedproblemet er søk.  De holder meldingene ganske lenge, og å gjøre fritekstsøk på såpass store datamengder er tungt/umulig i en database. Søkemotor må inn.

Relasjonelle databaser er dårlig egnet.

Laaang diskusjon om  design kokte basicly ned til dette:
- Vi tror at det er lurt å bruke en graph database. Dennne er godt egnet til å navigere i, kan håndtere store datamengder og funker bra sammen med distribusjon.
- Tilbyr greie søkemuligheter.  Bør flytte så mye som mulig ut i randsonene for å spare baser og slikt.
- Fornuftig å bruke asynkronitet til å spre postingene til etter en publish subscribe modell.
