# Timeline

In 2007 we coined the term *timeline* to describe the coupling between JigZaw test model and agile development methodology and related concepts as Continuous Integration (CI) and continuous production. In other words, **when should a certain group of tests be run and who is responsible for executing them**. *Timeline* builds on [Multidimensional Test Categorization](/web/20210123065624/https://wiki.cantara.no/display/dev/JigZaw+Multidimensional+Test+Categorization "JigZaw Multidimensional Test Categorization")  and provides a starting point and some guidelines. All projects are different, so finding one timeline that will fit all projects is obviously not possible.

*Build pipeline* and *deployment pipeline* are newer terms for the same concepts. See references at the bottom for more resources.

#### Logical timeline

The logical timeline of a project may look something like the following:

1. Developer push/commit code
2. CI server compile and run tests
3. CI server deploys artifacts to artifact repository
4. Deployment artifact is installed in production

The steps may be different or more steps can be added. Both before and after each step tests and other verification measures can be applied.   
Different actors are involved: Developer, CI server, tester, orchestration tools, etc.

#### Getting started

1. Initially, run all tests as often as possible. All tests in the same group. All tests run both developer and CI server.
2. When adding tests with special characteristics, consider adding a tag. Common test groups: *slow*, *externalDatabase*, *dataDriven*
3. If it is inconvenient to run a certain group of tests before developer commit/push his/her code, consider excluding that group from the default test suite. The CI server should still run all tests.
4. The CI server should run all tests, but when? After every commit if possible. If this takes too much time, consider running some tests later.
5. The build artifacts can be deployed to an environment as part of a build step.
6. At some point the artifact will be deployed to production.

#### Example: concrete timeline

*[Diagram: test.phase.timeline]*

**Within each sprint**

| Actor | When | What | Commandline example |
| --- | --- | --- | --- |
| Developer | pre-commit | Default test suite | mvn clean install |
| CI server | post-commit | Default test suite + tests that require special environment | mvn clean install -DdatabaseX -DjmsServerY |
| CI server | Every hour | Slow tests | mvn clean install -DslowTests |
| CI server | On-successful build | deploy artifacts to artifact repository | mvn deploy |
| CI server | Nightly | Deploy to a test environment &   run data-bound tests using data recorded from production |  |
| Developer | End of sprint, before release | compare technical debt/accidental complexity metrics with metrics from previous release |  |
| Developer | End of sprint | release | mvn release:prepare & mvn release:perform |

#### See also

- [Deployment Pipeline](http://martinfowler.com/bliki/DeploymentPipeline.html) by Fowler mai 2009
- [What Is a Deployment Pipeline?](http://www.informit.com/articles/article.aspx?p=1621865&seqNum=2) from the book [Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation](http://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley/dp/0321601912)  By Jez Humble and David Farley, sept 2010
- [The Delivery Pipeline is your DevOps Signature](http://devops.com/blogs/delivery-pipeline-devops-signature/)
- [Configure and run a delivery pipeline in Jenkins](https://www.safaribooksonline.com/library/view/devops-in-the/9780132836357/part65.html) by Paul M. Duvall
- [Orchestrating Your Delivery Pipelines with Jenkins](http://www.infoq.com/articles/orch-pipelines-jenkins)

---

Back to [JigZaw Design Principles and Drivers](/web/20210123065624/https://wiki.cantara.no/display/dev/JigZaw+Design+Principles+and+Drivers "JigZaw Design Principles and Drivers")
