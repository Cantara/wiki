# Configuration Categorization

#### Matrix 
- Support different dimensions of configuration 
|  | Startup <sup>1</sup> | Resource/ext. service setup <sup>2</sup> | Usage/Tuning <sup>3</sup> |
| Global |  |  |  |
| --- | --- | --- | --- |
| Environment |  |  |  |
| --- | --- | --- | --- |
| Application |  |  |  |
| --- | --- | --- | --- |
| Node |  |  |  |
| --- | --- | --- | --- |

<sup>1</sup> Startup configuration: java options, Environment Variables 
<sup>2</sup> Setup configuration (addresses, usernames, passwords) 
<sup>3</sup> Usage /tuning are parameters that change how the application behaves. Performance tuning is a typical example. 

#### Examples to illustrate what kind of configuration goes into each category 

- Global 
    - Tweak/usage defaults 

- Environment
    - JMS-server
    - The name of JMS Destinations to use
    - JDBC 

- Application 
    - Tweak/usage overrides 
    - Resources (e.g. a dbms) only used by this application 

- Node specific
    - Distribute work intervals evenly
    - tweak the application according to OS or hardware specifics (e.g. number threads must match available cpu and memory) 
While these seems like valid configurations parameters, moving this responsibility to the application should be considered.
