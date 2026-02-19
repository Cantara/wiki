# Deploy AWS Lambda

### What

1. Build über jar (jar with all dependencies) file and upload to Maven artifact repository
2. Download jar file and upload to S3.
3. Deploy lambda

### Strategy for DevTest, Systest and Prod environment

We support three environments; Devtest, Systest and Production. Devtest environment is automatically updated with latest and greatest version. Test environment is automatically updated with the latest release. Manual deploy to production. This set up supports continuous delivery, and it is easy to enable continuous deployment when/if we want.

Continuous deployment means that every change is automatically deployed to production. [Continuous delivery](https://en.wikipedia.org/wiki/Continuous_delivery) means that the team ensures every change can be deployed to production, but may choose not to do it.

We use maven profiles to differentiate deployment to different environments. lambda-deploy-devtest/lambda-deploy-systest profiles are using executions to hook into deploy phase and run plugin goal deploy-lambda.

| Trigger | CI server | Plugin internals | Comment |
| --- | --- | --- | --- |
| 1. Developer: push to Git   2. mvn clean deploy -Plambda-deploy-devtest | Job:  clean deploy -U -Plambda-deploy-devtest | alias LATEST and withPublish=false and forceUpdate=true is set in pom.xml |  |
| 1. CI server: successful mvn release | Release goals and options:  release:perform -Plambda-deploy-systest | alias <version>\* and withPublish=true is set in pom.xml |  |
| 1. CI server: manually | Job:   org.apache.maven.plugins:maven-dependency-plugin:2.10:copy artifact  mvn lambda:deploy-lambda -Dlambda.functionCode=/tmp/$MVN\_RELEASE\_VERSION.jar -Dlambda.version=$MVN\_RELEASE\_VERSION -Plambda-deploy-prod -DremoteRepositories= | alias <version>\* and withPublish=true is set in pom.xml | If using the same AWS account for test and prod environment, this deployment can easily be done manually without a CI server job. |

- (version is same as version from jar file, but with "-" instead of ".")

Deploy to production is using <http://maven.apache.org/plugins/maven-dependency-plugin/get-mojo.html> as a pre step

### Dev environment - autodeploy

1. Developer: push to Git
2. Jenkins: mvn clean deploy -Plambda-deploy-devtest
3. Jenkins: on successful build, trigger new step: lambda-maven-plugin
   1. Download snapshot version from mvn repo and upload to S3
   2. alias: LATEST (reused)
   3. withPublish=false, forceUpdate=true

### Test environment - autodeploy

1. Developer (in Jenkins): trigger mvn release -Plambda-deploy-devtest
2. Jenkins: on successful build, trigger new step: lambda-maven-plugin
   1. Download release version from mvn repo and upload to S3
   2. alias: <version> (version is same as version from jar file, but with "-" unstead of ".")
   3. withPublish=true

### Production environment - manual

1. Developer (in Jenkins): trigger new job: maven-dependency-plugin:copy and lambda-maven-plugin -Plambda-deploy-prod
   1. Download release from mvn repo
   2. Upload file to S3 and deploy
   3. profile:lambda-deploy-prod (reused), <lambda.version> mvn release version
   4. withPublish=true

**Example steps for deployment to production**

### Example pom.xml configuration using profiles

### Tech

- Git
- Maven
  - <https://maven.apache.org/plugins/maven-shade-plugin/>
  - <http://maven.apache.org/maven-release/maven-release-plugin/>
- Maven plugin for deloy to AWS Lambda, <https://github.com/Cantara/lambduh-maven-plugin>
- Jenkins

### Read more

- AWS Lambda
  - <https://aws.amazon.com/documentation/lambda/>
  - <http://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>
  - <https://aws.amazon.com/blogs/compute/new-deployment-options-for-aws-lambda/>
- Maven
  - <https://maven.apache.org/plugins/maven-shade-plugin/>
  - <http://maven.apache.org/maven-release/maven-release-plugin/>
  - <https://github.com/Cantara/lambduh-maven-plugin>
    - <http://maven.apache.org/plugins/maven-dependency-plugin/get-mojo.html>
