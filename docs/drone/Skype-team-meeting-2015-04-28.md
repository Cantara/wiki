# Skype team meeting 2015.04.28

### [Skype team meeting 2015.04.28](Skype-team-meeting-2015-04-28.md)

Main rest objectives:

1. Simulated drones back working (including showing zoom levels)
1. Show and register trackers (exclude simulated layer)
1. Thai -> one extra task for you -> add to wiki (show me) how to deploy the site

Desition:

Next [Sprint 3](Sprint-3.md) starts Monday 4 of may

```

Yep
[08:32:43] Leif H. Auke: first -> I looked the web page now -> Look very good. excatly as I image we should have.
[08:33:00] Leif H. Auke: Some simple update of trackers.
[08:33:10] Leif H. Auke: But I get som error when I try to add.
[08:33:36] Thai Huynh: what's is error ?
[08:33:53] Duong Thanh Huy: please use number for the ID field
[08:34:14] Leif H. Auke: ahh
[08:34:20] Leif H. Auke: Ok. I test again
[08:34:22 | Redigert 08:34:31] Thai Huynh: ahh, I still not yet apply validation on UI
[08:34:33] Stig Førrisdal: Good morning, Guys ;)
[08:34:45] Thai Huynh: morning Stig
[08:34:48] Leif H. Auke: Good morning Stig
[08:35:02] Duong Thanh Huy: morning
[08:35:58] Stig Førrisdal: We will continue with the Joomla environment in 10 hours...
[08:36:10] Thai Huynh: (y)
[08:36:42] Thai Huynh: for now you need only copy demo.html  put on your joomla server and run
[08:36:58] Thai Huynh: I had remove un-necessary files long time ago
[08:38:03] Leif H. Auke: Ok
[08:38:24] Leif H. Auke: Stig -> Is there any assistance you need from Thai or Huy
[08:38:43] Leif H. Auke: ?
[08:38:57] Stig Førrisdal: No, we have the resources we need at the moment..
[08:39:08] Stig Førrisdal: http://89.221.242.66:8080/drone/demo.html
[08:39:16] Stig Førrisdal: Can we use this URL?
[08:39:38] Leif H. Auke: I mean technical assiistance how to integrate or how existing solution works ?
[08:39:49] Stig Førrisdal: …no need...
[08:40:15] Leif H. Auke: ok
[08:40:32] Leif H. Auke: Ok -> lets get back to status
[08:40:47] Leif H. Auke: Short status from Huy?
[08:41:10] Duong Thanh Huy: yes
[08:41:28] Duong Thanh Huy: I finished up the layer
[08:41:37] Duong Thanh Huy: finished the polling EventData
[08:42:01] Duong Thanh Huy: create, update and delete from Device table
[08:42:15] Duong Thanh Huy: everything is parameterized for reusing
[08:43:08] Duong Thanh Huy: I need sometime to clean up, reload all Tracker when the server starts
[08:43:17] Duong Thanh Huy: that's all from me
[08:43:19] Duong Thanh Huy: any questions?
[08:43:32] Leif H. Auke: very good
[08:44:01] Leif H. Auke: So missing reload existing trackers when server start ?
[08:44:12] Duong Thanh Huy: yup, still working on that
[08:44:21] Leif H. Auke: finish before holyday?
[08:44:48] Duong Thanh Huy: I hope, but I'm afraid that I could break something
[08:45:30] Duong Thanh Huy: so I will commit today
[08:45:38] Leif H. Auke: hmm. ok.
[08:45:50] Duong Thanh Huy: but everything else should be fine
[08:46:13] Leif H. Auke: Q2: Live testing -> when can we enter a mobilphone as tracker and run live?
[08:46:50] Duong Thanh Huy: I think technically we can now?
[08:47:05] Leif H. Auke: but we need to do the procedure ?
[08:47:50] Leif H. Auke: ok -> maybe extend this testing to next sprint
[08:47:58] Duong Thanh Huy: what procedure please? I never tried to use mobile but according to what you said then it is possible now
[08:48:21] Leif H. Auke: the procedure of using a mobilephone as tracker and see the tracks in the map :)
[08:48:35] Leif H. Auke: yes
[08:48:44] Duong Thanh Huy: yes I never tried, I would need help from you and Thai
[08:48:53] Leif H. Auke: yep
[08:49:03] Leif H. Auke: ok. We extend this test to next sprint
[08:49:20] Thai Huynh: Yes, we can test together
[08:49:29] Leif H. Auke: Q3: What about simulated drones?
[08:50:50 | Redigert 08:50:53] Thai Huynh: I had issues relate to  method >>>
 public Collection<Tracker> loadWithinView(BoundingBox boundary, int zoom, String layerId) {..}
[08:51:16] Thai Huynh: and this methods can not load correct simulated drones
[08:51:26] Thai Huynh: maybe we need consider this again
[08:51:31] Duong Thanh Huy: I didn't touch it for long time
[08:51:54] Duong Thanh Huy: the simulated ones are already there, but is there something wrong with the zoom calculation?
[08:52:25] Leif H. Auke: hmm
[08:53:05] Leif H. Auke: This is suppose to load either from real or simulated layer. Same function for both. If real work, i think simulated will work as well.
[08:53:07] Leif H. Auke: ?
[08:54:19] Leif H. Auke: ok -> its very important we get the simulated drones back on map, because we use this for demostration purpose.
[08:54:53 | Redigert 08:55:24] Leif H. Auke: 1. they must run, 2. the loadView funtion must work
[08:55:44] Duong Thanh Huy: they are running. A Thai, can you check the load function?
[08:57:05] Thai Huynh: I had check and we can not simalated drone now :)
[08:57:11] Thai Huynh: look at    if(zoomLayers.containsKey(zoom)) {
             
                // LHA: if summarized exists, got trackerSUM from there
             return zoomLayers.get(zoom).loadWithinView(boundary, zoom);
             
            } else {
[08:57:35] Leif H. Auke: yes
[08:57:40] Thai Huynh: and next is 

 block.lock();

                for (Tracker positionUnit : getPositions()) {
}
[08:57:47] Leif H. Auke: yes
[08:57:48] Leif H. Auke: :)
[08:57:58] Thai Huynh: getPositions() << return empty always
[08:58:23 | Redigert 08:58:51] Thai Huynh: so I think we need update  position when make simulated drone ?
[08:58:48] Leif H. Auke: yes -> of cource
[08:59:03] Leif H. Auke: But Thai ->
[08:59:16] Leif H. Auke: You removed the creating of drones
[08:59:21] Leif H. Auke: that is the problems
[08:59:34] Duong Thanh Huy: I've put them back?
[08:59:35] Thai Huynh: no, I had add back again
[08:59:48] Thai Huynh: yep
[08:59:58] Leif H. Auke: ok
[09:00:31] Stig Førrisdal: Guys: Will we have Drones visible in 10 hours (tonight)
[09:01:28] Thai Huynh: btw, Huy: look at

 @PostConstruct
    public void initTrackerService() {
        crudDeviceDao.setPersistentClass(Device.class);
     logger.info("initializing tracker services");
        
     List<Tracker> trackers = new TrackerServiceFacade().createTrackersForCapitalCities();
        
        for (Tracker tracker : trackers) {
            TrackerData.getInstance().register((Observer) tracker);
        }
        logger.info("finished initializing tracker services");
    
        TrackerData.getInstance().startCalculate();
    }

>>> we need add some logic add position into Zoomlayer
[09:01:29] Thai Huynh: :)
[09:02:06] Duong Thanh Huy: what logic should we add?
[09:03:02] Duong Thanh Huy: ok, I will debug to see what happened to the zoom functionality
[09:03:11] Leif H. Auke: >>> we need add some logic add position into ZoomlayerIts all there
[09:03:13] Thai Huynh: Yes, the better debugs and see
[09:04:02] Leif H. Auke: Look positioncalculator ->
[09:04:03] Leif H. Auke:  trackerLayer.calculateZoomLayers();
[09:04:28] Leif H. Auke: but position calculator must run
[09:04:41] Leif H. Auke: Ok -> Here is the deal........
[09:05:20] Leif H. Auke: Thai -> when add, listing creating etc trackers, skip all about simulated layer
[09:05:28] Leif H. Auke: (so we dont show a list of simulated)
[09:06:13] Leif H. Auke: Huy -> make sure simulated is added an position calculator is running and loadview work for all zomm levels
[09:06:19] Thai Huynh: Yep
[09:06:19] Leif H. Auke: (I think it does)
[09:06:49] Leif H. Auke: We reserv simulated layer for server simulations and automatically added trackers
[09:07:31] Leif H. Auke: Thai -> make sure map postions from zomm level 1-15 also show in map
[09:07:53] Leif H. Auke: BIG Q:
[09:08:11] Leif H. Auke: Could we do this today and make sure we have a running demo system by tonight ???
[09:09:02] Thai Huynh: Ok, its fine for me
[09:09:09] Duong Thanh Huy: fine for me sir
[09:09:41] Leif H. Auke: (handshake)
[09:09:53] Leif H. Auke: Nest Q: You start holyday tomorrow?
[09:10:11] Duong Thanh Huy: yes, I will take holiday tomorrow
[09:10:21] Duong Thanh Huy: public holiday
[09:10:46] Leif H. Auke: yep -> So we finish this sprint today and start the next on monday ?
[09:11:02] Duong Thanh Huy: yes, that will be great
[09:11:10] Leif H. Auke: ok we do that
[09:11:17] Leif H. Auke: but....
[09:11:39] Leif H. Auke: -> lets put all togheter today
[09:11:57 | Redigert 09:12:04] Leif H. Auke: 1. simulated drones back working (including shoing zoomlevels)
[09:12:33] Leif H. Auke: 2. show and register trackers (exclude simulated layer)
[09:13:28] Leif H. Auke: main objective today -> When Stig integrate with droneradar site tonight it possible to show simulated drones flying
[09:13:33] Leif H. Auke: ???
[09:14:26] Leif H. Auke: Thai -> one extra task for you -> add to wiki (show me) how to deploy the site
[09:14:43] Leif H. Auke: (in case I need to fix anything while you are away)
[09:15:47] Thai Huynh: yes
[09:16:15 | Redigert 09:16:35] Thai Huynh: About main objective today >> we will try fix ASAP
[09:16:46] Thai Huynh: One Q ?
[09:17:07] Leif H. Auke: yepp
[09:17:39] Leif H. Auke: Stig -> you there ?
[09:18:16] Thai Huynh: 2. show and register trackers (exclude simulate)
[09:18:23] Thai Huynh: show real drone ?
[09:19:35] Leif H. Auke: yes
[09:20:01] Leif H. Auke: means. we only registere trackers in real.
[09:20:12] Thai Huynh: yes, ready is done so far
[09:20:39] Duong Thanh Huy: it is like that with the latest version
[09:21:03] Leif H. Auke: I was thinking -> if we show 100 simulated trackers in list, its confusing. So better leve them out of list :)
[09:21:05] Thai Huynh: but for show real >> maybe i will make selection box on Home Page allow user select view layer ?
[09:21:27] Leif H. Auke: but for show real >> maybe i will make selection box on Home Page allow user select view layer ?Yes, if you can. Its better
[09:21:37] Leif H. Auke: (handshake)
[09:22:13] Leif H. Auke: purpose was -> remove confutions when register :)
[09:22:46] Leif H. Auke: okay -> all setteled ?
[09:23:28] Leif H. Auke: You think you can get it back running so its possible to do integration work on droneradar site tonight, and see som nice simulated drones flying ?
[09:23:59] Leif H. Auke: (wasntme)
[09:24:21 | Redigert 09:24:31] Thai Huynh: OK, if  service ready and work correct then I can do it in today
[09:25:17] Leif H. Auke: Well -> you both must work togehter make sure all working (common responsibillity)
[09:25:27] Leif H. Auke: (wait)
[09:25:31 | Redigert 09:25:31] Duong Thanh Huy: sure
[09:25:31] Duong Thanh Huy: :)
[09:25:43] Thai Huynh: of course
[09:25:51] Leif H. Auke: :)
[09:25:52] Thai Huynh: we are team :)
[09:25:58] Leif H. Auke: yes, we are
[09:26:16] Leif H. Auke: okay -> Lets talk som later today and make a status ?
[09:27:12] Thai Huynh: Okie
```
