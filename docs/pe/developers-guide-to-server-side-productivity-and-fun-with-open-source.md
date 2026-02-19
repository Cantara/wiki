# Developers guide to server-side productivity and fun with Open Source

# 

# Developers guide to server-side productivity and fun with Open Source

## *A flight through the landscape of feature sets, technologies and Open Source implementations(45 min)*

### [Thor Henning Hetland](/web/20090419183026/http://wiki.cantara.no/display/~totto)

[Show](/web/20090419183026/http://wiki.cantara.no/plugins/slideshow/run-slideshow.action?pageId=394270)
 

[Show](/web/20090419183026/http://wiki.cantara.no/plugins/slideshow/run-slideshow.action?pageId=394270)
 
[Hide inline](#)

# motivasjon

1 / 21

# om oss

Totto:   
Tobias:   
Ole Martin:

Vår bakgrunn/mål: Ikke nødvendig vis å få folk til å bruke F/OSS, men men å få folk til å bruke hue. F/OSS er ofte riktig, men ikke alltid.

2 / 21

# Agenda

3 / 21

# "There can be only one"

- Debunk the myth that there is only one solution....
  - J2EE
  - Relasjonsdatabaser
  - Spring
  - Rails  
    (Selvfølgelig er det untak, men folk liker "oppskrifter" og har en tendens til å velge det som funket sist. (Folk=Utviklere, men også produkteiere, arkitekter og prosjektledere.)  
    Hvis vi ikke aktivt motarbeider dette mindsetet så kommer ikke bransjen videre.   
    Man må være bevist sine valg.   
    Morsom historie: Struts og Struts2. Hvorfor ville de så gjerne ha navnet?   
    (Theme from Highlander)   
    Totto

4 / 21

# Decisions, decisions, decisions

Eksempel på valg som er tatt  
**Nettsted**

1. Context : f.eks Artikkelbase til publisering.
2. Teknologi : f.eks CMS
3. Implementasjon f.eks OpenCMS

Bla opp millioner av teknologier, på alle nivåer. (Multi slide in, farger osv)

Men detter jo ikke hele bilde - det er jo implementasjoner.

Sartre: "Med valg følger angst"   
"Nobody evers been fired for choosing IBM"   
"You can´t go wrong with beige"   
Tobias

5 / 21

# company policies and decisions

Betyr at "there can only one" og er ulurt av alle de samme årsakene.

- Reduserer verdiskapning fra teknologi (50-90%)
- Øker oppstart og opplæringskostnadene med (30-200%)
- Insjekkingsprosesser, partisjoneringstrategier, teknologivalg.
- Så fort du har du har definert en company policy har du definert en veldig stor hammer som du sier på på alt fra å slå inn spikre til å skru inn lyspærer.

I hvilke grad er det formålstjenelig å la driftsleverandører legge rammene for hvilke teknologi man kan bruke?

OG... det er jo Java eller .Net

Opplæring:

- Bruke teknologi bare for
- Enda rarere hammere til å skru inn lyspærer?
- Trenger et bredt spekter av verktøy i kassa di.
- Problemer der man ikke har noen adekvat verktøy: Stop og tenk! Kunne vi ha brukt noe annet her?
- Opplæringsgjeld. (alle steder der du bruker hammer på noe annet en spiker)

-Ikke underestimer verdien du får av enabler av knowledge workers.

6 / 21

# kultur

Polarisering:   
Religionskrig som en konsekvens av skjev maktfordeling i softwarebransjen. (Kommersielle aktører har hatt all makt(penger) og opposisjon må ty til fanatisme for å bli hørt)

MS / Stallman / Linux

7 / 21

# How do YOU make decisions

(Håndsopprekning?)

- Lese om produktarkene? (CMS matrix)
- Teste ut demoer (CMS eksempelet?)
- Prototyper?
- Tidligere erfaringer(egne eller andres)?
- Implementere to løsninger?  
  (vurdere en slide seinere som tar for seg hvordan man faktisk burde ta valg)

Folk fokuserer på prosess, snarveier på kriterier.   
Prosessen er neglisjerbar - hvis ikke kriteriene er riktig:   
Du skal velge en regelmotor, men problemet ditt er bedre løst med en DSL.

Du skal løse en utfordring, ikke velge en teknologi/produkt. (There is no silver bullet)

8 / 21

# Categorising and exemplifying solutions

- To make good selections, we need to categorise the problems and contexts

Divide an conqurer.

For å ha konteksten klar vi har en app med tradisjonell lagdeling: persistens og forretningslag.

Forretningslogikken er mest spennende. Vi ser på den:

Tradisjonelt to leire:

- statefull
- stateless

Det er lite fokus på valg

Fokuserer på egenskaper ved løsniningen og krav til teknologi.

Utvalg av egenskaper på et utvalg av teknologier.

Teknologivalget gir deg et sett med egenskaper som du ikke blir kvitt. Ikkefunksjonelle krav er lette å finne egenskaper for.

De funksjonelle er ikke så lette.

Tobias

9 / 21

# Hva er essensen her:

Man må analysere hvilke valg du *faktisk* tar med teknologivalg.

- Skalere stort i fremtiden?
- Integrasjon med flere systemer?
- Utvidelse av forretningsområdet?

Litt leantenkning?: Hva kan endres? Hva er du stuck med?

10 / 21

# State

- Lets look at which strategies we have regarding handling state in server-side systems
- Gjennomgang av hvordan man håndterer objekter i forretningslaget og klientene.
  - Datastyles.
  - State.  
    Ole-Martin

11 / 21

# Data-style(s)

- And what are our options redarding datamodels?  
  Ole-Martin

12 / 21

# Landscapes

Schwær 3d modell.

- Totto

13 / 21

# CASE 1: Simple webapp

Gøy og produktivt.   
Kundesystem. Enterprise.

Kundedata i forskjellige databaser.

Create er umulig. Delete skjer ikke.   
Større kontroll over data.   
ORM faller bort

Forretningslaget.   
DSL.   
Regelmotor.

Kundedata.

Andere avdelinger i alle systemer.

Rails på initielle

EDR - open source.

Generer CRUD fra database.

Nivå: 2   
Endringshyppighet.   
Problem med oppetid.   
Konvertering til og fra en felles norm. (Overnormalisert og alt key value)

ORM funker bra i en av 100 tilfeller mot standardsoftware. Generisk datamodell.

14 / 21

# Alternativ

\*Groovy og Grails

- - RAD vhj scaffolding.
  - Enkel integrasjon med Java.  
    \*Ruby og Rails
  - XML støtte
  - RAD Scaffolding osv.  
    \*Scala og Lift
  - Concurrency (Actor)

15 / 21

# database

Det politisk korrekte er Relasjonsdatabase med ORM.

"nobody ever got fired for buying IBM equipment" - Ikke sant?

16 / 21

# hva er problemet med Rel DB?

Vise til teknologilandskap.

- Skalerer dårlig på komplekse strukturer. (eksempel med xml-struktur inn i en database - ref John Davies)
- Du skal jo ikke gjøre databaseintegrasjon likevel, hvor trenger du da SQL (og relasjonsdatabaser) ?
- ORM er vanskelig. (Spesielt når utviklerene dine ikke skjønner hvilkequeries de spinner av)

17 / 21

# ORM - alternativer

- Hva med active record? De fleste trenger *egentlig* ikke å mappe fra relasjoner til database anyway(speilbilde av databasen)

18 / 21

# Arkitekturgjennomgang?

Hvordan applyer du denne tankegangen?

Case:

- Hvilke sentrale egenskaper ønsker du å oppnå?
- Se på landskapet - hva gir deg det du ønsker?
- Velg noe, og se om det gir deg et du ønsker?
- Hvordan var dette annerledes mot det andre man kunne ha valgt?
- Retrospective?
- Ambisjoner?
- Hva er problemstillingene?
- Hvordan bruker jeg landskapet for dette caset

19 / 21

# CASE 2: Telecom provisioning

- Ole-Martin

20 / 21

# Wrap up..

For alle valg du gjør på serversideutvikling finnes det alltid et godt os alternativ.

Krav endres fra dag til dag. Teknologivalgene blir med deg lenge.

Selvom du finner en god hammer er ikke alt du ser en spiker.

Fokuser på egenskaper: hva ønsker du å oppnå.   
Fokuser på de forskjellige lagene.

- Totto  
  Sjekk wiki:

21 / 21
