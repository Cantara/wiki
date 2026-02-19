# Logging

#### Intro

LoggeAPI: [Simple Logging Facade for Java (SLF4J)](http://www.slf4j.org/)
Loggeimplementasjon: [Logback](http://logback.qos.ch/)

Dette gir oss følgende muligheter:

- Loggfiler skilt på enhver form for runtimeparametre, f.eks. bruker-ID
- En loggfil per type feil, f.eks. en for RuntimeExceptions og en annen for SystemExceptions
- Flere og bedre muligheter for triggere, f.eks. automatisk sending av mail av loggfiler basert på gitte parametre
- Flere og bedre muligheter for lagring av logg til f.eks. JMS-kø, database osv.
- Konfigurasjonsfiler med if/then/else for én configfil for forskjellige miljøer
- Flere og bedre muligheter for å rullere/komprimere gamle loggfiler basert på kriterier som dato, størrelse osv.
- GUI for loggfiler 'out<sub>~of</sub>~the-box' med Lilith

#### Konfigurasjonsfiler

| Bruksområde | Konfigurasjon | Kommentar |
| --- | --- | --- |
| Produksjon | \-Dlogback.configurationFile=./logback.xml i run.sh/jobber.sh | på roten av hver modul. \\ |
\* Logback-konfigurasjon for produksjon
    - Web [http://ngsvn1.joh.no/svn/engrosrep/asko<sub>~netthandel/trunk/web/logback.xml](http://ngsvn1.joh.no/svn/engrosrep/asko</sub>~netthandel/trunk/web/logback.xml)
    - Pocket [http://ngsvn1.joh.no/svn/engrosrep/asko<sub>~netthandel/trunk/pocket/logback.xml](http://ngsvn1.joh.no/svn/engrosrep/asko</sub>~netthandel/trunk/pocket/logback.xml)
    - Jobber [http://ngsvn1.joh.no/svn/engrosrep/asko<sub>~netthandel/trunk/jobber/logback.xml](http://ngsvn1.joh.no/svn/engrosrep/asko</sub>~netthandel/trunk/jobber/logback.xml)
    - Rapportserver [http://ngsvn1.joh.no/svn/engrosrep/asko<sub>~netthandel/trunk/web/logback.xml](http://ngsvn1.joh.no/svn/engrosrep/asko</sub>~netthandel/trunk/web/logback.xml)
    - WS<sub>~server [http://ngsvn1.joh.no/svn/engrosrep/asko</sub>~netthandel/trunk/web/logback.xml](http://ngsvn1.joh.no/svn/engrosrep/asko-netthandel/trunk/web/logback.xml) |
| Testmiljøer | \-Dlogback.configurationFile=./logback.xml i run.sh/jobber.sh | src/test/resources/logback-test.xml for hver deploymentenhet |
| Tester | src/test/resources/logback-test.xml i alle moduler |  |
| mvn jetty:run | $\/src/test/resources/logback-test.xml, konfigurert i pom.xml i web og pocket |  |

Dette oppsettet ble implementert i AN 8.1.

#### Implementerte konsepter

| Konsept | Beskrivelse | Loggfil | Epost | Kommentar |
| --- | --- | --- | --- | --- |
| Datakvalitet | Feil forårsaket av dårlig datakvalitet. Dette kan ikke fikses av utviklerne. | an-dataerror.log | 96andata@norgesgruppen.no |  |
| Integrasjon | Feil i en ekstern tjeneste eller problemer med å få kontakt med en ekstern tjeneste. | an-integrationerror.log | 96_NGFlyt@joh.no, 96_AN-Utv@joh.no | Dette kan i utgangspunktet ikke fikses av utviklerne, men vi utfører p.t. drift, så sendes til utviklerne inntil videre. Sender p.t. kun ut epost fra jobber, men planen er å sette opp dette for pocket og web også. |
| Generell feillogg | Alle feil som ikke er data eller integrasjon. | askonetthandel.log | 96_NGFlyt@joh.no, 96_AN-Utv@joh.no | Skal fikses av utviklerne. Sender p.t. kun ut epost fra jobber, men planen er å sette opp dette for pocket og web også. |
| Standard out | All output som sendes til std.out. I utgangspunktet kun wily som skal logge til denne. | server.log | nei |  |
| Brukerlog | Navigasjonslogg per bruker | userlog/user-username.log | nei |  |

#### Hvordan logge?

{**}HUSK\! Dersom du velger å håndtere og logge exceptions selv i stedet for å overlate dette til ANErrorHandler, må du hente ut{**}&nbsp;{**}riktig{**}&nbsp;{*}logg og logge til denne\!

**De tilgjengelige loggene er:**

```
private static final org.slf4j.Logger userLog = org.slf4j.LoggerFactory.getLogger("UserLog");
private static final org.slf4j.Logger log= org.slf4j.LoggerFactory.getLogger(<Klassenavn>);
```

###### Logge exception ved problemer med datakvalitet

Vi har satt opp egne appenders for datakvalitet og integrasjonsfeil. For at disse skal slå inn så må man legge på en [MARKER](http://logback.qos.ch/manual/appenders.html#marker_GEventEvaluator) slik at loggmeldingen havner i riktig logg. Hver exception har en 'marker' som er lik navnet på exceptionen. Basert på disser markerne logges feilene til hver sin fil, slik at filen skal kunne leses av/sendes til riktig vedkommende ved innslag. Eksempel:

```
ANDataException exception = new ANDataException(FeilMelding.FEIL_DATALAG_VARE_MANGLER_PRIS, vare.getDpakNummer());
log.warn(exception.getMarker(), exception.getMessage());
```

Hver type feil har en egen feilside i GUI. Type feil sier her noe om hvilken loggfil man skal se i.

Konfigurasjon av en logg skjer på denne måten i logback.xml

```
<appender name="ANDATAERRORFILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
	<file>${LOG_DIR}/log/an-dataerror.log</file>

	<Filter class="ch.qos.logback.core.filter.EvaluatorFilter">
		<evaluator class="ch.qos.logback.classic.boolex.JaninoEventEvaluator">
			<expression>marker != null &amp;&amp;
				marker.getName().equals("no.norgesgruppen.an.felles.exception.ANDataException")
			</expression>
		</evaluator>
		<OnMismatch>DENY</OnMismatch>
		<OnMatch>ACCEPT</OnMatch>
	</Filter>

	<RollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
		<FileNamePattern>${LOG_DIR}/log/old/an-dataerror.%d.log.gz</FileNamePattern>
		<maxHistory>30</maxHistory>
	</RollingPolicy>

	<encoder>
		<Pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</Pattern>
	</encoder>
</appender>
```

Her sjekkes det at exceptionen har en marker med navnet ANDataException\- har den det, blir feilen logget av denne appenderen.

For å logge til denne loggen, hentes den ut på vanlig måte (dette skjer i ANErrorHandler, så et unikt feilnummer blir lagt til for oppfølging iht bruker som har opplevd feilen)

```
private static final Logger log = LoggerFactory.getLogger(<klassenavn>);
logger.error(((ANApplicationException) anException).getMarker(), "\nUnikt feilnummer: " + feilId.toString(), anException.getMessage(), anException);
```
Her legges den originale exceptionen med og man får med stacktrace. Dersom du ikke legger med exception får du ikke stacktrace i loggen, noe som noen ganger kan være ønskelig.

###### Brukerlogg

Brukerlogg settes opp med en SiftingAppender på denne måten i logback.xml:

```
<appender name="SIFT">
        <discriminator>
            <key>userid</key>
            <defaultValue>UKJENT</defaultValue>
        </discriminator>
        <sift>
            <appender name="FILE-${userid}">
                <file>log/user-${userid}.log</file>
                <append>true</append>
                <layout>
                    <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
                </layout>
            </appender>
        </sift>
</appender>

<logger name="UserLog" additivity="false" level="DEBUG">
        <appender-ref ref="SIFT"/>
</logger>
```

Denne benytter parameteren userid - som settes i koden på denne måten:

```
MDC.put("userid", bruker.getBrukerSignatur()); // Dette brukes i SiftingAppender for å skille logger på brukerid om ønskelig.
{code}For å hente ut og logge til denne loggeren gjør man følgende:

```
private static final org.slf4j.Logger userLog = org.slf4j.LoggerFactory.getLogger("UserLog");
userLog.info("Bruker navigerer til " + request.toString());
```

h4. Gjennomgang av loggen

Loggleser-oppgaven går på rundgang blant utviklerne. Målet er å sikre at vi fanger opp feilene fra loggingen og at vi logger riktig. Oppgaven går ut på å lese feilloggene i produksjon, og dersom det er testuke, skal man også lese loggene fra systemtest.

Loggkatalogene ligger under rotkatalogen til web-serveren.

./log/an-dataerror.log - Datafeil-logg - feil mot database, manglende pris på vare osv. Bør rettes i grunndata
./log/an-integrationerror.log - Integrasjonsfeil - stort sett feil i pålogging til BO havner her
./log/an-runtimeerror.log - Feil i programmering i Nye AN - feil her er kodefeil som må rettes
./log/an-systemerror.log - Stort sett fatale feil havner her - bør helst være tom\!
./log/an-applicationerror.log - Noe uventet har skjedd, vi har tatt høyde for feilen i applikasjonen, men det er sannsynligvis kodefeil eller manglende validering et sted.
{color:#000000}./userlog/\* - Her ligger logg per bruker - dersom en gitt bruker rapporterer om feil kan vi sjekke brukerens logg her{color}
{color:#000000}./log/server_2.log - Logging fra Jetty og annet{color}
{color:#000000}./log/askonetthandel.log - generell logging - loggstatements som ikke er Nye AN-logg - men er NG Flyt logger eller gammel AN-logging.{color}\\

h6. {color:#000000}Nyttige kommandoer (fyll ut etterhvert){color}

* grep "mangler pris" anserver/log/an-dataerror.log \| cut \-d ' ' \-f 10 \| sort \| uniq > varerSomManglerpris-2011-04-27.txt

* grep "negativ enhetspris" anserver/log/an-dataerror.log \| cut \-d ' ' \-f 10\- \| sort \| uniq > varerMedNegativEnhetspris-2011-04-27.txt

* For å sjekke om det har kommet noen ERROR i jobber for en bestemt dag
** oracle@ngoas9bt:~> grep ERROR an-jobber-releaseTest/logger/*_20110812.log

* For å sjekke om det har kommet noen ERROR i jobber for en bestemt dag, men fjerne debug-logging fra logback
** oracle@ngoas9bt:~> grep ERROR an-jobber-releaseTest/logger/*_20110812.log \| grep \-v logback

* For å slette tmp-filer i userlog-katalogen hvis man får feilmeldingen "/bin/rm: Argument list too long."
** {code}
cd /u01/jetty/anserver/userlog
find . -name 'user-*.tmp' -print0 | xargs -0 rm
```
