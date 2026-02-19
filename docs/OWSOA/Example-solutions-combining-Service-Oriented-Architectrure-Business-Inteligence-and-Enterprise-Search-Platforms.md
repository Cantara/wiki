# Example solutions combining Service-Oriented Architectrure, Business Inteligence and Enterprise Search Platforms

## Om OW SOA relatert til BI

Det kan være litt begrepsforvirring i diskusjonen av bruk av [Data Warehouse (DW) and Business Intelligence (BI)](Data-Warehouse-DW-and-Business-Intelligence-BI.md), og [Search-driven Business Intelligence](Search-driven-Business-Intelligence.md) i forbindelse med SOA tjenester. 

[Search-driven Business Intelligence](Search-driven-Business-Intelligence.md) teknologi har to innfallsporter:
1. En enterprise søkemotor kan støtte seg på SOA tjenester for å indeksere ferdig sammenstilt informasjon 
1. Søketeknolgi kan benyttes som operativ komponent _inne i en SOA tjeneste_ for å f.eks. gjøre indeksering av informasjon som leveres av tjenesten og som et intelligent repository for EDR.

Tilsvarende perspektiv kan skisseres for [Data Warehouse (DW) and Business Intelligence (BI)](Data-Warehouse-DW-and-Business-Intelligence-BI.md) teknologi:
1. Et enterprise datavarehus kan støtte seg på SOA tjenester for å laste data om kjerneentiteter inn i dimensjoner i varehuset
1. BI relatert teknologi (ETL verktøy) kan i noen tilfeller benyttes internt i en SOA tjeneste for batchorientert lasting av tjenestens repository.

## OW SOA og [Data Warehouse (DW) and Business Intelligence (BI)](Data-Warehouse-DW-and-Business-Intelligence-BI.md)

### The killing of ET in ETL

Målsetning: Tjenester i SOA arkitekturen tar det totale ansvar for sammenstilling og leveranse av data om kjernebegreper (vanlig mapping: domeneobjekt <-> dimensjon). Extract og Transform blir i så måte en overflødig aktivitet fordi datavarehusteknologi kan koble seg rett på tjenestene og laste data uten transformering.

## OW SOA og [Search-driven Business Intelligence](Search-driven-Business-Intelligence.md)
Eks. Fast

## OW SOA og [Data Warehouse (DW) and Business Intelligence (BI)](Data-Warehouse-DW-and-Business-Intelligence-BI.md) og [Search-driven Business Intelligence](Search-driven-Business-Intelligence.md)

### Ansvar for forretningsbegrepene

Kan "bridge-the-gap" ved at SOA tjenestene tilordnes ansvaret for begrepsdefinisjonene, og at søk eller trad bi løsninger kan hente verdi av det.
