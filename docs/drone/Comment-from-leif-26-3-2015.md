# Comment from leif 26.3.2015

### [Comment from leif 26.3.2015](Comment-from-leif-26-3-2015.md)

Look nice so far. 

I tried the map. Could not test run calculator. 

**Some functionality issues:**

- To be discussed -> see comment on current map view and loadTrackWithinView
- Showing flying and stand still drones in different color ?

**Some develop issues:**

- consider making some unit tests?
- Using logger

**MILESTONE**

Showing moving drones on map by 31 of marsh ??

**Skype comments:**

```

HI Guys
[23:09:11 | Redigert 23:10:20] Leif H. Auke: I looked. Look fine. Did some comments and adjustments in code. Thai -> look this function
[23:09:12] Leif H. Auke: public List<PositionUnit> loadTrackWithinView(double lat, double lon, int height, int width);
[23:09:58 | Redigert 23:10:37] Leif H. Auke: Seem to me that we within a couple of days (maybe over weekend) are ready for a live moving drones demo ?
[23:10:05] Leif H. Auke: :)
[23:19:37] Leif H. Auke: Look fine getting drone information within current view (the circle), but maybe to clearify what I mean with 'current view' = the map shown on page at any time. Mean when zooming map in, the current view get smaller and zooming out = current view get bigger.
[23:20:24] Leif H. Auke: The retieval loadTrackWithinView -> is to retieve any drone position within this map view.
[23:30:55] Leif H. Auke: One other factor. could we show on map with a color or something if drone is moving or stand still ?
[23:31:35] Leif H. Auke: (this is some idea we might consider as we go)
[23:33:52 | Redigert 23:34:27] Leif H. Auke: When flying drones. The drones possibly stand still on ground with gps on and still reportig position. People fly normally 10-20 minutes flight. So we distinct between drones standing still on the ground or actually in the air. We might consider only show drones actually in the air (having speed)

```
