# Tech stack for modern frontend

#### Context

Set up a basic webapp using modern tools.

Tech stack: Grunt, Bower, Angular  
Generate skeleton with Yeoman.

#### Install software

- Install [node.js](http://nodejs.org/download/)

- Setup [Yeoman](http://yeoman.io/learning/)

  Unknown macro: {code}

  npm install -g yo --save-dev  
  npm install -g generator-angular --save-dev  
  npm install -g grunt-cli bower  
  npm install -g imagemin --save-dev  
  npm install -g imagemin-optipng --save-dev

  Not sure if it is necessary to install grunt-cli bower.

- Install [Ruby](http://rubyinstaller.org/)
- Install compass

  Unknown macro: {code}

  gem install compass

- Create git project

- Generate basic project structure for Angular app

  Unknown macro: {code}

  cd into dir   
  yo angular

#### Release and deploy to production

|  | **"yeoman-grunt error"** When yeoman/grunt/karma fails during **release:perform** Unknown macro: {code} mvn release:perform -Darguments="-Dyo.test.skip=true" |

###### Rationale for strategy

- Release: build a binary archive and deploy it to a Maven artifact repository (e.g. Nexus).

- Deploy to production: download artifact, unpack and move to correct location, reload web server (e.g. Apache, NginX or Jetty)

It is (at least) three ways to deploy a a javascript application to a production environment:

1. Deploy files to an existing web server (typically copy files to a folder served by Apache).
2. Run node and/or grunt on the production server.
3. Self-contained deployment (for example embedded Jetty in a zip or executable jar file)

Many considers option 3 the only sane solution, so we will describe how to set this up.

###### Self-contained deployment unit for static javascript application

Use standalone Java application with embedded Jetty to serve static files. This setup can for example be used to host a pure javascript frontend in a separate deployment unit.   
Note that backend services must set up [CORS](/web/20230531223636/https://wiki.cantara.no/display/dev/CORS "CORS") to circumvent the same origin policy.

The javascript files are scaffolded with yeoman and all files are placed in a separate *yo* folder (both sources, downloaded dependencies and generated files).   
The [yeoman-maven-plugin](https://github.com/trecloux/yeoman-maven-plugin) is used to call grunt from maven.

Standard maven plugins can the be used for the rest of the build process.

Frontend developers can work only with grunt and don't even need to have Maven installed.   
Backend developers need to have a some extra tools installed (node, grunt, bower++), but can call regular Maven commands to build, deploy and release as usual.

- [pom.xml yeoman and embedded jetty](/web/20230531223636/https://wiki.cantara.no/display/dev/pom.xml+yeoman+and+embedded+jetty "pom.xml yeoman and embedded jetty")

- [Main class with embedded jetty](/web/20230531223636/https://wiki.cantara.no/display/dev/Main+class+with+embedded+jetty "Main class with embedded jetty")

- [assembly.xml to create zip with support for config\_override](/web/20230531223636/https://wiki.cantara.no/display/dev/assembly.xml+to+create+zip+with+support+for+config_override "assembly.xml to create zip with support for config_override")

- Configuration is handled by overriding variables in a config\_override.js file which is put in a config\_override folder by the deployscript. index.html typically contains

  Unknown macro: {code}

  <script src="config/config.js"></script>  
  <script src="config\_override.js"></script>

  with contents something like

Unknown macro: {code}

var SOME\_SERVICE\_BASEURL = 'http://devtest.company.com:4301/context';

#### Read more

- [The State of JavaScript in 2015](http://www.breck-mckye.com/blog/2014/12/the-state-of-javascript-in-2015/)

- Resources
  - <http://blog.tfnico.com/2013/07/considerations-for-javascript-in-modern.html>
  - <http://thesassway.com/beginner/getting-started-with-sass-and-compass>
  - <http://yeoman.io/learning/>
  - <http://yeoman.io/codelab/prepare-production.html>
  - <http://gruntjs.com/getting-started>
  - <http://bower.io/>

- Integration grunt with Maven
  - <https://github.com/trecloux/yeoman-maven-plugin>
  - <http://addyosmani.com/blog/making-maven-grunt/>
  - <http://blog.bguiz.com/post/79804496081/making-maven-grunt-windows-edition/>
  - <https://github.com/allegro/grunt-maven-plugin>
  - <https://github.com/smh/grunt-maven-tasks>

- <http://eng.yammer.com/managing-node-js-dependencies-and-deployments-at-yammer/>
- <http://www.kidsil.net/2013/07/adding-config-to-your-angularjs-app/>
