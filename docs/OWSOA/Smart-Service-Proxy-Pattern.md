# Smart Service Proxy Pattern

### Problem

- Simplify usage/reuse of a remote service

### Context

- Mostly useful in a service oriented context, but not faithful to the multi-language paradigm. (Can deliver multi-language clients if needed)
- We're in the distributed systems space

### Forces

- Reduse config/setup time
- Provide evolvabillity and scalabillity
- Provide optimization of addressing and network transport

### Solution

- Extension of the Business Facade pattern, with added support for
  - caching
  - defaulting
    - configuration
    - protocol handeling
  - network optimization

### Resulting Context

### Rationale

### Extensions / Advanced Scenarios
