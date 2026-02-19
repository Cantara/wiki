# How to use Unitils for data-driven regression testing

#### Description 
The page [Test strategy for Oracle PL_SQL](Test-strategy-for-Oracle-PL_SQL.md) describes how we can write tests based on Unitils to test pl_sql code. For many data-driven applications the same approach can be used for _regression_ tests on the [Application tier](http://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture) / [business logic](http://en.wikipedia.org/wiki/Business_logic). 

See [Testaco](http://testaco.org/) and [what is testaco](http://testaco.org/what-is-testaco.html) for more thorough descriptions of this kind of testing. 

#### Howto 

This approach is nearly identical to [Test strategy for Oracle PL_SQL](Test-strategy-for-Oracle-PL_SQL.md). The only differences are: 

- Tests call functionality on the Application tier instead of on the Data tier. 

- The application is "simple enough" to make it feasible to write input data and expected test results at the application tier. If not, this setup still makes sense, but the scope should then be _selective_ smoke tests instead of full permutation coverage.
