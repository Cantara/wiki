# Skype team meeting 2015.04.21

### [Skype team meeting 2015.04.21](Skype-team-meeting-2015-04-21.md)

refs: 

- [20.04.2015 - Joomla - First Site Setup](20-04-2015-Joomla-First-Site-Setup.md)
- [Terry and Stig adding droneradar24 comment 20.4.2015](Terry-and-Stig-adding-droneradar24-comment-20-4-2015.md)

**Conclustion:**

- Thai improve web page for trager register and auke js cross domain 
- Huy make integration openGTS -> PollEvent class

- General Issue -> tomcat concurreny -> [drone:Site concurrency and scaling capacities](../drone/Site-concurrency-and-scaling-capacities.md)

```

[03:31:02] Thai Huynh: hmm, I am check now
[03:34:50] Thai Huynh: its seem demo server is stop
[09:55:26] Leif H. Auke: Good day
[09:55:59] Thai Huynh: Good morning :)
[09:56:09] Thai Huynh: how are you today ?
[09:57:14] Duong Thanh Huy: good day
[10:02:59] Leif H. Auke: I am fine. lowly day in norway (cool)
[10:03:14] Leif H. Auke: Are we ready for some status?
[10:03:35] Duong Thanh Huy: yup
[10:04:20] Thai Huynh: yes
[10:05:37] Thai Huynh: I had deploy lastest version into demo server for register /update tracker. make page show list all tracker and allow edit/delete
[10:05:37] Leif H. Auke: Thai?
[10:06:11] Thai Huynh: one issues: Just update json file after update tracker, Not update opentGTS yet. (huy will done soon)
[10:06:36] Thai Huynh: buid new UI for show map
[10:08:08] Leif H. Auke: cool
[10:08:35] Leif H. Auke: I have a comment and Q:
[10:09:08] Thai Huynh: yep, I look
[10:09:15] Leif H. Auke: If I am a user and having a drone tracker. how do I register my tracker?
[10:10:33] Thai Huynh: The first user need go to web page register ?
[10:11:06 | Redigert 10:11:13] Thai Huynh: e.g show form as Name, IMEI,... ?
[10:11:12] Leif H. Auke: Look sprint 2.  I added a "how to register my tracker to site"
[10:11:27] Leif H. Auke: Let's explain in there ?
[10:12:09] Leif H. Auke: Hmm.  yes.
[10:12:56] Leif H. Auke: Thai.  spend 30 minutes figure and explain in wiki page ?
[10:13:13] Thai Huynh: OK, I do now
[10:13:17] Leif H. Auke: Some suggestion. We discuss after..
[10:13:32] Duong Thanh Huy: ok
[10:13:33] Leif H. Auke: huy status?
[10:13:48] Duong Thanh Huy: I've finished the creation for Device table
[10:13:59] Duong Thanh Huy: and getting EventData table
[10:14:06] Duong Thanh Huy: all web services are prepared
[10:14:47] Duong Thanh Huy: written with parameterized so it should be very easy to extend and reuse
[10:15:37] Leif H. Auke: How you get eventdata?
[10:16:12] Duong Thanh Huy: http://89.221.242.66:8888/drone/get-event?accountID=demo&deviceID=demo
[10:16:19] Duong Thanh Huy: if there are no parameters available
[10:16:23] Duong Thanh Huy: then it will get all
[10:16:44] Leif H. Auke: Look "integration with opengts database"
[10:16:46] Duong Thanh Huy: CRUDDaoImplement
[10:16:56] Duong Thanh Huy: this is the integration class
[10:17:02] Duong Thanh Huy: it will read from openGTS
[10:17:19] Leif H. Auke: One moment. I pull code.
[10:17:27] Duong Thanh Huy: ok
[10:21:00] Leif H. Auke: Must turn my pc on
[10:21:35] Leif H. Auke: on PC
[10:21:47] Duong Thanh Huy: ok
[10:21:48] Leif H. Auke: 2 sek
[10:21:49] Duong Thanh Huy: :)
[10:22:40] Leif H. Auke: ok. get event service
[10:23:01] Duong Thanh Huy: yup
[10:24:13] Leif H. Auke: ok. But this only pull off all events for one tracker?
[10:24:35] Leif H. Auke: we need only the current event?
[10:25:22] Duong Thanh Huy: it is very flexible
[10:25:23] Leif H. Auke: https://wiki.cantara.no/display/drone/Integrate+with+openGTS+data
[10:25:34] Duong Thanh Huy: if you want then you can pass a properties
[10:26:49] Leif H. Auke: make a full class for this embedding the crudEventDao
[10:27:05] Leif H. Auke: call the class GetLastPositions (or something)
[10:27:43] Leif H. Auke: and look my select, because this automatically select last position in SQL (much quicker)
[10:27:44] Leif H. Auke: :)
[10:27:56] Duong Thanh Huy: thanks Leif
[10:27:57] Duong Thanh Huy: :)
[10:27:59] Duong Thanh Huy: noted
[10:28:09] Duong Thanh Huy: how about SELECT TOP 10 or TOP 5
[10:28:17] Duong Thanh Huy: then we don't have to base on the time
[10:29:15] Leif H. Auke: not sure, but i think this contruct take case of that?
[10:29:42] Leif H. Auke: WHERE 
 
timestamp >= 
    
   (
       SELECT max(timestamp) - 100
       FROM EventData AS x 
       WHERE x.deviceid = d.deviceid
 
    )
[10:29:58] Leif H. Auke: but this only retrive last postion for all devices
[10:30:21] Duong Thanh Huy: we can also pass accountID and deviceID
[10:30:26] Leif H. Auke: regardless of when it happend
[10:30:38] Leif H. Auke: yes (ofcource)
[10:30:40] Leif H. Auke: no....
[10:30:43] Leif H. Auke: sorry
[10:31:03] Leif H. Auke: just grab all positions and distibute to trackers
[10:31:57] Leif H. Auke: we have a new service thread class -> called PollEvents (or something) with a loop every 10 seconds pulling all latest events from opengts
[10:32:01] Leif H. Auke: follow?
[10:32:13] Duong Thanh Huy: ok
[10:32:42] Duong Thanh Huy: ok
[10:33:34] Duong Thanh Huy: any more ideas?
[10:33:54] Leif H. Auke: to sek
[10:34:35] Leif H. Auke: https://wiki.cantara.no/display/drone/Integrate+with+openGTS+data
[10:34:41] Leif H. Auke: specification :)
[10:34:47] Leif H. Auke: (quick and dirty)
[10:34:51] Leif H. Auke: are you agree ?
[10:35:19] Duong Thanh Huy: I do
[10:35:22] Duong Thanh Huy: :)
[10:35:26] Leif H. Auke: cool :)
[10:35:32] Duong Thanh Huy: just thinking a little bit about the architecture
[10:35:44] Leif H. Auke: yes,
[10:36:01] Duong Thanh Huy: beside this
[10:36:16] Duong Thanh Huy: anymore requirements about writing, reading from DB?
[10:36:40] Duong Thanh Huy: if there is then we should choose something strong so we could move on fast and robust
[10:36:45] Leif H. Auke: but dont be to theoretical about integration. Its a simple select, returning a list. No parameters involved. It do the same every time.
[10:37:09] Duong Thanh Huy: ok, maybe I've overdesigned it
[10:37:17] Leif H. Auke: direct SQL is fastest.
[10:37:19] Leif H. Auke: :)
[10:37:30] Leif H. Auke: no need for a lot of wrapping
[10:37:40] Duong Thanh Huy: ok, agree
[10:37:40] Duong Thanh Huy: :)
[10:37:46] Leif H. Auke: (handshake)
[10:38:04] Duong Thanh Huy: (handshake)
[10:38:17] Leif H. Auke: but CRUDDao look nice for normal table on by one integrations
[10:38:30] Leif H. Auke: (don remove it, work fine for Device updates) :)
[10:38:51] Duong Thanh Huy: thanks, I will refactor. Working on it
[10:38:57] Leif H. Auke: cool
[10:39:22] Thai Huynh: https://wiki.cantara.no/display/drone/How+to+register+my+tracker+to+site
[10:39:26] Leif H. Auke: Make the PollEvent class with a thread
[10:39:31] Thai Huynh: some idea :)
[10:40:06] Leif H. Auke: look nice
[10:40:18] Duong Thanh Huy: will do today, so it is totally transparent
[10:41:09] Leif H. Auke: Thai. Yes. I agree. What will user do to update his tracker info?
[10:41:17] Leif H. Auke: Put on spec...
[10:41:41] Thai Huynh: yep
[10:43:16] Thai Huynh: for now web page on Our Server just work around for demo. Not check permisson. So I will improve
[10:43:37] Thai Huynh: next plan make direction + tail on drone
[10:44:36] Leif H. Auke: we need one single page for user (create/update tracker) maybe better prioritized before direction and tail ?
[10:45:22] Leif H. Auke: And we test this page by register our phones as tracker devices and start tracks posistions. Same time we will test the integration from Huy
[10:45:23] Leif H. Auke: ?
[10:45:48] Leif H. Auke: So, a page for register tracker I think is important to finish up?
[10:45:52] Thai Huynh: OK, I see
[10:45:58] Duong Thanh Huy: ok
[10:46:01] Leif H. Auke: ok
[10:46:06] Thai Huynh: btw, one Q?
[10:46:07] Leif H. Auke: Some status from me
[10:46:16] Leif H. Auke: yepp Q
[10:46:35] Thai Huynh: for single page just flat html ?
[10:46:59] Leif H. Auke: for single page just flat html ?
[10:47:03] Leif H. Auke: Yes?
[10:47:09] Leif H. Auke: (simplest)?
[10:47:51] Thai Huynh: think..
[10:48:03] Leif H. Auke: make a page... User.jsp and we add everything regaring user in there ?
[10:48:55] Thai Huynh: User.jsp >> that mean we will using web context (e.g using tomcat,..)
[10:49:02] Leif H. Auke: yes
[10:49:03] Thai Huynh: then not flat hml :)
[10:49:07] Leif H. Auke: its a part of our site
[10:49:20] Leif H. Auke: ahh. I missunderstood the flat html Q
[10:50:05 | Redigert 10:50:23] Thai Huynh: I think we can make single page flat html and deliver joomla server for user register at here for ex.
[10:50:28] Leif H. Auke: hmm
[10:50:45] Leif H. Auke: but its as easy making a .jsp as it is making a flat html ?
[10:50:46] Thai Huynh: flat html + js
[10:51:04] Leif H. Auke: flat html + jsyes
[10:51:06] Leif H. Auke: agree
[10:51:12] Leif H. Auke: best solution
[10:51:22] Thai Huynh: Okay :)
[10:51:24] Leif H. Auke: then its easy integrate to joomla site
[10:51:33] Leif H. Auke: Some status from me
[10:51:42] Duong Thanh Huy: yes please
[10:51:59] Leif H. Auke: Stig and Terry worked onjoomla site yesterdat
[10:52:01] Leif H. Auke: day
[10:52:10] Leif H. Auke: www.droneradar24.no
[10:52:24] Leif H. Auke: the tried integrate our page with iframe...
[10:52:33] Leif H. Auke: did not work to well
[10:52:51] Leif H. Auke: but integration is started...
[10:53:02] Leif H. Auke: i added some comments fro this here
[10:53:16] Leif H. Auke: https://wiki.cantara.no/display/drone/Terry+and+Stig+adding+droneradar24+comment+20.4.2015
[10:53:33] Leif H. Auke: and Terry added this
[10:53:34] Leif H. Auke: https://wiki.cantara.no/display/drone/20.04.2015+-+Joomla+-+First+Site+Setup
[10:53:40] Leif H. Auke: take a look
[10:54:31] Leif H. Auke: but I think iframe is not to good. They need integrate html, but they got some trouble doing that
[10:56:23] Leif H. Auke: Later maybe Thai help out for the joomla integration
[10:56:50] Thai Huynh: strange..., before I had make joomla folder include html + js (url connect into demo server) and check more
[10:57:09] Thai Huynh: but for now on joomla server not see any drone :(
[10:57:42] Leif H. Auke: Because its uses iframe
[10:57:45] Leif H. Auke: i think
[10:57:58] Thai Huynh: explain ?
[10:58:19] Leif H. Auke: iframe ? -> include whole pages from other sites into a frame
[10:59:29] Leif H. Auke: but this link
[10:59:29] Leif H. Auke: http://www.droneradar24.no/dronemap/demo.html
[10:59:37] Leif H. Auke: should show positions (not iframe)
[11:00:05] Leif H. Auke: some mess with java script putting posistion into map
[11:00:09] Leif H. Auke: ?
[11:00:56 | Redigert 11:01:03] Leif H. Auke: Thai -> why not include java script with full URL to aukeGTS site?
[11:01:17] Leif H. Auke: So they dont need to copy the scripts?
[11:01:33] Thai Huynh: yes, we can
[11:01:37] Leif H. Auke: its better
[11:01:48] Thai Huynh: good idea :x
[11:02:10] Leif H. Auke: yes
[11:02:43] Thai Huynh: one moment
[11:02:49] Leif H. Auke: only distribute the html code nessesary. Rest keep on aukegts site
[11:03:52] Leif H. Auke: one Q from me ?
[11:03:56] Thai Huynh: OKie
[11:04:17] Leif H. Auke: do we run with tomcat on server now?
[11:04:26 | Redigert 11:04:31] Thai Huynh: yes, correct
[11:04:29] Leif H. Auke: ok
[11:04:52] Leif H. Auke: seemed we had som trouble when more than one user used the map
[11:05:57] Leif H. Auke: lets test and make sure multiple requests work. For ex. 10 concurrent position fetch from server at same time
[11:06:27] Leif H. Auke: i.e @Path("/load-drone-in-view/{layerId}/{zoom}") -> at least 10 concurrent calls
[11:06:52 | Redigert 11:07:18] Thai Huynh: call every user zoom or drag map
[11:07:02] Leif H. Auke: ?
[11:07:40] Thai Huynh: this method will call when user zoom or drag map
[11:07:46] Leif H. Auke: i know
[11:08:18] Leif H. Auke: but server should handle at least 10 conncurrent calls at same time (diffrent users look at the map)
[11:08:37] Leif H. Auke: follow?
[11:08:37] Duong Thanh Huy: tks
[11:09:00 | Redigert 11:09:08] Thai Huynh: make some thread for process for ex. 10 ?
[11:09:12] Leif H. Auke: no, tomcat handle?
[11:09:32] Thai Huynh: ok, maybe realate to config in tomcat
[11:09:35 | Redigert 11:09:48] Leif H. Auke: tomcat should handle the concurrecy?
[11:09:48] Thai Huynh: yes, let me check this issues
[11:09:52] Leif H. Auke: yep
[11:10:02] Thai Huynh: http://stackoverflow.com/questions/18372464/how-many-concurrent-request-can-tomcat-handle-by-default
[11:10:15] Thai Huynh: :)
[11:10:21] Leif H. Auke: make a test. Open 10 browesers and lett each broverser pull every second
[11:10:51] Leif H. Auke: yepp -> you look into :)
[11:11:04] Thai Huynh: Yep, One more issues I see when using flat html + js >> issues cross domain
[11:11:24] Leif H. Auke: hmm. Explain?
[11:12:40] Thai Huynh: by default we can not send request direct into server from  out site for e.g in js file we can ajax.send(url)
[11:13:25] Thai Huynh: some explain at here
[11:13:26] Thai Huynh: http://www.d-mueller.de/blog/cross-domain-ajax-guide/
[11:13:31] Thai Huynh: I also tried
[11:14:22 | Redigert 11:14:29] Thai Huynh: issues relate to security on per browser
[11:14:28] Leif H. Auke: hmm
[11:15:11] Leif H. Auke: How does facebook or other sites handle this. (I think they sometimes work cross domain ???
[11:15:45 | Redigert 11:15:57] Thai Huynh: b/c facebook using api key for send requst (i think )
[11:15:52 | Redigert 11:16:24] Leif H. Auke: if we are going to store to site aukegts from jommla droneradar site, we need cross domain handling ?
[11:16:16] Thai Huynh: yes,
[11:16:35] Thai Huynh: and I had add filter class cross domain on aukegts
[11:16:35] Leif H. Auke: we must figure out.....
[11:17:08] Leif H. Auke: ahh. This is not my irst line of expertise
[11:17:10] Thai Huynh: look CrossDomainFilter.java
[11:17:17] Leif H. Auke: but we need cross domain for sure....
[11:17:38] Thai Huynh: yes, current CrossDomainFilter >> work as expect
[11:17:51] Thai Huynh: but not good
[11:18:01 | Redigert 11:18:09] Thai Huynh: if hacker make loop on client site and send reqeust forever
[11:18:18] Leif H. Auke: so site droneradar24.no can send data with ajax.send(aukegts)
[11:18:21 | Fjernet 11:18:31] Thai Huynh: Denne meldingen er blitt fjernet.
[11:18:34] Leif H. Auke: :)
[11:18:44] Leif H. Auke: tackle this problem later :)
[11:19:10] Leif H. Auke: make a IP source address filter
[11:19:20] Leif H. Auke: block to many request from same IP address.
[11:20:00] Thai Huynh: ok, tackle this problems later (but we need notes this issues )
[11:20:53] Leif H. Auke: yep
[11:21:10] Leif H. Auke: ok. I must leave...
[11:21:17] Leif H. Auke: thank for meeting :)
[11:21:23] Leif H. Auke: (y)
[11:21:28] Thai Huynh: ok, Summray my taks for today, 

1. improve web page 
2. include full url with js on aukegts
[11:21:30] Leif H. Auke: good job so far. keep up
[11:21:40] Leif H. Auke: yepp
[11:21:54] Thai Huynh: thanks :) and you too
[11:22:20] Leif H. Auke: look this -> I start made a page for scaling
[11:22:21] Leif H. Auke: https://wiki.cantara.no/display/drone/Site+concurrency+and+scaling+capacities
[11:22:29] Leif H. Auke: just not to forget the issue
[11:22:36] Thai Huynh: (y)

```

