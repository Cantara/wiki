# User Stories

_An agile way to express requirements._

## User story definitions from various sources 

[Wikipedia](http://en.wikipedia.org/wiki/User_story) 
[extremeprogramming.org](http://www.extremeprogramming.org/rules/userstories.html)
[Agile Modelling](http://www.agilemodeling.com/artifacts/userStory.htm) 

## User story template 

Source: [Dan North](http://dannorth.net/whats-in-a-story)

```
Title (one line describing the story)

Narrative:
As a [role]
I want [feature]
So that [benefit]
```

```
Acceptance Criteria: (presented as Scenarios)

Scenario 1: Title
Given [context]
  And [some more context]...
When  [event]
Then  [outcome]
  And [another outcome]...

Scenario 2: ...
```

#### Examples 

- As a customer, I want to calculate the prices of a car insurance online, so I can figure out which insurance I want to buy.
 
- As an IT-techie, I want to run the solution seamlessly on a cluster, so I can deliver high uptime (as specified in the Service Level Agreement).

- As customer-support, I want the information from the customer merged automatically and correctly into our CRM, so I do not have to do this manually.

## Granularity, composites and levels 

In general we have two types of user stories **regular** and **epic**. 

#### Regular user stories 
Regular user stories should adhere to the following 

- Limited size 
    - Possible to implement within two weeks is a good rule of thumb, at least within one sprint. 
- Must add business value 
- The _**so that**_ clause is important so all stakeholders understand the purpose. 

#### Epic user stories 

Epic user stories are user stories that have not yet been broken down to regular user stories. They can be put on the backlog, but should never make it into a sprint. They can be used directly for **release planning**, but are normally only used to ensure that requirements are not forgotten. 

- Don't spend time breaking down an epic user story until it is relevant for the upcoming sprint. Postponing the activity is always a good idea, because you may learn something in the meantime that changes how it should be broken down, if it should be implemented at all, etc. 

- When an epic user story has been broken down into multiple regular user stories, the epic user story is redundant and should be deleted. 

## Requirement tracking

It is important to have requirement tracing during a systems life cycle to ensure that requirements are not lost. A requirement matrix (or something similar) will make it easier to:
-identify which requirements that are affected by code changes. 
-identify which system components we have to change if the requirement is changed
-what do we have to retest if the requirement is changed
Whenever the system requirement is changed, the affected areas in the software life cycle must be kept consistent with the updated requirements.  

It should be possible to follow the life of a requirement, in both a forward and backward direction. A single requirement must be able to be traceable during all stages of the production, delivery and installation.

Requirements tracing should capture all levels of requirement engineering. The customer's interests and needs should be applied to the product's goals, constraints, and outcomes.  Another important level is the understanding between the customer and the supplier on the functionality, non functionality, and possible side effects of the technical level.  

So, how should this tracing (and communication within the project) be performed so all involved parties are notified when a requirement is changed? Consider how the change of the requirement impact the rest of the system? And of course, when a component/functionality is changed has that any impact on the requirements? 

## Resources 

- [Advantages of User Stories for Requirements, by Mike Cohn](http://www.mountaingoatsoftware.com/article_view/27-advantages-of-user-stories-for-requirements)
- [Don't know what I want, but I know how to get it](http://agileproductdesign.com/blog/dont_know_what_i_want.html)
- [Requirements considered harmful](http://agileproductdesign.com/blog/requirements_considered_harmful.html)
