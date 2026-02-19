# Skype start sprint meeting 2015.4.13

```

[00:58:50] Thai Huynh: Hi leif
[01:04:44] Thai Huynh: Are you stilling working ?
[01:14:51] Leif H. Auke: no :)
[01:15:05] Leif H. Auke: going to be now
[01:15:49] Leif H. Auke: talk tomorrow morning (my time)
[09:14:21] Thai Huynh: Good morning
[09:24:07 | Redigert 09:24:21] Thai Huynh: About retrieve data from openGTS we can use to Events class in openGTS (this is HttpServlet) and customize this servlet (e.g add more API )

for example  we can get track for device (thaimobile) by url
http://89.221.242.66:8080/events/data.json?a=demo&u=thaitest&p=thaitest123&d=thaimobile
[09:43:00] Leif H. Auke: good morning
[09:44:42] Duong Thanh Huy: morning
[09:44:56] Leif H. Auke: how is everything
[09:45:02] Leif H. Auke: ?
[09:45:38] Thai Huynh: I am fine
[09:46:52] Leif H. Auke: Ok. let us start meeting for sprint 2 preparation, but first lets discuss status.
[09:47:09] Thai Huynh: yep
[09:47:20] Leif H. Auke: is everything commited?
[09:47:49] Duong Thanh Huy: not yet, I'm writing several test cases
[09:48:19] Duong Thanh Huy: will commit very soon
[09:48:44] Leif H. Auke: okay
[09:48:49] Leif H. Auke: but rest is commited ?
[09:49:03] Duong Thanh Huy: yup
[09:49:09] Leif H. Auke: good
[09:49:16] Thai Huynh: btw, the last weeks I had look structure opentGTS and test some service for retrieve data also how to customize
[09:49:43 | Redigert 09:49:53] Thai Huynh: I will notes on wiki in today
[09:50:07] Leif H. Auke: okay
[09:50:48 | Redigert 09:50:58] Thai Huynh: have you try inspect my sql on openGTS ?
[09:50:58] Leif H. Auke: I did to yesterday, with focus on direct look up in database ?
[09:50:59] Leif H. Auke: https://wiki.cantara.no/display/drone/Integrate+with+openGTS+data
[09:51:26] Leif H. Auke: but first, lets summaraize sprint 1
[09:52:30] Leif H. Auke: 1. We manage to make a map and draw positions, zoom in/out and show position is view pluss adding layers -> very good
[09:53:00] Leif H. Auke: 2. We manage to make the core service with drone simulations, and service calls -> very good
[09:53:26] Leif H. Auke: 3. We installed openGTS and inspect the database -> good
[09:54:15 | Redigert 09:54:27] Leif H. Auke: 4. we did not manage to test live feed from physical trackers with open GTS -> this must be moved to sprint 2
[09:54:35] Leif H. Auke: are you agree ?
[09:54:42] Duong Thanh Huy: (y)
[09:55:28] Thai Huynh: yep
[09:55:44] Leif H. Auke: very good
[09:56:04] Leif H. Auke: do you have som ideas of overall objectives for sprint 2
[09:56:36 | Redigert 09:57:01] Thai Huynh: I think shuold be add direction show on Map and get data real time from open GTS
[09:56:37] Duong Thanh Huy: how about making a "tail" for moving?
[09:57:31] Leif H. Auke: finish up layser and summarized posistions ?
[09:57:45] Leif H. Auke: add web page for register trackers?
[09:57:58] Leif H. Auke: 2 sek
[10:01:28] Leif H. Auke: look this
[10:01:38] Leif H. Auke: https://wiki.cantara.no/display/drone/Sprint+2
[10:03:48] Leif H. Auke: (refresh page)
[10:04:06] Leif H. Auke: more ideas ?
[10:04:53] Duong Thanh Huy: how long it will last?
[10:05:03] Thai Huynh: started 13.4.2015 - finish 25.4.2015
[10:05:11] Leif H. Auke: 2 weeks
[10:05:45] Thai Huynh: its seem pkt 3 and 4 duplicate ?  get data real time from open GTS == Retrive current posistions from openGTS to AukeGTS
[10:06:23] Leif H. Auke: hm, 2 sec
[10:07:23] Leif H. Auke: ahh. yes
[10:11:18] Leif H. Auke: look again https://wiki.cantara.no/display/drone/Sprint+2
[10:11:32] Leif H. Auke: is it to mush for 2 weeks ?
[10:12:07] Duong Thanh Huy: don't know yet. Maybe we will figure out during the way
[10:12:08] Duong Thanh Huy: :)
[10:13:41] Leif H. Auke: is there any other idea or details we should add not to forget?
[10:14:04] Thai Huynh: thinking...
[10:15:58] Duong Thanh Huy: about the website
[10:16:05] Duong Thanh Huy: do we have to define how many fields we need
[10:16:48] Leif H. Auke: yes, i think so
[10:17:26] Thai Huynh: maybe we make simple page for e.x show list tracker in grid and click per drone for edit/delete
[10:18:26] Duong Thanh Huy: should we make a database for such information?
[10:19:18] Leif H. Auke: -> we store tracker info as json files, but -> we must also update the device table in open GTS to be able to retrive posistions via openGTS
[10:19:57] Leif H. Auke: si i think aukeGTS store tracker as json files, but we just add same infor to openGTS table when storing.
[10:20:16] Leif H. Auke: ?
[10:20:31] Leif H. Auke: because we try to make aukeGTS independent from openGTS
[10:20:54] Duong Thanh Huy: that's a better approach. Then we could have more freedom
[10:20:59] Leif H. Auke: yep
[10:24:00] Leif H. Auke: look
[10:24:01] Leif H. Auke: https://wiki.cantara.no/display/drone/Web+page+for+register+and+update+tracker+info
[10:24:57] Leif H. Auke: overall: If we meet this objectives in 14 days work we do a good sprint :)
[10:25:50] Duong Thanh Huy: yup, just a little bit skeptical about OpenGTS. Don't know if it is easy to use
[10:26:50] Leif H. Auke: we do not use it directly
[10:27:06] Leif H. Auke: we just borrow the tracker feed services
[10:28:23 | Redigert 10:28:47] Leif H. Auke: the tracker must be registred in a table called Device and tracker posisitons are stored in a table called EventData, so we access the daabase of openGTS directly (without using any openGTS code)
[10:28:56] Duong Thanh Huy: oh really, so we have to make an Data Access Layer for such DB?
[10:29:14] Duong Thanh Huy: could we use JPA based on existing DB?
[10:29:32] Leif H. Auke: JPA ?
[10:29:46] Thai Huynh: Java Persistence API :)
[10:30:00] Leif H. Auke: ahh
[10:30:02] Leif H. Auke: :)
[10:30:28] Leif H. Auke: I think sometime java over designed the DB interface
[10:30:40] Duong Thanh Huy: it's the fastest and simplest way to make such queries
[10:30:49] Leif H. Auke: we only need to do one query -> just mock out an add result to a table
[10:31:25] Leif H. Auke: ok -> its no my line of expertese, I must study it
[10:31:53] Leif H. Auke: but look here -> this is possibly thje query we must do to get current posistions out of opengts
[10:32:07] Leif H. Auke: https://wiki.cantara.no/display/drone/Integrate+with+openGTS+data
[10:32:46 | Redigert 10:33:00] Leif H. Auke: dont need a lot of db layers stuff to do that ?
[10:33:26] Duong Thanh Huy: yup, it seems currently. But when it comes new requirement then it's harder to reuse
[10:34:18] Duong Thanh Huy: we could use native MySql query but it will take more effort if we need new requirement from time to time
[10:34:18] Leif H. Auke: yes, but just make a class, it will not be to many changes in this query
[10:35:02 | Redigert 10:35:17] Leif H. Auke: I think we sometime over design the DB interfacing, exspessialy if we only need a simple query
[10:35:54] Leif H. Auke: this query with return only the current living tracker positions
[10:37:40] Leif H. Auke: (but for some reason I never used java and DB. I know very vell .net/sql datasets etc, but java db integration is blank page for me) :)
[10:37:53] Duong Thanh Huy: (y)
[10:38:10] Duong Thanh Huy: it is ok, then we just use very simple JDBC for querying such data
[10:38:17] Leif H. Auke: But I think for simple queries that like never will change. use pure SQL.
[10:39:30] Leif H. Auke: but there are DB interfasing classes in openGTS. For updating Device table. Maybe just steel this classes for inserting Device (tracker) info
[10:40:21] Leif H. Auke: look here https://github.com/openGtsD/OpenGTS_2.5.8/tree/master/src/org/opengts/db/tables
[10:40:24 | Redigert 10:40:32] Thai Huynh: My opinion: the most programmer using  pure SQL when working google map.
[10:42:23] Duong Thanh Huy: just had a look, they're using their own import org.opengts.dbtools.*;
[10:42:35] Leif H. Auke: Okay -> you to fix kmost easy way, but I think we can use this query (with som modifications) to retrieve positions from openGTS database
[10:42:38] Duong Thanh Huy: would be very complicated to reuse such classes
[10:42:59] Leif H. Auke: yes, maybe if to many dependent classes
[10:43:18] Leif H. Auke: there is another solution
[10:44:33] Leif H. Auke: Skip eventdata in open GTS -> pipe posistions to AukeGTS from the tracker agents
[10:44:35] Leif H. Auke: ?
[10:45:04] Leif H. Auke: The we must modify openGTS code, but there is one method only to modify
[10:45:10] Leif H. Auke: one moment
[10:45:10] Thai Huynh: you mean using service API public for get/post data ?
[10:45:16] Leif H. Auke: no
[10:45:28] Leif H. Auke: using linux pipes
[10:45:48] Leif H. Auke: one moment, I show you
[10:48:16] Leif H. Auke: I show you some code
[10:48:22] Duong Thanh Huy: ok?
[10:48:25] Leif H. Auke: https://github.com/openGtsD/OpenGTS_2.5.8/blob/master/src/org/opengts/servers/tk10x/TrackClientPacketHandler.java
[10:48:53] Leif H. Auke: look this code, this is implementation in openGTS for reading feed one tracker type
[10:49:00] Leif H. Auke: on bottom
[10:49:19] Leif H. Auke: look method  private void insertEventRecord(Device device,
[10:49:47] Leif H. Auke: look then
[10:49:49] Leif H. Auke:         if (!DEBUG_MODE) {
            device.insertEventData(evdb);
            this.incrementSavedEventCount();
        }
[10:50:13] Leif H. Auke: this method device.insertEventData(evdb); store tracks to db
[10:50:27] Leif H. Auke: we modify this to also send tacks to AukeGTS directly
[10:50:43] Leif H. Auke: follow? (look close in code you will see)
[10:50:50] Duong Thanh Huy: I see it
[10:50:56] Duong Thanh Huy: but sounds overcomplicated
[10:51:10] Leif H. Auke: hmm
[10:51:28] Duong Thanh Huy: very easy to get bugs or break something
[10:51:32] Leif H. Auke: its simple -> bypass the openGTS database
[10:51:54] Leif H. Auke: we need to buiild openGTS with our changes
[10:52:49] Leif H. Auke: but its just one line of code -> aukeGTS.sendPipe(evdb)
[10:53:12] Leif H. Auke: at other side AukeGTS.readPipe()
[10:53:32] Leif H. Auke: using linus pipes for inter process comunication
[10:54:08] Leif H. Auke: you know how to use linux pipes ?
[10:54:17] Duong Thanh Huy: not yet
[10:54:32] Duong Thanh Huy: sorry, I'm not a linux geek
[10:54:57] Leif H. Auke: its very simple -> open a pipe as a file, and write/read from that file. Its a fifo queue
[10:55:00] Duong Thanh Huy: but I guess JMS would do the same thing
[10:55:12] Duong Thanh Huy: Java Message Service
[10:55:26] Leif H. Auke: yes, but no need
[10:55:29] Leif H. Auke: :)
[10:55:33] Duong Thanh Huy: ok
[10:56:05] Leif H. Auke: just create a names pipe on linux an open that pipe as a binary IO file in java.
[10:56:25] Leif H. Auke: (wotk on linux not on windows)
[10:56:56] Duong Thanh Huy: I'm programming on windows so it would need some work
[10:59:47] Leif H. Auke: but I think, first version we retrive from evendata table
[11:00:09] Leif H. Auke: i can fix the pipe stuff
[11:00:27] Leif H. Auke: So we need 2 integrations to openGTS
[11:00:40] Leif H. Auke: 1. add a device entry in device table when storing trackers
[11:01:23] Leif H. Auke: 2. retrive current posisitions from EventData table (have a process retriving openGTS database every 10 second)
[11:01:39] Leif H. Auke: are you with me ???
[11:01:44] Leif H. Auke: :)
[11:01:54] Duong Thanh Huy: yup
[11:01:56] Duong Thanh Huy: :)
[11:02:13] Duong Thanh Huy: 1 question
[11:02:17] Leif H. Auke: yep
[11:02:30] Duong Thanh Huy: we're going to have service for registering real drones
[11:02:42] Duong Thanh Huy: so what openGTS will do in our project?
[11:02:52] Duong Thanh Huy: I'm looking at https://wiki.cantara.no/display/drone/Drone+radar+design
[11:03:36] Duong Thanh Huy: and I don't see the purpose of using it. Sorry maybe I'm too noob
[11:03:51] Leif H. Auke: you are 100 correct
[11:03:54] Leif H. Auke: 100%
[11:04:13] Leif H. Auke: only need to openGTS is the tracker feed services
[11:04:38] Leif H. Auke: because we dont like to spend tme making this our self..
[11:04:53] Leif H. Auke: i.e all code in here in openGTS
[11:05:10] Leif H. Auke: https://github.com/openGtsD/OpenGTS_2.5.8/tree/master/src/org/opengts/servers
[11:05:23] Leif H. Auke: (that was my master plan)
[11:05:58] Leif H. Auke: but there is a lot of work to do if we are going to make integration for different trackers.
[11:06:13] Leif H. Auke: follow?
[11:06:18] Duong Thanh Huy: yup
[11:06:28] Duong Thanh Huy: you don't want to reinvent the wheel
[11:06:34] Leif H. Auke: no
[11:07:24] Leif H. Auke: I will adjust the overall design figure
[11:07:32] Duong Thanh Huy: (y)
[11:09:19] Leif H. Auke: So stratgy is -> first use openGTS as is and retrive positions from openGTS DB, later, adjust openGTS trackerservices, skip open GTS DB and send tracks directly from tracker servcice process to aukeGTS process
[11:10:01] Thai Huynh: (cool)
[11:11:02] Leif H. Auke: I did not put any name on the tasks on sprint. Who will do what from the tasks listed?
[11:11:10] Thai Huynh: I will do it
[11:11:23] Thai Huynh: edit and update who is working :)
[11:11:31] Duong Thanh Huy: (y)
[11:11:35] Leif H. Auke: okay
[11:11:52] Leif H. Auke: then Sprint 2 is started
[11:11:56] Leif H. Auke: (handshake)

```
