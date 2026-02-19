# ConfigService Admin API

# ConfigService Admin APIs

**Content-Type: application/json**  
\*Required security role: admin

## Service status check

| Method | Description | Roles | Request body | Response body | Examples | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| GET /health | return the status and version of the service |  |  | ConfigService OK, version 0.8-beta-7, now=2016-11-02T08:56:31.528Z, running since 2016-11-01T12:49:28.960Z |  |  |

## Client - administration

- Resource class: ClientResource

| Method | Description | Roles | Request body | Response body | Examples | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| PUT /client/{**clientId**} | Create or update client | Admin | [Client](/web/20210228125608/https://wiki.cantara.no/display/JAU/Client "Client") | [Client](/web/20210228125608/https://wiki.cantara.no/display/JAU/Client "Client") | Use cases:  \* [Preregister Client with specific ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/Preregister+Client+with+specific+ApplicationConfig "Preregister Client with specific ApplicationConfig")   \* [Change ApplicationConfig for one existing Client](/web/20210228125608/https://wiki.cantara.no/display/JAU/Change+ApplicationConfig+for+one+existing+Client "Change ApplicationConfig for one existing Client") \* autoUpgrade=true/false, etc. |  |
| GET /client/{**clientId**} |  | Admin |  | [Client](/web/20210228125608/https://wiki.cantara.no/display/JAU/Client "Client") |  |  |
| GET /client/{**clientId**}/config | return the ApplicationConfig currently registered on the client | Admin |  | [ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/ApplicationConfig "ApplicationConfig") |  |  |
| GET /client/{**clientId**}/status | return overview of client, including last heartbeat data from sync/registerClient | Admin |  | [ClientStatus] = [Client](/web/20210228125608/https://wiki.cantara.no/display/JAU/Client "Client") + [ClientHeartbeatData](/web/20210228125608/https://wiki.cantara.no/display/JAU/ClientHeartbeatData "ClientHeartbeatData") |  | ED: The results doesn't look like expected. Use with caution! |
| GET /client/{**clientId**}/events | return events/log statements extracted from data received from sync/registerClient | Admin |  | [ExtractedEventsStore](/web/20210228125608/https://wiki.cantara.no/display/JAU/ExtractedEventsStore "ExtractedEventsStore") |  |  |
| GET /client/{**clientId**}/env | return last received environment variables from sync/registerClient | Admin |  | [ClientEnvironment](/web/20210228125608/https://wiki.cantara.no/display/JAU/ClientEnvironment "ClientEnvironment") |  |  |
| GET /client/ | return list of all registered clients | Admin |  | List of [Client](/web/20210228125608/https://wiki.cantara.no/display/JAU/Client "Client") |  |  |

For å få verktøystøtte for bl.a. links så bør vi vurdere et ferdig hypermediaformat hvor det finnes helperlibs. Tenker admin-api-ene er naturlig å stare med først. F.eks. siren og collection+json kan antagelig brukes. Mulig siren passer best:

- <http://mvnrepository.com/artifact/no.arktekk/siren-java>
- <http://mvnrepository.com/artifact/net.hamnaberg.rest/json-collection>

## Application

- Resource class: ApplicationResource

| Method | Description | Roles | Request Body | Response Body | Examples | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| POST /application/ | Create a new application with the given artifactId. | Admin | artifactId | [Application](/web/20210228125608/https://wiki.cantara.no/display/JAU/Application "Application") | [Create Application and ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/Create+Application+and+ApplicationConfig "Create Application and ApplicationConfig") | TODO should application have a defaultApplicationConfigId reference? |
| GET /application/{**artifactId**}/status | Data on clients that are registered on this application | Admin |  | [ApplicationStatus](/web/20210228125608/https://wiki.cantara.no/display/JAU/ApplicationStatus "ApplicationStatus") |  | Tenker her typisk hvor mange klienter totalt, hvor mange har vært aktive siden x tid, hvor mange klienter kjører hver versjon, osv.   **TODO**: artifactId -> applicationId (requires that we store applicationId in [ClientHeartbeatData](/web/20210228125608/https://wiki.cantara.no/display/JAU/ClientHeartbeatData "ClientHeartbeatData")) |
| GET /application/ | return all registered applications | Admin |  | List of [Application](/web/20210228125608/https://wiki.cantara.no/display/JAU/Application "Application") |  |  |
| *GET /application/config* | *return all ApplicationConfig for all applications* | Admin |  | List of [ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/ApplicationConfig "ApplicationConfig") |  | *Suggestion*, not implemented yet |

## ApplicationConfig

- Resource class: ApplicationConfigResource (former serviceconfig)

| Method | Description | Roles | Request Body | Response Body | Examples | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| POST /application/{**applicationId**}/config | Create applicationconfig for the given application. RegisterClient will return this config for matching artifactId. | Admin | [ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/ApplicationConfig "ApplicationConfig") | [ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/ApplicationConfig "ApplicationConfig") | [Create Application and ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/Create+Application+and+ApplicationConfig "Create Application and ApplicationConfig") |  |
| PUT /application/{**applicationId**}/config/{**applicationConfigId**} | Update applicationconfig. Clients will receive updated config when they call sync/checkForUpdate. | Admin | [ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/ApplicationConfig "ApplicationConfig") | [ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/ApplicationConfig "ApplicationConfig") | [Update ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/Update+ApplicationConfig "Update ApplicationConfig") | lastChanged must always be updated   TODO: when to create a new one vs when to change? |
| GET /application/{**applicationId**}/config/{**applicationConfigId**} | return a specific ApplicationConfig | Admin |  | [ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/ApplicationConfig "ApplicationConfig") |  |  |
| DELETE /application/{**applicationId**}/config/{**applicationConfigId**} | delete the specific ApplicationConfig | Admin |  |  |  |  |
| GET /application/{**applicationId**}/config/ | return all ApplicationConfigs for the given applicationId | Admin |  | Map from id to [ApplicationConfig](/web/20210228125608/https://wiki.cantara.no/display/JAU/ApplicationConfig "ApplicationConfig") |  | Currently returns *all* ApplicationConfigs for all applications, see [#39](https://github.com/Cantara/ConfigService/issues/39) |

#### Example application config

---

## Old documentation (still useful for older versions of ConfigService and Java Auto Update

- [Old ConfigService API documentation - Application endpoint](/web/20210228125608/https://wiki.cantara.no/display/JAU/Old+ConfigService+API+documentation+-+Application+endpoint "Old ConfigService API documentation - Application endpoint"), dashboard/statistics for all clients using certain software.
- [Old ConfigService API documentation - ServiceConfigResource endpoint](/web/20210228125608/https://wiki.cantara.no/display/JAU/Old+ConfigService+API+documentation+-+ServiceConfigResource+endpoint "Old ConfigService API documentation - ServiceConfigResource endpoint"), administrate service configurations for clients
