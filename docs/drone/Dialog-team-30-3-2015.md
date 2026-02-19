# Dialog team 30.3.2015

```

Good morning
[11:07:39] Thai Huynh: some info need update: I am still working on task (integrate) for moving drone every 10s on map.
[11:08:28] Leif H. Auke: good morning
[11:08:30] Leif H. Auke: :)
[11:09:47] Thai Huynh: Btw, about HTML5 code to be inserted into Joomla I think i do it in wednesday. B/c I need verify all before go to joomla
[11:11:16] Leif H. Auke: We wait for joomla until everything works. For now we do the testrigg :)
[11:11:48] Leif H. Auke: More easy work in a simple html page rig
[11:12:07] Thai Huynh: Yes, just HMLT + JS
[11:12:21 | Redigert 11:12:32] Thai Huynh: I also  try complete moving task ASAP
[11:13:09] Leif H. Auke: do it solid, not fast :)
[11:13:45] Leif H. Auke: when it moves, we have other functions regarding move we must solve.
[11:14:08] Thai Huynh: what's is function ?
[11:15:43] Leif H. Auke: we must take into consideration the size of map view. If map view is big, no need to show each drone posistion. Only one position showing there are drones at a certain spot.
[11:16:42] Leif H. Auke: for ex. if you show a world map. No need to show all drones in ho chi minh city. They will not show anyway. We then calulate on position on server showing there are drones in ho chin minh :)
[11:17:08] Leif H. Auke: I make specifications on wiki. But first thin first. Make drone move.
[11:17:23 | Redigert 11:17:35] Leif H. Auke: Is the simulator from Huy(2) ready ?
[11:18:49] Leif H. Auke: for ex. if map view is bigger than 10 km in size. Individual drones will not show anyway
[11:19:06] Duong Thanh Huy: still don't get it, what simulator please?
[11:19:36] Leif H. Auke: the simulation of drone position you work on ?
[11:20:15] Duong Thanh Huy: oh, I thought I will make the server side and Thai will make the client side, then we will integrate together
[11:20:24] Leif H. Auke: yes
[11:20:34] Leif H. Auke: :)
[11:20:59] Leif H. Auke: you make the serviceside position simulations and Thai mak the map view
[11:21:06] Duong Thanh Huy: I think it is done from my side. Yesterday I've finished writing unittests and now I'm reading the documents
[11:21:32 | Redigert 11:21:37] Duong Thanh Huy: it is now possible to invoke web services for registering, removing and getting drone position
[11:21:33] Thai Huynh: Yes, I had see some code for Unit Test
[11:21:48] Leif H. Auke: Ok. maybe i need to explain a little.
[11:22:51] Leif H. Auke: The service you make Huy is to run on continuesly on server to simulate drones. Thai retrieve this positions and show in map.
[11:23:13] Leif H. Auke: follow?
[11:23:38] Duong Thanh Huy: yup
[11:23:40] Duong Thanh Huy: go on please
[11:24:43] Thai Huynh: yes
[11:25:47] Leif H. Auke: so you make a service that start when service start, adding for ex. 100 drones on different spots
[11:26:22] Leif H. Auke: for ex. 10 drones in ho chi minh, 10 drones in oslo, 10 drones in new your, 10 drones in london etc.. :)
[11:26:36] Leif H. Auke: simulating activites around the world.
[11:27:01] Leif H. Auke: we open the map, zoom in to diffrent views and look the drones flying :)
[11:27:22] Duong Thanh Huy: thanks, understood
[11:27:37] Duong Thanh Huy: so I will make a service start when the application is deployed
[11:27:47] Leif H. Auke: yes
[11:27:49] Leif H. Auke: yep
[11:27:50] Duong Thanh Huy: and make a random 100 drones with different positions?
[11:27:57] Leif H. Auke: yep
[11:28:03] Leif H. Auke: we see how it looks
[11:28:04] Duong Thanh Huy: it is clear :)
[11:28:26] Leif H. Auke: after this first step we do the following
[11:29:10] Leif H. Auke: -> make the drones fly flights. i.e Fly for for ek 10 minutes, land and stand still for 10 minutes, the fly again :)
[11:29:19] Leif H. Auke: (simulate real world)
[11:29:31] Thai Huynh: :)
[11:29:34] Leif H. Auke: next step ->
[11:30:37] Leif H. Auke: we have a list of individual drone positions. We make some summarized position lists.
[11:31:09] Leif H. Auke: on list for all drones (one postion) for all drones with a radius of 10km
[11:31:44] Leif H. Auke: one list for all drones (one positions) for all drones within a radius of 10 mile.. -> so on..
[11:31:53 | Redigert 11:32:53] Thai Huynh: that's mean we make funtion looking all drone in radius range 10km ?
[11:31:57] Leif H. Auke: we experiment to see what look nice
[11:32:06] Leif H. Auke: no.
[11:32:11] Leif H. Auke: no.
[11:32:32] Thai Huynh: [11:31] Leif H. Auke: 

<<< on list for all drones (one postion) for all drones with a radius of 10km?? please explain here
[11:32:46] Leif H. Auke: if mapview is bigger that 10 km, you retrive position for the 10km summarized position list
[11:32:58] Leif H. Auke: because.....
[11:33:19] Leif H. Auke: if mapview is big, you will not see individual drones on map anyway
[11:33:30] Thai Huynh: ahh, OKie
[11:33:39] Leif H. Auke: you only need to se on point showing drone activities :)
[11:34:28] Leif H. Auke: 10 km is just an estimate. We try out and see how it look. Maybe 10km in not right size, but we just try out.
[11:34:46] Leif H. Auke: :)
[11:35:49] Leif H. Auke: Huy must consider this when he make the position list (make a function the summaraize into new lists for highter map size.
[11:36:06] Leif H. Auke: follow ?
[11:36:18] Duong Thanh Huy: thinking...
[11:36:38] Leif H. Auke: but we do one step at a time :)
[11:37:20] Leif H. Auke: we dont leave this overall task before be have a map and positions that look natrual.
[11:37:50] Leif H. Auke: we will spend at least 2 more weeks on this tasks, so dont worry (and get nervous) :)
[11:38:30] Leif H. Auke: this is the core of our system. We use the time nessesary to get it cool and nice..
[11:38:38] Leif H. Auke: ok ?
[11:39:01] Thai Huynh: Okie
[11:39:11] Duong Thanh Huy: ok
[11:39:23] Thai Huynh: (handshake)
[11:40:55] Leif H. Auke: (handshake)
[11:41:25] Leif H. Auke: if we dont do it 100% correct first time, we just refactor and try again....
[11:42:04] Duong Thanh Huy: thanks for making it clear
[11:43:28] Leif H. Auke: okay. overall, dont hesitate to ask if any issue or unclearities. (this is agile development, spesify as we go) :)
[11:43:45] Duong Thanh Huy: and you're the product owner
[11:43:46] Duong Thanh Huy: :)
[11:43:51] Leif H. Auke: yep
[11:44:05] Duong Thanh Huy: (y)
[11:44:22] Thai Huynh: Yes
[11:45:22] Leif H. Auke: to both of you. Maybe you put you understanding of the functionallity into wiki ?
[11:45:34] Leif H. Auke: one moment
[11:46:56] Leif H. Auke: this is you task page thai (spend a little time explaing here)
[11:46:58] Leif H. Auke: https://wiki.cantara.no/display/drone/Request+and+plot+the+positions+into+the+current+map+view+every+10+second
[11:47:19] Leif H. Auke: this is you task page Huy (spend a little time explaining here)
[11:47:34] Leif H. Auke: https://wiki.cantara.no/display/drone/Add+a+process+for+each+drone+that+refresh+new+positions+every+10+seconds+on+server
[11:47:56] Leif H. Auke: (might be good for clearify)
[11:48:32] Leif H. Auke: ok ?
[11:51:52] Thai Huynh: Okie it's  good for you view and feeedback
[11:53:58] Duong Thanh Huy: this is very good
[11:54:01] Duong Thanh Huy: thank you Leif
[11:56:12] Leif H. Auke: https://wiki.cantara.no/display/drone/Add+a+process+for+each+drone+that+refresh+new+positions+every+10+seconds+on+server
[11:58:14] Duong Thanh Huy: description updated, thank you
[12:03:59] Leif H. Auke: yes. I like your explain as well on the page.
[12:04:17] Duong Thanh Huy: sure thing, we will update accordingly from time to time
[12:04:28] Leif H. Auke: good

```
