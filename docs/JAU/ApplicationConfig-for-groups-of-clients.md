# ApplicationConfig for groups of clients

Use case: ApplicationConfig for groups of clients

Several groups of clients, where each group has the same ApplicationConfig.

Clients must specify a specific *clientName* or *tag*. ConfigService will use this information to select the correct ApplicationConfig.   
The implementation in ConfigService must be generic so that the matching logic can be specified as configuration.

If no rules match, the client should get the *default* ApplicationConfig. If not default config is specified, the client registration should be rejected.

### Rules for choosing ApplicationConfig - *registerClient*

ClientRegistrationRequest.java

1. clientId (client may already be registered)
   1. if autoUpgrade=true, do *checkForUpdatedClientConfig*
2. clientName
3. tags
4. default ApplicationConfig
5. reject registration
