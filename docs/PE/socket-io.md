# socket.io

### socket.io

Internet have for many years been limited by the half duplex in HTTP. This is about to change with the WebSocket specification recently landed as a native part in modern browsers. WebSockets are full duplex communication between the server and the browser. Tough, the need for doing full duplex communication have been present for a long time and there has been several attempts to provide that even before WebSockets.

socket.io is a node.js library which implements the native WebSocket API found in modern browser and provides fallback strategies for older browsers. Einar Otto Stangvik has implemented his own WebSocket library for node.js and are a core developer on socket.io. He will take us trough the exiting world of full duplex communication between the server and browser.