**Conclustion:**

- Thai improve web page for trager register and auke js cross domain 
- Huy make integration openGTS -> PollEvent class

- General Issue -> tomcat concurreny -> [drone:Site concurrency and scaling capacities](../drone/Site-concurrency-and-scaling-capacities.md)

```

[03:31:02] Thai Huynh: hmm, I am check now
[03:34:50] Thai Huynh: its seem demo server is stop
[09:55:26] Leif H. Auke: Good day
[09:55:59] Thai Huynh: Good morning :)
[09:56:09] Thai Huynh: how are you today ?
[09:57:14] Duong Thanh Huy: good day
[10:02:59] Leif H. Auke: I am fine. lowly day in norway (cool)
[10:03:14] Leif H. Auke: Are we ready for some status?
[10:03:35] Duong Thanh Huy: yup
[10:04:20] Thai Huynh: yes
[10:05:37] Thai Huynh: I had deploy lastest version into demo server for register /update tracker. make page show list all tracker and allow edit/delete
[10:05:37] Leif H. Auke: Thai?
[10:06:11] Thai Huynh: one issues: Just update json file after update tracker, Not update opentGTS yet. (huy will done soon)
[10:06:36] Thai Huynh: buid new UI for show map
[10:08:08] Leif H. Auke: cool
[10:08:35] Leif H. Auke: I have a comment and Q:
[10:09:08] Thai Huynh: yep, I look
[10:09:15] Leif H. Auke: If I am a user and having a drone tracker. how do I register my tracker?
[10:10:33] Thai Huynh: The first user need go to web page register ?
[10:11:06 | Redigert 10:11:13] Thai Huynh: e.g show form as Name, IMEI,... ?
[10:11:12] Leif H. Auke: Look sprint 2.  I added a "how to register my tracker to site"
[10:11:27] Leif H. Auke: Let's explain in there ?
[10:12:09] Leif H. Auke: Hmm.  yes.
[10:12:56] Leif H. Auke: Thai.  spend 30 minutes figure and explain in wiki page ?
[10:13:13] Thai Huynh: OK, I do now
[10:13:17] Leif H. Auke: Some suggestion. We discuss after..
[10:13:32] Duong Thanh Huy: ok
[10:13:33] Leif H. Auke: huy status?
[10:13:48] Duong Thanh Huy: I've finished the creation for Device table
[10:13:59] Duong Thanh Huy: and getting EventData table
[10:14:06] Duong Thanh Huy: all web services are prepared
[10:14:47] Duong Thanh Huy: written with parameterized so it should be very easy to extend and reuse
[10:15:37] Leif H. Auke: How you get eventdata?
[10:16:12] Duong Thanh Huy: http://89.221.242.66:8888/drone/get-event?accountID=demo&deviceID=demo
[10:16:19] Duong Thanh Huy: if there are no parameters available
[10:16:23] Duong Thanh Huy: then it will get all
[10:16:44] Leif H. Auke: Look "integration with opengts database"
[10:16:46] Duong Thanh Huy: CRUDDaoImplement
[10:16:56] Duong Thanh Huy: this is the integration class
[10:17:02] Duong Thanh Huy: it will read from openGTS
[10:17:19] Leif H. Auke: One moment. I pull code.
[10:17:27] Duong Thanh Huy: ok
[10:21:00] Leif H. Auke: Must turn my pc on
[10:21:35] Leif H. Auke: on PC
[10:21:47] Duong Thanh Huy: ok
[10:21:48] Leif H. Auke: 2 sek
[10:21:49] Duong Thanh Huy: :)
[10:22:40] Leif H. Auke: ok. get event service
[10:23:01] Duong Thanh Huy: yup
[10:24:13] Leif H. Auke: ok. But this only pull off all events for one tracker?
[10:24:35] Leif H. Auke: we need only the current event?
[10:25:22] Duong Thanh Huy: it is very flexible
[10:25:23] Leif H. Auke: https://wiki.cantara.no/display/drone/Integrate+with+openGTS+data
[10:25:34] Duong Thanh Huy: if you want then you can pass a properties
[10:26:49] Leif H. Auke: make a full class for this embedding the crudEventDao
[10:27:05] Leif H. Auke: call the class GetLastPositions (or something)
[10:27:43] Leif H. Auke: and look my select, because this automatically select last position in SQL (much quicker)
[10:27:44] Leif H. Auke: :)
[10:27:56] Duong Thanh Huy: thanks Leif
[10:27:57] Duong Thanh Huy: :)
[10:27:59] Duong Thanh Huy: noted
[10:28:09] Duong Thanh Huy: how about SELECT TOP 10 or TOP 5
[10:28:17] Duong Thanh Huy: then we don't have to base on the time
[10:29:15] Leif H. Auke: not sure, but i think this contruct take case of that?
[10:29:42] Leif H. Auke: WHERE 
 
timestamp >= 
    
   (
       SELECT max(timestamp) - 100
       FROM EventData AS x 
       WHERE x.deviceid = d.deviceid
 
    )
[10:29:58] Leif H. Auke: but this only retrive last postion for all devices
[10:30:21] Duong Thanh Huy: we can also pass accountID and deviceID
[10:30:26] Leif H. Auke: regardless of when it happend
[10:30:38] Leif H. Auke: yes (ofcource)
[10:30:40] Leif H. Auke: no....
[10:30:43] Leif H. Auke: sorry
[10:31:03] Leif H. Auke: just grab all positions and distibute to trackers
[10:31:57] Leif H. Auke: we have a new service thread class -> called PollEvents (or something) with a loop every 10 seconds pulling all latest events from opengts
[10:32:01] Leif H. Auke: follow?
[10:32:13] Duong Thanh Huy: ok
[10:32:42] Duong Thanh Huy: ok
[10:33:34] Duong Thanh Huy: any more ideas?
[10:33:54] Leif H. Auke: to sek
[10:34:35] Leif H. Auke: https://wiki.cantara.no/display/drone/Integrate+with+openGTS+data
[10:34:41] Leif H. Auke: specification :)
[10:34:47] Leif H. Auke: (quick and dirty)
[10:34:51] Leif H. Auke: are you agree ?
[10:35:19] Duong Thanh Huy: I do
[10:35:22] Duong Thanh Huy: :)
[10:35:26] Leif H. Auke: cool :)
[10:35:32] Duong Thanh Huy: just thinking a little bit about the architecture
[10:35:44] Leif H. Auke: yes,
[10:36:01] Duong Thanh Huy: beside this
[10:36:16] Duong Thanh Huy: anymore requirements about writing, reading from DB?
[10:36:40] Duong Thanh Huy: if there is then we should choose something strong so we could move on fast and robust
[10:36:45] Leif H. Auke: but dont be to theoretical about integration. Its a simple select, returning a list. No parameters involved. It do the same every time.
[10:37:09] Duong Thanh Huy: ok, maybe I've overdesigned it
[10:37:17] Leif H. Auke: direct SQL is fastest.
[10:37:19] Leif H. Auke: :)
[10:37:30] Leif H. Auke: no need for a lot of wrapping
[10:37:40] Duong Thanh Huy: ok, agree
[10:37:40] Duong Thanh Huy: :)
[10:37:46] Leif H. Auke: (handshake)
[10:38:04] Duong Thanh Huy: (handshake)
[10:38:17] Leif H. Auke: but CRUDDao look nice for normal table on by one integrations
[10:38:30] Leif H. Auke: (don remove it, work fine for Device updates) :)
[10:38:51] Duong Thanh Huy: thanks, I will refactor. Working on it
[10:38:57] Leif H. Auke: cool
[10:39:22] Thai Huynh: https://wiki.cantara.no/display/drone/How+to+register+my+tracker+to+site
[10:39:26] Leif H. Auke: Make the PollEvent class with a thread
[10:39:31] Thai Huynh: some idea :)
[10:40:06] Leif H. Auke: look nice
[10:40:18] Duong Thanh Huy: will do today, so it is totally transparent
[10:41:09] Leif H. Auke: Thai. Yes. I agree. What will user do to update his tracker info?
[10:41:17] Leif H. Auke: Put on spec...
[10:41:41] Thai Huynh: yep
[10:43:16] Thai Huynh: for now web page on Our Server just work around for demo. Not check permisson. So I will improve
[10:43:37] Thai Huynh: next plan make direction + tail on drone
[10:44:36] Leif H. Auke: we need one single page for user (create/update tracker) maybe better prioritized before direction and tail ?
[10:45:22] Leif H. Auke: And we test this page by register our phones as tracker devices and start tracks posistions. Same time we will test the integration from Huy
[10:45:23] Leif H. Auke: ?
[10:45:48] Leif H. Auke: So, a page for register tracker I think is important to finish up?
[10:45:52] Thai Huynh: OK, I see
[10:45:58] Duong Thanh Huy: ok
[10:46:01] Leif H. Auke: ok
[10:46:06] Thai Huynh: btw, one Q?
[10:46:07] Leif H. Auke: Some status from me
[10:46:16] Leif H. Auke: yepp Q
[10:46:35] Thai Huynh: for single page just flat html ?
[10:46:59] Leif H. Auke: for single page just flat html ?
[10:47:03] Leif H. Auke: Yes?
[10:47:09] Leif H. Auke: (simplest)?
[10:47:51] Thai Huynh: think..
[10:48:03] Leif H. Auke: make a page... User.jsp and we add everything regaring user in there ?
[10:48:55] Thai Huynh: User.jsp >> that mean we will using web context (e.g using tomcat,..)
[10:49:02] Leif H. Auke: yes
[10:49:03] Thai Huynh: then not flat hml :)
[10:49:07] Leif H. Auke: its a part of our site
[10:49:20] Leif H. Auke: ahh. I missunderstood the flat html Q
[10:50:05 | Redigert 10:50:23] Thai Huynh: I think we can make single page flat html and deliver joomla server for user register at here for ex.
[10:50:28] Leif H. Auke: hmm
[10:50:45] Leif H. Auke: but its as easy making a .jsp as it is making a flat html ?
[10:50:46] Thai Huynh: flat html + js
[10:51:04] Leif H. Auke: flat html + jsyes
[10:51:06] Leif H. Auke: agree
[10:51:12] Leif H. Auke: best solution
[10:51:22] Thai Huynh: Okay :)
[10:51:24] Leif H. Auke: then its easy integrate to joomla site
[10:51:33] Leif H. Auke: Some status from me
[10:51:42] Duong Thanh Huy: yes please
[10:51:59] Leif H. Auke: Stig and Terry worked onjoomla site yesterdat
[10:52:01] Leif H. Auke: day
[10:52:10] Leif H. Auke: www.droneradar24.no
[10:52:24] Leif H. Auke: the tried integrate our page with iframe...
[10:52:33] Leif H. Auke: did not work to well
[10:52:51] Leif H. Auke: but integration is started...
[10:53:02] Leif H. Auke: i added some comments fro this here
[10:53:16] Leif H. Auke: https://wiki.cantara.no/display/drone/Terry+and+Stig+adding+droneradar24+comment+20.4.2015
[10:53:33] Leif H. Auke: and Terry added this
[10:53:34] Leif H. Auke: https://wiki.cantara.no/display/drone/20.04.2015+-+Joomla+-+First+Site+Setup
[10:53:40] Leif H. Auke: take a look
[10:54:31] Leif H. Auke: but I think iframe is not to good. They need integrate html, but they got some trouble doing that
[10:56:23] Leif H. Auke: Later maybe Thai help out for the joomla integration
[10:56:50] Thai Huynh: strange..., before I had make joomla folder include html + js (url connect into demo server) and check more
[10:57:09] Thai Huynh: but for now on joomla server not see any drone :(
[10:57:42] Leif H. Auke: Because its uses iframe
[10:57:45] Leif H. Auke: i think
[10:57:58] Thai Huynh: explain ?
[10:58:19] Leif H. Auke: iframe ? -> include whole pages from other sites into a frame
[10:59:29] Leif H. Auke: but this link
[10:59:29] Leif H. Auke: http://www.droneradar24.no/dronemap/demo.html
[10:59:37] Leif H. Auke: should show positions (not iframe)
[11:00:05] Leif H. Auke: some mess with java script putting posistion into map
[11:00:09] Leif H. Auke: ?
[11:00:56 | Redigert 11:01:03] Leif H. Auke: Thai -> why not include java script with full URL to aukeGTS site?
[11:01:17] Leif H. Auke: So they dont need to copy the scripts?
[11:01:33] Thai Huynh: yes, we can
[11:01:37] Leif H. Auke: its better
[11:01:48] Thai Huynh: good idea :x
[11:02:10] Leif H. Auke: yes
[11:02:43] Thai Huynh: one moment
[11:02:49] Leif H. Auke: only distribute the html code nessesary. Rest keep on aukegts site
[11:03:52] Leif H. Auke: one Q from me ?
[11:03:56] Thai Huynh: OKie
[11:04:17] Leif H. Auke: do we run with tomcat on server now?
[11:04:26 | Redigert 11:04:31] Thai Huynh: yes, correct
[11:04:29] Leif H. Auke: ok
[11:04:52] Leif H. Auke: seemed we had som trouble when more than one user used the map
[11:05:57] Leif H. Auke: lets test and make sure multiple requests work. For ex. 10 concurrent position fetch from server at same time
[11:06:27] Leif H. Auke: i.e @Path("/load-drone-in-view/{layerId}/{zoom}") -> at least 10 concurrent calls
[11:06:52 | Redigert 11:07:18] Thai Huynh: call every user zoom or drag map
[11:07:02] Leif H. Auke: ?
[11:07:40] Thai Huynh: this method will call when user zoom or drag map
[11:07:46] Leif H. Auke: i know
[11:08:18] Leif H. Auke: but server should handle at least 10 conncurrent calls at same time (diffrent users look at the map)
[11:08:37] Leif H. Auke: follow?
[11:08:37] Duong Thanh Huy: tks
[11:09:00 | Redigert 11:09:08] Thai Huynh: make some thread for process for ex. 10 ?
[11:09:12] Leif H. Auke: no, tomcat handle?
[11:09:32] Thai Huynh: ok, maybe realate to config in tomcat
[11:09:35 | Redigert 11:09:48] Leif H. Auke: tomcat should handle the concurrecy?
[11:09:48] Thai Huynh: yes, let me check this issues
[11:09:52] Leif H. Auke: yep
[11:10:02] Thai Huynh: http://stackoverflow.com/questions/18372464/how-many-concurrent-request-can-tomcat-handle-by-default
[11:10:15] Thai Huynh: :)
[11:10:21] Leif H. Auke: make a test. Open 10 browesers and lett each broverser pull every second
[11:10:51] Leif H. Auke: yepp -> you look into :)
[11:11:04] Thai Huynh: Yep, One more issues I see when using flat html + js >> issues cross domain
[11:11:24] Leif H. Auke: hmm. Explain?
[11:12:40] Thai Huynh: by default we can not send request direct into server from  out site for e.g in js file we can ajax.send(url)
[11:13:25] Thai Huynh: some explain at here
[11:13:26] Thai Huynh: http://www.d-mueller.de/blog/cross-domain-ajax-guide/
[11:13:31] Thai Huynh: I also tried
[11:14:22 | Redigert 11:14:29] Thai Huynh: issues relate to security on per browser
[11:14:28] Leif H. Auke: hmm
[11:15:11] Leif H. Auke: How does facebook or other sites handle this. (I think they sometimes work cross domain ???
[11:15:45 | Redigert 11:15:57] Thai Huynh: b/c facebook using api key for send requst (i think )
[11:15:52 | Redigert 11:16:24] Leif H. Auke: if we are going to store to site aukegts from jommla droneradar site, we need cross domain handling ?
[11:16:16] Thai Huynh: yes,
[11:16:35] Thai Huynh: and I had add filter class cross domain on aukegts
[11:16:35] Leif H. Auke: we must figure out.....
[11:17:08] Leif H. Auke: ahh. This is not my irst line of expertise
[11:17:10] Thai Huynh: look CrossDomainFilter.java
[11:17:17] Leif H. Auke: but we need cross domain for sure....
[11:17:38] Thai Huynh: yes, current CrossDomainFilter >> work as expect
[11:17:51] Thai Huynh: but not good
[11:18:01 | Redigert 11:18:09] Thai Huynh: if hacker make loop on client site and send reqeust forever
[11:18:18] Leif H. Auke: so site droneradar24.no can send data with ajax.send(aukegts)
[11:18:21 | Fjernet 11:18:31] Thai Huynh: Denne meldingen er blitt fjernet.
[11:18:34] Leif H. Auke: :)
[11:18:44] Leif H. Auke: tackle this problem later :)
[11:19:10] Leif H. Auke: make a IP source address filter
[11:19:20] Leif H. Auke: block to many request from same IP address.
[11:20:00] Thai Huynh: ok, tackle this problems later (but we need notes this issues )
[11:20:53] Leif H. Auke: yep
[11:21:10] Leif H. Auke: ok. I must leave...
[11:21:17] Leif H. Auke: thank for meeting :)
[11:21:23] Leif H. Auke: (y)
[11:21:28] Thai Huynh: ok, Summray my taks for today, 

1. improve web page 
2. include full url with js on aukegts
[11:21:30] Leif H. Auke: good job so far. keep up
[11:21:40] Leif H. Auke: yepp
[11:21:54] Thai Huynh: thanks :) and you too
[11:22:20] Leif H. Auke: look this -> I start made a page for scaling
[11:22:21] Leif H. Auke: https://wiki.cantara.no/display/drone/Site+concurrency+and+scaling+capacities
[11:22:29] Leif H. Auke: just not to forget the issue
[11:22:36] Thai Huynh: (y)

```
