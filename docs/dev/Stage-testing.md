# Stage testing

### The concept of stages

Having one or more environments that are identical to production. It is a very common pattern because it allows processes of QA and testing that does not affect production data.

### Typical stages

- Development stage
- Test stage
- Pre-production stage

Different stages usually signify different levels of maturity or production<sub>~readiness. The development stage might be used for latest</sub><sub>and</sub><sub>greatest code deployed by a nightly build. The pre</sub>~production environment could be used as the final go/no-go before production.

### Challenges

- Migrating data from production into stage environment.
- Production environment is not identical to the test environments.
- Automatically deploying to staged environment.
- Getting good tests and good test-data that can be executed in the testing stages.
- Automatically advancing a deployment unit through stages with minimal overhead work (is it just the click of a button?).

### Resources

- Staged Spring, helps you configure your project for different stages: http://projects.kaare<sub>~nilsen.com/projects/show/staged</sub>~spring
- Merilo, a utility combining CI with scripts that can re-run traffic from the production environment in a staged environment: http://boss.bekk.no/display/BOSS/Merilo
