# IAM_MODE

IAM\_MODE is used to run the modules in different mode

| Mode | Comments |
| --- | --- |
| PROD | Production mode, UiB will run with external LDAP and role DB |
| TEST | Integration test mode, UiB will run with embedded LDAP and embedded HSQL DB |
| TEST\_LOCALHOST | Test mode on locoalhost (Not a full mode, just config files for localhost setup). |
| DEV | Development mode |

The artefacts are equipped with default property files for each of these modes.
