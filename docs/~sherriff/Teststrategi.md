# Teststrategi

#### Teststrategi

NG Flyt har valgt teststrategien [JigZaw](https://wiki.cantara.no/display/dev/JigZaw)istedet for den mer fossefallsorienterte [V<sub>~modellen](http://en.wikipedia.org/wiki/V</sub>~Model_(software_development)). Grunnprinsippene i JigZaw er:

- Verify expected behavior versus finding bugs
- Maximize the value of the testing efforts

- Divide and conquer
- Test Categorization

- Timeline
- Control state

Både Beholdningsmodulen og Asko Netthandel er databasesentriske applikasjoner. Vedlikehold av testdata og "enkelt å komme igang" med nye tester er prioriterte drivere.

Hver testmetode er ansvarlig for å sørge for at tilstanden til databasen (eller JMS eller whatNot) er som den testen forventer.

Konkrete oppskrifter som passer til ulike typer tester:

- [Test strategy for Oracle PL_SQL](https://wiki.cantara.no/display/dev/Test+strategy+for+Oracle+PL_SQL) og funksjonalitet hvor databasen må være med.
    - Oversikt over jobber som er testet med denne strategien: [BM<sub>~jobber](BM</sub><sub>jobber.md) og [AN</sub><sub>Jobber](AN</sub>~jobber.md)

- [JMS testing](https://wiki.cantara.no/display/dev/JMS+Testing+according+to+JigZaw)+ [How to start ActiveMQ JMS Broker in a separate process](https://wiki.cantara.no/display/dev/How+to+start+ActiveMQ+JMS+Broker+in+a+separate+process)
    - Tanken er å bruke dette oppsettet til å teste BongMottaket.

- Ytelsestest av via Web GUI basert på WebDriver/Selenium2. (Joachim)
    - **TODO**: Foreslår at Line beskriver dette når AN-1195 er ferdig.
    - Kildekode: [http://utvikling.norgesgruppen.no/svn/engrosrep/an<sub>~ytelsestest](http://utvikling.norgesgruppen.no/svn/engrosrep/an</sub>~ytelsestest)

#### Test database
Oracle enterprise edition basen benyttes for å kjøre integrasjonstestene. Oracle XE 11g støtter ikke bitmap indexes heller ikke partisjonering av tabeller. Disse manglene gjør XE uegnet som testbase.

#### Hvordan vi bruker TestNG groups

TestNG har konseptet [test groups](http://testng.org/doc/documentation<sub>~main.html#test</sub><sub>groups), som lar oss gruppere tester. Dette konseptet brukes primært for å avgjøre hvorvidt en gitt test skal kjøres som en del av **standardbygg (mvn install)** eller som en del av **utvidet bygg (mvn install \</sub><sub>P test</sub>~env**).

I hver Maven<sub>~modul ligger det to testng</sub><sub>konfigurasjonsfiler: testng.xml og testng</sub><sub>env.xml. testng.xml brukes i standardbygget, mens vi bytter konfigurasjon til testng</sub><sub>env.xml ved å aktivere profilen test</sub><sub>env. Forskjellen på disse to konfigurasjonsfilene er at testng.xml ekskluderer tester som vi av diverse årsaker ikke ønsker skal inngå i standardbygget. Trege tester og tester som avhenger av spesielt oppsett (f.eks. database eller en ekstern tjeneste) er derfor tester som kun kjøres når man aktiverer profilen test</sub>~env.

CI<sub>~server, Bamboo, kjører alltid med test</sub>~env-profilen aktivert.

###### Testgrupper og hva de brukes til

| Gruppe | Forklaring |
| --- | --- |
| disabled | test som midlertidig ikke skal kjøres. Valgt å bruke en gruppe istedet for enabled = false fordi disabled gir en fin oversikt over hvilke tester som er inaktive i TestNGs rapporter. |
| slow | Test som ikke har noen spesielle avhengigheter men som vi likevel ikke ønsker som en del av standardbygget fordi den tar lang tid. Ytelsestester og tester som krever mye oppsett er typiske eksempler. |
| database-an | Test avhenger av askonetthandel sin database. |
| database-bm | Test avhenger av Beholdningsmodulen sin database. |
| ws-bm | Test som krever at Beholdningsmodulen Webservice er tilgjengelig. |
| ws-an | Test som krever at Askonetthandle Webservice er tilgjengelig. |
| ws-brs | Test som krever at ButikkRegisterService er tilgjengelig. |
| filtjener | Test som krever at [filtjener | Apache filtjener] er tilgjengelig. |
| dependsOnLocalBMServer | Test som krever at det kjører en BM<sub>~WS</sub>~server lokalt. Se BehkorrDaoCXFImplIntegrationTest.java. |
| bongmottak-jms | Avhenger av JMS-server (mq://ngbongcapst1.joh.no). |
|  | Tester som ikke har noen spesielle avhengigheter/egenskaper trenger ikke noen gruppe. Alle uten eksplisitt gruppe inngår som en del av standardbygget. |

Vi kunne ha begrenset oss til kun én gruppe for å gjøre skillet mellom standardbygg og utvidet bygg, men ofte dukker det opp behov for å kunne lage noen særoppsett for mer avanserte testformål. Eksempelvis kjøring av tunge ytelsestester en gang per natt og ikke som en del av utvidet bygg som kjøres av Bamboo for hver commit. Hvis man har etablert dette konseptet fra starten av så kan man ta i bruk denne typen tester uten å måtte bruke så altfor mye tid på "plumbing".

#### Verktøyvalg for utviklertester

- [TestNG](http://testng.org)
- [Spring TestContext Framework](http://static.springsource.org/spring/docs/2.5.x/reference/testing.html#testcontext-framework)og spesielt [AbstractTestNGSpringContextTests](http://static.springsource.org/spring/docs/2.5.x/api/org/springframework/test/context/testng/AbstractTestNGSpringContextTests.html)
- [unitils](http://www.unitils.org)
- [dbmaintain](http://www.dbmaintain.org)

- [Mockito](http://mockito.org/)

- Maven 2 og 3
- Bamboo Continuous Integration (CI) server

###### Begrunnelse for valg av verktøy

- Vi har flere typer tester som av ulike grunner ikke er ønsket som en del av standardbygget. For eksempel ønsker vi at veldig trege tester primært skal kjøres av CI<sub>~server og at utvikler eksplisitt kan velge å inkludere disse testene. Et annet eksempel er integrasjonstester hvor vi kun har denne integrasjonen i et bestemt testmiljø. For å løse disse utfordringene bruker vi _groups_\</sub>~konseptet i TestNG for å kunne velge hvilke tester som skal kjøres av hhv. utviklere og CI-server og når de skal kjøres.

- Spring TestContext Framework forenkler oppsett av tester siden vi da kan gjenbruke det vanlige _dependency injection_\-oppsettet som brukes i produksjon.

- Unitils tilbyr funksjonalitet for å sette inn testdata i en database fra en xml<sub>~fil. Dette er det samme konseptet som db</sub><sub>unit eller Testaco tilbyr, men Unitils støtter TestNG og integrerer godt med dbmaintainm, noe de to andre alternativene ikke gjør. Vi har deployet en egen versjon av unitils 4.0</sub><sub>SNAPSHOT fra revision 1355 til [Archiva](http://utvikling.norgesgruppen.no/archiva/browse/org.unitils/unitils/4.0</sub>~ngd-r1355) siden 4.0 ikke har blitt releaset enda og v3.x ikke dekker vårt behov.

- dbmaintain automatiserer oppsett av en tom database for hver test. Les mer om konseptet med å kontrollere tilstand: [Control+state](https://wiki.cantara.no/display/dev/Control+state). Kort fortalt så starter hver test med et tomt database schema, legger inn databasestrukturen (tabeller, constraints, osv.), alle endringsscript og PL_SQL-kode. Deretter legger untils inn datasettet som den aktuelle testen har spesifisert.

- Vi ønsker å mocke minst mulig, men når mocking er nødvendig, så foretrekkes Mockito over EasyMock og JMock fordi det er et nyere rammeverk hvor en del av ulempene som finnes i de to andre er rettet. (Mockito startet som et påbygg til EasyMock.)

- Maven som byggesystem og Bamboo som continuous integration server var allerede bestemt da strategien ble utarbeidet. Maven er en forutsetning for oppsettet, mens enhver moderne (Hudson/Jenkins, Bamboo eller Continuum) CI-server kan brukes.

#### Verktøyvalg for funksjonelle tester som skal brukes til kommunikasjon med ikke-teknikere

NGD har valgt FitNesse som preferert verktøy for funksjonelle tester der kommunikasjon med ikke-teknisk personell er sentralt. Hittil har vi hatt mest utbytte av utviklernære tester for å verifisere at koden er korrekt, så foreløpig så har vi ingen tester basert på FitNesse.

Det har vært utført forsøk på å skrive tester med GreenPepper. Erfaringen med dette arbeidet var at bl.a. at det krevde mye støtte fra drift for å holde infrastrukturen oppe, at testene var vanskelige å debugge når noe ikke virket og at utviklerne følte det som en omvei å bruke en wiki når ikke kommunikasjon med ikke-teknikere ikke var sentralt. Det var også utfordringer knyttet til versjonskontroll av disse testenen.
