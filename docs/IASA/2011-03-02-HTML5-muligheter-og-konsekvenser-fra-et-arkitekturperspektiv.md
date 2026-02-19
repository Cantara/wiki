# 2011-03-02 - HTML5 - muligheter og konsekvenser fra et arkitekturperspektiv

#### Praktisk

- Tid: kl 18:00
- Sted: Scotsman, 2. etg.
- Påmelding: Ingen påmelding denne gang grunnet tekniske problemer med påmeldingssystemet. **Det er bare å møte opp!**
- Trådløst nett
  - SID: *kontor*
  - Passord: blir opplyst på møtet

#### Motivasjon

Grunnen til at vi setter søkelyset på HTML5 i IASA er tre ting:

- HTML 5 endrer på balansen mellom ansvaret til klienter og underliggende "tjenester"
- HTML 5 er på vei til å bli definert som morgendagens og fremtidens standard, og ventetiden/frontend krigen ser ut til å være vunnet
- temaet er enkelt å organisere et møte om, og det er manglende kompetanse både hva HTML 5 er og hva det betyr for arkitekter

### Agenda (tentativ)

Todelt opplegg denne gangen: Først lyntaler for å sette kontekst og gi tilhørerne felles basis. En del forkunnskaper om HTML5 er en fordel men ikke nødvendig. Del 2 blir "styrt openspace" med Totto som fasilitator.

###### Del 1 - lyntaler

**HTML5 i et applikasjonsperspektiv (intro)** [Thor Henning Hetland](/web/20221205153812/https://wiki.cantara.no/display/~totto)

- La oss glemme HTML5 video politikken og canvas magi ikveld
- HTML5 vil medføre mere enn fancy websider
- HTML5 ser ut til å bli den savnede **enterprise rich internet applications (RIA)** client platformen
- Fra websider til **chubby HTML5 apps**
- Denne endringen er det viktig at vi software arkitekter skjønner rekkevidden og konsekvensen av..
- (Og ha i bakhodet, at dette er **samme trend** som iOS og android apps representerer...)
- Så la oss starte opp med en liten HTML 5 teknologi oppvarming...

**Valg av HTML5 teknologi for grafisk fremstilling på web, bruk av SVG og canvas.** - Sverre Ølnes

**WAC** - [Trygve Lie](/web/20221205153812/https://wiki.cantara.no/display/~cantara@trygve-lie.com)

- Ikke web sider, men **applikasjon**. Vi må endre tankesett.
- Hva finnes av applikasjoner skrives i html, css og js i dag og hvor kjører de?
- Hvordan gå "native" og hvordan bygge og pakketere.
- Spesifikasjonene W3C Widgets og WAC

**I hvilke typer løsninger passer de ulike spesifikasjonene fra HTML5 inn og hva bør utviklere på klientsiden inneha av kompetanse.**

- Geir Wavik - [@geirwavik](http://twitter.com/geirwavik) - Miles.no
- Det man får ut av presentasjonen er da hvilke spekker som passer inn  
  for hvilken type løsning man utvikler samt hvilke fordeler dette vil gi.

**Local storage** - [Trygve Lie](/web/20221205153812/https://wiki.cantara.no/display/~cantara@trygve-lie.com)

###### Del 2: Unconference workshop

**"Hva betyr HTML5 (og apps) for virksomhetsarkitekturen?"**

- [G1 - Bruksmønstre facilitator Trygve](/web/20221205153812/https://wiki.cantara.no/pages/viewpage.action?pageId=22216904 "G1 - Bruksmønstre facilitator  Trygve")
  - trafikk (økt trykk, uforutsigbar last)
  - data (JSON, REST, XML)
  - API - usecases OG ressurs API-er
  - SLA - apps poller ofte, 24x7x365
  - latency - Web 2.0 mennesker takler ikke latency,
  - on-line-/offline - inkonsistente data fra apps... data fra "gamle versjoner"
- [G2 - Gjenninnfører vi problemene med tykke klienter? Facilitator Ove Jordbakke](/web/20221205153812/https://wiki.cantara.no/pages/viewpage.action?pageId=22216910 "G2 - Gjenninnfører vi problemene med tykke klienter? Facilitator Ove Jordbakke")
- [G3 - Sikkerhet Facillitator Bjørn Nordlund](/web/20221205153812/https://wiki.cantara.no/pages/viewpage.action?pageId=22216912 "G3 - Sikkerhet Facillitator Bjørn Nordlund")
- [G4 - Krav - åpne API Facilitator Totto](/web/20221205153812/https://wiki.cantara.no/pages/viewpage.action?pageId=22216908 "G4 - Krav - åpne API Facilitator Totto")

### Ressurser

- [Diverse HTML 5 teknologi presentasjoner](../FRONT/Presentations.md)
- [Front:HTML 5 Code Camp]
- [Front:HTML5 overview]
