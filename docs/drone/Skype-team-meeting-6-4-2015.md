# Skype team meeting 6.4.2015

### [Skype team meeting 6.4.2015](Skype<sub>~team</sub><sub>meeting</sub><sub>6</sub>~4-2015.md)

Sprint 1 run for this week. New Sprint 2 on monday

##### main target this week 

```

[12:35:36] Leif H. Auke: but what will you be able to finish up by this week ?
[12:36:02] Duong Thanh Huy: I will finish the web service for getting different layers of trackers
[12:36:14] Duong Thanh Huy: serializing to json
[12:36:21] Thai Huynh: for me finished demo site (integrate from Huy) and make webpage (simple)
[12:36:25] Duong Thanh Huy: and web service to update such information

```

```

[11:35:29] Duong Thanh Huy: morning
[11:35:58] Thai Huynh: Good morning
[11:37:06] Thai Huynh: i had update new test on http://89.221.242.66:8080/drone/
[11:37:11] Thai Huynh: still checking
[11:37:24] Thai Huynh: its seem a bit slow when send request
[11:42:29] Leif H. Auke: good morning :)
[11:45:44] Leif H. Auke: ahh. now it shows drones all over the world !!!
[11:48:17 | Redigert 11:49:18] Thai Huynh: yes, dummy data just for 5 position: HCM, OSLO, UK, Lodon, Canada (e.g total 50 drone flying)
[11:48:46] Thai Huynh: its seem a bit slow when send request, I am consider this issues
[11:49:27] Duong Thanh Huy: I've also committed the change to store the flight history to JSON files
[11:49:31] Duong Thanh Huy: please take a look
[11:49:45] Thai Huynh: yep, i do now
[11:52:13] Leif H. Auke: is this drones moving from simulations?
[11:52:43] Thai Huynh: yep
[11:53:21 | Redigert 11:53:30] Thai Huynh: every drone after load again, will  update new position from calculate method
[11:54:15] Leif H. Auke: ok. I zoom in an look
[11:54:36] Thai Huynh: very slow when load drone ?
[11:55:08] Leif H. Auke: hmm..
[11:55:21] Leif H. Auke: the web service is slow?
[11:55:49] Leif H. Auke: thai. Make a button on test page to refresh?
[11:57:11] Thai Huynh: yep, its simples (i will ), I am going investiagte issues load drone on map
https://developers.google.com/maps/articles/toomanymarkers
[11:59:13 | Redigert 11:59:22] Thai Huynh: Make a button on test page to refresh?I also will add stop/start button on per drone and then we view drone flying
[12:00:41] Leif H. Auke: I have one idea -> for furture use for the web service
[12:00:58] Leif H. Auke: 1. add zoom factor as parameter (wil be nady on server)
[12:01:33] Leif H. Auke: 2. add a layer id (string)
[12:02:17] Leif H. Auke: examples of layer id is -> "simulated" and "realdrones"
[12:02:37] Thai Huynh: layer id  = drone id ?
[12:02:54] Leif H. Auke: no, its a grupping
[12:03:15] Leif H. Auke: for ex. we add all simulated drones to one layer = "simulated"
[12:03:32] Leif H. Auke: and all real drones to one layer = "real"
[12:03:45] Leif H. Auke: you might select what layer to show or all layers
[12:05:00] Leif H. Auke: This must be reflected on server. i.e we have position list for diffrente layers -> we leve this blank for now, but in next sprint we extend this functionallity (I have som structural idea i slow you later)
[12:05:09] Leif H. Auke: follow??
[12:05:18] Thai Huynh: think...
[12:05:34] Duong Thanh Huy: I think it is clear for me
[12:06:17] Duong Thanh Huy: I will make a different map for real drones and another one for simulated ones
[12:06:46] Leif H. Auke: yes, or you can select what layer to show...
[12:07:23 | Redigert 12:07:32] Thai Huynh: Ahh, Ok >> select layer id to show
[12:08:13] Leif H. Auke: we put that layer id to the drone or a drone might be attached to multiple layers
[12:08:54] Leif H. Auke: yepp..
[12:09:34] Leif H. Auke: very handy to show activity -> you either select 'all layers' or some selections of layer to show.
[12:10:00] Leif H. Auke: you identify a drone (tracker) to a certain layer
[12:10:54] Leif H. Auke: we add the layer functionallity later, but make som parameter on web service
[12:11:07] Leif H. Auke: 2 more parameters. 1.zoom, 2 layer
[12:11:34] Leif H. Auke: okay ?
[12:11:40] Leif H. Auke: (think)
[12:12:41] Leif H. Auke: Huy -> you there
[12:12:45] Thai Huynh: Currently, zoom factory I can send as parameter just is number
[12:12:54] Leif H. Auke: yepp
[12:13:06] Thai Huynh:  for layer I will look api and check
[12:13:33] Leif H. Auke: you dont need to involve map for this layer id
[12:14:00] Leif H. Auke: its just a parameter you set your self
[12:14:16] Leif H. Auke: map layers are something else
[12:14:43] Thai Huynh: Ahh, Okie
[12:14:54] Duong Thanh Huy: understood, parameter as "real" then show real drones, otherwise show simulated ones
[12:14:58] Leif H. Auke: instead of calling it layer, we might call it position group
[12:16:00] Thai Huynh: yep
[12:16:02] Leif H. Auke: Huy -> build in to service a general positiongroup object (layer)..
[12:17:07] Leif H. Auke: get the position group from the drone and add everything regaring postions or list of drones for each group to this object.
[12:17:32] Leif H. Auke: then we can freely extend everything within diffrent groups (layers)
[12:17:33] Leif H. Auke: ??
[12:17:35] Leif H. Auke: follow ?
[12:17:39] Duong Thanh Huy: roger that
[12:17:44] Leif H. Auke: (y)
[12:18:00] Thai Huynh: (handshake)
[12:18:25] Leif H. Auke: Huy -> one more request :)
[12:18:30] Duong Thanh Huy: yes please
[12:18:40] Leif H. Auke: rename 'drone' to tracker
[12:19:11] Leif H. Auke: we are actually dealing with 'trackers' -> the identity is tight to a physical tracker
[12:19:37] Leif H. Auke: the tracker only happens to be attached to a drone.
[12:19:50] Leif H. Auke: from this system perspective, we deal with trackers ?
[12:20:06] Duong Thanh Huy: noted
[12:20:09] Duong Thanh Huy: thanks Leif
[12:20:25] Duong Thanh Huy: anymore tasks for me this week?
[12:20:40] Leif H. Auke: for the administration of this system, we do it very simple (i think)
[12:20:56] Leif H. Auke: one moment
[12:21:44 | Redigert 12:21:55] Leif H. Auke: Huy -> serialize the 'tracker' to file with json -> for administration we simply make one web page for update this tracker object.
[12:22:11] Leif H. Auke: make sence (huy/Thai)
[12:22:35] Duong Thanh Huy: so you mean
[12:22:45] Duong Thanh Huy: we will serialize the whole tracker object to json?
[12:23:01] Duong Thanh Huy: and a webpage for updating this object?
[12:23:06] Leif H. Auke: yes?
[12:23:27] Leif H. Auke: via a web service
[12:23:46] Thai Huynh: how about webpage for administrator. we will make new ?
[12:24:05] Duong Thanh Huy: okie, via web service or web page please?
[12:24:59] Leif H. Auke: web page use a web service to update the tracker object stored on server as a object (serialized with json)
[12:25:18] Duong Thanh Huy: clear :)
[12:25:57] Leif H. Auke: because the tracker have a long ideitication (IME code) we possibly do not need any user accout functionallity
[12:26:20] Leif H. Auke: to update the tracker you need to know the tracker id and this is is hidden from public eye.
[12:26:36] Leif H. Auke: (for first verion simplisity)
[12:26:52] Duong Thanh Huy: yup, so we don't need user authentication right now
[12:27:02] Leif H. Auke: no
[12:27:26] Thai Huynh: huy, we are usig IME code for indentify
[12:27:53] Leif H. Auke: this is a core service -> we keep the structure as simple as possible..
[12:28:46] Leif H. Auke: administrations can be done on other web sites the just deliver a tracker object and also contain all other stuffs of add on information
[12:29:01] Leif H. Auke: this core server on deal with the central info to measure positions...
[12:30:09] Duong Thanh Huy: ok
[12:30:28] Duong Thanh Huy: so we keep it small and simple
[12:30:54] Thai Huynh: btw, I have question relate to webpage ?
[12:31:29 | Redigert 12:31:36] Thai Huynh: we will make simple page load all tracker and manage (e.g: add or edit. ?)
[12:32:22] Leif H. Auke: no, each user manage its own tracker firste version.
[12:32:43] Leif H. Auke: (I can make some spec on wiki for this (later))
[12:33:00] Leif H. Auke: ok guys -> A question
[12:33:10] Thai Huynh: yup ?
[12:33:48] Leif H. Auke: if we run this sprint for this week and end it by friday -> what you think we can achive
[12:34:00] Leif H. Auke: (we start a sprint 2 nect monday)
[12:34:45] Leif H. Auke: so what might we be able to finish up by friday?
[12:34:56] Leif H. Auke: Thai?
[12:35:10] Thai Huynh: it's fine for me.
[12:35:18] Duong Thanh Huy: fine for me
[12:35:21] Thai Huynh: cool
[12:35:36] Leif H. Auke: but what will you be able to finish up by this week ?
[12:36:02] Duong Thanh Huy: I will finish the web service for getting different layers of trackers
[12:36:14] Duong Thanh Huy: serializing to json
[12:36:21] Thai Huynh: for me finished demo site (integrate from Huy) and make webpage (simple)
[12:36:25] Duong Thanh Huy: and web service to update such information
[12:36:34] Leif H. Auke: w
[12:37:30] Leif H. Auke: very nice. -> if we can get this by this week + Trim the map retieval so it work fast enough (thai) we achieved a lot...
[12:37:37] Leif H. Auke: agreed (handshake)
[12:37:46] Duong Thanh Huy: thanks

```
