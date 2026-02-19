# CI Terminology

#### Job

In Hudson, each CI schedule is called a _job_. A job defines 

- when/how often a build should run
- One or more tasks. E.g.
    - Running a shell-script
    - Running ant tasks
    - Running maven goals

#### Build definition

Continuum has the concept of a _build definition_, which roughly translates to a job in Hudson. I.e., a build definition has a _schedule_ which explains when to run, a task to do (e.g. mvn clean install) and some configuration parameters. 

#### Artifact

An output from a job/build, examples:

- A JAR file
- An executable library 
- A web application WAR file
- A test report (text or html)
