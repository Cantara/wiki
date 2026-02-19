# Sprint 1

### [Sprint 1](Sprint-1.md)

Started 3.3.2015, ended 12.4.2015

##### Sprint objective summarize

1. We manage to make a map and draw positions, zoom in/out and show position is view pluss adding layers -> very good (/)
1. We manage to make the core service with drone simulations, and service calls -> very good (/)
1. We installed openGTS and inspect the database -> good (/)
1. we did not manage to test live feed from physical trackers with open GTS -> this must be moved to sprint 2 (?)

##### Comments and meetings

- [Comment from leif 26.3.2015](Comment-from-leif-26-3-2015.md)
- [Comment leif 27.3.2015](Comment-leif-27-3-2015.md)
- [Dialog team 30.3.2015](Dialog-team-30-3-2015.md)
- [Skype team meeting 6.4.2015](Skype-team-meeting-6-4-2015.md)
- [Skype team meeting 10.4.2015](Skype-team-meeting-10-4-2015.md)

##### Tasks 

| task | Description | Who | Status |
| 8 | [Integrate with openGTS data](Integrate-with-openGTS-data.md) integrate and retrive data from openGTS | lha |  |
| 7 | [Next step simulation, make and save flights](Next-step-simulation-make-and-save-flights.md) When drone fly (are in motion, there is a flight) | huy |  |
| 6 | [Thai and Tommy tracker recording testing](Thai-and-Tommy-tracker-recording-testing.md) run live test for openGTS to read tracks from a tracker | tommy/Thai |  |
| 5 | [Show drone identity](Show-drone-identity.md) | thai | Completed |
| 4 | [Request and plot the positions into the current map view every 10 second](Request-and-plot-the-positions-into-the-current-map-view-every-10-second.md) |
show zoom factor and boundary on page + number of postions in current view
 (make it more easy to test) | thai | In-progress |
| 3 | [Add a process for each drone that refresh new positions every 10 seconds on server](Add-a-process-for-each-drone-that-refresh-new-positions-every-10-seconds-on-server.md). \\ |
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
