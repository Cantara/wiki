# TestNG vs JUnit

###### JUnit 4.12
- Con: Categories is still experimental / inmature. 
- Con: Asserts have parameters in the "wrong" order 
- Pro: Use annotations and marker interfaces -> better refactoring support. 
- Pro: JUnit is more popular (I think) than TestNG, so toolsupport may be better. 
- Con: Designed for unit tests only. E.g. Kent Beck insists that there should be no dependency between tests. So not supported to run setup once for a group of tests. 

###### TestNG 6.8
- Pro: Has had groups for a very long time. 
- Pro: JigZaw has been implemented using TestNG many times. 
- Con: Use text strings for groups. 
- Pro: Designed for more than unit tests. 
    - DataProvider functionality 
    - Explicit support for letting a group of tests depend on the same setup. 

#### Resources 

- http://maven.apache.org/plugins/maven-surefire-plugin/ 
- https://github.com/kentbeck/junit/wiki
- http://testng.org/doc/documentation-main.html#methods
- http://www.sonatype.com/books/mcookbook/reference/ch07s04.html
