# Documentation team3

## Source code
http://code.google.com/p/html5<sub>~code</sub>~camp-3/
 

## localStorage

We have implemented use of localstorage in order to prevent loss of data i the user navigates away from the site, close the browser or close the tabs. 

We solved this by implementing 3 features: A deamon, serializing of the form an storage to localstorage and deserializing of values back to form values. 

```title
var wunnyfumble = {
    initStore : function () {
        wunnyfumble.readAll();
        localStorage.clear();
        var daemon = function f () {
            wunnyfumble.saveArticle();
            setTimeout(f, 2000);
        };
        daemon();
    }

```

```title
   saveArticle : function () {
       var inputs = $("article > form > input[name]");
       var data = {};
       for (var key in inputs) {
           var input = inputs[key];
           data[input.name] = input.value;
       }
       var textArea = $("#article");
       data[textArea.attr("id")] = textArea.attr("value");
       localStorage.setItem("wunnyfumble.formdata", JSON.stringify(data));
   }
```

```title
   readAll : function () {
       var jsonString = localStorage.getItem("wunnyfumble.formdata");
       var data = JSON.parse(jsonString);
       for (var key in data) {
           var el = $("form > *[name='"+key+"']");
           var val = "localStorage{ " + data[key] + " }";
           switch (el.get(0).tagName.toLowerCase()) {
             case "input":
                 el.attr("value", val);
                 break;
             case "textarea":
                 el.html(val);
           }
       }

   }
};
```
