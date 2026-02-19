# Data laget

## Datalaget.

Hvilke alternativer har vi?

**RDBMS**
SQL - Spørringer utenfor domenemodellen. SQL kan være et godt valg. Enkle updates. Ting som du må bygge en stor domenemodell for å få tak i, men hvor du bare er interessert i et subset av data.

ORM - Det politisk korrekte alternativ.

ActiveRecord  - Administrasjonsapper

Generelt: Krever at du lever i en strukturert verden. At dataene dine strukturerte. Ofte har du ikke strukturerte data.
Relasjonsdatabaser skalerer dårlig på informasjonskopleksitet. Og vi vet jo at informasjonskompleksiteten i verden bare øker. Og dataene blir mindre og mindre strukturerte.

Implementasjoner:
MySQL / Postgres - Holder stort sett.
Oracle/MS SQLserver. Hvis du ikke har et rikt nok featureset
HSQLDB/JavaDB - Effektiv stopper for integrasjon via databasen

**Non-relational**
Document oriented databases - Enkelt å skalere opp.
Column og map oriented databases.
Object databases -
Hierarchical databases - Store datamengder og ad-hoc relasjoner. Yter som bare det. Vanskelig å skalere over 1 CPU.
Network databases - Store datamengder og ad-hoc relasjoner. Yter som bare det. Vanskelig å skalere over 1 CPU.
GraphDatabaser - neo4J
Generelt: Ikke standarder. Små leverandører. Dårlige på strukturerte data. Varierende kvalitet. Høy risk, høy gain for det rette usecaset.

**No DB** (Skjult persistens)
Søkemotor - brukt som persistensmekanisme. Gir gode muligheter for ad-hoc queries. Ustrukturerte data.
Grid -
Service (not your problem)
Flatfil - come on....
Minne  -

Generelt: Litt svake på dataintegritet. ;-)

**Transaksjoner**
Skalerer _IKKE_
Så hvis du skalere kan du du bare glemme i transaksjoner: og da kan du enten ikke ha dataintegritet eller gjøre kompenserende tiltak. Ved kompenserende tiltak - Ekstremt viktig med Audit.

Tips: fokuser på krav, ikke på teknolig.

Forsøk på å tegne opp relativt landskap
|  | NON DB |  |  |  |  | Non-relational |  |  |  | RDBMS |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Søkemotor | Grid | Service | flatfil | minne | document | column | object | graph | SQL | ORM | Active record |
| Scalability | 8 | 8 | ? | 4 | 10 | 6 | 8 | 4 | 9 | 6 | 5 | 6 |
| Availability | 6 | 9 | ? | 3 | 10 | 7 | 7 | 7 | 7 | 9 | 8 | 9 |
| Integritet | 6 | 6 | ? | 2 | ? | 4 | 4 | 8 | 7 | 8 | 9 | 8 |
| Query | 9 | 4 | 2 | 2 | ? | 7 | 5 | 4 | 8 | 6 | 4 | 5 |
| Latency | 7 | 8 | 10 | 4 | 10 | 6 | 8 | 4 | 9 | 6 | 3 | 6 |
| Persistens | 5 | 7 | 7 | 2 | 0 | 7 | 8 | 7 | 9 | 8 | 7 | 8 |
| Transaksjoner | 0 | 4 | 0 | 3 | 4 | 6 | 7 | 9 | 6 | 8 |
