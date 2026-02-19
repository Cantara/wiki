# Common Factor list

The purpose of this page is to identify which factors, which _drivers_, different tactics should adhere to. 

- Testability and maintainability should in general be the two most important drivers. Exceptions should not be made lightly. 

- The final artifact should not require build-time changes to facilitate deployment to different environments. (I.e., all configuration required to deploy to a specific environment should be configurable run-time.) 

- All artifacts must be uniquely identified. 

- All releases (any non-snapshot artifact) must be reproducible. E.g. dependencies on snapshots is not allowed. 

- Pull-based configuration schemes should be preferred over push-based. (All projects/services need to know where to find its configuration. No single service is responsible for updating all clients.)
