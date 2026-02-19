# Guide til hvordan velge teststrategi

Unit testing is a popular and well-proven testing technique, but what about _the rest_? What's your strategy for verifying a software application or system when traditional test tools and testing methodology is not good enough? 

In this talk you will NOT learn about yetAnotherCoolerThanTheRestTestingTool. Instead the focus is on how to analyze a concrete problem and choose a strategy and tool set appropriate for the task at hand. 

This talk is aimed at architects and developers, but testers and project managers will probably also benefit from learning a new viewpoint. 

---

#### Hva 

Guide til hvordan velge teststrategi som passer i **din** kontekst. 
Vise tankegangen og vektlegging av prioriteringer gjennom et konkret eksempel. 

#### Why should I care? 

Mange "defaulter"

Få kjenner de ulike mulighetene godt nok til å ta veloverveide valg. 

Det har kommet nye verktøy som gjør implementasjon enklere. Testaco, Unitils 4. 

#### Problem 

| Feil oppdages for sent 

Utfordringer: 

- Mange deler samme database - går i beina på hverandre 
- Restore default state er tidkrevende
- Testdata er "moving target" siden ulike bruker og systemer ikke nødvendigvis har samme oppfatning av hva som er korrekt og mange legger inn data. 
- Tjeneste/funksjon for kompleks til at man klarer å spesifisere forventet output gitt bestemte input. 

- Man har forsøkt før og feilet. 
    - Rollback-strategi (typisk basert på Spring) 
    - Verktøytilnærming, f.eks. GreenPepper eller fra HP, Rational, etc. 

#### 1 

Vedlikehold, kontroll, innlegging av testdata 
(Ut)valg

Unitils, dbUnit, export fra db, generere 

#### 2 

Integrasjon med Oracle db 
deling av database schema 

dbmaintain vs manuelt 
Inspirasjon/målbilde - refactoring databases av Scott Ambler 

#### 3 

- Enkelt å ta i bruk 
    - Spring for wiring og gjenbruk av reell applicationContext 
    - db installert sentralt, men egne schema 

- Forbli enkelt over tid -> mao. tilnærmingen må skalere 
    - Et schema per multi-module, så per modul, per test, per testmetode 

TestNG groups 

#### Kontekst / behov 

Regresjonstest

Datasentriske - "det er data som er vanskelig" 

PL/SQL og Java 

Kontroll på db-struktur, håndtere at db endrer seg. 

###### Generelt 

Minimal terskel for å legge til en ny test, billige å skrive 

Enkelt å vedlikehold av testene

Glidende overgang mellom enhetstest og regresjonstest. 

#### Sammenligne denne strategien med andre strategier 

- Rollback 
    - Støtter ikke RequiresNew (hibernate annotation) 
    - + enkel å sette opp og bruke 

- GreenPepper, FitNesse 
    - Mye infrastruktur og oppsett. Trenger bistand/hjelp fra drift ved problemer. Generell usikkerhet rundt hva som er galt når en test ikke kjører. 
    - God på kommunikasjon med ikke-teknikere, men det er ikke hovedutfordringen. 
    - Wiki er en "omvei" for en utvikler. Ren overhead sammenlignet med mer utviklernære tester. 

- Record - playback 
    - Kan være tungt å implementere hvis ikke arkitekturen støtter å hente data uten å påvirke produksjon. 
    - Tidkrevende ved store datamengder. 
    - Krever stabile grensesnitt 
    - Krever kontroll på forventet output gitt forventet input
