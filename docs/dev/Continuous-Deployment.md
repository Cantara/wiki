# Continuous Deployment

_Automatically deploy the latest changes._

#### Continuous Deployment

A process that detects new releases into your software repo. Essentially, each time this process detects a new artifact, it will attempt to deploy it to a specified environment. Typically, this is applied in organizations where users want to test functionality as soon as possible. Example:

1. You commit your code
1. The Nightly Build deploys a artifact/application file into your repository
1. The Continuous Deployment process detects the new application and copies it into a deployment folder (see for example [How to deploy to IBM WebSphere 6.x](How<sub>~to</sub><sub>deploy</sub><sub>to</sub><sub>IBM</sub><sub>WebSphere</sub>~6-x.md))
1. The process executes a routine that instruments a test server into undeploying the previous version installing the new application  and booting it up
1. The process also triggers integration tests that verifies that the server is running correctly afterwards.

See also [Continuous deployment in 5 easy steps](http://radar.oreilly.com/2009/03/continuous<sub>~deployment</sub><sub>5</sub><sub>eas.html), [Why Continuous Deployment?](http://startuplessonslearned.blogspot.com/2009/06/why</sub>~continuous-deployment.html)
