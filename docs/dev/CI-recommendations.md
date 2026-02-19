# CI recommendations

#### CI server responsibilities

The CI server is a critical component in Enterprise Maven Infrastructure. It has the following responsibilities: 

1. Automatic testing 
2. Automated warning notification
3. Automatic deployment of snapshot versions to a build artifact repository manager 
4. Site information deployment (maven-site-plugin)
5. Graphical front-end for performing releases with the maven-release-plugin (supported in Continuum v1.1). 

There are several CI servers on the market - see [sysadm:Continuous Integration Server Overview](../sysadm/Continuous-Integration-Server-Overview.md) for a feature comparison. 

#### Basic CI strategy 

We have found that the [classic build definitions](http://wiki.community.objectware.no/display/smidigtonull/CI+Strategies#CIStrategies-Classicbuilddefinitions) are not sufficient to implement a complete CI strategy. Instead we base our strategies on [JigZaw](JigZaw.md). A basic CI strategy is illustrated by the build definitions listed in the table below:  

| Name | Maven example | Schedule (cron expressions) | Purpose |  |
| --- | --- | --- | --- | --- |
| Quick test | mvn deploy | every 10-30 minutes (three times per hour: 0 0/20 * * * ?) | Detect build failures as soon as possible. This is the default build and should not require any special parameters or any specific environment. deploy is also important to ensure that the latest snapshots are always available. |  |
| Environment-dependent tests | mvn clean deploy -Denv=someEnvironment | at least nightly (0 0 3 * * ?), preferably every hour (0 0 * * * ?) | Run tests that require some specific environment. |  |
| Documentation build | mvn clean site-deploy | at least nightly, preferably every third hour: 0 0 0/3 * * ? | Its purpose is to deliver automatic reports, docs and analysis of the latest code found in the source repository. In case of a build failure, the job **should not break**, proceeding to cover as many modules as possible with documentation. |  |

Deployment units like e.g. RPM has seldom any environment-dependent tests and the documentation build is probably not that useful. The following _Project Groups_ may thus be a good starting point: 
- lib 
    - Quick test
    - Environment-dependent tests
    - Documentation build
- products 
    - ** Quick test

#### Resources

- [Continuous Integration (CI), by Martin Fowler](http://www.martinfowler.com/articles/continuousIntegration.html)
