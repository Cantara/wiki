# Simple property strategy

#### Principles 

1. Default configuration bundled with the application (e.g. inside jar file) 
1. Possible to override properties. It should not necessary to override all properties like Spring's _PropertyPlaceholderConfigurer_ require. _PropertyOverrideConfigurer_ may be used, but the restrictions on key naming is an disadvantage. 
1. All consumers of the configuration must see the same values (singleton?). 
1. Support for different configuration defaults (e.g. DEV, TEST, PROD, PROD-HA). Choose template/default values and then add overrides. 
1. Make a copy of configuration templates available as documentation outside deployment unit (jar file). 
1. Could should behave properly both when run from jar file and IDE. 

#### Possible extensions 

- Implement AppConfig as a Singleton?  

- Is run-time reload necessary/needed? 
    - Yes, for some properties. E.g. dns, scalability properties, tuning parameters 
    - See http://johannesbrodwall.com/2014/10/02/dead-simple-configuration/ for inspiration.

- Necessary to support several files or group the properties? 
    - Applications should not grow too large. No old school monoliths. Users should normally only change a few properties (overrides). 

#### Implementation example 

**TODO** Link to Whydah when new version of AppConfig is finished.
