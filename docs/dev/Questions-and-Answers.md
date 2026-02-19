# Questions and Answers

Taken from discussion topics after October 2. presentation
In lack of a better place to put the discussion :)

### Test data
- Q: How should test data best be stored? Excel files, xml, property files?
- Q: How partitioned should the test files be?
- Q: How should the data be populated? A: DBUnit, Hibernate
- Q: How does one create test data for big ESB's or similar?
- Q: Should I rely on a static test data where I roll back the transaction to restore state?
- Test data should be connected to the role it plays (Rich customer, sick customer)

### Mocking
- Q: What is the difference between mocks and stubs?
- Q: What kind of tests are optimal for mocking?

### Simulating production conditions
The goal here is to simulate the problems your application will face in a production environment. There should be defined layer where one can hook in the instability-simulator that runs a set of standard and tailored exceptions that provoce errors. The test scenarios could include:
- Increasing latency
- Create timeouts or connection loss
- Decrease accessible CPU and Memory
- Multiple threads
