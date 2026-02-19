# Droneradar

### Formål:

Flyr du en drone i offentlig rom bør du identifisere deg og gi offentligheten tilgang til å følge dine aktiviteter. (real time)

### Løsning:

Droner utstyres med gps tracker som plottes i et offentlig tilgjengelig kart.

### Prosjektgjennomføring:

- Felles prosjektsite
- Felles programkode (open source)
- Alle interessenter får samme info
- Gjennomføres og driftes med en stiftelsesmodel

### Kapre brukere

Hovedstrategi:

- Drones are good strategien.
- Lage hype på at droneflygere selv bør være i forkant av krav som uansett vil komme.
- Selge inn via eksisterende kontakter i dronemiljø.

### [Drone radar design](Drone-radar-design.md)

Det er 3 hovedkomponenter i løsningen som må på plass:

- Trackere med gsm/gprs/3g kommunikasjon
- Server for mottak og håndering av tracker data (posisjonsfeed)
- Bruker website (konto, id og kart plotting)

### Gps tracker teknologi

Drone radar er avhengig av at det monteres en gps tracker på hver drone som avgir forløpende posisjoner til drone radar systemet. Dette gir noen krav til trackerene

1. Må kunne lese posisjoner minst hvert sekund fra gps systemet
1. Må kunne sende posisjon via mobilnettverket minst hvert 5 sekund til drone radar systemet. Via IP (udp/tcp)

**refs:** [Gps tracker technology](Gps-tracker-technology.md) 

### System 

- [drone server info](drone-server-info.md)
- [OpenGTS demoserver](OpenGTS-demoserver.md)

### Document relate to GTS

- http://opengts.sourceforge.net/documentation.html

### Diversje materiell og dokumenter
