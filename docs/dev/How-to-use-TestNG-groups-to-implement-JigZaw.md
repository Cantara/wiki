# How to use TestNG groups to implement JigZaw

|  | The golden rule is that *mvn clean install* should **ALWAYS** return *Build Successful*.   This means that the test suite which is run by default cannot depend on any external resources like database, JMS, Files, WebServices, etc. |

This does not mean that you cannot have tests that use *in-memory*, embedded alternatives! For now let's assume that we have two types of tests: simple unit tests that only test business and doesn't need any external environment and tests that need external services. Lets look at a concrete example to make things more concrete.

## How to set this up

1. Annotate the tests in question
2. Configure surefire (in pom.xml) to exclude these groups of tests
3. Remember to enable the profile to run all tests in the continuous integration server.
   1. In Jenkins, Build - Goals and options:
