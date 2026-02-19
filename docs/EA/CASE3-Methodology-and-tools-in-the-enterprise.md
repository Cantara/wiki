# CASE3 - Methodology and tools in the enterprise

Responsible: Johannes Brodwall 

I have never written a piece of code that worked the first time I tried it. This has turned me into a fundamentalist  when it comes to automated testing. I don't want my users - or my testers! - to spend their time dealing with my bugs.

Over the last year, I have been able to extend the our build system to cover automated tests of requirements and full scale integration test of a fully deployed system. The system automates all our testing and gives us a turn around to (partial) production of 2-3 weeks.

In the session, I plan to describe the elements of the tools that we use to support testing:
- Continuous integration with a custom system
- Functional tests using FitNesse
- Automatic run of recorded production data after every build
- Systematic run of large amounts of recorded production data before release
- Automatic parallel execution of every operation in an isolated staging environment
- Automatic comparison of test runs with historical production
- Monitoring of all environments

I want most of the session to be a discussion on:
- How much testing is enough?
- What are the perils of too much or too little automated testing?
- How can our approach of using canned production data be used in another setting?

Moderator: Johannes Brodwall, (future) Chief Scientist at Steria
