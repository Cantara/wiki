# HLT — HTTPLoadTest Baseline

HTTPLoadTest-Baseline is simple starting point for building LoadTests to be used for continuous deploy/continuous production QA pipelines. Baseline projects are meant to be a git clone starting point for for software which are expected to grow and flourish in different ways which are not easy to parameterize in early stages. It should be usable for quite a few settings, but is expected to grow in different directions. We would love to receive pull-request for enhancements both on current codebase and extensibility features.

Why another load-test OpenSource project? We think this is a reasonable question. There exist quite a few "full-fledged" alternatives. Our concern is that the uptake of those solutions are way below what the industry need, and this is an attempt to try to offer a different alternative which may or may not fulfill you needs/requirements. The main goal for this codebase is to simplify Companies efforts in ensuring that an agile or continuous investment into software development does not compromise the quality assurance processes on non-functional requirements, we have tried to focus on making the load-test QA process easily embedable to a Company's continuous CI/CD processes.

We have built HTTPLoadTest-Baseline on an underlaying cicuit-breaker framework called hystrix and timed execution blocks to avoid any blocking or dangeling HTTP requests and internal threads.

Coming from development backgrounds, we hope that a baseline you might contribute to, or just form and change to your requirements/needs might increase the quality of produces software by making it less "expensive" to add this type of quality processes into your software development process.

- <https://github.com/Cantara/HTTPLoadTest-Baseline>

### Release log

| Version | Main changes | Comment(s) |
| --- | --- | --- |
| 0.24 | Added OAUTH2 support, and adjusted embedded TestSpecifications and LoadTest baselines to test internal resources |  |
