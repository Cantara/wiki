# Architecture suggestions for systems like Altinn

Grunnide: Gitt de åpenbare kravene til systemer alà altinn, 

a) hvorfor er db-sentrisk og batch-orientert arkitektur feil vei

b) hvilke egenskaper bør være grunnleggende drivere, 

c) hvilke arkitekturbyggeklosser og patterns er aktuelle for denne typen systemer 

Rapport fra DNV om altinn: http://www.regjeringen.no/upload/NHD/Vedlegg/Rapporter_2012/altinn_sluttrapport_20120321.pdf Se spesielt kapittel 5.5.

"Økende datamengde vil gi begrensninger i backup mulighetene. Datavolumet som det tas backup av er i dag på 8,8 Terrabytes (TB). Backup tar 12 timer og vil øke med økende datamengder (ref figuren under). En plan for hvordan fremtidige datavolumer skal håndteres har vi ikke funnet." 

"Det er ennå ikke forsøkt å deploye i fart. Deploy innebærer dermed nedetid. Man må ta ned systemet ved deploy fordi databasen må oppdateres ved hver deploy og stenger da for andre brukere, komponentene er ikke designet med versjonsnummer og systemet håndterer ikke flere samtidige versjoner av komponenter." 

Systemet synes ikke designet for å håndtere store datamengder da batchkjøring reduserer responstid 
bl.a. ved bruk av basen, og det ikke er mulig å kjøre parallelle batcher, slik det er i Altinn 1. Dagens 
vindu er i ferd med å gå fullt, og med forventet økning i datamengde vil det sannsynligvis føre til 
behov for batchkjøring på dagtid med tilsvarende vanskeligheter med å opprettholde responstid på 3 
sekunder.

"I litteraturen som beskriver databasesentrisk arkitektur sies det
at skalering gjennom økning av HW fungerer kun i en viss grad, etter et gitt punkt må skalering også 
omfatte redesign av komponenten"

"Stored procedures er i seg selv 
ikke et problem men en vanlig måte å organisere felles databaseoperasjoner ved at prosedyrene legges 
i databasen. Dette gjøres ofte for å forenkle og for å forbedre responstidene i systemet. "
