# Whydah Docker packaging strategy

### Goal

|  | **Explore and produce an out-of-the-box Whydah environment for medium complex and secure HA scenarios on a set of docker engines.** *Even if you think you won't need it, we will provide it out-of-the-box for free* |

**A sample deployment of a Whydah system with several replicas on a set of physical servers (a 11-on-7 / 2-5-2-1-1 config)**

|  |  |
| --- | --- |
| [Full Size](/web/20210731195145/https://wiki.cantara.no/plugins/gliffy/viewlargediagram.action?name=Docker deployment&ceoid=40797296&key=whydah&pageId=40797296)  |  | |

**NOTE** Early focus on the Whydah components. The internal persistence components of UIB at a later stage (HA SQL DB, HA LDAP and HA lucene/solrcloud)

### Coded networks

- SDN1: SSOLoginWebApp Round-robin load-balancer
- SDN2: STS load-balancer (with QoS?)
- SDN3: Shared hazelcast cluster state
- SDN4: UAS QoS priority load balancer (whydah - 3rd party access)

### Suggested toolchain

- helios - cluster management
- socketplane - software defined network / management (Now bought by Docker)
- docker engine(s)
- docker image(s)

Some thoughts on the suggested tools.

helios - seems simple and to the point to configure and run the cluster configuration. A bit overhead with zookeper setup which might be too much. Does not look like it do any useful network management for out purpose

### Docker images

- <https://registry.hub.docker.com/repos/totto/>

### SDN1: SSOLoginWebApp Round-robin load-balancer

### SDN2: STS load-balancer (with QoS?)

### SDN3: Shared hazelcast cluster state

- multicast nett

### SDN4: UAS QoS priority load balancer (whydah - 3rd party access)

---

|  | WORK IN PROGRESS |

### Discussions

TODO: RDBMS, LDAP, LuceneIndex; separate containers, I assume?   
A: Yes.

TODO: Any Apache instances? In Which roles? In same Docker-container or separate  
A: a) proxypass and HA responsibillity => Docker SDN. b) TSL termination/negotiation: TBD

---

**Some extract form a chat log**

