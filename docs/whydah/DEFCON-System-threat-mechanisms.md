# DEFCON - System threat mechanisms

|  | Whydah is a light-weight, modular, open source Single Sign-on and Identity and Access Management (IdM, IAM) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | The **DEFCON IT Security&Threat Concept** is *borrowed* from this JavaZone presentation: <http://vimeo.com/105861379>  |  | This is work in progress, and mainly a discussion of possibilities in Whydah right now | |

### Whydah Threat Actions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DEFCON 5**  Normal operations | **DEFCON 4**  Limit sessions to security\_level-1 or higher on app and users  Invoke exponential retry timer per app/user  Split SSO cluster in separate public and private cluster sets and inform apps in apptoken  Revoke all application sessions, empty user sessions  Confuse attackers with *dummy* https-responses and headers  STS renew\_usertoken action stopped  STS get\_usertoken\_from\_usertokenid action stopped  Inform all Whydah applications of threat level: DEFCON-4 so they can take appropriate actions | **DEFCON 3**  Limit Whydah functionality to only to DEFCON configured Applications  Inform *existing* Whydah applications of threat level: DEFCON-3 so they can take appropriate actions  Security level minimum 2 on applicationtokens and usertokens  Kill all appsessions and user sessions every 5 min  Limit Whydah access to a predefined sub-set of known IP addresses | **DEFCON 2**  Delete RoleIndex and UserRoleDataBase  Kill SSOLWA, STS and UAS | **DEFCON 1**  Kill LDAP server  KILL UIB |

---

### Whydah Threat Detection

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DEFCON 5**  Normal operations | **DEFCON 4**  Network traffic peak >50x normal detected  Asymmetric Whydah usage statistics, i.e form 10% auth vs session to 90% auth vs session detection  Increase in abnormal payload on services | **DEFCON 3**  Network traffic peak >5000x normal detected  Asymmetric port usage (strange and not commonly used ports for normal Whydah operations) detection  IDS alerts  High level of abnormal payload on services  Outbound traffic detection | **DEFCON 2**  Anormal traffic from inside Whydah security boundaries detected  Strange inter-component traffic detection  IDS alerts  Tripwire alerts | **DEFCON 1**  3rd party alarms  Tripwire alerts |

---

**From Whydah workshop 2015-1 on DEFCON**

Diskusjon den 13/6-2015 på Whydah-workshop om signaler som bør overvåkes i forbindelse med evaluering av DefCon-level.

### Signaler som kan mottas

- Høy påloggingsfrekvens fra en IP/subnett på forskjellige brukere
- Høy påloggingsfrekvens på samme bruker fra forskjellige IPer
- Flere påloggingsforsøk fra geografisk spredte steder innenfor kort tid for samme bruker
- Flere påloggingsforsøk fra geografisk spredte steder innenfor kort tid for mange bruker av samme applikasjon
- Høy frekvens av nytt-passord forespørsler for en bruker
- Høy frekvens av nytt-passord forespørsler for mange brukere (bør ikke tillate høyeste sikkerhetsnivå)
- Høy frekvens av release eller session handover innenfor en sesjon på samme applikasjon (applikasjonsgruppe) (samme auth-id)
- Økt frekvens av expired sessions
- Uvanlig reautentisering av applikasjon
- Endring av applikasjonsinstanser (antall, lokasjon, adresse)
- Aktiv bruk av hard-close på sesjoner
- Uvanlig UserAdmin-aktivitet

- Infrastruktursignaler
  - Uvanlig prosessorlast fra egen eller andre prosesser på server
  - Uvanlig IO-belastning på server
  - Uvanlig minneforbruk på server
  - Mottak av uvanlige datapakker
  - Mottak av requests med uvanlig innhold (URI, header, body-content)
  - Full disk på server
  - Uvanlig mange events og påfølgende logg-belastning

# Tasks

- Legge til Defcon i Heartbeat-API
- Håndtere sesjons-signaler i SDS
- Ha en egen DefCon-service som kontrollerer eksterne signaler (infrastruktur, etc.)
