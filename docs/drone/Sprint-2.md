# Sprint 2

### [Sprint 2](Sprint-2.md)

- Started 13.4.2015 - finish 25.4.2015
- Ref last sprint [Sprint 1](Sprint-1.md)
- [Skype start sprint meeting 2015.4.13](Skype<sub>~start</sub><sub>sprint</sub><sub>meeting</sub><sub>2015</sub><sub>4</sub>~13.md)
- Establish test RSSfeed from Flight Data DB inkl picture of Drone (Ex.: Last 10 Drone flight activities) 

**refs:**

- [Demo map](http://89.221.242.66:8080/drone/)
- [Code base github](https://github.com/openGtsD/AukeGTS)
- [How to test drone on Server](How<sub>~to</sub><sub>test</sub><sub>drone</sub><sub>on</sub><sub>Server</sub><sub>Demo</sub><sub>4</sub>~1-2015.md)
- [Web service calls](Service-calls.md)
- [How to deploy the site](How<sub>~to</sub><sub>deploy</sub><sub>the</sub>~site.md)

- [Skype team meeting 2015.04.17](Skype<sub>~team</sub><sub>meeting</sub><sub>2015</sub>~04-17.md)
- [20.04.2015 - Joomla - First Site Setup](20<sub>~04</sub><sub>2015</sub><sub>Joomla</sub><sub>First</sub><sub>Site</sub>~Setup.md)
- [Terry and Stig adding droneradar24 comment 20.4.2015](Terry<sub>~and</sub><sub>Stig</sub><sub>adding</sub><sub>droneradar24</sub><sub>comment</sub><sub>20</sub><sub>4</sub>~2015.md)
- [Skype team meeting 2015.04.21](Skype<sub>~team</sub><sub>meeting</sub><sub>2015</sub>~04-21.md)
- [Skype team meeting 2015.04.28](Skype<sub>~team</sub><sub>meeting</sub><sub>2015</sub>~04-28.md)

**specs:** 

- [Jommla front end main specification](Jommla<sub>~front</sub><sub>end</sub><sub>main</sub>~specification.md)
- [How to register my tracker to site](How<sub>~to</sub><sub>register</sub><sub>my</sub><sub>tracker</sub><sub>to</sub>~site.md)
- [Site concurrency and scaling capacities](Site<sub>~concurrency</sub><sub>and</sub><sub>scaling</sub>~capacities.md)

##### Main objectives

**Master objective**

- User can add/update tracker info (real tracker or mobile phone app) and positions show in map
- Make simulated drones look real
- Document so far functionality 

**Details**

| task | Description | Who | Status |
| 1 | [Add map to joomla site](Add<sub>~map</sub><sub>to</sub><sub>joomla</sub>~site.md) - Thai completed for document and Stig will update Joomla Server | Thai/Stig | Completed |
| 2 | Test physical trackers (Tommy) | Tommy |  |
| 3 | Retrieve current positions from openGTS to AukeGTS ([drone:Integrate with openGTS data](../drone/Integrate<sub>~with</sub>~openGTS-data.md)) | Huy | Completed |
| 4 | Add direction show on Map | Thai | under development |
| 5 | [Making a "tail" for moving](Making<sub>~a</sub><sub>tail</sub><sub>for</sub>~moving.md) | Thai |  |
| 6 | Finish up [Layers and summarized positions](Layers<sub>~and</sub>~summarized-positions.md) | leif | under testing |
| 7 | [Web page for register and update tracker info](Web<sub>~page</sub><sub>for</sub><sub>register</sub><sub>and</sub><sub>update</sub>~tracker-info.md) |
a. User register/update/Delete tracker - Done with some field on UI. Need added more in developing
b. Make Page list all Tracker - Done
c. make page center
d. make flat html + js
Notes: For register Tracker we had insert new record into openGTS, But not work for update and delete (Need check service)|Thai| under development \\ LHA: comment \\ user must be able to update \\ delete |
| 8 | Make integration and unit tests | Huy/Thai/Leif |  |
| 9 | Document service calls [Service calls](Service-calls.md) | huy/Thai/Leif |  |  |
| 10 | [Test system using mobile phones for tracker](Test<sub>~system</sub><sub>using</sub><sub>mobile</sub><sub>phones</sub><sub>for</sub>~tracker.md) - Thai Updated document on wiki | huy/Thai/Leif |  |  |
