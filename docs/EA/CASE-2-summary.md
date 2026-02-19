# CASE 2 summary

CASE 2

5 different hardware types for reporting meter counters
- Different protocols
- Different link layers
- Different application layers
- Some online 24/7
- Some push night
- Some support pulling of meter counters
- Several different uses of meters

4 different systems
#1 Reporting
 * handles input from meters (external)
 * batch, gprs, etc
#2 Collecting
 * In-memory representation of readings
 * Responsible for readings
 * Post-processes result data from s1
#3 Accounting
 * Attaches s2-data to customers
#4 Rules for fetching data
 * Fetches information from

System Rules
- status: read_at, power failure, etc

**RÖ**: Not enough separation of concerns
**ED**: No control over customer interface
**ED**: No control over meter input
**ED**: Messages between systems send XML-messages
**RÖ**: Two systems need to agree on something (contract) -- RDF would be ideal. XML is "ok".
**TFN**: Is performance the problem?
**ED - on problem**: Well, stability, maintainability, scalability, performance, common language, validation of results are all issues. 
**ED - on rules**: i.e. estimation of results available for data type 1 & N but not M.

Problems:
- no common ground
- no agility
- no validity of data
- no trustworthiness(tm) of system implementation
- many bottlenecks
- big integration
- data duplication
- low separation of concerns
- no control over endpoints (reporting system and customer system)
- poor scalability

Solution!
- Good fit for REST-based architecture
- Important to simplify the architecture, not introduce more complexity
- partition data sets
- use several flows
- use neo4j!
- Use compressed RDF(JSON/XML/ETC) for cross-system messages (GZIP, etc)
- Distributed protocol for flows possible (i.e. XMPP)
