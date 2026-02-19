# Data-driven testing

[Data<sub>~driven testing](http://en.wikipedia.org/wiki/Data</sub>~driven_testing) is a well-known concept and many different implementations exists. 

###### When to consider data-driven testing?

1. A mature API exists and the data format is fairly static. 
1. The test itself is simple. 
1. Big variation of input data. 
1. Easy to determine the expected output of processing the given input. 

###### How to design data-driven tests 

Data-driven testing is not the silver bullet which solves all problems, of course not. It's power comes from the simplicity of extending the test suite with new variants. 

This means data-driven tests can be ideal for **regression testing**. 

It also means it can be the perfect tool to **quickly find and fix a bug in production**. I.e., get a copy of the input data that caused the bug, add it to the test and the bug should be reproduced. Fix the bug and watch the test go green again. 

###### TestNG's DataProvider 

TestNG has support for parameterizing tests by using a [DataProvider](http://testng.org/javadoc/org/testng/annotations/DataProvider.html). This makes it really easy to do small scale data-driven testing. 

A simple example of using DataProvider can be found here: [TestNG – Parameter Test (XML and @DataProvider), by mkyong](http://www.mkyong.com/unittest/testng<sub>~tutorial</sub><sub>6</sub><sub>parameterized</sub>~test)
