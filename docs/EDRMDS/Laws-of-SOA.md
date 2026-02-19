# Laws of SOA

1. Forget WS\* and products
   - SOA is design and architecture. The WS-\* standards is not much more than candidate technology for decorating your service endpoints...
2. Establish service categories and service universe
   - Without defining/typing your services, you are building your SOA universe with simple blocks. (We have different types of building blocks for building houses, why not in SOA..)
3. Find and decompose services
   - Focus on the responsibility aspect of your services.
   - Split and rule. Remember to satisfy both explicit and implicit consumer expectations
4. Establish service ownership and Key Performance Indicators for your services
   - SOA is challenging on an organization, and as services should provida business value, its a dead giveaway to visualize this value in a graphical dashboard.
5. Establish design rules for your service categories up-front
   - Basically design-time governance...
     - SOA Center of Excellence - Policy Advisory Board
     - Do not forget pre-production service QA
6. Start limited and controlled
   - Start with a vertical, stay 100 % faithful to your architecture and design rules.
   - Use mocks/adapters when you have to take shortcuts
7. Establish lean and agile deployment routines
   - Goal: from test to production-test, and from prod-test to production in less than 20 minutes.  
     T\*\* his is a major change, which will take a lot of effort, but you have to plan for 10 times as many deployments, so there is really no option