> jeg har lyst å samles og drikke øl og hakke igjennom SDN-Whydah med folket en kveld.... anyone?  
> stiglau 10:57 AM  
> Kan la seg gjøre det, så lenge jeg får tid til å sende søknad  
> totto 10:57 AM  
> (har liten lyst å løpe fra dere på Docker og SDN fronten... )  
> ...og dere har ikke tatt ballen ennå... så da må kanskje en samlokalisering med sosialt til..  
> erikd 11:01 AM  
> Sist vi snakket om Docker I Whydah så ønsket dere å bruke Docker til problemer jeg i utgangspunktet ikke prioriterer.  
> Siste jeg testet Docker så ble jeg ikke imponert. Har noen grunnleggende ting jeg må lære før det er aktuelt å vurdere Docker til noe som helst for min del.  
> stiglau 11:02 AM  
> Ser oxo Docker som bedre match for f.ex ACS, men der må jeg sette av tid til å se på der du er kommet til @totto  
> Og for min del vurderer jeg .pkg/.rpm pakker som et bedre utgangspunkt enn hårete Dockerfile. Jeg har jobbet nok med hårete Ansible, men er fortsatt positiv til initativ for SDN diskusjon  
> totto 11:05 AM  
> Docker = zones... pkg/rpm = install på barebone server  
> så docker = mange instanser/fleksibilitet per jern...  
> erikd 11:06 AM  
> Jeg vil gjerne starte med å løse integrasjon med process og pakke-manager. Hvis docker har de tingene man trenger så er det helt klart bedre enn rpm/deb.  
> stiglau 11:06 AM  
> men, ved å ha .rpm/.deb pakking rundt Whydah komponenter kan vi fjerne en del "manuelle" steg rundt installasjon av applikasjonen. Som blir synlig i Dockerfile  
> erikd 11:06 AM  
> Alternativt så lurer jeg på om AMI kanskje er en bedre pakke enn rpm/deb.  
> stiglau 11:07 AM  
> Amazon AMI? Ikke av den oppfatningen!  
> erikd 11:07 AM  
> Spørsmålet er vel hva vi ønsker å eksponere til "brukerne"?  
> Jeg ønsker convention over configuration og mest mulig som virker ut av boksen.  
> totto 11:08 AM  
> Docker+SDN = alt virker ut av boksen selv med rimelig hårete konfgurasjoner (mitt mål)  
> erikd 11:09 AM  
> Vi klarer aldri å vedlikeholde pakker for alle relevante distroer. Jeg tror også det krever noe ekstra av brukerne å faktisk vurdere og sette opp alle de ulike alternativene som Whydah kan brukes til.  
> totto 11:09 AM  
> eller vi standariserer på Dockerimaget :stuck\_out\_tongue:  
> erikd 11:09 AM  
> Jeg vil derfor ønske én måte å gjøre det på (docker hvis det vi trenger er der) og så dok som forklarer avvik fra "normal".  
> stiglau 11:10 AM  
> Hvis vi tar f.ex <https://github.com/altran/Whydah/blob/master/config/Docker/sts/Dockerfile> vs <https://github.com/altran/Whydah/blob/master/config/Docker/uib/uib-all-in-one/Dockerfile> - så er det dette jeg vil vekk fra! (edited)  
> totto 11:10 AM  
> fordelen med Docker strategien, er at install er så eksplisitt at de som ikke vil bruke Docker kan kjøre kommandoene, linje for linje  
> @stiglau: det du vil ha er SDN overbygget... en install 1-2-4-1-1-1 konfig av Whydah på 1/2/3 jern  
> erikd 11:11 AM  
> Denne diskusjonen bør tas face2face hvor vi alle har skrevet ned hva vi ønsker å oppnå og hvordan.  
> stiglau 11:12 AM  
> enig med @erikd  
> Jeg tror vi ikke er så langt unna hverandre  
> men @erikd, jeg er absolutt ikke med på hva du mener om "AMI"  
> Hvis du tenker på det jeg forbinder med den teknologien, kunne vi like gjerne shippet ut lenovo-laptopper!  
> erikd 11:13 AM  
> @totto: 1. Har pakkemanager "inni" Docker avhengigheter til baseos Docker kjøres på?  
> totto 11:14 AM  
> 1. nei  
> erikd 11:14 AM  
> Les: Kan jeg bruke Debian inni og kjøre Docker-container på RedHat?  
> totto 11:14 AM  
> jepp  
> erikd 11:14 AM  
> Flott. Det er første avklaring.  
> 2. Du har snakket om supervisord for process start/stopp/basic monitoring. Kan du forklare hvordan dette oppsettet virker relatert til "inni" D-container og for baseOS?  
> totto 11:16 AM  
> 2. bruker supervisord kun inni imaget... syntes det var enklere og mere eksplisitt enn alternativene å konfigurere og som bonus så kjører den uavhengig av image sitt os sitt valg av prosessmanager  
> erikd 11:17 AM  
> 2b. Blir da hvordan virker processmanager for styring av docker-container? For der er det vel integrasjon med baseOS?  
> totto 11:19 AM  
> 2b. Der er det naturlig med docker-extension... som kan være samme som SDN eller en kombinasjon... shipyard er et alternativ... socketplane kan være et SDN alternativ  
> erikd 11:20 AM  
> @stiglau: AMI - Amazon EC2-image? Da abstraherer vi oss også bort fra at brukerne trenger å forholde seg til hvilket baseOS som kjører. Da velger vi ett baseOS og integrerer tett med det. Dårligere enn Docker, men bedre enn RPM/DEB, siden det er flere ting vi kan automatisere og skjule for brukerne.  
> totto 11:20 AM  
> det skjer veldig mye på 2b).. og vi er litt bleading edge... men det begynner å løsne og vil kunne fikse det store hårete målet vårt  
> stiglau 11:20 AM  
> @erikd: AMI = finger i halsen for meg  
> brb, mat  
> erikd 11:22 AM  
> Hvis vi ikke har en løsning (enda) på 2b, så har vi jo ikke (enda) en prodklar løsning. Vil anta at det er enklere å få høyere oppetid hvis man da bruker det eksisterende oppsettet.  
> totto 11:23 AM  
> jeg vil ikke lage en løsning på 2b) uten at dere er med å skjønner vurderinger/valgene og kan ta del i videreutvikling... vil ikke at vi lager nok en "black box" som er personavhengig  
> erikd 11:24 AM  
> 3. Hvilke andre avhengigheter har vi til baseOS og hvilke valg gjør man der? F.eks. hvor lagres logger? Hvor lagres config-filer?  
> 4. Kommunikasjon mellom dockerimages og mellom eksterne tjenester som f.eks. ldap, database er også ukjent hvordan man løser i Docker.  
> totto 11:24 AM  
> ...og jeg er ikke sikker på at mine vaøg/prioriteringer på 2b) er kompatible med hva dere tenker/vil  
> 3. opp til oss om vi vil lage avhengigheter dit  
> erikd 11:25 AM  
> 3. Vet det er opp til oss, men må vurderes og finne en god løsning.  
> totto 11:25 AM  
> 4. det er der SDN vil hjelpe oss... hvor vi får abstrahert vekk dne kompleksiteten fra imagene... og gjort dette smart og lett å forvalte/skalere  
> erikd 11:25 AM  
> Inn/ut av docker-image virket umodent og få gode retningslinjer på hvordan.  
> Ja, vet du peker på SDN, men for meg er det teori om hvordan ting bør være, så man evt. må lage, ikke noe som finnes klart p.t.  
> totto 11:26 AM  
> 3. jeg ville holdt log-filene inni imaget... og kanskje t.o.m. godta å kunne miste dem på et image-reboot... unntaket er UAS og UIB som nok bør ha persistent log  
> les litt om socketplane som et SDN eksempel... og se om ikke det gjør akkurat det vi trenger for routing/HA mellom et cluster av jern som kjører sett av docker images  
> inkludert hazelcast oppsett  
> ....de "ekleste" bitene å få økt oppetid på vil være et HA-oppsett for DB (fra AWS sin PaaS DB) og tilsvarende for LDAP (hvor vi ikke har HA idag)
