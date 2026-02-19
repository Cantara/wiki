# Code coverage using Surefire, TestNG, Jacoco and Sonar

#### Goal

- mvn install should not require any external environment and should be fast.
- Possible to run a certain group of tests from commandline.
- CI server should run all tests, calculate test coverage and update Sonar.
  - Test coverage and number of tests in Sonar must be correct.
  - Nice if tests are not run more times than necessary.

#### Surefire plugin in parent pom

#### Disable all tests in default surefire config.

#### Add profiles which runs different groups of tests

Notice that *defaulttests* profile is activated if testgroup is not set.

#### Profile for code coverage

#### Gotchas

###### There seems to be some problems related to argLine:

<http://osdir.com/ml/issues.maven.apache.org/2012-05/msg00394.html>  
<http://stackoverflow.com/questions/12269558/maven-jacoco-plugin-error>  
<https://github.com/jacoco/jacoco/issues/44>  
<http://jira.codehaus.org/browse/MEVENIDE-435>'

###### Sonar and TestNG

- Sonar doesn't support TestNG test reports, but TestNG can generate reports in JUnit format.

- Maven generates the test coverage reports and *reuse* these in Sonar.
