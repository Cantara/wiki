# Webapp caching strategy

The purpose of this page is to describe one strategy for caching of static resources in a JSP based web application.   
The term "*assets*" is used to denote static files javascript, CSS, images, etc.

Credit go to [Trygve Laugstøl](https://twitter.com/trygvis) and [Erlend Hamnaberg](https://twitter.com/hamnis) for describing the concepts and suggesting implementations.

#### What

1. External assets should be cached forever.
2. Internal images should be cached forever.
3. Internal JavaScript and CSS files should be reloaded for every new release.
4. Minify JavaScript and CSS

#### Abstract implementation steps

1. Ensure internal and external assets are put in separate folders.
2. Ensure all external assets are versioned
   1. version in folder OR
   2. version in filename
3. Ensure internal images are versioned if changed.
4. Use [auto-versioning](http://derek.io/blog/2009/auto-versioning-javascript-and-css-files/) for internal assets.
5. Set Cache-Control headers
6. Remove ETags and Last-Modified headers (to increase chance of browsers have the same caching behaviour)
7. Minify JavaScript and CSS build time

#### 4. and 5. - Auto-version based on Tucket UrlRewriteFilter

###### pom.xml

###### Intermediate property file

###### ServletFilter to set session attribute

<http://www.tuckey.org/urlrewrite/>

###### In WEB-INF/urlrewrite.xml:

###### web.xml

###### Script tag in JSP file

Note the url encoding using c:url.

#### Resources

<http://derek.io/blog/2009/auto-versioning-javascript-and-css-files/>

Good guide to web caching: <http://www.mnot.net/cache_docs/>

<http://stackoverflow.com/questions/2630885/auto-versioning-of-static-content-with-jboss>
