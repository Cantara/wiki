# In SOA - Is my customer the same entity as your customer? Is my product list the same as your product list? In which situations?

A SOA need to support both models: i.e.

    * My customer is the same as your customer (except data-filtering might remove som sensitive info depending on the Security Token), but we typically have Context-Mapped Customer-entities which add/change some of the behaviour. This is done as aggregated core services, building on top of the CustomerRepoService (EDR or EDR-MDS) The core services are the repos, and are responsible for ID strategies and CRUD.

---
