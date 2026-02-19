# Error management

Se også [Feilhåndtering BM](Feilhåndtering-BM.md).

**Diagram: exceptions**

## Oversikt over exceptions i Asko netthandel (AN og NG Flyt)

| Exception | Beskrivelse | Varsle utviklere og drift | Tilbakemelding til bruker | Eksempler | Kommentar |
| --- | --- | --- | --- | --- | --- |
| ANLoggableException | ANLoggableException skal arves av alle exceptions i exception-hierarkiet i AN/NGF. \\ |
 Den sørger for at hver exception får sin egen unike id, en default getMarker-metode og en default feiltype-streng. | | | | abstract \\ |
| ANApplicationException | ANApplicationException brukes til styring av programflyt vha. exceptions og bryter med best practice for exceptionhåndtering. \\ |
Denne skal KUN brukes når vi anser det som for tidkrevende å sikre for denne typen feil i GUI vha. av validatorer og design. Vurdèr alternative løsninger nøye før denne benyttes. | Logges IKKE. | Bruker må varsles om hva som gikk galt og hva vedkommende kan gjøre for å komme rundt problemet. \\ | Valideringsfeil, ulovlige ordrestatuser, manglende betingelser osv. | |
| ANRuntimeException | En generisk RunTimeException for AN og NGF. \\ |
Skal kun brukes hvis ingen av de andre exceptiontypene passer, og vi vil håndtere dette dette som en generisk feil på "toppnivå". | Logges på ERROR | Bruker blir ført til generisk feilside | Feil som må rettes av utvikler og verken skyldes dårlig datakvalitet eller integrasjonsproblemer. | |
| ANDataException | feil eller inkonsistens i data.&nbsp; | Logges normalt på WARN, men særs alvorlige datafeil kan logges på error. \\ |
Rette vedkommende (dataeier) bør varsles om at data må utbedres. I dag varsles 96andata@norgesgruppen.no om datafeil i jobber. | Bruker kan \(?) varsles om at feilen skyldes problemer med data. | LastKampanjeRabattFraImi&nbsp; - Ignorerer rad: epd-nummer 3051000 finnes ikke. | |
| ANIntegrationException | Problemer med tilkobling eller bruk av en ekstern tjeneste. \\ |
 Bruk helst subklasser. | Logges på ERROR. \\
