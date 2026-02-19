# Layers and summarized positions

### [Layers and summarized positions](Layers<sub>~and</sub>~summarized-positions.md)

##### What is a layer

- A layer have a layer-id and a layer name + some explanations (possibly)
- All processing is done within layer
- One tracker are always connected to a Layer
- User might create layers
- for no only two layers, real and simulated drones
- All layers are selectable on map page

##### Position calculation

- A layer contain a list of positions for each zoom level
- For all some levels less that 18, position are a sum of all tracker within a certain area
- A map on a certain zoom level have a grid, for ex 100 X 100 squares for summarize all drones in each square into on position

###### Zoom level calculation 

- Zoom Longitude = ROUND( LONGITUDE / ( 360 / ( 2 ^^(ZOOMLEVEL-1) ) ) , 1) * 10
- Zoom Latitude = ROUND( LATITUDE / ( 180 / ( 2 ^^(ZOOMLEVEL-1) ) ) , 1) * 10

###### Solution to zoom level calculation

- For each zoom level we calculate position lists longitude and latitude, containing the calculated Zoom Longitude and Zoom Latitude positions from each tracker position.
- If more than one tracker present in a certain positions, we increment a counter number_of_trackers
- When ask for positions on a certain zoom level, we use this lists to retrieve a positions, instead of direct tracker positions

- Each tracker level has its own set of calculated position between zoom level 1 and zoom level 17

##### Code implementation

- class **ZoomLayerServiceImpl** contain and calculate posistion for one zoomlevel
- class **TrackerLayer** contain a list of 15 ZoomLayerServiceImpl objects, one for each calculating zoom level.

- Test class **ZoomLayerTest**

##### debate 2015.04.22

