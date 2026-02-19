# WS-diskusjon med Totto

(10:29:46 AM) Erik: Tror neste på den fronten blir "Howto test Webservices based on Cxf using JaxB and Soap". 
(10:30:21 AM) Totto - Thor Henning Hetland: ikke JAVX for guds skyld :)  test med XPATH på XML payloaden :)(
(10:30:27 AM) Totto - Thor Henning Hetland: JAXB
(10:32:04 AM) Erik: Hvorfor ikke JAXB? http://cxf.apache.org/docs/databindings.html som er tigljengelig 
(10:32:28 AM) Totto - Thor Henning Hetland: for tett/typet kobling
(10:32:47 AM) Erik: Hvilken http://cxf.apache.org/docs/databindings.html mener du er bedre? 
(10:33:17 AM) Erik: (Jeg må nok teste det de har valgt hos NGD og antar det er Jaxb) 
(10:33:35 AM) Totto - Thor Henning Hetland: ingen... bruk XPATH rett på XML payloaden - det jeg alltid gjør :)
(10:33:51 AM) Totto - Thor Henning Hetland: ESE må vite :)
(10:34:02 AM) Erik: hmm
(10:35:01 AM) Totto - Thor Henning Hetland: støtter plutselig versjonering mye bedre, alternative endepunkt og semi-structured data
(10:35:32 AM) Totto - Thor Henning Hetland: JAXB har ikke lært, gjør det samme som CORBA/IDL for 20 år siden
(10:36:08 AM) Erik: Kjenner jo XPATH, men må innrømme at jeg ikke intuitivt ser hvordan det gjør databindingen så mye bedre. 
(10:36:27 AM) Totto - Thor Henning Hetland: ikke bedre, men løsere
(10:36:33 AM) Erik: XPATH-expressions blir vel liggende inni pakkene, compile-time som alt annet? 
(10:36:56 AM) Totto - Thor Henning Hetland: jepp... men du plukker bare det du vil ha...  får ikke med deg all dritten
(10:37:40 AM) Totto - Thor Henning Hetland: og man kan kjøre skjemaløst, som er en stor fordel
(10:38:22 AM) Erik: Har hørt argumenter både for og imot schemas. Hvorfor mener du det er en fordel å kjøre uten? 
(10:38:35 AM) *****Erik syk hjemme og i læremodus
(10:38:40 AM) Totto - Thor Henning Hetland: det kan være en fordel å kunne kjøre uten
(10:38:52 AM) Totto - Thor Henning Hetland: jeg er også hjemme med sykt barn
(10:38:55 AM) Erik: Så det
(10:40:14 AM) Totto - Thor Henning Hetland: skjema gir sterkere typing enn hva som er nødvendig...   som er et problem hvis man ikke har ESE endepunkter (som folk ikke har)  kjører man skjemaløst, så blir kontrakten mindre statisk, og klientene plukker bare ut de delene av meldingene de er interessert i og ikke alt rælet
(10:42:02 AM) Totto - Thor Henning Hetland: fattigmans xml ducktyping :)
(10:42:23 AM) Erik: veldig mange liker å støtte seg på schemavalidering for å sikre "gyldige" meldinger da. 
(10:42:59 AM) Totto - Thor Henning Hetland: den støtten er hypotetisk og koster mye mere enn den smaker
(10:43:10 AM) Erik: Merker at argumentene dine er veldige like Geir sine. 
(10:43:17 AM) Totto - Thor Henning Hetland: og den hemmer gode grensesnitt
(10:43:33 AM) Erik: "Make work" over regelrytter-strategi.
(10:43:46 AM) Totto - Thor Henning Hetland: https://wiki.cantara.no/display/HESS/Token+service+-
(10:43:59 AM) Totto - Thor Henning Hetland: kan du jo hive deg over og kritisere
(10:44:08 AM) Erik: Hvordan blir versjonering med disse ulike strategiene? 
(10:45:25 AM) Totto - Thor Henning Hetland: med xpath så komemr det ann på....   som konsument så kommer det ann på hvordan du skriver uttrykkene....   i.e. ren ducktyping vil fungere helt til parametrene endrer navn/semantikk
(10:46:01 AM) Totto - Thor Henning Hetland: event så kan du skrive uttrykk mhhp versjonstagger i dokumnetet
(10:48:39 AM) Erik: Tror jeg forstår fordelene og fleksibiliteten her. Ser også at mulighetene for feil for enkle tjenester (der tettere kobling er akseptabelt) er mindre med f.eks. Jaxb. 
(10:49:04 AM) Erik: Må se an kompetansenivået i teamet også. Må lære å krabbe før de kan løpe. 
(10:49:19 AM) Totto - Thor Henning Hetland: mindre fingerfeil med xpath enn med jaxb
(10:49:32 AM) Erik: hmm, lovende. 
(10:49:50 AM) Totto - Thor Henning Hetland: skjemaer, jaxb, soap og navnerom skaper trøbbel for de fleste ferske
(10:50:04 AM) Erik: mm
(10:50:20 AM) Totto - Thor Henning Hetland: og så blir det så mye magi, at de ikke kan etterprøve eller skjønne hva som egentlig skjer
(10:50:21 AM) *****Erik _er_ ganske fersk på dette. 
(10:51:34 AM) Totto - Thor Henning Hetland: en annen fordel med å splitte endepunkt og payload på denne måten er at samme test/klient plutselig støtter flere transportmekanismer, og man kan teste klientene lokalt :)
(10:52:14 AM) Totto - Thor Henning Hetland: ...og plutselig så begynner man å produsere fornuftig xml payload, ikke autogenerert ræl som skal passe en fæl kontrakt
(10:52:54 AM) Erik: Mente du nå at Jaxb er så tett knyttet til overføringen at det er vanskelig å teste databindingen uten å dra på seg selve overføringen? 
(10:56:25 AM) Totto - Thor Henning Hetland: jeg mener at det kan virke som det ikke oppleves som naturlig å skille for prosjekter som bruker jaxb, siden payloaden blir generert på den ene siden og auto-mappet på den andre siden, som gjør at folk driter i hvordan payloaden faktisk ser ut
(10:57:22 AM) Erik: For mange kan jo det høres ut som kompleksitet man ikke trenger bry seg om. :P 
(10:57:51 AM) Erik: Det forklarer dog ganske mye om hvorfor det sendes så mye drit. :P 
(10:59:09 AM) Totto - Thor Henning Hetland: xpath tar jo bort mesteparten av kompleksiteten i parsingen...  og siden man får et forhold til payloaden, så lager man den sånn den er lett å tolke/bruke som er en viktig egenskap med tjenester, må vite
(10:59:40 AM) Erik: mm
(11:03:38 AM) Erik: Hva med frontend? JAX-WS? 
(11:04:29 AM) Totto - Thor Henning Hetland: jeg bruker JAX-RS men JAX-WS vil jo være soap alternativet
(11:05:12 AM) Totto - Thor Henning Hetland: har dog ikke mye praktisk erfaring med JAX-WS
(11:05:34 AM) Erik: Ser på REST og SOAP som to ulike tilnærminger ja. 
(11:06:18 AM) Erik: Innbiller meg at når startpunktet er trelags-silo-applikasjoner så er SOAP og synkrone ws-er enklere å forholde seg til enn REST-tankegangen. 
(11:06:23 AM) Totto - Thor Henning Hetland: du ser jo REST tilnærmingen min på SSO Token tjenesten
(11:07:21 AM) Totto - Thor Henning Hetland: ikke sikker...   spørs om man vil rydde frem ressursene/dataene i prosessen, eller bare metodene/aktivitetene
(11:07:57 AM) Totto - Thor Henning Hetland: det å få endret mindsettet til å se på dataene, pleier raskt å lønne seg som vi fort lærte i OW SOA
(11:08:20 AM) Erik: Ja, men da sikter du rimelig høyt igjen. 
(11:08:23 AM) Erik: :D 
(11:08:56 AM) Erik: Tør liksom ikke hoppe over så mange trinn av gangen jeg. 
(11:09:02 AM) Totto - Thor Henning Hetland: mja...   det å putte litt "fun" tilbake pleier ikke å være vanskelig å selge
