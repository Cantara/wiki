# Documentation5

## Observations

### Opera does not support the poster attribute on the video tag.
To display an image while video is loading, or fails. like this:
```html
<video poster="path/to/image.ext">
</video>
```
However the Opera people have confirmed that this will be fixed in the next minor version of Opera.

## Code snippets

### Local storage:
```html
jQuery(function($) {
    $(".autostore").keyup(function(){
	localStorage.setItem($(this).attr("id"), $(this).val());
    });
    if (localStorage.length > 0) {
	for (i=0; i<=localStorage.length-1; i++) {
            key = localStorage.key(i);
	    val = localStorage.getItem(key);
	    $("#" + key).val(val);
	}
    }
});
```
