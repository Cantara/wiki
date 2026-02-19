# Drone radar design

## [Drone radar design](Drone<sub>~radar</sub>~design.md)

### Overall design using OpenGTS

OpenGTS have 4 main modules

1. GUI with map and account and vehicle administration
1. Feed web services working to support UI and retrieve tracker feeds, vehicle info and account info
1. Tracker feed, trackers (vehicle and account database (my sql)
1. Tracker feed collect agents

In general each feed is done from a unique device, and this devise is identified as a vehicle on a specific account.

We keep all this intact an make extra retrieval process

### We need 

1. On map showing all alive vehicles within each users map boundaries
1. A list of active vehicles

**How to solve: (extra retrieval process)**

Two step retrieval from openGTS tracker feed table

1. A process that query the tracker feed table on current feeds (alive ones with a time frame) and put to a tracker feed run time table
1. The user request feeding showing all tracks within a geographical boundaries for each active retrieving user.
1. Track simulator for simulate drone movments for demo purpose [Add a process for each drone that refresh new positions every 10 seconds on server](Add<sub>~a</sub><sub>process</sub><sub>for</sub><sub>each</sub><sub>drone</sub><sub>that</sub><sub>refresh</sub><sub>new</sub><sub>positions</sub><sub>every</sub><sub>10</sub><sub>seconds</sub><sub>on</sub>~server.md)

### Tasks and issues

- [Add a process for each drone that refresh new positions every 10 seconds on server](Add<sub>~a</sub><sub>process</sub><sub>for</sub><sub>each</sub><sub>drone</sub><sub>that</sub><sub>refresh</sub><sub>new</sub><sub>positions</sub><sub>every</sub><sub>10</sub><sub>seconds</sub><sub>on</sub>~server.md)
- [Request and plot the positions into the current map view every 10 second](Request<sub>~and</sub><sub>plot</sub><sub>the</sub><sub>positions</sub><sub>into</sub><sub>the</sub><sub>current</sub><sub>map</sub><sub>view</sub><sub>every</sub><sub>10</sub>~second.md)
- [Show drone identity](Show<sub>~drone</sub>~identity.md)
