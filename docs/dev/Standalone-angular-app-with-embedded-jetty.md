# Standalone angular app with embedded jetty

###### Rationale for strategy

- Release: build a binary archive and deploy it to a Maven artifact repository (e.g. Nexus). 

- Deploy to production: download artifact, unpack and move to correct location, reload web server (e.g. Apache, NginX or Jetty) 

It is (at least) three ways to deploy a a javascript application to a production environment: 
1. Deploy files to an existing web server (typically copy files to a folder served by Apache). 
1. Run node and/or grunt on the production server. 
1. Self-contained deployment (for example embedded Jetty in a zip or executable jar file) 

Many considers option 3 the only sane solution, so we will describe how to set this up. 

###### Self-contained deployment unit for static javascript application 

Use standalone Java application with embedded Jetty to serve static files. This setup can for example be used to host a pure javascript frontend in a separate deployment unit. 
Note that backend services must set up [CORS](CORS.md) to circumvent the same origin policy.  
 
The javascript files are scaffolded with yeoman and all files are placed in a separate _yo_ folder (both sources, downloaded dependencies and generated files). 
The [yeoman<sub>~maven</sub><sub>plugin](https://github.com/trecloux/yeoman</sub><sub>maven</sub>~plugin) is used to call grunt from maven. 

Standard maven plugins can the be used for the rest of the build process. 

Frontend developers can work only with grunt and don't even need to have Maven installed. 
Backend developers need to have a some extra tools installed (node, grunt, bower++), but can call regular Maven commands to build, deploy and release as usual. 

- [pom.xml yeoman and embedded jetty](pom<sub>~xml</sub><sub>yeoman</sub><sub>and</sub>~embedded-jetty.md)

- [Main class with embedded jetty](Main<sub>~class</sub><sub>with</sub><sub>embedded</sub>~jetty.md)

- [assembly.xml to create zip with support for config_override](assembly<sub>~xml</sub><sub>to</sub><sub>create</sub><sub>zip</sub><sub>with</sub><sub>support</sub><sub>for</sub>~config_override.md)

- Configuration is handled by overriding variables in a config_override.js file which is put in a config_override folder by the deployscript. index.html typically contains 
```
<script src="config/config.js"></script>
<script src="config_override.js"></script>
```
with contents something like 

```
var SOME_SERVICE_BASEURL = 'http://devtest.company.com:4301/context';
```
