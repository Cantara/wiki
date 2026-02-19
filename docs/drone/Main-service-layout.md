# Main service layout

### [Main service layout](Main<sub>~service</sub>~layout.md)

##### Figure 

**[Diagram: auke](../Diagram/auke.md)**

##### Processes 

| Item | Description | refs |
| --- | --- | --- |
| OpenGTS | existing opengst system used for reading real tracks from trackers |  |
| [get current opengts positions](get<sub>~current</sub>~opengts-positions.md) | process the read current positions into the temporary position list |  |
| [Track simulator](Track-simulator.md) | make simulated drones flying | [Add a process for each drone that refresh new positions every 10 seconds on server](Add<sub>~a</sub><sub>process</sub><sub>for</sub><sub>each</sub><sub>drone</sub><sub>that</sub><sub>refresh</sub><sub>new</sub><sub>positions</sub><sub>every</sub><sub>10</sub><sub>seconds</sub><sub>on</sub>~server.md) |
| aukegts real time tracks | list of current positions, both simulated and real positions |  |  |
| [Track processor](Track-processor.md) | process the current tracks |  |  |
| [Flights database](Flights-database.md) | database storage for individual drone flights |  |
| single positions | current positions for one by on drone |  |
| 10 km positions | summarized position for all drone with and area of 10 km |  |
| 10 mile positions | summarized position for all drone with and area of 10 mile |  |
| 100 mile positions | summarized position for all drone with and area of 100 mile (maybe bigger, we see how it looks |  |
| [ws get positions](ws<sub>~get</sub>~positions.md) | retrieve positions with a current view | [Request and plot the positions into the current map view every 10 second](Request<sub>~and</sub><sub>plot</sub><sub>the</sub><sub>positions</sub><sub>into</sub><sub>the</sub><sub>current</sub><sub>map</sub><sub>view</sub><sub>every</sub><sub>10</sub>~second.md) |
| [ws get flights](ws<sub>~get</sub>~flights.md) | retrieve a flight list for a certain area at a certain time |  |
| web map | google map showing positions |  |
| web flight list | select and view a list of flights (select on area and time frame ) | To be specified |
