# A custom performance testing framework

#### Drivers/goals  

- Browser/environment independent modus
- Resource efficient 
- Ajax support 
- Http session (e.g. login) support
- Possible to automate statistics and report generation 
- Possible to deduct changes in performance over time 
- Possible to debug when something goes wrong 
- Support for different load "profiles" 
    - e.g. linear increase in load, peak load testing, exponential increase, endurance testing, stress test, etc. 

#### Typical use cases

- Flow: Navigate throw a web based wizard which requires login and steps rely on data entered by the user in previous steps. 
    - Concurrency/Throughput 
    - Server response time
- DDoS specific pages 
- Crawl: Find dead links
- Try to trigger an error by varying possible input values (bypassing any client-side validation) to verify server-side validation 

#### Important design choices 

- Open source 
- Use [The grinder 3](http://grinder.sourceforge.net) as the execution framework? 
    - Hopefully they utilize (or plan to adopt) the features found in java.util.concurrrent from JDK7
- Results from a test run can be persisted to different datasources. 
- Statistics and report generation is separated from the actual test run. 
- Test configuration outside binary file 
- Separate environments config from test config
- XML for test configuration 
- Possible to combine functional system testing with non-functional testing? 
    - Run without a browser (use commons-httpclient to execute http requests)
    - Utilize webdriver/Selenium2 to be able to choose with or without browser? 
- use jodatime and perf4j where applicable 
- jfreechart may be used for reports
