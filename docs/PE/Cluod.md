# Cluod

## Clouds

Følger behov for å kategorisere clouds.

1) Infrastructure clouds (EC2, ...)
2) Platform clouds (MS; S3, ... )

Forskjellige muligheter for deployment:

1) _THE_ cloud  (Altså - cloudene som finnes rundt om kring)
2) Private enterprise clouds. (Cloud OS på "private maskiner")

Grunnen til at vi har tro på at private enterprise clouds er paranoia. Folk tør (foreløpig) ikke å distribuere data og prossessering.

Vi har tror på at Clouds får stor utbredning i norge fordi det er et duopol på driftssiden. Tro på at det kommer driftsleverandører som tilbyr drifting på _THE_ cloud.

Noe diskusjon rundt om cloud computing påvirker programeringsmodellene dine:
- Ja, Må leggge på guards mot f.eks ddos angrep.
- Unlimilited scale == Unlimited cost. (Du kan ikke skalere til himmels) Distribusjon er
- Enklere billigere raksere å få opp _mange_ maskiner. Dette bør føre til at man distribuerer mer.
- Uforutsigbar latency.

Gode erfaringher med EC2 i real live løsninger.

EC2 - instansene er flyktige - Dataene er ikke persistert på disk. Typisk kan du mounte/remote til platform for persistering.

Distribuert persistent: Finnes i minne på 3 noder, på 2 forskjellige geografiske noder.

Når er det man skal vurdere cloudning?

_THE_ cloud: Hvis kunden har en outsourcingstrategi på drift, har en applikasjon som endres, og ikke har spesialkompetanse på applikasjonsdrift hos driftsleverandøren:  Ingen grunn til å ikke deploye på _THE_ cloud
- Kjappere T2M
- Kjappere respons
- Billigere
- \+\+

Enterprise private clouds: Vi tror dette kommer til å komme, men det ligger nok litt frem i tid, da de to store neppe tilbyr noe slikt. Hvis du har:
- Interndrift
- Sensitive data
- Rigide sikkerhetsregimer
Kan begynne å se på cloud OS.... Neppe modent nok, men greit å se på.

Arkitekturkrav:
Robust arkitektur som kan skaleres horisontalt og vertikalt.
"Databaseintegrasjon er ikke en god idee for clouding - hehehe .."
Det skal være veldig lett å legge til en ny server instans.

Hvorfor bruker vi ikke tjenester som finnes i _the_ cloud nå? De finnes og er ready for prime time.

Pass på vendorlockin\![\](\)
- De kan gå konk.
- De kan endre oppsett på maskinene
- Du kan ikke gå bort fra en leverandør enkelt.

Gir ikke mulighet til redundans utover en leverandør.

Se forøvrig [blogpost](https://projects.knowit.no/display/FAGF/Cloud+Blog).

Merk at dersom du har "Siloer" med mye statisk konfigurasjon - Clouding hjelper deg neppe.

Kommersielle lisenser på cloud er vanskelig. "Support på drools i en EC2 instans" .... hehehe...
MS har jo løst dette med å levere hele greia på Azure. Cloud er veldig open source orientert.

Diskusjon omkring hvorvidt vi vil ha ting på disk eller om minne holder (i en periode i alle fall)
Eksempel: Hvordan klare 10 000 transer / sec - Eneste mulig løsning er å asynkront putte på disk.

Man bør ha en switch for å kunne persistere på disk. For utvikling. Slitsomt å ha så mange maskiner oppe samtidig. Må selvfølgelig testes i distribuerte omgivelser.
