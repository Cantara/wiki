# Continuous Integration

_Automatic build and integration._

## Principles

- To fix a broken build must **+always+** have highest priority. Otherwise, most of the benefit of doing continuous integration is lost. 
- [Integrate often](http://www.extremeprogramming.org/rules/integrateoften.html)
- When deciding which product to use and which CI strategies to implement the goal is (and must always be) to _maximize value gained_. To illustrate: 
    - "_install productX and all your problems will be solved_" <- of course not 
    - "_hourly and nightly builds is the best CI strategy_" <- of course not, which CI strategies to implement **+always+** depend on the project. 
    - etc. 

## Continuous Integration Server Farms (distributing builds)

Building, testing, generating reports is tedious work for the CPU and Memory of a server. Even though it might seem tempting to centralize the configuration of a the CI<sub>~strategy in one CI</sub>~system, this does not scale far beyond a couple of projects. The CI-server will become a bottleneck, and developers will be waiting for hours to get their builds complete.

There are two alternative solutions to this:

1. Set up one CI system on a new server for each project.
1. Set up distributed/remote build agents for the centralized CI System.

Not all CI systems support the second feature. Among those who do are Hudson:
- http://wiki.hudson-ci.org/display/HUDSON/Distributed+builds

.. and Bamboo:
- http://confluence.atlassian.com/display/BAMBOO/2.1+About+Agents+and+Capabilities

An illustration of a working centralized environment is displayed below:

| (?) | Revision | Timestamp | Committer | Project | Build time | Message | CI-server | Status | Commands |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (!) | 262 - [changes | http://svn/diff?old=260&new=261] | 13:05 | Ferris | Petshop | 3:39 | Introduced some warnings, silly me.. | continuum1 | [Warnings | http://results/build/262] | [Notify | http://svn/notify?name=Ferris] - [Revert | http://svn/revert?rev=262] |
| (/) | 261 - [changes | http://svn/diff?old=260&new=261] | 12:56 | Ronnie | Demo | 3:35 | Fixed some other stuff | continuum3 | [Successful | http://results/build/261] | [Notify | http://svn/notify?name=Ronnie] - [Revert | http://svn/revert?rev=261] |
| (/) | 260 - [changes | http://svn/diff?old=259&new=260] | 12:54 | Kjartan | Petshop | 3:35 | Reverted r259 because it broke. | continuum2 | [Successful | http://results/build/260] | [Notify | http://svn/notify?name=Kjartan] - [Revert | http://svn/revert?rev=260] |
| (x) | 259 - [changes | http://svn/diff?old=258&new=259] | 12:45 | Ferris | Petshop | 3:50 | Fixed some stuff. | continuum1 | [Errors | http://results/build/259] | [Notify | http://svn/notify?name=Ferris] - [Revert | http://svn/revert?rev=259] |

Each revision is immediately dispatched to an available instance, and the results are aggregated into the central instance.

See also:

- http://www.infoq.com/news/2007/09/CI_Pipeline
- http://www.jroller.com/gnirpaz/entry/tigris_distributed_testing

## Internal resources

See also [BCT](../<sub>sherriff/Backward</sub><sub>Compatibility</sub>~Tester-Home.md)

## External resources

[The Hudson Build Farm Experience](http://blogs.sonatype.com/people/2009/01/the<sub>~hudson</sub><sub>build</sub><sub>farm</sub><sub>experience</sub><sub>volume</sub>~i/)

[Olve Maudal on TANDBERG's internal CI processes and "Advanced Feedback<sub>~Driven Development"](http://olvemaudal.wordpress.com/2009/03/26/advanced</sub><sub>feedback</sub><sub>driven</sub>~development/)

[Martin Fowler's article](http://martinfowler.com/articles/continuousIntegration.html)

[Wikipedia on CI](http://en.wikipedia.org/wiki/Continuous_Integration)

[The One Minute Build](http://jupitermoonbeam.blogspot.com/2008/01/one<sub>~minute</sub>~build.html)

[Automation for the people: Continuous Integration anti<sub>~patterns](http://www.ibm.com/developerworks/java/library/j</sub>~ap11297/index.html?S_TACT=105AGX02&S_CMP=ART), By Paul Duvall

[Automation for the people: Continuous Integration anti<sub>~patterns, Part 2](http://www.ibm.com/developerworks/java/library/j</sub>~ap03048/index.html?ca=drs-), by Paul Duvall

[Continuous Integration: Improving Software Quality and Reducing Risk](http://www.amazon.com/gp/product/0321336380/?tag=integratecom-20), Paul Duvall's book

[If it hurts, automate it (Hadoop and Distributed Computing at Yahoo!)](http://developer.yahoo.com/blogs/hadoop/2007/12/if_it_hurts_automate_it_1.html) - automatically apply patches that pass basic QA tests.
