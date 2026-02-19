# Hardware

## Cluster, Grids og Container

Elementer som forsøker å gjøre noe av det samme.

### Container.

- Omslutter din komponent
- Livssyklus egenskaper
- Kan tilby infrastrukturtjenester
- Transaksjoner
- out of process scaling
- Tilby endepunkt til komponenter
- Sammenkopling av komponenter

Skeptisk til infrastrukturtjenester, da de ofte blir benyttet i hytt og gevær.

**OSGI**
+
Versjoner
Classpath
Multiversjonstøtte
Full lifecycle

\-
Komplekst
Classpath-hell
Big BLOBS
intrusive

**EJB**
+
SSB
JPA
Defaulting og annotations

\-
Lang oppstartstid
Intrusive
Localbeans
Mobilitet

**Spring**
+
Non-intrusive
Valg
JDBC-template
Interface orientert

\-
XML-hell
BLOAT
WS/remoting
Spring MVC

OSGi: Versjonering - full lifsyklus. Eneste valget her.
Brukes av: Dynamisk distribuerte applikasjoner

Spring: Defaulter til dette.
Brukes av: 2,5 lags webapper.

EJB: Bred industristandard backet av mange open source og komersielle leverandører.
Brukes av folk som er opptatt av bred industristøtte og standarder.

### Grid.

Grid vs spaces.
En kontrollerende master worker. Push.
Space. Ingen kontrollerende enhet. Pull

### Cluster

**Hardwarecluster** (delt state)
Øke SLA for en Silo. Failover.

**DB-cluster** (delt state)
Øke oppetid.
Økt ytelse vhj vertikal partisjonering.
Økt kompleksitet, oppsett og driftskostnader.
Økt ytelse løses best ved partisjonering "på utsiden".

Container cluster (delt state)
"Poor mans solution for bad design"
Bedre å dele state med f.eks distribuert cache, en å dele ved hjelp av clustering.

Vi liker hardwareclustering og DB-clustering hvis vi må. Containerclustering er vi ikke kjempeglade i.

Lastbalanserer:
Gå for enkel strategi. Ikke noen flere magiske bokser.
Sticky session.

Begrense deg til det du trenger og ikke gjør noe mer en det du trenger. Verdien kommer høyere opp i stacken. Disse punktene redder deg ikke hvis du ønsker å skalere til himmels.

Ofte kommer driftsleverandøren trekkene med disse løsningene da de vil sikkre ryggen sin.
