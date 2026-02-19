# Potentially shippable

This antipattern comes from Scrum. The idea is that after a sprint of 2-4 weeks, a version of the system is placed in a test environment. This test environment is as similar as possible to the real production environment. The name "potentially shippable" implies that the version should theoretically be complete enough to have been put into production if the organization had decided to do so.

Regularly putting a new version in the test environment makes it possible for users and other stakeholders to experiment with the system being built. Valuable insights are gained that inform the project and its stakeholders about whether things are on the right track.

## The problem with Potentially shippable versions

Creating potentially shippable versions after each iteration is highly recommended, but do not fool yourself. It is not nearly as valuable as a real release. With a release in production users will interact with the system on a daily basis in ways that often are not anticipated during testing. Many projects find that the feedback that potentially shippable releases provides is imprecise and incomplete.

## Determining the value of Potentially shippable versions

The value of a potentially shippable version depends on the context. There are projects that can get almost as good feedback from a version in a test environment as from a released version. Here are some factors that will determine the value of a potentially shippable version:

- **How closely can the test environment mimic the real world?**  
  The test environment should ideally be a copy of the production environment. In many organizations this is not possible. Some systems do not have a test version and some systems have poor support for copying production data to test. If there are significant differences between the test and production environment the value of testing is reduced.

- **What kinds of users/testers are available?**  
  Technical users are much better than non-technical users at understanding how to evaluate a system in a test environment. Many projects have experienced surprises where features that have been accepted in test are rejected once the system is in production.

- **How representative are the testers?**  
  Users are often experts in one sub-domain and ignorant of others. If you don't manage to get testers that are knowledgeable in all sub-domains there will be surprises when the system is deployed.

- **How much time do the users/testers have to test?**  
  Users tend to have other tasks besides testing (big understatement). It can be very difficult in practice to get users to allocate enough time to testing.
