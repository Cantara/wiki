# Maximize value of testing

In most real-world situations there is a limited amount of money and time available, and the people with the money want to maximize Return on Investment (ROI). Test is about reducing risk. The amount of testing can thus be rephrased as *what risks are acceptable* and what is the cheapest approach to reduce the risk to an acceptable level.

**The cost of a test can be split into several parts:**

- Creation
- Execution time (and the number of executions in the lifespan of the system/feature)
- Test maintenance, including both functionality, environment and test-data maintenance.

The cost of test maintenance must also be considered and balanced against the expected lifetime of the system. In short, we should invest more in making tests easy to repeat and maintain if the system is expected to live (and change) for a long time.

A unit test is cheap to write because it is the test for a single unit. A service test is cheaper than a system test for much the same reason. Additionally, white box tests are often cheaper than black box tests, but not always. The most important reason for choosing a service test over a black box system test is that service tests are easier to **automate and re-use**.

To maximize the value from testing the total cost of the test must be weighted against the value it gives.   
Example: Test getters and setters  
The cost of these tests are irrelevant, because they give no value. They are easy to create and have low execution time, but because the return on investment is low (perhaps even negative according to for example Coplien), these tests should be avoided.

This boils down to **prefer a cheap test to an expensive test** if the risk reduction is the same.

###### References

See chapter on *Low-Risk Tests Have Low (even potentially negative) Payoff* from [Why Most Unit Testing is Waste](http://www.rbcs-us.com/documents/Why-Most-Unit-Testing-is-Waste.pdf) by James O. Coplien.

---

Back to [JigZaw Design Principles and Drivers](/web/20210123074625/https://wiki.cantara.no/display/dev/JigZaw+Design+Principles+and+Drivers "JigZaw Design Principles and Drivers")
