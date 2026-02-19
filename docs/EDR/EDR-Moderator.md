# EDR - Moderator

### Moderator Extension for EDR

### Responsibility

- Log Differences in data between providers
- Notify moderator to verify data.
- Keep list of updates awaiting moderator aproval
- Notify Controller if a domain object should be flaged dirty.

### Dependent on

- Provider Object Sync Controller

### Discussion

- Should we have Moderator funcionality also for Update (answere is yes).
- Challenge how to handle that a user does not have rights to update one of the providers.
  - Solved by updating the providers the user has write-access to.
  - Must as a minimum log that update failed, with the corresponding data.
- Not sure if Moderator will call ProviderObjecSyncController. A different aproach is for ProviderObjectSyncController to return error if sync failed, and then call the Moderator.

### Examples implemented

in Java so far.

1. Felles Contact Person - ikke lik verdi - log  
2. Felles Contact Person - ikke lik verdi - oppdater automatisk, samme verdi på neste kall

Bruk moderator som dependency injection (fra testklasse)

### ModeratorExcampleV1

### ModeratorExampleV2

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
**Moderator example for running EDR.**  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
\*This Example will first retreive a domain object. The providers will have \*  
\*different contact persons. A message about these differences will be logged, \*  
\*and the Legacy Provider will update it´s Contact Person from Billing Provider. \*

- \*  
  \*On the next run, data will be the same, and no info will be put into the log. \*
