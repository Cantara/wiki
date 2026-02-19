# Reducing release costs

When Kent Beck first described Extreme Programming, one of the more counter-intuitive notions was: If something is hard, do it more often.

The act of releasing is often difficult. It requires time and coordination to install and upgrade all the component parts of the system, and it often requires a lot of people to be involved. And the consequences of failure are real. When a service goes down because of a new release, nobody is happy.

When faced with challenges like these, our first instinct is to increase the ceremony of releasing. More signoffs, more documentation, more analysis of possible repercussions.

We, like Kent Beck, recommend a different approach: Instead of trying to deal with the complexity and risk, by releasing often, you can learn reduce the complexity and risk involved.

### Some techniques

- Increase automated verification: By reducing the time required to regression test the application, the testing efforts in front of a release can be spend more cost-effective.

- Run several versions in parallel: If you can deploy the new version and distribute it to some of your users, you can verify the release under more real conditions, and you have a backup plan for the releases where something goes very wrong.

- Simplify the architecture: The more separately deployed components a system depends upon, the more risky and time consuming installation will be. By bundling more of the system together in fewer units of deployment, you will reduce the risk and complexity of a deployment. Similarly, avoid depending on non-standard software being separately installed on the target machines. In some situations, the service-orientation trend has made this aspect of system governance much harder.

- Perform backwards compatible data migrations: The most risky changes to the system are those that involve changing the data structure. In many situations, this leaves projects with no possibility of rolling back a failed release. However, most data schema changes can be performed in a way that is backwards compatible with the previous version. For example, changing a column name can be performed by first adding a new column in one release and dropping the old column in the next release. Performing migrations slowly in this way may sound like a time consuming path to changing your software. And it will be, as well, if you don't release frequently. This is one of the many situations where a high release frequency as a practice will benefit the release cycle directly [urk, bad sentence!](urk-bad-sentence.md)

- Practice, practice, practice: Preferably, the development team should install the whole software package to a system that is as close to production as possible at least every iteration. Use this chance to verify installation documentation. If you find the installation difficult: Don't update the documentation - simplify the architecture and scripts used to install.
