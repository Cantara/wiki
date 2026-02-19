# Control at the application level

To achieve control at the application level the following concepts must be in place: 

- Traceability ([EMI](Enterprise-Maven-Infrastructure.md)) (/)
    - Source code version control 
    - Artifact versioning 

- Artifacts can be configured runtime. (/)
    - Non-sensitive, default values may be included in the artifact, BUT it must be possible to override the included configuration. 
    - Spring-based configuration management. E.g. [Classic Spring configuration tactics](Classic-Spring-configuration-tactics.md). 

- Quality Assurance (/) 
    - Automated service tests (EMI, [JigZaw](JigZaw.md))
    - [Automatic code review](Automatic-code-review.md) (EMI)
    - Establish practices that encourage good [Software Craftsmanship](Software-Craftsmanship.md). 

- [Installation and Deployment Automation](Installation-and-Deployment-Automation.md) (/)
    - Automated installation 
    - Start, stop scripts
