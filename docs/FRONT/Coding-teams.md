# Coding teams

# [Team 1](/web/20101022040118/http://wiki.cantara.no/display/FRONT/Team+1 "Team 1")

- Morgan Kjølerbakken
- Oddbjørn
- Thea Christine Steen
- Robin
- Stig Nicolaisen

# [Team 2](/web/20101022040118/http://wiki.cantara.no/display/FRONT/Team+2 "Team 2")

- Espen Dalløkken, <http://github.com/leftieFriele/h5o-team2>
- Helge Thomas Hellerud
- Jerome Lacoste, <http://github.com/lacostej/h5o-team2>
- Thomas Finneid

## Målet

- learning > delivery
  - learn by delivering
  - local (no server for all)
- Lage en blog editor uten noe admin interface
- Bruke mest mulig av det vi har lært
- Lage individuelle kompeonter først også forsøke å ved magi merge de til en app,

## Organization

- no functional design
  - very FOSS cathedral and bazaar
- start merging late (1030 today)
- small changes
  - git rules

## Koden

Du kan se en kjørende versjon på <http://totalworldannihilation.org/cc/blog.html>  
Den validerer selvsagt for HTML5 --> <http://html5.validator.nu/?doc=http%3A%2F%2Ftotalworldannihilation.org%2Fcc%2Fblog.html>

## Issues

- Drag and drop fungerte i Firefox men ikke i Opera....
- bug(s)
- PC died
- not all could git

## Learnings

- need the net...
- one can do much with little (editor, browser, git, net)
- when Jerome starts speaking french, better keep your head down

## Improvements (on the coding performance)

- polish feature focus ?
- sharing environment from the start ?
- less beers, more sleep

# [Team 3](/web/20101022040118/http://wiki.cantara.no/display/FRONT/Team+3 "Team 3")

- Anders Sandberg Nordbø
- Øyvind Aaraas
- Hans Ole
- Kristoffer
- Tobias

# [Team 4](/web/20101022040118/http://wiki.cantara.no/display/FRONT/Team+4 "Team 4")

- Rikard Halvorsen
- Ivar Conradi Østhus
- Arve Systad
- [Kris-Mikael Krister](/web/20101022040118/http://wiki.cantara.no/display/~km)
- Tor Martin

- [Code repository](#Team4-Coderepository)
- [Implementation](#Team4-Implementation)

- [Forms](#Team4-Forms)
- [Editor](#Team4-Editor)
- [Websockets using hosted Hookbox](#Team4-WebsocketsusinghostedHookbox)
- [Drag and Drop File Upload](#Team4-DragandDropFileUpload)
- [Canvas](#Team4-Canvas)

# Code repository

We are using Github as a repository for our code. Everyone has read access. The main HTML is located in dashboard.html, and the scripts of interest are located in the scripts-folder. See <http://github.com/ivarconr/html5-codecamp> for these files.

# Implementation

We have built a single-page HTML5-based web page that does not require any plugins to render. We have focused on the following technologies.

- HTML5 declarative form validation
- HTML5 canvas logo together with the new canvas javascript APIs
- Canvas and javascript for viewing images in a slideshow with overlay blending
- Local storage using the new WebSQL APIs (blog posts are stored locally)
- New CSS3 properties are utilized
- Websockets implementation using hosted Hookbox to publish new blog posts.
- Using a rich text editor powered by pure javascript
- Web fonts for header text

The following is a list of possible improvements, patches are welcome

- Additional storage of blog posts on a server
- Authentication
- Adding comments to blog posts

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

CKEditor <http://ckeditor.com/>

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

Ripped from Robert Nyman: <http://robertnyman.com/html5/fileapi/fileapi.html>

### Canvas

Cheat Sheet: <http://www.selfhtml5.org/wp-content/uploads/2010/07/HTML5_Canvas_Cheat_Sheet.png>

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

# [Team 5](/web/20101022040118/http://wiki.cantara.no/display/FRONT/Team+5 "Team 5")

- Tux
- Asbjørn Goa
- Egil
- Jone Lura
- Aud Marie

# [Team 6](/web/20101022040118/http://wiki.cantara.no/display/FRONT/Team+6 "Team 6")

- Anton
- Svein Arild
- Gunnar
- Trygve Lie
- Viggo Normann
- Gregers