```

good morning
[11:17:25] Thai Huynh: Good morning
[11:17:52] Duong Thanh Huy: morning
[11:18:09] Leif H. Auke: all vell?
[11:18:29] Duong Thanh Huy: I think so
[11:18:31] Duong Thanh Huy: :)
[11:18:32] Duong Thanh Huy: how about you
[11:18:43] Leif H. Auke: fine to
[11:18:57] Leif H. Auke: Do you have 2 minutes for discussion?
[11:19:05] Duong Thanh Huy: sure thing
[11:19:05] Duong Thanh Huy: :)
[11:19:13] Thai Huynh: I am fine :)
[11:19:16] Thai Huynh: yes
[11:20:06] Leif H. Auke: I figures out a function for recalculate postions on different zoom levels so we dont have to show every tracker postions, but instread use summarized positions.
[11:20:28 | Redigert 11:20:57] Leif H. Auke: Could you have al look and see if this is understandable according to description
[11:20:31] Leif H. Auke: ??
[11:20:39] Leif H. Auke: https://wiki.cantara.no/display/drone/Layers+and+summarized+positions
[11:20:42] Duong Thanh Huy: ok can you give us
[11:23:38] Leif H. Auke: (its on wiki page)
[11:23:39] Duong Thanh Huy: ok
[11:23:41] Duong Thanh Huy: just had a look
[11:24:14] Leif H. Auke: got the idea ?
[11:24:55] Duong Thanh Huy: not really, sorry
[11:25:02] Leif H. Auke: you might see from the attached excel sheet how it calculate
[11:25:16] Leif H. Auke: I explain
[11:26:12] Leif H. Auke: case: If there are 10.000 drone spread out of the world and you show map on zoom level 1, you will only show maximum 10 X 10 posistions
[11:26:41] Leif H. Auke: each postition on map contain a numer of trackers included
[11:26:46] Leif H. Auke: follow...
[11:26:47] Leif H. Auke: ?
[11:26:55] Duong Thanh Huy: ok, please go on
[11:27:06] Leif H. Auke: can you open the excel sheet ?
[11:27:10] Duong Thanh Huy: I did
[11:27:37] Leif H. Auke: ok, look for ex zoom level 10
[11:28:31] Leif H. Auke: this give for longitude -2560 to 2560 decree sectors around the world
[11:28:41] Leif H. Auke: and same for longitude
[11:29:35] Leif H. Auke: that means there are 5120 X 5120 possible positions to show globally on this zoom level.
[11:29:42] Leif H. Auke: (using this calculation)
[11:30:22] Duong Thanh Huy: ok, understood
[11:31:17] Leif H. Auke: the shown size og a map on this zoom is one of 512 x 512 possible areas around the globe
[11:31:55 | Redigert 11:32:26] Leif H. Auke: this means, we only retrive a max og 100 positions on any viewed area on this zoom level.
[11:32:03] Leif H. Auke: got the Idea?
[11:32:49] Duong Thanh Huy: got it
[11:32:54] Leif H. Auke: (cool)
[11:33:10] Duong Thanh Huy: so that's the view calculation we could do
[11:34:13] Leif H. Auke: so, when we calculate positions for a tracker level, we simply precalcuate a list of postions for each zoom level beforehand (zoom 1 to 17)
[11:34:40] Leif H. Auke: and use this lists to retrive postions, reather that the basice tracker list.
[11:35:13] Leif H. Auke: UI stays the same, it simply get a diffrente postions list for each zoom level.
[11:35:25] Duong Thanh Huy: Each tracker level has its own set of calculated position between zoom level 1 and zoom level 17
[11:35:34] Leif H. Auke: yepp
[11:35:36] Duong Thanh Huy: this would mean we have to calculate a lot
[11:35:52] Duong Thanh Huy: and store such data is very costly for memory
[11:36:46 | Redigert 11:37:57] Leif H. Auke: My quess is, its 17 x 2 calculation for each tracker each time using this spcesial function. I think its pretty fast.
[11:37:16] Leif H. Auke: The list will not be to big, because there are not that many areas covered
[11:37:31] Leif H. Auke: I like to try?
[11:38:12] Duong Thanh Huy: it's ok, but I think we will run into performance issues.
[11:38:34] Leif H. Auke: hmm
[11:38:50] Duong Thanh Huy: for examples: you have 10000 drones
[11:38:55] Leif H. Auke: java in memory on a modern computer are suprisingly fast
[11:40:00] Duong Thanh Huy: then you have to store 18 levels, thatn means 10000 x 18 objects
[11:41:05] Leif H. Auke: you dont store one object pr. tracker. You store one object pr. calulated position
[11:41:24] Leif H. Auke: it means on zoom 1, maximun 10 X 10 = 100 entries
[11:41:28] Leif H. Auke: and so on....
[11:41:52] Leif H. Auke: imagine speed ->
[11:42:38] Leif H. Auke: a cpu with 2 GHZ clock, spending for ex 100.000 cycles pr. calculation do 20.000 calculations a second
[11:43:20] Leif H. Auke: if is use 10.000 cycles, it will be 200.000 calculations a second. (CPU's are stubidetly fast)
[11:43:25] Leif H. Auke: ;)
[11:43:42] Duong Thanh Huy: ok
[11:43:44] Duong Thanh Huy: :)
[11:43:51] Leif H. Auke: lets try?
[11:44:13] Duong Thanh Huy: ok... I'm still a little bit hesitate
[11:45:21] Leif H. Auke: alternativly the UI work harder to retrive 1000 tracker positions when showing world map (in case 1000 active trackers)
[11:45:50] Leif H. Auke: 1000 postions each 10 second X 100 users is also som network load.
[11:46:35] Leif H. Auke: a computer 1000 times faster than the network, so everything you can calculate to reduse network traffic is very good for scaling.
[11:46:39] Leif H. Auke: (its a fact)
[11:46:40] Leif H. Auke: :)
[11:47:39 | Redigert 11:47:47] Leif H. Auke: it cheaper add CPU capaseties than networking capaseties.
[11:48:28] Duong Thanh Huy: will there any changes in data structure? now we're showing a list of trackers every call
[11:49:05] Leif H. Auke: let me see....
[11:49:12] Duong Thanh Huy: how often we will recalculate for tracker layer, 10 seconds?
[11:49:52 | Redigert 11:49:57] Thai Huynh: maybe make set timer  in java code ?
[11:50:01] Leif H. Auke: we try every 10 second but actually we migh differ on different zooms possibly
[11:50:16] Leif H. Auke: a world view dont need that quick update.
[11:50:25] Thai Huynh: yep
[11:50:56] Leif H. Auke: for ex. zoom 1 every minute, and zoom 17 every 10 second and rest in between ?
[11:51:05 | Redigert 11:51:12] Thai Huynh: its depend on zoom level from user
[11:51:43] Leif H. Auke: data structure ...
[11:52:34] Leif H. Auke: we send tracker ID to UI, but on summarices positions we dont have tracker ID, but insead a figure = number of trackers on positions
[11:52:48] Leif H. Auke: I think its ony a minor adjustment ?
[11:52:56] Duong Thanh Huy: it is
[11:53:14] Duong Thanh Huy: so that means it is just for the number of trackers
[11:53:31] Leif H. Auke: yepp
[11:53:31] Duong Thanh Huy: showing drones moving is still the same?
[11:53:41] Leif H. Auke: yes
[11:53:57] Leif H. Auke: but for summarized level you possibly will not see any movements
[11:54:43] Leif H. Auke: I think is oly when you zoom in to individual drones (zoom > 17) (for ex) you will see anything move..
[11:55:05] Duong Thanh Huy: ok, so at which level we will see drones?
[11:55:52] Leif H. Auke: I think we summarize for level 1 to 17, above 17 se show individual drones ?
[11:56:31] Duong Thanh Huy: ok :)
[11:56:44] Duong Thanh Huy: but maybe 17 is a little bit too much
[11:57:11] Duong Thanh Huy: user will wonder why they don't see any drones when they are at level 14 for examples
[11:57:23] Duong Thanh Huy: just the number of drones
[11:57:50] Leif H. Auke: hmm
[11:58:18] Leif H. Auke: I calculated -> at zoom level 17 the with of the map will be 600 meters
[11:58:19] Leif H. Auke: ??
[11:58:26] Leif H. Auke: yes, maybe to small.
[11:59:03] Leif H. Auke: at zoom level 15 -> 2.5 KM
[11:59:57] Leif H. Auke: at zoom level 14 -> 4.9 KM
[12:00:19 | Redigert 12:00:34] Leif H. Auke: (rule is, map dooble in height and width for each zoom level up)
[12:00:20] Leif H. Auke: :)
[12:00:36] Duong Thanh Huy: thanks for the info
[12:00:37] Duong Thanh Huy: :)
[12:00:55] Leif H. Auke: (I did spend some hours yesterday study) :)
[12:01:05] Leif H. Auke: and figure out the function
[12:01:47] Thai Huynh: :)
[12:01:48] Leif H. Auke: oki, maybe 1 to 14 calculated
[12:01:56] Leif H. Auke: (we try, see how it looks)
[12:03:10 | Redigert 12:03:23] Thai Huynh: Okie, my summary >> still imrpove single web page, commit in todays. Remove more files un-used for js :) all refer to auke-js
[12:03:59] Leif H. Auke: cool
[12:04:10] Duong Thanh Huy: ok Leif, you will write an abstract for that?
[12:04:35] Duong Thanh Huy: honestly I'm a little bit confused how to proceed. Maybe I will screw up
[12:04:37] Leif H. Auke: yes, on this page https://wiki.cantara.no/display/drone/Layers+and+summarized+positions
[12:05:22 | Redigert 12:06:15] Leif H. Auke: you cant screw up any existing with this, Is added functionallity, with no change in existing :)
[12:05:32] Leif H. Auke: no problem............................... |-(
[12:06:02] Leif H. Auke: maybe I can make some stubs and commit
[12:06:12] Duong Thanh Huy: yes, that would be great
[12:06:20] Leif H. Auke: oki . i do
[12:06:36] Thai Huynh: better make more unit Test and then i and huy can study :)
[12:06:41] Duong Thanh Huy: thanks Leif
[12:06:57] Duong Thanh Huy: please pull first, we made some changes

```
