# Norwegian User Manual

### Bruk

- [ACS:Redigere din personlige info](../ACS/Redigere<sub>~din</sub>~personlige-info.md)
- [ACS:Redigere en CV<sub>~profil](../ACS/Redigere</sub><sub>en</sub><sub>CV</sub>~profil.md)
- [ACS:Last ned flere CVer samtidig](../ACS/Last<sub>~ned</sub><sub>flere</sub><sub>CVer</sub>~samtidig.md)
- [ACS:Last ned én CV med forhåndsvisning og mulighet for justeringer](../ACS/Last<sub>~ned</sub><sub>én</sub><sub>CV</sub><sub>med</sub><sub>forhåndsvisning</sub><sub>og</sub><sub>mulighet</sub>~for-justeringer.md)

### Problemer

- [ACS:Faq](../ACS/Faq.md)

### Introduksjon

**ACS - Awesome Competence System** er **ikke** det navnet indikerer et rent CV arkiv men et **Competence Management System**.  Vi kan dele hovedfunksjonaliteten til systemet i følgende hovedområder:

- **_Salgsstøtte_** 
    - aktiv hjelp til å finne gode kandidater på etterspurt erfaring og kompetanse (både for selgere og for konsulenter som sitter i kundeaksen)
    - rask tilgang og verifikasjon av kandidater til et behov
- **_CV produksjon_**
    - støtte for å vise de beste sidene tl kandidater opp mot forskjellige roller og profiler
    - god støtte for detaljert tilpassninger og fremheving av kompetanse og erfaring
    - produksjon av CV-dokumenter til videre justeringer og distribusjon
- **_Tilbudsstøtte_**
    - rask og kvalitetssikret utarbeidelse og gjenbruk av kompetansematriser med koblinger til erfaringer som støtter ratingen
    - gjenbrukbare rangeringer for tidsbesparelse og oppdatert scoring
- **_Kompetanseutvikling og kompetansestyring_**
    - nå, mål og oppfølgingsprosesser for styrking av kompetanseområder samt identifikasjon og tetting av kompetansehull. Løsningen er under sterk utvikling for å støtte disse prosessene bedre fremover.

### Systemets oppbygging

Løsningen er bygget opp av følgende kjerneelementer som den enkelte person aktivt forvalter:

| !Add person - ACS CV.png | align=right,thumbnail! | * **Person** Navn, personopplysninger, og avdelingstilhøringhet. |
    - **Technology** (Competence). Nøkkelkvalifikasjoner som f.eks teknologier og andre sentrale egenskaper ved en person. Her skal vi ikke ha oppsummering av personens profil, det kommer senere.
    - **Erfaring**. Arbeidserfaringer personen har hatt, gjerne ned på prosjektnivå med oppgaver, roller, ansvar og teknologier.
    - **Education**. Utdanning og skolegang.
    - **Workplaces**. Nåværende og tidligere arbeidsgivere. Selvom disse elementene ikke er vanlig å bruke i CV-produksjon fra konsulentmiljø, utgjør de sentral informasjon som er viktig for bl.a. salgsstøtteprosessen.
    - **Other**. Her er det litt friere hva den enkelte ønsker å eksponere, men språk, publikasjoner, sentrale verv, sertifiseringer m.m. er gode eksempler på informasjon mange vil ønske å benytte. |
|  | I selve CV-modulen, så har vi følgende domeneobjekter som den enkelte, samt selgerne aktivt benytter |
\\
- **CV**. Systemet støtter opp til 4 forskjellige profiler/CV<sub>~er for en person. Man lager en CV per profil. På selve CV</sub>~en, så velger man de relevante innslagene fra en person, som til sammen utgjør den erfaringselementene som man ønsker presentert for den enkelte profilen. I tillegg så har man et rollefelt og en innledende profiltekst som sammen skaper det førsteintrykket man ønsker av personen for den gitte profilen.|
|  | I kompetansemodulen har man følgende domeneobjekter |
\\
- **Kompetansematrise**. Består av en samling av kompetanseområder som er forespurt for en oppgave/rolle internt eller i et kundetilbud.
- **Rating**. Består av kompetanse beskrivelse, scoring og referanser til erfaringselementer som synliggjør riktig scoring på kompetanseområdet.
\\
NB!  Kompetansematriseområdet er i en tidlig alfa-fase, og det forventes endel endringer og justeringer på dette området fortsatt.|

### Datamodell

![https://wiki.cantara.no/download/attachments/33293770/CVAPP+DB+model.png](https://wiki.cantara.no/download/attachments/33293770/CVAPP+DB+model.png)(https://wiki.cantara.no/download/attachments/33293770/CVAPP+DB+model.png)

### Altran spesifics (fra Wenche)

Bruk din altran CV som mal og legg inn informasjonen i databasen.
(et tips er å klippe lime via notepad eller den drag/drop funksjonen som er på siden.)
 
NB!! Ikke legg inn noe informasjon på delen Workplace. Alt skal inn som Experiences som prosjekt.
 
### Slik gjør du det:

- Gå inn her i ACS
- Fyll inn personopplysninger og last opp bilde

---

Bruk din eksisterende cv som mal – alt der skal med ..

- Alle nøkkelkvalifikasjoner legges inn under teknologi
 
Dersom du ønsker å se hvordan dette ser ut i Word må du opprette en CV.

- Edit CV
- Legg inn profil = selgende hovedtekst
- Velg hvilke elementer du vil ha med i CV-en  (technology, experience++)
- Velg lagre

- View CV, download .doc

**Voila!**

---
