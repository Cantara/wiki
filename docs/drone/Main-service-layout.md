# Main service layout

### [Main service layout](Main-service-layout.md)

##### Figure 

![auke](../images/gliffy/41877549-auke-gts-main-layout.png)

##### Processes 

| Item | Description | refs |
| --- | --- | --- |
| OpenGTS | existing opengst system used for reading real tracks from trackers |  |
| [get current opengts positions](get-current-opengts-positions.md) | process the read current positions into the temporary position list |  |
| [Track simulator](Track-simulator.md) | make simulated drones flying | [Add a process for each drone that refresh new positions every 10 seconds on server](Add-a-process-for-each-drone-that-refresh-new-positions-every-10-seconds-on-server.md) |
| aukegts real time tracks | list of current positions, both simulated and real positions |  |  |
| [Track processor](Track-processor.md) | process the current tracks |  |  |
| [Flights database](Flights-database.md) | database storage for individual drone flights |  |
| single positions | current positions for one by on drone |  |
| 10 km positions | summarized position for all drone with and area of 10 km |  |
| 10 mile positions | summarized position for all drone with and area of 10 mile |  |
| 100 mile positions | summarized position for all drone with and area of 100 mile (maybe bigger, we see how it looks |  |
| [ws get positions](ws-get-positions.md) | retrieve positions with a current view | [Request and plot the positions into the current map view every 10 second](Request-and-plot-the-positions-into-the-current-map-view-every-10-second.md) |
| [ws get flights](ws-get-flights.md) | retrieve a flight list for a certain area at a certain time |  |
| web map | google map showing positions |  |
| web flight list | select and view a list of flights (select on area and time frame ) | To be specified |
