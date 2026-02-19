# Development and test FAQ

### I get logged out the moment I refresh the page. What's the problem?

Check the properties file in SSOLoginWebApp you are running. The cookiedomain property should be equal to the domain name your application is running in.  
In default case, this property can be left empty, unless there are some cases when your actual domain is behind firewall
