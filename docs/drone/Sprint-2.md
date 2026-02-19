# Sprint 2

### [Sprint 2](Sprint-2.md)

- Started 13.4.2015 - finish 25.4.2015
- Ref last sprint [Sprint 1](Sprint-1.md)
- [Skype start sprint meeting 2015.4.13](Skype-start-sprint-meeting-2015-4-13.md)
- Establish test RSSfeed from Flight Data DB inkl picture of Drone (Ex.: Last 10 Drone flight activities) 

**refs:**

- [Demo map](http://89.221.242.66:8080/drone/)
- [Code base github](https://github.com/openGtsD/AukeGTS)
- [How to test drone on Server](How-to-test-drone-on-Server-Demo-4-1-2015.md)
- [Web service calls](Service-calls.md)
- [How to deploy the site](How-to-deploy-the-site.md)

- [Skype team meeting 2015.04.17](Skype-team-meeting-2015-04-17.md)
- [20.04.2015 - Joomla - First Site Setup](20-04-2015-Joomla-First-Site-Setup.md)
- [Terry and Stig adding droneradar24 comment 20.4.2015](Terry-and-Stig-adding-droneradar24-comment-20-4-2015.md)
- [Skype team meeting 2015.04.21](Skype-team-meeting-2015-04-21.md)
- [Skype team meeting 2015.04.28](Skype-team-meeting-2015-04-28.md)

**specs:** 

- [Jommla front end main specification](Jommla-front-end-main-specification.md)
- [How to register my tracker to site](How-to-register-my-tracker-to-site.md)
- [Site concurrency and scaling capacities](Site-concurrency-and-scaling-capacities.md)

##### Main objectives

**Master objective**

- User can add/update tracker info (real tracker or mobile phone app) and positions show in map
- Make simulated drones look real
- Document so far functionality 

**Details**

| task | Description | Who | Status |
| 1 | [Add map to joomla site](Add-map-to-joomla-site.md) - Thai completed for document and Stig will update Joomla Server | Thai/Stig | Completed |
| 2 | Test physical trackers (Tommy) | Tommy |  |
| 3 | Retrieve current positions from openGTS to AukeGTS ([drone:Integrate with openGTS data](../drone/Integrate-with-openGTS-data.md)) | Huy | Completed |
| 4 | Add direction show on Map | Thai | under development |
| 5 | [Making a "tail" for moving](Making-a-tail-for-moving.md) | Thai |  |
| 6 | Finish up [Layers and summarized positions](Layers-and-summarized-positions.md) | leif | under testing |
| 7 | [Web page for register and update tracker info](Web-page-for-register-and-update-tracker-info.md) |
a. User register/update/Delete tracker - Done with some field on UI. Need added more in developing
b. Make Page list all Tracker - Done
c. make page center
d. make flat html + js
Notes: For register Tracker we had insert new record into openGTS, But not work for update and delete (Need check service)|Thai| under development \\ LHA: comment \\ user must be able to update \\ delete |
| 8 | Make integration and unit tests | Huy/Thai/Leif |  |
| 9 | Document service calls [Service calls](Service-calls.md) | huy/Thai/Leif |  |  |
| 10 | [Test system using mobile phones for tracker](Test-system-using-mobile-phones-for-tracker.md) - Thai Updated document on wiki | huy/Thai/Leif |  |  |
