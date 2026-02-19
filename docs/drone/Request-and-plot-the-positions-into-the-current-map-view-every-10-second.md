# Request and plot the positions into the current map view every 10 second

### [Request and plot the positions into the current map view every 10 second](Request<sub>~and</sub><sub>plot</sub><sub>the</sub><sub>positions</sub><sub>into</sub><sub>the</sub><sub>current</sub><sub>map</sub><sub>view</sub><sub>every</sub><sub>10</sub>~second.md)

_ref:_ 

- [Drone radar design](Drone<sub>~radar</sub>~design.md)
- [Main service layout](Main<sub>~service</sub>~layout.md)
- [How to test drone on Server Demo - 4.1.2015](How<sub>~to</sub><sub>test</sub><sub>drone</sub><sub>on</sub><sub>Server</sub><sub>Demo</sub><sub>4</sub>~1-2015.md)

##### Comment leif 2.4.2015

- Refresh positions when zoom is changed or map view is slided (catch some event and re-read positions form server)

##### Function

Retrieve list of current positions within current map boundary each 10 second and update map

##### Solution

- Service query with map boundary (map area) as parameter. (Longitude, latitude and current zoom factor)
- Deliver back position list for each drone with the area
- When click on position, show drone information (id,name, speed, position, altitude) 

##### Issues

- Size of map view. Only show individual drone positions when map view is less the 10km in size. If bigger, use the summarized positions 

_Solve with a java script loop on page_
