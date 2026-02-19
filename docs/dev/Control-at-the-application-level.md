# Control at the application level

To achieve control at the application level the following concepts must be in place: 

- Traceability ([EMI](Enterprise<sub>~Maven</sub>~Infrastructure.md)) (/)
    - Source code version control 
    - Artifact versioning 

- Artifacts can be configured runtime. (/)
    - Non-sensitive, default values may be included in the artifact, BUT it must be possible to override the included configuration. 
    - Spring<sub>~based configuration management. E.g. [Classic Spring configuration tactics](Classic</sub><sub>Spring</sub><sub>configuration</sub>~tactics.md). 

- Quality Assurance (/) 
    - Automated service tests (EMI, [JigZaw](JigZaw.md))
    - [Automatic code review](Automatic<sub>~code</sub>~review.md) (EMI)
    - Establish practices that encourage good [Software Craftsmanship](Software-Craftsmanship.md). 

- [Installation and Deployment Automation](Installation<sub>~and</sub>~Deployment-Automation.md) (/)
    - Automated installation 
    - Start, stop scripts