Ansvarlige for ekstern tjeneste og ansvarlig for teknisk infrastruktur må varsles. | Bruker må varsles om at tjenesteX er utilgjengelig  p.t. men prøv gjerne igjen senere. | | Bør bli abstract. |
| TjenesteUtilgjengeligException | Klarer ikke koble til en ekstern tjeneste (en gjenopptagbar feil, ref  Utviklingsrammeverket). \\ |
Naturlig scenario for retry av kobling mot en ekstern tjeneste (webservice, bildeserver,  eller at BO er nede). \\ | Logges på ERROR. \\
Ansvarlige for ekstern tjeneste og ansvarlig for teknisk infrastruktur må varsles. | Bruker må varsles om at tjenesteX er utilgjengelig  p.t. men prøv gjerne igjen senere. | | abstract |
| FeilIEksternTjenesteException | Feil i tjenesten som applikasjonen  forsøker å kalle. | Logges på ERROR. \\ |
Ansvarlige for ekstern tjeneste må varsles. \\ | Bruker må varsles om at tjenesteX er utilgjengelig  p.t. men prøv gjerne igjen senere. | | Bør bli abstract. |
| [DataAccessException | http://static.springsource.org/spring/docs/3.0.x/spring-framework-reference/htmlsingle/spring-framework-reference.html#dao] | Skal brukes til å wrappe HibernateException og SQLException. | Logges på ERROR som default |  |  |  |

## Hvordan implementere feilhåndtering ved kall mot database

Vi bruker Springs [DataAccessException](http://static.springsource.org/spring/docs/3.0.x/spring-framework-reference/htmlsingle/spring-framework-reference.html#dao)\-hierarki for feilhåndtering av kall mot databasen.
Ved å integrere med DataAccessException-hierarkiet til Spring så får man enhetlig exceptions fra database-logikk slik at applikasjonen kan forholde seg til disse på en ryddig måte. Det er lagt ned en del arbeid i DataAccessException-hierarkiet, så vi sparer oss en del jobb ved å gjenbruke dette i stedet for å skrive disse tingene selv.

Det finnes to måter å sette opp dette på for hhv. SQL-spørringer og Hibernate-kall:

1. Med templates: hver Dao extends [HibernateTemplate](http://static.springsource.org/spring/docs/3.0.x/javadoc-api/org/springframework/orm/hibernate3/HibernateTemplate.html) eller [JDBCTemplate](http://static.springsource.org/spring/docs/3.0.x/javadoc-api/org/springframework/jdbc/core/JdbcTemplate.html)
1. Template-less: getCurrentSession().createQuery eller createSQLQuery og må annoteres med [@Repository](http://static.springsource.org/spring/docs/3.0.x/javadoc-api/org/springframework/stereotype/Repository.html)

Stored Procedures kalles typisk med [jdbcTemplate.call](http://static.springsource.org/spring/docs/3.0.x/javadoc-api/org/springframework/jdbc/core/JdbcTemplate.html#call%28org.springframework.jdbc.core.CallableStatementCreator,%20java.util.List%29) eller createSQL på samme måte som annen ren SQL.

Designretningslinjer for om man skal bruke templates eller ikke er foreløpig ikke avklart (se [ANARK-97@JIRA](ANARK-97-JIRA.md)).
Mtp. feilhåndtering så spiller det ingen rolle så lenge man ikke bruker sql direkte. Se [Eksempler på feilhåndtering ved databasekall](Eksempler-på-feilhåndtering-ved-databasekall.md) for flere detaljer.

## Hvordan implementere feilhåndtering ved kall mot Webservice

Når vi kaller en ekstern webservice forholder vi oss til to klasser av feil: _FeilIEksternTjenesteException_ og _TjenesteUtilgjengeligException_. Denne oppdelingen er valgt fordi det er forskjell på hvem som skal gjøre noe for å rette opp feilen. Hvis vi får en exception fra ekstern tjeneste, så vet vi at den i hvert fall er oppe. Alle andre feil anses fra kallende applikasjon som at tjenesten er utilgjengelig.

#### Eksempel

```java
public ButikkBeholdning hentBeholdning(Long gln) {
	HentBeholdningElementType behElemType = new HentBeholdningElementType();
	behElemType.setGln(gln);
	HentBeholdningElementListType behListType = new HentBeholdningElementListType();
	behListType.getHentBeholdningElement().add(behElemType);
	HentBeholdningRequestType reqType = new HentBeholdningRequestType();
	reqType.setHentBeholdningElementList(behListType);

	HentBeholdningResponseType response;
	try {
		response = getCurrentStub().hentBeholdning(reqType);
	} catch (BMForExportRuntimeException e) {
		String feilmelding = "Kunne ikke hente beholdning for gln: " + gln + ".";
		throw new FeilIBehkorrServiceException(feilmelding, e);
	} catch (Exception e2) {
		throw new BehkorrServiceUtilgjengeligException("gln: " + gln, e2);
	}
	return BeholdningConverter.lagButikkBeholdning(response);
}
```

## Noen andre kommentarer

#### Om stacktrace i loggen

- Stacktrace skal **alltid logges** når applikasjonen ikke har tilstrekkelig informasjon om problemet til å avgjøre hva som må gjøres.

- Stacktrace skal **IKKE logges** når den ikke gir noen ny informasjon. F.eks. en ConnectionRefusedException trenger vi ikke stacktrace, for der den oppstår så vet vi både hvilken klasse som prøver å opprette en Connection og hvordan.

I praksis så betyr dette at alle feilmeldinger som inneholder stacktrace er meldinger rettet mot **utviklere**. For å kunne forvente at drift skal ta tak i en feilmelding uten å involvere en utvikler, så må mao. feilmeldingen være så god at drifter kan forstå den uten å måtte tolke en stacktrace.

#### Hva bør en loggmelding inneholde?

- Alle loggmeldinger som logges på WARN og oppover skal inneholde følgende informasjon:
    - tidsstempel
    - Hvor oppsto (eller detekterte vi feilen)
    - hva er galt (hvis vi vet)
    - hvem (drift, utviklere, ansvarlige for data) (hvis vi vet)
    - hvordan rette feilen (hvis vi vet)
    - Opplyse om evt. tiltak som applikasjonen gjør for å fikse feilen. (F.eks. retries)
    - Informasjon om hvilken kunde, transaksjon dette gjelder slik at det blir enklere å debugge feilen i etterkant.

- Skille på hva som logges og hva som vises til bruker. [Feilmeldinger](http://utvikling.norgesgruppen.no/confluence/pages/viewpage.action?pageId=14876915#Feilh%C3%A5ndtering-Feilmeldinger) som omtales i Utviklingsrammeverket ser f.eks. ut til å være en måte å holde orden på hvilke feilmeldinger vi viser til brukere. Dette er en GOD IDE. Dette er ikke det samme som feilmeldinger vi ønsker å logge. Mottagere av loggen er jo utvikling og drift og disse er interessert i mest mulig informasjon om problemet for å fikse feilen. Utviklingsrammeverket inneholder også rettningslinjer for logging. Disse bør vi ta i betraktning når vi nå er i planleggingsfasen.
- Feilen skal kaste AN-spesifikke exceptions der de oppstår (f.eks. datafeil skal kastes helt fra DAO-en) osv - håndtering av feil skjer så snart man har mulighet til å håndtere feilen. Dersom beskjed skal vises i GUI må exception propageres helt opp til MBean-laget.

#### Implementasjon av retningslinjer

- Nye ASKO Netthandel benytter seg av Unchecked exceptions - som så kan fanges der man enten skal
    - Vise tilbakemelding til brukeren
    - Håndtere feilen på annet vis

- Dersom feilen ikke blir håndtert, sendes de videre til 'siste instans' (ANErrorHandler) som videresender til en feilside som viser informasjon om feilen, inkludert stacktrace.

## Ressurser

- Utviklingsrammeverket - feilhåndtering
    - [Feilhåndtering rettningslinjer](http://utvikling.norgesgruppen.no/confluence/pages/viewpage.action?pageId=14876919)
    - [Feilhåndtering bruksanvisning](http://utvikling.norgesgruppen.no/confluence/pages/viewpage.action?pageId=14876915)
- Utviklingsrammeverket - logging
    - [Rettningslinjer for logging](http://utvikling.norgesgruppen.no/confluence/display/UTVRV/Retningslinjer+for+logging)
    - [Bruksanvisning for logging](http://utvikling.norgesgruppen.no/confluence/display/UTVRV/Logging+for+utviklere)

- [Catch oriented exception strategy](https://wiki.cantara.no/display/dev/Catch+oriented+exception+strategy)
- [Rules for Developing Robust Programs with Java Exceptions](https://wiki.cantara.no/display/dev/Error+Handling+And+Exception+Management#ErrorHandlingAndExceptionManagement-RulesforDevelopingRobustProgramswithJavaExceptions)
