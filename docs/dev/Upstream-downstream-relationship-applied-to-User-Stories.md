# Upstream-downstream relationship applied to User Stories

Given a system that adheres to the upstream downstream pattern from DDD, following strategy can be useful.

- The topmost consumer is responsible for all user stories.  
- If the topmost consumer needs something from the component below, new user stories that express this need must be written. The **_so that_** clause of these user stories should include references to the user stories from the consumer that depend on it. 

This chain of responsibility must be continued until the level where one can be implemented in its entirety. 

This tactic is probably most useful where different development teams use a strict producer/consumer model.
