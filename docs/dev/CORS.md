# CORS

#### Learn

- What is CORS? <http://www.w3.org/wiki/CORS_Enabled#What_is_CORS_about.3F>
  - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests>

- Browser support: <http://enable-cors.org/client.html>.

- What about security? <https://code.google.com/p/html5security/wiki/CrossOriginRequestSecurity>

#### How to set up CORS in Jetty

<http://www.eclipse.org/jetty/documentation/current/cross-origin-filter.html>, requires jetty-servlets.

The CrossOriginFilter should be configured on the backend server which expose the JSON over http APIs. In a scenario with a separate deployment unit which serves the frontend, only the backend server needs the CORS setup.

###### pom.xml

###### web.xml

#### Other resources

- <http://spring.io/guides/gs/rest-service-cors/#_filter_requests_for_cors>

- <http://chstrongjavablog.blogspot.no/2013/04/enabling-cors-for-jetty.html>
