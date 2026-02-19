# The Laws of SOA

# To succssfully implement a service oriented architecture you should:

###### 1. Forget WS\* and products

- SOA is design and architecture. The WS-\* standards is not much more than candidate technology for decorating your service endpoints...

###### 2. Establish service categories and service universe.

- Without defining/typing your services, you are building your SOA universe with simple blocks. We have different types of building blocks for building houses, why not in SOA..  
  See [SOA - Service Categorization](/web/20220817071412/https://wiki.cantara.no/display/OWSOA/SOA+-+Service+Categorization "SOA - Service Categorization")

###### 3. Find and decompose services

- Focus on the responsibility aspect of your services.
- Split and rule. Remember to satisfy both explicit and implicit consumer expectations.

###### 4. Establish service ownership and Key Performance Indicators for your services

- SOA is challenging on an organization, and as services should provida business value, its a dead giveaway to visualize this value in a graphical dashboard.

###### 5. Establish design rules for your service categories up-front

- Basically design-time governance...
  - SOA Center of Excellence - [Policy Advisory Board](/web/20220817071412/https://wiki.cantara.no/display/KM/Policy+Advisory+Board+%28PAB%29 "Policy Advisory Board (PAB)")
  - Do not forget pre-production service QA.

###### 6. Start limited and controlled

- Start with a vertical, stay 100 % faithful to your architecture and design rules.
- Use mocks/adapters when you have to take shortcuts.

###### 7. Establish lean and agile deployment routines

- Goal: from test to production-test, and from prod-test to production in less than 20 minutes.
- his is a major change, which will take a lot of effort, but you have to plan for 10 times as many deployments, so there is really no option

###### 8. Security is not optional in SOA

- You basically need to pass a Security Token with each service invocation. On pre-invocation you do the normal access control, of post-invocation you need to filter the data-values (i.e. remove sensitive data if the security token does not have the right access. This is necessary, since we no longer have any single point of control, or trying to establish a single point of control will break the agility and time-to-marked values of your SOA.

###### 9. Reflect and work strategically against SOA Maturity Model.

- See [http://wiki.cantara.no/display/EDRMDS/SOA+Maturity+Models+and+EDR-MDS](../EDRMDS/SOA-Maturity-Models-and-EDR-MDS.md)

---

|  | To be merged with content above |

### Intro

Service Oriented Architecture is all over us. And after several years with SOA we still have an extremely high rate of failure in SOA projects. SOA architects have no clue of what a service is, development leads spend all their time on making product workarounds, developers create silo services, and BPEL/BPM gurus use most of their time scrolling the enormous models, application management waste most of their time trying to restart parts of the SOA, and so on and so on...

This can not continue forever - there is a new sheriff in town! And this sheriff will shoot to kill.

In this presentation, the sheriff will introduce a set of SOA laws which, when followed, will guide your SOA effort from certain failure to the nirvana SOA promises and when ignored lead to certain death.

|  |  |  |  |
| --- | --- | --- | --- |
| The laws... **0. Forget about focusing WS** and products\*   - SOA is [design](/web/20220817071412/https://wiki.cantara.no/display/KM/Design-Time+Governance+-+SOA+Design+Rules "Design-Time Governance - SOA Design Rules") and [architecture]. The WS-\* standards and ESBs are not much more than candidate technology for decorating your service endpoints...   By this we mean that all SOA projects which focuses on the protocol (WS-) or the middleware (ESB) seldom have any success. If you on the other hand focuses of the atom of SOA, namely the services and how you build from these building blocks you are much more likely to have success. How the services collaborate can then happen in a myriad of ways. Both movable services (like in Jini/JavaSpaces) in-process services with a collaborating backbone, REST-endpoints and WS- endpoints all become a matter of deployment - and we usually have several endpoints with different protocols for each service.  **1. Establish service categories and service universe**   - Without defining/typing your [services](/web/20220817071412/https://wiki.cantara.no/display/KM/Service+Manifest "Service Manifest"), you are building your SOA universe with simple blocks. (We have different types of building blocks for building houses, why not in SOA..)   **2. Find and decompose services**   - Focus on the responsibility aspect of your services. Divide and conquer. Remember to satisfy both explicit and implicit consumer expectations   **3. Establish service ownership and Key Performance Indicators for your services**   - SOA is challenging on an organization, and as services should provide business value, it is a dead giveaway to visualize this value in a graphical dashboard.   **4. Establish design rules for your service categories up-front**   - Basically [design-time governance](/web/20220817071412/https://wiki.cantara.no/display/KM/Design-Time+Governance+-+SOA+Design+Rules "Design-Time Governance - SOA Design Rules")...   - SOA Center of Excellence - [Policy Advisory Board]   - Do not forget pre-production service QA   **5. Start limited and controlled**   - Start with a business vertical, stay 100 % [faithful] to your architecture and design rules.   - Use mocks/adapters when you have to take shortcuts   **6. Establish lean and agile deployment routines**   - Goal: from test to production-test, and from prod-test to production in less than 20 minutes.   - This is a major change, which will take a lot of effort, but you have to plan for 10 times as many deployments, so there is really no option   **7. Versioning is not optional in SOA**   - See section for design rules for services and details about Evolving Service Endpoint pattern and strategies.   **8. Security is not optional in SOA**   - You basically need to pass a Security Token with each service invocation. On pre-invocation you do the normal access control, of post-invocation you need to filter the data-values (i.e. remove sensitive data if the security token does not have the right access. This is necessary, since we no longer have any single point of control, or trying to establish a single point of control will break the agility and time-to-marked values of your SOA.   **9. Reflect and work strategically against SOA Maturity Model.**   - See <http://wiki.community.objectware.no/display/EDRMDS/SOA+Maturity+Models+and+EDR-MDS>  ---   |  | **Gartner humor - To the CIO, CEO, CFO, CTO and shareholders** As a result of the following I can now only deduce that SOA is a failure and any attempts at SOA will result in failure. Under my direction:  - I have failed to associate our SOA initiatives with our business needs, therefore I cannot show any value for the hundreds of services we have created , - I have failed to properly create and support an SOA Center of Excellence, Steering Committee or Competency Center, - I have failed to enlist the executive staff as true supporters and evangelists for our SOA efforts. - I chose to buy an ESB prior to truly understanding our SOA infrastructure needs (In reality this wasn't my fault, the vendor said it was super duper necessary) - I have failed to provide my developers incentives to reuse artifacts, - It was not my responsibility to follow what was going on next door where there was a separate team dealing with BPM, I mean they are two different initiatives, - I firmly believe that SOA is nothing more than fancy CORBA or COM.   Despite all of the things I have NOT done, SOA has failed. My additional failure to recognize and implement best practices that have been proven successful in many other companies worldwide also play into the failure of SOA.  Oh well, we should move on and try something new. On the bright side 70% of our initiatives fail anyway. The failure of SOA is SOA's fault not mine.  Thanks for understanding and I'd like to declare in advance that Cloud Computing, Virtualization and SaaS will be failures under my direction as well.  Quoted from: <http://blogs.gartner.com/frank_kenney/2008/11/12/ahh-shucks-soa-is-a-failure/> |  As you can see, if you fail to follow the laws of SOA, you are getting yourself into trouble.. | Terminology  - [Service](/web/20220817071412/https://wiki.cantara.no/display/KM/Service+Manifest "Service Manifest") [Service Manifest](/web/20220817071412/https://wiki.cantara.no/display/KM/Service+Manifest "Service Manifest") [Service Categories] [H2A Services](/web/20220817071412/https://wiki.cantara.no/display/KM/H2A "H2A") [A2A Services](/web/20220817071412/https://wiki.cantara.no/display/KM/A2A "A2A") [ACS Services](/web/20220817071412/https://wiki.cantara.no/display/KM/ACS "ACS") [Core Services](/web/20220817071412/https://wiki.cantara.no/display/KM/CS "CS") - [Evolving Service Endpoint (ESE)](http://wiki.community.objectware.no/display/ESE/Home) [Governance](/web/20220817071412/https://wiki.cantara.no/display/KM/Design-Time+Governance+-+SOA+Design+Rules "Design-Time Governance - SOA Design Rules") [Architecture] [Policy Advisory Board]  [The laws of SOA FAQ]  - [WebServices can lead to function oriented services, while REST can lead to a resource oriented architecture. Are both SOA?](/web/20220817071412/https://wiki.cantara.no/pages/viewpage.action?pageId=8486989 "WebServices can lead to function oriented services, while REST can lead to a resource oriented architecture. Are both SOA?")  - [Law 1 and 2 - Does this mean that you recommend small, fine grained services?](/web/20220817071412/https://wiki.cantara.no/pages/viewpage.action?pageId=8486988 "Law 1 and 2 - Does this mean that you recommend small, fine grained services?")  - [I don't think I understand what's meant with law 4 and 5 (I understand the words, but not what you want people to do and when)](/web/20220817071412/https://wiki.cantara.no/display/OWSOA/I+don%27t+think+I+understand+what%27s+meant+with+law+4+and+5+%28I+understand+the+words%2C+but+not+what+you+want+people+to+do+and+when%29 "I don't think I understand what's meant with law 4 and 5 (I understand the words, but not what you want people to do and when)")  - [I think I agree with law 3, Establish service ownership and Key Performance Indicators for your services, but an example of a KPI would be helpful](/web/20220817071412/https://wiki.cantara.no/display/OWSOA/I+think+I+agree+with+law+3%2C+Establish+service+ownership+and+Key+Performance+Indicators+for+your+services%2C+but+an+example+of+a+KPI+would+be+helpful "I think I agree with law 3, Establish service ownership and Key Performance Indicators for your services, but an example of a KPI would be helpful")  - [I think I agree with law 8, Security is not optional in SOA, but I don't understand what you mean by it yet](/web/20220817071412/https://wiki.cantara.no/display/OWSOA/I+think+I+agree+with+law+8%2C+Security+is+not+optional+in+SOA%2C+but+I+don%27t+understand+what+you+mean+by+it+yet "I think I agree with law 8, Security is not optional in SOA, but I don't understand what you mean by it yet")  - [In SOA - Is my customer the same entity as your customer? Is my product list the same as your product list? In which situations?](/web/20220817071412/https://wiki.cantara.no/pages/viewpage.action?pageId=8486990 "In SOA - Is my customer the same entity as your customer? Is my product list the same as your product list? In which situations?") |
