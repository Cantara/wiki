# Scratcharea for the talk

DENNE BØR KOMME FØR Laws for Project architects

#### Agenda 

1. Terminology chaos 

2. The troublesome architects - developer perspective

3. Even agile teams needs an architect 

#### Intro 

Det er mange spørsmål knyttet til arkitekter og arkitektroller. For eksempel: 
Hva _er_ en arkitekt? 
Hva definerer en _god_ arkitekt? 
Hvordan _bli_ en god arkitekt? 
Hvorfor er det så mange (utviklere) som er negative til arkitekter? 
Hvorfor får det ingen konsekvenser når noen (arkitekter) tar store, viktige avgjørelser og de er helt på jordet? 
Hvorfor _lærer_ ikke arkitekter? 
Trenger vi _egentlig_ arkitekter? 
Hva skal vi bruke disse arkitektene til? 

Nei, vi skal ikke løse ALLE verdensproblemene i dag, men vi skal prøve å rydde litt og gi noen tips til hvordan man bør tenke for å løse noen av disse utfordringene. 

#### 1. Terminology chaos 

- Talk about the different names, titles and roles in use
    - [architecture:Architect roles and responsibilities](../architecture/Architect<sub>~roles</sub>~and-responsibilities.md)
    - Conclude that people use these names differently and that they _are_ overlapping. 
    - Show diagram: [architecture:Communication vs Technology focus](../architecture/Communication<sub>~vs</sub>~Technology-focus.md)

- Suggest solution: 
    - be aware of the terminology jungle 
    - use the simpler scope<sub>~based [architecture:Architect categorization](../architecture/Architect</sub>~categorization.md)
    - Separate between roles, titles, and names and be concrete and precise when dividing responsibilities. 

#### 2. The troublesome architects - as seen from a developer's perspective 

- The cooperation between developers and architects is not always good. We will now take a quick look at some of the common misunderstandings and mistakes and try to give some advice on how to proceed. 

- Age gap: young developers, middle-aged architects 
- Sort of a language barrier; (organization) architects and hard-core programmers use different domain languages 
- Agile vs waterfall, RUP 
- Powerpoint vs working code 
- Heavyweight vs lightweight 

- Vise bilde av [Ivory tower](http://www.metalvortex.com/blog/tower.jpg) vs. bilde av coordinating achitect.
    - Vær ikke fremmed for hverandre.
    - Gjem deg ikke bort i møter.
    - Vis ansiktet ditt (husk en arkitekt har 80% av tiden sin som kommunikasjon) Ref. til den andre praten.

 
- Go through [architecture:Bridging the gap between developers and architects](../architecture/Bridging<sub>~the</sub><sub>gap</sub><sub>between</sub><sub>developers</sub><sub>and</sub>~architects.md) 

- Conclusion: 
    - We need to continuous feedback and we need to learn.
    - Content from [architecture:Learning circle](../architecture/Learning-circle.md)
    - Vi må spille hverandre gode.
    - Høre, lære, forbedre

#### 3. Even agile teams needs an architect 

Subtitle: ALL teams need a tech lead

Vi har nå sett på en del generelle problemer. Vi har sett på to tiltak for å få bukt med disse: 
- tydeliggjøre roller, ansvar og kommunikasjonskanaler 
- legge til rette for feedback og læring 

Som en avslutning vil vi gjerne gå inn på arkitektens rolle i smidige team. 
JA, også smidige team trenger en arkitekt. Det betyr ikke at man trenger en ha en person med _sjefsarkitekt_ som stilling på hvert eneste team. Det betyr at hvert team bør ha én person som er ansvarlig for å ta valg som påvirker arkitektur og design. Denne rollen er innenfor _project scope_ og kalles ofte _tech lead_, men det er ikke noe i veien for å bruke f.eks. Chief Engineer som Olve har snakket om. 

Nevne eksempler på hvilke oppgaver en person med denne rollen bør ta: 
- Støtte opp om at teamet har felles designansvar. 
    - "Lukte" problemer, ta dette opp med en eller flere fra teamet, og finne god nok løsning.
- Ha beslutningsansvar, og ta beslutningen når det er dissens i utviklergruppen.
- Brøyte veg for teamet. Se etter hvilke grep som skal ligge 2-3 steg forran.
- Tilrettelegge for tekniske spørsmål. Sikre at teknologi ikke hindrer teamet å nå målene.
- Utvilkler skal utfordre Tech-lead når beslutninger ikke er fornuftige, eller reduserer farten på teamet.
- Tech-Lead skal utfordre regler og føringer fra PAB.
    - Når disse er i vegen for at teamet skal kunne levere.
    - Kontaktperson mot Coordinating Architectt.
- Oversikt mot kundens totale behov på semi-detalj nivå.
- Sikre at eksterne avhengigheter identifiseres, følges opp og løses. 
- Sikre at vanskelige temaer tas opp, forfølges og løses. Prosjektleder kan godt være utøvende på denne.
    - Høre på summingen i prosjektet, lytt etter om noe skurrer.
- Oversikt over hvem som gjør hvilke oppgaver i prosjektet. Støtte for PL og eksterne som trenger hjelp.
- Ha oversiktsbildet for å kunne svare på spørsmål som:
    - hvem i teamet kan løse en gitt oppgave.
    - hvem i teamet kjenner denne Use-Casen best.
    - hvem hos kunden kan utvikleren gå til for å få svar på sine sp.mål?

Det er ikke Org arkitekter som skal spesifisere hvordan et team skal utvikle, det er TECH LEAD som skal være smøringen og erfaringen som gjør at teamet produserer optimalt innenfor de rammene PAB gir.

Hvilke valg bør diskuteres med coordinating architect? 
- Ønskede brudd på eksisterende arkitektur.
- Regler som forsinker utvikling.
- Implementasjon i eksterne (for teamet) systemer, som gir dårligere løsning i dette prosjektet.
- Tilbakemeldinger på ting dette prosjektet gjør bra.

Hvilke valg må opp i PAB? 
- TODO trenger konkrete eksempler
- Brudd mot "Alle tjenester skal ha aktivitetslogg."
- Ønsker brudd mot: "Alle tjenester skal ha accesskontroll mot AD."
