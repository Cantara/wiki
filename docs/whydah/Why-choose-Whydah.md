# Why choose Whydah?

###### Q: Why not SAML2 tokens/OpenSSO/OpenAM? 

A: OpenSSO has had it's issues in the transition from Sun Microsystems to ForgeRock, especially regarding setup and administration. This is better now, but the resistance from dev-teams to integrate with SAML2 tokens is still so high that many projects _still_ implement their own auth and user databases. Whydah was made to **remove these impediments** so Companies get a working IAM/SSO strategy.

###### Q: Infrastructure angle: Shouldn't IAM  be bought as black-box solution? 

A: IAM/SSO should be black<sub>~box purchases, but as commented above, today's black</sub><sub>box solutions keep failing in organizations by being to "different" or "difficult" for many development teams/projects. One of the reasons seems to be that developers gets confused by the massive XML</sub><sub>scaffolding in SAML2 tokens and the lack of development/test stand</sub>~alone deployments which easily integrate with the project CI infrastructure.

###### Q: Gartner EA policies (What's wrong with IBM Tivoli IAM Suite, NetIQ and similar?)

A: Those products are great and full of functionality. But, and there is a but. If we look at companies which have implemented them you will find that in most companies more than 50% of their in-house developed systems do not integrate with the IAM/SSO solution, rendering the investment not very valuable. The reasons are usually/probably a combination of the ones mentioned above.

###### IAM/SSO and testability - how to test IAM solution and what can/should be automated? 

=> Q: What do you want to automate?

1. Deployment of IAM solution 
1. Known state - i.e. clean all content and automated set up of users, roles and privileges. 
1. CI support in controlled, non-production manner
