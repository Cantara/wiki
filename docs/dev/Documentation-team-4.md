# Documentation team 4

### Forms

```
                <form id="addPost" method="POST">
                    <label for="title">Title</label>
                    <input type="text" name="title" id="title" required>

                    <label for="content">Content </label>
                    <textarea name="content" id="content"></textarea>

                    <label for="files-upload">Image</label>
                    <input id="files-upload" name="file-upload" type="file" multiple>

                    <p id="drop-area">
                        or drag and drop files here
                    </p>

                    <h3>Uploaded files</h3>
                    <ul id="file-list">
                        <li class="no-items">(no files uploaded yet)</li>
                    </ul>
                    <input type="submit">
                </form>
```

### Editor
CKEditor http://ckeditor.com/

### Websockets using hosted Hookbox

```
var ourUsername;
var subscription = null;
var conn = null;
$(function() {
    conn = hookbox.connect('http://km.hosted.hookbox.org');
    conn.onOpen = function() { console.log("connection established!"); }
    conn.onError = function(err) { alert("connection failed: " + err.msg); }

    conn.subscribe("my_events");

    conn.onSubscribed = function(channelName, _subscription) {
        ourUsername = conn.username;
        console.log("onsubscribed with username " + ourUsername);
        subscription = _subscription;

        subscription.onPublish = function(frame) {
            if (frame.user != ourUsername) {
                console.log(frame.user + " said: " + frame.payload);
                html5team4.webdb.addBlogpost(JSON.parse(frame.payload));
            }
        }
    }

});

function publishBlogPost(blog) {
    console.log("skal publishe %o ", blog);
    console.log(subscription);
    try {
        conn.publish("my_events", JSON.stringify(blog));

    } catch (e) {
        console.log(e);
    }
}
```

### Drag and Drop File Upload
Ripped from Robert Nyman: http://robertnyman.com/html5/fileapi/fileapi.html

### Canvas
Cheat Sheet: http://www.selfhtml5.org/wp-content/uploads/2010/07/HTML5_Canvas_Cheat_Sheet.png

Our "Fb" logo is coded as follows:

```
$(function() {
  var logoCanvas = document.getElementById('logo');
  var ctx = logoCanvas.getContext('2d');
  

  // Build the B
  ctx.beginPath();
  ctx.moveTo(90, 60);
  ctx.lineTo(90, 140);
  ctx.lineTo(110, 140);
  ctx.lineTo(110, 60);
  ctx.moveTo(110, 115);
  ctx.arc(110, 115, 25, Math.PI*-0.5, Math.PI*0.5, false);
  ctx.closePath();
  
  // set up the stroke for F
  ctx.strokeStyle = "#ffffff";
  ctx.stroke();
    
  
  // setup the line style
  ctx.strokeStyle = '#ffffff';
  ctx.lineWidth = 2;
  ctx.fillStyle = "#ffffff";
  
  //cxt.arc(x,y,radius,Math.PI*startingAngle,Math.PI*endingAngle,anticlockwise);
  ctx.arc(110, 115, 25, Math.PI*-0.5, Math.PI*0.5, false);
  ctx.fill();
  
  // colour the path
  ctx.stroke();
  
  ctx.rotate(0.1);

  // Build the shadow for F
  ctx.beginPath();
  ctx.moveTo(20, 20);
  ctx.lineTo(20, 140);
  ctx.lineTo(60, 140);
  ctx.lineTo(60, 100);
  ctx.lineTo(100, 100);
  ctx.lineTo(100, 70);
  ctx.lineTo(60, 70);
  ctx.lineTo(60, 50);
  ctx.lineTo(100, 50);
  ctx.lineTo(100, 20);
  ctx.lineTo(20, 20);
  ctx.closePath();
  
  // set up the stroke for F
  ctx.lineWidth = 1;
  ctx.strokeStyle = "#ffffff";
  ctx.stroke();
  
  //Create a drop shadow
  ctx.shadowOffsetX = 5;
  ctx.shadowOffsetY = 5;
  ctx.shadowBlur = 7;
  ctx.shadowColor = "#A2BAA8";

  ctx.fillStyle = "#ffffff";
  ctx.fill();
        
  //Turn off the shadow
  ctx.shadowOffsetX = 0;
  ctx.shadowOffsetY = 0;
  ctx.shadowBlur = 0;
  ctx.shadowColor = "transparent";
  
  // Build the F
  ctx.beginPath();
  ctx.moveTo(20, 20);
  ctx.lineTo(20, 140);
  ctx.lineTo(60, 140);
  ctx.lineTo(60, 100);
  ctx.lineTo(100, 100);
  ctx.lineTo(100, 70);
  ctx.lineTo(60, 70);
  ctx.lineTo(60, 50);
  ctx.lineTo(100, 50);
  ctx.lineTo(100, 20);
  ctx.lineTo(20, 20);
  ctx.closePath();
  
  // set up the stroke for F
  ctx.strokeStyle = "#DFD";
  ctx.stroke();
  
  // set up the gradient for F
  var grad = ctx.createLinearGradient(0, 0, 0, 140);
  grad.addColorStop(0, '#38F56B'); 
  grad.addColorStop(1, '#228F3F'); 

  // apply the gradient to the F
  ctx.fillStyle = grad;
  ctx.fill();

});
```

### Web fonts

```
@font-face {
	font-family: 'Harabara';
	src: url('fonts/Harabara.ttf');
	src: local('?'), url('fonts/Harabara.ttf') format('truetype');
	font-weight: normal;
	font-style: normal;
}
```
