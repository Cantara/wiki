# Web page for register and update tracker info

### [Web page for register and update tracker info](Web-page-for-register-and-update-tracker-info.md)

##### Comments Leif 22.4.2015

###### Use case update user update his trackers

User must be able to 

1. Add a tracker -> put unique code (ref structure)
1. Update tracker -> Enter unique ID and get tracker info
1. Delete a tracker -> Enter unique ID and delete tracker

###### Structure:

Because reals trackers are registered wit a unique ID (I think IMEI number) and data retrieved is identified with this unique id.\\

**IMPORTANT:** look/study openGTS to see how they do it, use same type of device identification that openGTS do

Either:

1. UMEI is a unique code, tracker id = IMEI code for real trackers
1. Sim ID 
1. UUID

For simulated tracker, (layer SIMULATED, no user registry)

I think user only register tracker for now in layer REAL, later a tracker might associate in more layers, but the we must add some structure to tracer object to handle this, and some service call to list available layers.

For first, real tracker always register in layer REAL (maybe just remove this selection from UI)

###### UI

In general we have a User page for users, containing tracker registration

1. Have a full page for this (remove the split on bottom) 
1. More explain in page, ie. title "update your tracker"
1. Center page (not that wide one)

1. Make a menu on top "register trackers"
1. Admin is for infernal use

###### view different layers

- Must be able to select layer to view on map
- First version, only one layer, later on, tick on layers to show simultaniusly

---

### Specification 

**must do:** Define what fields need for tracker info 

- maybe we make simple page for e.x show list tracker in grid and click per drone for edit/delete
- Store tracker data to json files
- Update Device table in opengts when storing json file

```

about webpage >> maybe we added accout admin for login and management tracker ?
[11:22:50] Leif H. Auke: hmm
[11:24:20] Leif H. Auke: for each tracker owner I think for now we only user tracker Id. So for a user to be able to update his trackers add tracker id to page and just retrieve..
[11:24:39] Leif H. Auke: (no user account system for now)
[11:24:48] Duong Thanh Huy: (y)
[11:25:41 | Redigert 11:26:16] Leif H. Auke: for admin of all -> yes one page for list all with a single password for access to page
[11:25:54] Leif H. Auke: (make it very very simple)

```

```

maybe we make simple page for e.x show list tracker in grid and click per drone for edit/delete
[10:18:26] Duong Thanh Huy: should we make a database for such information?
[10:19:18] Leif H. Auke: -> we store tracker info as json files, but -> we must also update the device table in open GTS to be able to retrive posistions via openGTS
[10:19:57] Leif H. Auke: si i think aukeGTS store tracker as json files, but we just add same infor to openGTS table when storing.
[10:20:16] Leif H. Auke: ?
[10:20:31] Leif H. Auke: because we try to make aukeGTS independent from openGTS
[10:20:54] Duong Thanh Huy: that's a better approach. Then we could have more freedom
[10:20:59] Leif H. Auke: yep

```
