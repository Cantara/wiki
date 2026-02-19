# Group 1 - Groups of scalabillity problems

### Introduction

This group will focus on looking into how we can categorize the different scalability challenges. Typically by breaking down scale like

- data volume
- data complexity
- request volume
- computation complexity
- .. and so forth...

### Group members...

- Tobias Torrissen
- Kjetil Valstadsve
- Johannes Brodwall
- Emil Eifrem
- Finn-Robert Kristensen

### The result..

#### Runtime scalability:
Request load 
 * Read
  ** Random
  ** Sequential
 * Write
  ** Append-only
  ** Random
  ** process and forward: large datasets who needs to be aggregated
 * Prio?

Data load
 * size
 * complexity
  ** connectedness
  ** semi-structure
 * volatility?

Consisteny requirements
 * availablitity, reliability, freshness
 * overall: when does an actor require to see the effects of the operations (its own and others)

#### Development time scalability:
 * "What happens when you get many of---"
 * KLOC [size](size.md)
   ** unintended consequences
 * Distributed services/components [size](size.md)
  ** performance
  ** change cost (formalized)
  ** debugging
 * technologies [complexity](complexity.md)
  ** open source frameworks + libraries + languages
  ** => assumptions inherited
  ** => interactions n^2
 * Developers - scaling numbers of developers

#### Operation scalability
 * Layers
  ** infrastructure
  ** OS 
  ** Platform (app server)
  ** App
 * Concerns
  ** Monitoring/management
  ** Configuration
  ** Deployment
  ** Security
 

#### Causality / dependency suite
 * Problem domain
  ** => Runtime issues
  ***** => development issues
  ****** => Operational issues

#### Case study: Twitter
Data is no naturally partitionable
High random reads
High write, append mostly
Milk data - interested in recent data

#### Case study: Instrument data acquisition
10" write clients
10" packets/sec
Compress and store
Aggregate data

#### Case study: Green driving:
Each 1km road has a price 1-10 cents

Norway 2 billion sensors
Peak of number of cars 500"
Each car drives at 60 km/h
15 million messages/sec -> sends: carId + sensorId
Extremely partitionable
