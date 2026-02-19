# Skype team meeting 2015.04.17

```

good morning
[10:30:19] Thai Huynh: Good morning
[10:30:46] Thai Huynh: how are you today ?
[10:30:48] Leif H. Auke: how is life?
[10:30:55] Leif H. Auke: very fine
[10:30:58] Thai Huynh: I am fine, :) thanks
[10:31:09] Duong Thanh Huy: I'm ok
[10:31:28] Leif H. Auke: one week into sprint 2
[10:31:43] Thai Huynh: I am going  make web page and play around direction on google API
[10:31:44] Leif H. Auke: shall we make a quick status?
[10:31:50] Duong Thanh Huy: yup
[10:31:52] Thai Huynh: Yep
[10:32:14] Leif H. Auke: Thai tasks first ?
[10:32:43] Leif H. Auke: Add direction show on Map  
Making a "tail" for moving
[10:32:46] Thai Huynh: I am going make web page show list tracker.
[10:32:53] Leif H. Auke:   Web page for register and update tracker info
[10:33:13] Leif H. Auke: task says page for register
[10:33:56] Thai Huynh: for 'tail' I am in-process.
[10:34:18 | Redigert 10:34:33] Thai Huynh: I want to init web page for integrate this tail + direction when user click view tracker
[10:35:19] Thai Huynh: my summary

1. make web page
2, show all tracker
3, click per tracker
4, user can start/stop > show tail + direction
[10:35:42] Leif H. Auke: thats whats done for now ?
[10:36:11 | Redigert 10:36:16] Thai Huynh: web page + show all tracker in grid
[10:36:59] Thai Huynh: I will commit all in today, need check before
[10:37:16] Leif H. Auke: what about tasks on Spt
[10:37:23] Leif H. Auke: Sprint 2 ?
[10:37:40] Thai Huynh: yes, these task work for sprint 2
[10:38:06] Leif H. Auke:  Web page for register and update tracker info?
[10:38:40] Thai Huynh: its ready done,
[10:38:49] Thai Huynh: but just some field on UI
[10:39:16] Leif H. Auke: no service update ?
[10:39:31 | Redigert 10:39:44] Thai Huynh: included for call service update,..
[10:39:54] Leif H. Auke: ok -> put in here how we can test
[10:39:59] Leif H. Auke: https://wiki.cantara.no/display/drone/Web+page+for+register+and+update+tracker+info
[10:40:23] Leif H. Auke: This is requirements form tail ->
[10:40:38] Leif H. Auke: https://wiki.cantara.no/pages/viewpage.action?pageId=41878194
[10:41:09] Leif H. Auke: Add map to joomla site -> finish ?
[10:41:09] Leif H. Auke: Add map to joomla site -
[10:41:21] Thai Huynh: joomla site finished long time ago
[10:41:38] Thai Huynh: i had make joomla folder in git
[10:41:48] Thai Huynh: just pull and click demo.html
[10:41:52] Leif H. Auke: ok
[10:41:53] Thai Huynh: all flat html
[10:42:02] Leif H. Auke: yepp, i seen it
[10:42:30] Leif H. Auke: ok. I think priority -> finish up so we can test tracker register and update
[10:42:38] Leif H. Auke: most important
[10:42:50] Leif H. Auke: next is tail on map (not that important)
[10:43:17] Leif H. Auke: then   Document service calls Service calls
[10:43:29] Leif H. Auke: https://wiki.cantara.no/display/drone/Service+calls
[10:43:36] Thai Huynh: Ok, My plan is commit all in todays for register/update
[10:43:48] Leif H. Auke: ok
[10:43:54] Leif H. Auke: Huy ?
[10:43:56] Thai Huynh: yep, and will update services on wiki
[10:44:15] Duong Thanh Huy: I've finished the web service for making tails
[10:44:18] Duong Thanh Huy: finished up the layers
[10:44:42] Duong Thanh Huy: installed openGTS locally and working on inserting and getting information to Device and EventData tables
[10:44:55] Leif H. Auke: good
[10:45:08] Duong Thanh Huy: this should not be too complicated, will intend to finish on Monday
[10:45:17] Duong Thanh Huy: and take time for making tests and test cases
[10:45:23] Leif H. Auke: Did you grab the idea about openGTS ?
[10:45:31] Leif H. Auke: why we use it ?
[10:45:49] Duong Thanh Huy: yes, quite, but I'm still reading the document
[10:45:56] Leif H. Auke: yep
[10:46:01] Duong Thanh Huy: still don't know the mechanism how it could fetch the data from real drones
[10:46:17] Leif H. Auke: important spend some time understanding the overall purpose
[10:46:17] Duong Thanh Huy: is that something we have to handle, or openGTS will take care?
[10:46:34] Leif H. Auke: One moment
[10:47:04] Leif H. Auke: --- > we finish status -> when finish today -> you both update status on wiki page
[10:47:20] Duong Thanh Huy: ok
[10:47:23] Thai Huynh: Yep
[10:48:03] Leif H. Auke: good -> could we we have system operational for new testing (with what we have) on monday?
[10:49:05] Leif H. Auke: Huy/Thai -> lets spend 10 minutes on openGTS versus AukeGTS design
[10:49:21] Leif H. Auke: Huy -> this is how it all work (I will also add it to wiki)
[10:49:41] Leif H. Auke: 1. A GPS tracker is monted on the drone
[10:50:28 | Redigert 10:52:10] Leif H. Auke: 2. tracker send data to our server via internett (mobile phone network) as UDP packets to our server
[10:51:23] Leif H. Auke: 3. On our server we have service in openGTS reading UDP packets with position data and store to openGTS eventdata table
[10:51:45] Leif H. Auke: 4. AukeGTS poll Eventdata table for last posistions
[10:51:57] Leif H. Auke: follow ?
[10:52:04] Duong Thanh Huy: follow
[10:52:17] Thai Huynh: yes, I had
[10:52:53] Leif H. Auke: reason for needing Device table in openGTS is because this services in opne GTS use it when read and strore
[10:53:36] Leif H. Auke: this code
[10:53:37] Leif H. Auke: https://github.com/openGtsD/OpenGTS_2.5.8/tree/master/src/org/opengts/servers
[10:53:50] Thai Huynh: Since we need using service in openGTS so we must be need Device table for the same
[10:54:23] Leif H. Auke: shows the openGTS implementation of different position store service for different tracker types supported
[10:54:28] Leif H. Auke: follow?
[10:54:51] Duong Thanh Huy: not yet on this one
[10:55:10 | Redigert 10:55:23] Thai Huynh: Its agent for process data ? (e.g send from mobile...)
[10:55:18] Leif H. Auke: yes
[10:55:37] Leif H. Auke: lets call it tracker position agents
[10:56:05] Leif H. Auke: huy ->
[10:56:25] Leif H. Auke: tracker -> interernett -> opengts agent -> eventdata
[10:57:00] Leif H. Auke: dont bother about how. Its IP/UDP packets
[10:57:25] Leif H. Auke: tracker have a sim card and a mobile nettwork subscription
[10:57:31] Duong Thanh Huy: ok
[10:57:31] Leif H. Auke: follow?
[10:57:40] Duong Thanh Huy: until now yes
[10:57:47] Leif H. Auke: good
[10:57:50] Leif H. Auke: ok
[10:58:10] Leif H. Auke: (study the openGTS code, its pretty obvious actually)
[10:58:12] Leif H. Auke: :)
[10:58:22] Duong Thanh Huy: thanks, I am
[10:58:43] Leif H. Auke: https://github.com/openGtsD/OpenGTS_2.5.8/blob/master/src/org/opengts/servers/aspicore/TrackClientPacketHandler.java
[10:58:48] Leif H. Auke: this one for ex.
[10:59:07] Leif H. Auke: How data comes from tracker and it prosessed and store to openGTS database
[10:59:42] Duong Thanh Huy: so, for my understanding: 
Tracker -> register on AukeGTS -> insert to AukeGTS JSON and OpenGTS Device table
[11:00:01] Leif H. Auke: yep
[11:00:12] Leif H. Auke: 100% correct
[11:00:26] Duong Thanh Huy: Our Map <-  AukeGTS core processing <- OpenGTS EventData table
[11:00:41] Leif H. Auke: 100% correct
[11:01:01] Duong Thanh Huy: and Tracker -> OpenGTS EventData table
[11:01:03] Duong Thanh Huy: ?
[11:01:10] Leif H. Auke: yes
[11:01:16] Duong Thanh Huy: thanks, everything clear
[11:01:17] Duong Thanh Huy: :)
[11:01:36] Leif H. Auke: (but only physical trackers, not simulated) (think)
[11:01:48] Leif H. Auke: cool
[11:01:52] Duong Thanh Huy: ok physical ones
[11:02:00] Leif H. Auke: Ok, guy, we talk on monday
[11:02:08] Duong Thanh Huy: thanks Leif, have a nice weekend
[11:02:18] Leif H. Auke: same to you both
[11:02:26] Thai Huynh: btw, i think we maybe have some demo for update/registe in my case :)
[11:02:28] Thai Huynh: thanks

```
