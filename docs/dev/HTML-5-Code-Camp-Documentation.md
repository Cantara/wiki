# HTML 5 Code Camp Documentation

## New Javascript features/APIs
Canvas: http://dev.w3.org/html5/spec/Overview.html#the<sub>~canvas</sub>~element, https://developer.mozilla.org/en/Canvas_tutorial, 
Media playback: http://dev.w3.org/html5/spec/Overview.html#video, http://dev.w3.org/html5/spec/Overview.html#audio
Web Storage: http://dev.w3.org/html5/webstorage/
Drag and drop: http://html5doctor.com/native<sub>~drag</sub>~and-drop/
Online/Offline: http://www.whatwg.org/specs/web<sub>~apps/current</sub>~work/multipage/offline.html#offline

## Less strict markup, compared to xhtml
No need to end tags like p, img, etc. Simpler doctype. No need for quotations marks on element attributes, &lt;html lang=no&gt; is perfectly valid.

## New semantic elements
No need for &lt;div id="header"&gt; anymore. We now have &lt;header&gt;, &lt;footer&gt;, &lt;nav&gt;, &lt;section&gt;, &lt;article&gt;, &lt;aside&gt;.

## Observations

### Neither `<menu>` or `<command>` works in any browser

It would be great to add a toolbar (rich text area) using the new [`<menu>`](http://www.w3.org/TR/html5/interactive<sub>~elements.html#menus) and [`<command>`](http://www.w3.org/TR/html5/interactive</sub>~elements.html#the-command) elements, like this:
```html
<menu type="toolbar">
    <command type="checkbox" onclick="..." label="strong" icon="bold.gif" />
    <command type="checkbox" onclick="..." label="em" icon="italic.gif" />
    <command type="checkbox" onclick="..." label="link" icon="link.gif" />
</menu>
```

However, none of the elements are supported in browsers yet.

### Offline detection is pretty flaky
IE supports checking on navigator.onLine, but does not support listening for "online"/"offline" events. Chrome doesn't seem to support either.

### Local storage works well
Seems to work well in Chrome, see http://robertnyman.com/html5/webstorage/webStorage.html.

## Resources
- [HTML5 W3C Spec](http://www.w3.org/TR/html5/)
- [HTML5 differences from HTML4](http://www.w3.org/TR/html5-diff/)
- [ARIA Roles Model](http://www.w3.org/TR/wai-aria/roles)
