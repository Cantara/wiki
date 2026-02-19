# Comment leif 27.3.2015

### [Comment leif 27.3.2015](Comment<sub>~leif</sub><sub>27</sub><sub>3</sub>~2015.md)

Use : map.getBounds()

Send to server (posupper.lon,posupper.lat, postlower.lon,poslower.lat)

caclulate withing

```

if ((post.lon >= posupper.lon && post.lon <= poslower.lon)) &&
    (post.lat>= posupper.lat && post.lat <= poslower.lat) 

{
   isok

}
 

```

- Nice try out page to map [http://www.w3schools.com/googleAPI/tryit.asp?filename=tryhtml_ref_getzoom](http://www.w3schools.com/googleAPI/tryit.asp?filename=tryhtml_ref_getzoom)

```

<!DOCTYPE html>
<html>
<head>
<script
src="http://maps.googleapis.com/maps/api/js">
</script>

<script>
var map;
function initialize()
{
var mapOpt = {
  center:new google.maps.LatLng(51.508742,-0.120850),
  zoom:6,
  mapTypeId:google.maps.MapTypeId.ROADMAP
  };
map=new google.maps.Map(document.getElementById("googleMap"),mapOpt);
}

google.maps.event.addDomListener(window, 'load',initialize);
</script>
</head>
<body>

<button onclick="alert(map.getBounds());">Get bounds</button>

<button onclick="alert(map.getZoom());">Get Zoom</button>
<br><br>
<button onclick="alert(map.getCenter());">Get Center</button>
<br><br>
<div id="googleMap"style="width:400px;height:300px;"></div>

</body>
</html>

```
