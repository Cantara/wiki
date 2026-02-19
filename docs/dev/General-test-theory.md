# General test theory

The purpose of this page is to list some "rules" with regards to general test theory. If you disagree or don't understand the following statements, please leave a comment. These rules are assumed to be common knowledge, so no explanation will be provided unless someone ask. 

1. Don't test trivial code!
1. Use test coverage tools only as indications as to where your testing efforts will give the most value. Aiming for a certain level of test coverage just don't make sense! 
1. Main reasons for writing tests: 
    1. make sure we deliver the functionality the customer is paying us for
    1. its a very efficient way of producing working code 
    1. easily testable code has quality attributes we want. 
1. While a bottom-up approach is best when developing a new system, a top-down approach is often advantageous when writing tests for an existing system. 
1. A test should have only one reason to change. (Try to avoid writing tests that test overlapping functionality.)
1. It does not matter _when_ you write tests as long as you work efficiently and tests are written during development.
