# Book club system

In this project the customer wanted to replace a book club system. The goal was to integrate the book clubs into an Internet bookshop in order to be able to increase cross selling between the two channels. The existing book club system was operated as a third party ASP service that was not accessible for any type of integration. The existing system was very expensive and was also built for much more complex book clubs than the customer had. 

The company had a number of book clubs that operated in different ways. Some of the clubs had a fixed sequence of books while other clubs continually added new books and changed the ordering of these.

## First strategy
Because of the closed nature of the legacy system it was not possible to go for any strategy that required integration with it. The first strategy that was considered was to develop support for a completely new book club. In that way the first release would not have to migrate any users or need to have any of the functionality that comes to play over time in a club. This strategy had to be rejected since the customer was not planning to launch any new clubs. There was no point in delivering something to production that no one would use.

## Second strategy
The second strategy considered was to take an existing club and split it so that new members would be handled by the new system while existing members would stay in the old one. Again, this would have allowed the project to focus on a core set of functionality. Unfortunately this strategy also turned out to be unfeasible. The killer detail this time was customer support. When customers call in they often do not know their customer id (they often do not know the name of their club!). With a club split across systems, customer support would have to look for the customer in both systems.

## Final strategy
The strategy that ultimately was chosen was to develop enough functionality to be able to migrate one of the smallest clubs. This was a larger [MRP](MRP.md) than the other strategies since the project now had to develop support for both new and existing customers as well as the migration code. This strategy worked well but there were some drawbacks. Customer support still had to cope with two systems but now they knew which system to use as long as the customer remembered which club they belonged to. Some customers were split across both systems since they belonged to more than one club. Finding and rejecting bad customers was complicated by the fact that records of bad customers resided in two systems.
