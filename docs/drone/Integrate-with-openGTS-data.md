# Integrate with openGTS data

### Interation with openGTS database

mysql client tool >> http://89.221.242.66/phpmyadmin (account: root/radarteam$#@1)

##### Tables 

- Device -> containing list of trackers    
- EventData -> containing tracker data

##### Procedure for polling events

- -> service class with a tread loop every 10 second pulling all last events from all devices in opengts
- Distribute positions to trackers in aukegts

```

[10:30:43] Leif H. Auke: sorry
[10:31:03] Leif H. Auke: just grab all latest positions and distibute to trackers
[10:31:57] Leif H. Auke: we have a new service thread class -> called PollEvents (or something) with a loop every 10 seconds pulling all latest events from opengts
[10:32:01] Leif H. Auke: follow?

```

##### How to

A device must be created before event data can be stored.
Device use IMEI code of tracker as unique ID

When adding trackers in AukeGTS, also create a Device entry in opengts database. Add all trackers on account Demo.

##### Get last positions for each tracker

Getting last positions for each tracker. When reading in real, limit retrival by timestamp. This example show how to get last for each device in general. 
Using last timestamp registrered for each tracker. 

TimeStamp is in UTC second

```

SELECT

  d.deviceid, 
  e.altitude,
  e.latitude,
  e.longitude,
  e.heading,
  e.creationTime,
  e.timeStamp

FROM Device AS d INNER JOIN EventData AS e ON e.deviceid = d.deviceid 

WHERE 

timestamp >= 
   
   (
       SELECT max(timestamp) - 100 
       FROM EventData AS x 
       WHERE x.deviceid = d.deviceid

    )

```
