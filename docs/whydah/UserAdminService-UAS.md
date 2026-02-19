# UserAdminService - UAS

#### Responsibility

Borderline guard for UIB

1. Ensure validated access to UIB before forwarding request to UIB
   1. Validate application. Main focus is that no requests are forwarded to UIB unless origin is from a validated application.
   2. Validate user. MWhen requests to UIB require admin access, only requests with validated user are forwarded to UIB.
2. DDos attac will be stoped at UAS, and might bring UAS to a halt. UIB will remain intact.

Fine-grained access-control of administration APIs.

1. for å kunne låse ned UIB (borderline security)
   1. BLI: obfuscate url i SsoLoginService, ikke i UAS
   2. BLI: validering av payload, stoppe altfor store ting, f.eks. unngå sql-injection
2. for å kunne rendyrke ansvar og funksjonalitet i UIB... og la UAS fasillitere flerskrittsprosesser inn mot UIB
3. audit - spesielt på flerskrittsprosesser

###### Details

- Backend for Whydah UserAdminWebApplication
- Backend for 3rd party SSO Applications with **self service** functionality
  - Provide a configurable and protectable self service API so that your application can tackle user admin tasks itself.

Actions that could be allowed through the 3.party self-service API includes:

- Adding new users to an application with a default role (**signup**)
- Adding a secondary role to existing users of the application (**intra application role management**)
- Listing existing users and their roles (**intra application role management**)

### Design principles

- secured proxy for UIB API/functionality (Whydah UserAdminWebApp)
- secured process-API for administrative actions which require several UIB actions (3rd party API)

### Configuration properties

The Artefact contains default properties for the different [IAM\_MODE](/web/20230208102542/https://wiki.cantara.no/display/whydah/IAM_MODE "IAM_MODE")'s being used.

- <- \* Indicates same value as the one to the right.

| Property | Example values PROD  Use external config  Exists as embedded - not recommended | Default values TEST | Default values DEV | Comment |
| --- | --- | --- | --- | --- |
| **prop.type** | PROD | TEST | DEV | [IAM\_MODE](/web/20230208102542/https://wiki.cantara.no/display/whydah/IAM_MODE "IAM_MODE") for this property file |
