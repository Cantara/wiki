# Skype team meeting 10.4.2015

Thai, Huy and Leif

Main agreement: 

- New sprint start on monday. Be discussed on monday
- Showin moving drones on map from simulator major objective for sprint 1, seems to haave been met.
- Thai install my sql client
- Huy purify code, make more unit tests
- Leif study integration to openGTS database

```

[10.04.2015 02:36:41] Thai Huynh: http://89.221.242.66:8080/drone/
[10.04.2015 02:37:04] Thai Huynh: added start/stop select layerid into Our server
[10.04.2015 02:43:54] Thai Huynh: TrackerBase >> its seem you missing commit this class :)
[10.04.2015 09:07:43] Duong Thanh Huy: Hello, did you forget to commit TrackerBase.java?
[10.04.2015 09:07:44] Duong Thanh Huy: :)
[10.04.2015 09:10:30] Thai Huynh: good morning
[10.04.2015 10:45:20] Leif H. Auke: good morning
[10.04.2015 10:45:32] Leif H. Auke: yes I did, sorry
[10.04.2015 10:46:01] Thai Huynh: :)
[10.04.2015 10:47:03] Thai Huynh: looked code and see threadsafe from you
[10.04.2015 10:48:16] Leif H. Auke: okay, I am very sorry
[10.04.2015 10:48:17] Leif H. Auke: :)
[10.04.2015 10:48:30] Leif H. Auke: can we have a meeting i 1 hours ?
[10.04.2015 10:48:35] Thai Huynh: Okie
[10.04.2015 10:48:46] Leif H. Auke: is Huy here to?
[10.04.2015 10:49:55] Duong Thanh Huy: I'm here
[10.04.2015 10:50:09] Leif H. Auke: I look the map. Its seems we in general have met our target for this sprint. We show on map, zoom in and out and it seems workng perfectly
[10.04.2015 10:50:17] Leif H. Auke: very good.
[10.04.2015 10:50:58] Leif H. Auke: I maybe screewed up code yesterday to program more to clean up.
[10.04.2015 10:51:35] Leif H. Auke: but what we are going to du to meet our other target is to run the simulator and really wath one drone move.
[10.04.2015 10:51:42] Leif H. Auke: can we do that today ?
[10.04.2015 10:53:00 | Redigert 10:53:13] Thai Huynh: you mean, that's time for integrate OpenGTS  now ?
[10.04.2015 10:53:25] Leif H. Auke: yes. but first we need to see the simulator in action
[10.04.2015 10:53:45] Leif H. Auke: when can we do that ?
[10.04.2015 10:54:02] Leif H. Auke: i like to see drone moving on map :)
[10.04.2015 10:54:14] Duong Thanh Huy: seems the drone stops moving, it was like that few days ago
[10.04.2015 10:54:19] Duong Thanh Huy: let me check what happened
[10.04.2015 10:54:59] Thai Huynh: one moment
[10.04.2015 10:55:13 | Redigert 10:55:18] Thai Huynh: its seem I had added moving button per drone on map
[10.04.2015 10:55:24] Leif H. Auke: we need to be able to controll the service, and verify it run and also it must run without break
[10.04.2015 10:55:41] Leif H. Auke: Maybe its time to strap this code in unit tests ?
[10.04.2015 10:56:25] Duong Thanh Huy: it was tested with unittests but since we're changing a lot so I just skipped it
[10.04.2015 10:56:43] Leif H. Auke: ahh :)
[10.04.2015 10:56:54] Leif H. Auke: okay
[10.04.2015 10:57:09] Leif H. Auke: but i did only see one unit test in git ?
[10.04.2015 10:57:21] Leif H. Auke: when I adjusted.
[10.04.2015 10:57:46] Leif H. Auke: Ok (the meeting we have now)
[10.04.2015 10:58:07] Leif H. Auke: A Q for me?
[10.04.2015 10:58:11] Leif H. Auke: (cool)
[10.04.2015 10:58:29] Thai Huynh: Okie
[10.04.2015 10:59:04] Leif H. Auke: can we work duing weekend having it all function by monday. I can work as vell.
[10.04.2015 10:59:07] Leif H. Auke: ???
[10.04.2015 10:59:57] Thai Huynh: Yes, I can
[10.04.2015 11:00:05] Leif H. Auke: we do -> strap code in unittests, have simulator working 'perfect'
[10.04.2015 11:00:13] Leif H. Auke: What about you Huy?
[10.04.2015 11:00:30] Duong Thanh Huy: it's ok for me
[10.04.2015 11:00:38] Leif H. Auke: very very good.
[10.04.2015 11:00:56] Duong Thanh Huy: but can you describe the simulator working 'perfect'?
[10.04.2015 11:01:37] Leif H. Auke: = running always, showing all drones moving, and start/stop working
[10.04.2015 11:01:51] Leif H. Auke: maybe it does :), but I like to verify
[10.04.2015 11:02:35] Leif H. Auke: but maybe most important is that we strap the code in unittest, before we move forward. If we dont do now, its likly we did not do.
[10.04.2015 11:03:06] Leif H. Auke: It going to help us 'big time' if we have a vell strapped test environment for our code.
[10.04.2015 11:03:45] Leif H. Auke: for Thai -> install a my sql client on server so we can inspect the openGTS database
[10.04.2015 11:04:07] Leif H. Auke: make sence ?
[10.04.2015 11:04:39] Thai Huynh: you mean make remote sql ?
[10.04.2015 11:05:36] Leif H. Auke: we need to insect the my sql database for opengts. See the tables and data.
[10.04.2015 11:06:40] Thai Huynh: that's mean we need install Desktop (e.g KDE) on our server
[10.04.2015 11:06:49] Thai Huynh: and then install mysql client
[10.04.2015 11:07:14] Thai Huynh: ahh
[10.04.2015 11:07:26] Thai Huynh: mysqlphpAdmin for ex
[10.04.2015 11:07:36] Leif H. Auke: there is som web based tool awal?
[10.04.2015 11:07:37] Thai Huynh: ok, no need instlal KDE
[10.04.2015 11:07:43] Leif H. Auke: yepp
[10.04.2015 11:07:54] Thai Huynh: yes, phpMyAdmin
[10.04.2015 11:07:55] Thai Huynh: :)
[10.04.2015 11:08:03] Leif H. Auke: we can use that.
[10.04.2015 11:08:08] Thai Huynh: OK,
[10.04.2015 11:09:12] Leif H. Auke: Huy -> I know i screewed up you code by doing refactor. Let us get it all togehter. I can help out making unit testing.
[10.04.2015 11:09:32] Leif H. Auke: By monday we are ready, and can move to next sprint.
[10.04.2015 11:09:46] Leif H. Auke: (cool)
[10.04.2015 11:09:53] Duong Thanh Huy: Thanks Leif, but I can take care of unit testing ;)
[10.04.2015 11:09:56] Duong Thanh Huy: no big deal
[10.04.2015 11:10:17] Duong Thanh Huy: there is something with the thread safe, I'm having some exceptions locally
[10.04.2015 11:10:22] Duong Thanh Huy: trying to figure out
[10.04.2015 11:11:02] Leif H. Auke: Its actually more easy inspect this with a unit test.
[10.04.2015 11:12:07] Leif H. Auke: make a test that run up the whole service, and make som addtional threads simultat the web service queries. You will very quickly see where the treading problems are.
[10.04.2015 11:12:39] Leif H. Auke: Likly there are some point where updateing variables get concurrent. This will caouse java to freeze.
[10.04.2015 11:13:29] Leif H. Auke: its a very good practice to be able to run the whole service in a test environment (som integration test actually)
[10.04.2015 11:13:55] Leif H. Auke: for our future development this will save us a lot of trouble
[10.04.2015 11:15:39] Duong Thanh Huy: (y)
[10.04.2015 11:15:54] Thai Huynh: maybe I will look structure openGTS and make document on wiki ?
[10.04.2015 11:15:55] Duong Thanh Huy: so that's Spring Integration test
[10.04.2015 11:16:21] Leif H. Auke: Thay -> yes, make that you primary task
[10.04.2015 11:16:51] Leif H. Auke: Huy -> welcome to Auke team -> the team leader (me) sometime sticks his finger into code :)
[10.04.2015 11:17:15] Duong Thanh Huy: in Agile there is no code owner ;)
[10.04.2015 11:17:23] Leif H. Auke: correct :)
[10.04.2015 11:17:25] Duong Thanh Huy: thank you for pointing out
[10.04.2015 11:17:38] Leif H. Auke: (cool)
[10.04.2015 11:17:56] Leif H. Auke: okay ->
[10.04.2015 11:20:56] Leif H. Auke: Ok, we agree -> work this weekend
[10.04.2015 11:21:06] Thai Huynh: Yep
[10.04.2015 11:21:11] Leif H. Auke: I will work as vell, but I need some task
[10.04.2015 11:21:29] Leif H. Auke: Maybe Huy -> give me some testing tasks
[10.04.2015 11:21:40] Duong Thanh Huy: oh
[10.04.2015 11:23:03] Duong Thanh Huy: I give you tasks?
[10.04.2015 11:23:12] Thai Huynh: no :)
[10.04.2015 11:23:14] Leif H. Auke: yes
[10.04.2015 11:24:09 | Redigert 11:24:17] Thai Huynh: him will make new task for himself :)
[10.04.2015 11:24:31] Leif H. Auke: but I also need something to do over weekend
[10.04.2015 11:25:08] Thai Huynh: oki, I will install my sql client in todays and then You can get more task look DB opentGTS
[10.04.2015 11:25:13] Thai Huynh: (chuckle)
[10.04.2015 11:25:23] Leif H. Auke: ok
[10.04.2015 11:25:41] Leif H. Auke: I can look into how to retrieve data from openGTS
[10.04.2015 11:25:50] Thai Huynh: (y)
[10.04.2015 11:25:53] Leif H. Auke: and make the integration provess
[10.04.2015 11:25:58] Leif H. Auke: (y)
[10.04.2015 11:26:26] Thai Huynh: btw, @leif: have you try start moving button on every drone ?
[10.04.2015 11:26:33] Leif H. Auke: yes
[10.04.2015 11:26:40] Leif H. Auke: I see it move
[10.04.2015 11:27:03] Leif H. Auke: but this movement is not from simulator ?
[10.04.2015 11:27:17] Duong Thanh Huy: it should be moving automatically, but there was some changes and now I don't see it move anymore
[10.04.2015 11:27:17] Thai Huynh: hope its improve more on next monday
[10.04.2015 11:27:18] Leif H. Auke: its just a manual movement?
[10.04.2015 11:27:19] Duong Thanh Huy: wierd
[10.04.2015 11:27:49] Leif H. Auke: huy-> maybe because my refactor?
[10.04.2015 11:28:13] Duong Thanh Huy: I don't know yet. still checking
[10.04.2015 11:28:39] Leif H. Auke: Thai -> when hitting start on drone -> drone is started on server, when hitting stop -> stopped on server ?
[10.04.2015 11:29:01 | Redigert 11:29:09] Thai Huynh: for now, I set timeout send request into server when click start
[10.04.2015 11:29:06] Leif H. Auke: and 2 -> we need to look drone on zoom levels bigger than 13
[10.04.2015 11:29:22] Thai Huynh: yes, I can
[10.04.2015 11:29:57] Leif H. Auke: to meet our target -> drone must start / stop on server by clicking button
[10.04.2015 11:30:15] Thai Huynh: Okie
[10.04.2015 11:30:22] Leif H. Auke: to meet our target -> we must see drones moving on map from simulated positions
[10.04.2015 11:30:50 | Redigert 11:30:58] Leif H. Auke: this is major target for this sprint 1
[10.04.2015 11:31:00] Duong Thanh Huy: this should be done today
[10.04.2015 11:31:06] Duong Thanh Huy: :)
[10.04.2015 11:31:09] Leif H. Auke: verry verry good
[10.04.2015 11:31:11] Leif H. Auke: :)
[10.04.2015 11:31:15] Leif H. Auke: (handshake)
[10.04.2015 11:31:52] Duong Thanh Huy: (handshake)
[10.04.2015 11:31:56] Leif H. Auke: ok, i leave now, talk later
[10.04.2015 11:32:39] Thai Huynh: nice weekends :)
[10.04.2015 11:33:08] Duong Thanh Huy: thanks Leif, will inform you when everything is done
[10.04.2015 13:44:43] Thai Huynh: https://wiki.cantara.no/display/drone/Drone+Server+Info << I had updated info login for mysql client tool
[10.04.2015 13:44:44] Thai Huynh: :)
[10.04.2015 19:37:39 | Redigert 19:40:46] Thai Huynh: http://89.221.242.66:8080/drone/

I had update start/stop should be done at server. And allow show drones at bigger zoom level
[10.04.2015 19:39:31] Thai Huynh: check popup window and see altitude=0  and flying = false when stop
[10.04.2015 19:44:34] Leif H. Auke: Are you asleep or working ?
[10.04.2015 19:44:54] Leif H. Auke: Is there some commits ?
[10.04.2015 19:45:32] Thai Huynh: just commit some changes
[10.04.2015 19:46:00] Thai Huynh: and prepare go to sleep :)
[10.04.2015 19:47:46] Leif H. Auke: Ok.  have a nice sleep
[10.04.2015 19:47:58] Thai Huynh: thanks
[10.04.2015 19:48:08] Thai Huynh: demo server ready for check
[10.04.2015 19:48:54] Leif H. Auke: Did you add address to opengts database?
[10.04.2015 19:49:06] Thai Huynh: yes, I had
[10.04.2015 19:49:14] Leif H. Auke: (y)
[10.04.2015 19:49:17] Thai Huynh: https://wiki.cantara.no/display/drone/Drone+Server+Info
[10.04.2015 19:50:33] Thai Huynh:  http://89.221.242.66/phpmyadmin

>>> account info look at https://wiki.cantara.no/display/drone/Drone+Server+Info
:)
[10.04.2015 19:50:56 | Redigert 19:51:03] Thai Huynh: OK, I am leave out now, continuos for tommorrow

```
