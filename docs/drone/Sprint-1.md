# Sprint 1

### [Sprint 1](Sprint-1.md)

Started 3.3.2015, ended 12.4.2015

##### Sprint objective summarize

1. We manage to make a map and draw positions, zoom in/out and show position is view pluss adding layers -> very good (/)
1. We manage to make the core service with drone simulations, and service calls -> very good (/)
1. We installed openGTS and inspect the database -> good (/)
1. we did not manage to test live feed from physical trackers with open GTS -> this must be moved to sprint 2 (?)

##### Comments and meetings

- [Comment from leif 26.3.2015](Comment<sub>~from</sub><sub>leif</sub><sub>26</sub>~3-2015.md)
- [Comment leif 27.3.2015](Comment<sub>~leif</sub><sub>27</sub><sub>3</sub>~2015.md)
- [Dialog team 30.3.2015](Dialog<sub>~team</sub><sub>30</sub><sub>3</sub>~2015.md)
- [Skype team meeting 6.4.2015](Skype<sub>~team</sub><sub>meeting</sub><sub>6</sub>~4-2015.md)
- [Skype team meeting 10.4.2015](Skype<sub>~team</sub><sub>meeting</sub><sub>10</sub>~4-2015.md)

##### Tasks 

| task | Description | Who | Status |
| 8 | [Integrate with openGTS data](Integrate<sub>~with</sub>~openGTS-data.md) integrate and retrive data from openGTS | lha |  |
| 7 | [Next step simulation, make and save flights](Next<sub>~step</sub><sub>simulation</sub><sub>make</sub><sub>and</sub><sub>save</sub>~flights.md) When drone fly (are in motion, there is a flight) | huy |  |
| 6 | [Thai and Tommy tracker recording testing](Thai<sub>~and</sub><sub>Tommy</sub><sub>tracker</sub>~recording-testing.md) run live test for openGTS to read tracks from a tracker | tommy/Thai |  |
| 5 | [Show drone identity](Show<sub>~drone</sub>~identity.md) | thai | Completed |
| 4 | [Request and plot the positions into the current map view every 10 second](Request<sub>~and</sub><sub>plot</sub><sub>the</sub><sub>positions</sub><sub>into</sub><sub>the</sub><sub>current</sub><sub>map</sub><sub>view</sub><sub>every</sub><sub>10</sub>~second.md) |
show zoom factor and boundary on page + number of postions in current view
 (make it more easy to test) | thai | In-progress |
| 3 | [Add a process for each drone that refresh new positions every 10 seconds on server](Add<sub>~a</sub><sub>process</sub><sub>for</sub><sub>each</sub><sub>drone</sub><sub>that</sub><sub>refresh</sub><sub>new</sub><sub>positions</sub><sub>every</sub><sub>10</sub><sub>seconds</sub><sub>on</sub>~server.md). \\ |
for ex. 10 drones that update new position every 10 second with random speed and movement. each 'drone' update to the current position list. You retrieve from this position list to map (every 10 second). this is a good page for different calculations
http://www.movable-type.co.uk/scripts/latlong.html   | Huy/Thai (Support)| Completed |
| 0 | Make a project for this in github https://github.com/openGtsD/AukeGTS | thai | Completed |  |
| 1 | a. make a service (witout opengts) the simulate a table with some units and some fee |
    b.  make the web service for request
    c. make the web page with google map included
d. Requst and plot the simulated positions into the map | Thai | a. Completed
b. Completed
c. Completed
d. Completed |
| 2 | Integrate with opneGTS = get the postions from open GTS feed into the service | Thai |  |
