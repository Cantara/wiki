# Requirements for container application

## Context

- [https://wiki.cantara.no/display/KM/Service+Manifest](../KM/Service-Manifest.md)
- [https://wiki.cantara.no/display/OWSOA/Service+Categories](../OWSOA/Service-Categories.md)

- Cattle, not pets
- Micro services
- High Availability
- Deploy without downtime
- Docker

- AWS

## Minimal

- Container Orchestration - Fargate or ECS
- Docker with alpine linux
- CloudWatch, application must log to stout and use Docker CloudWatch log support
- ALB, health endpoint, example todo
- No local state - i.e. oo persistence to disk or "sticky sessions", must use database, HazelCast or similar for sharing data between nodes.
  - Might be possible to use <https://aws.amazon.com/efs/>, but avoid if possible.

## Improvements

- Metrics

## Baselines

- <https://github.com/capraconsulting/microservice-baseline>

- Spring variant (Spring Core, not Spring Boot):
