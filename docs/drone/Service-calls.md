# Service calls

### [Service calls](Service-calls.md)

_Thai and Huy document_

##### Edited by Huy:

There are several web services available for testing the data only. 
Just go to 

- [http://89.221.242.66:8888/drone/getall](http://89.221.242.66:8888/drone/getall) for getting all drones available
- [http://89.221.242.66:8888/drone/register?id=?&name=?](http://89.221.242.66:8888/drone/register?id=?&name=?) for registering
- [http://89.221.242.66:8888/drone/id](http://89.221.242.66:8888/drone/id)
- [http://89.221.242.66:8888/drone/remove?id=?](http://89.221.242.66:8888/drone/remove?id=?)

Event Data could be access through 
- [http://89.221.242.66:8888/drone/get-event?accountID=demo&deviceID=demo](http://89.221.242.66:8888/drone/get-event?accountID=demo&deviceID=demo)
if there are no parameters for accountID and deviceID, all events will be retrieved
