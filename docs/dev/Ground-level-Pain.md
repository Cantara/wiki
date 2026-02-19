# Ground level - Pain

At this level Agile is mostly absent, or at least at its most immature - development at its most painfull. 
Some characteristics below.

#### Dependency handling
- artifacts (typically jar's) handled manually 
All external artifacts needed by a development team is handled manually and made available to each developer either by copy, or by some central repository. This is tedious, difficult to get right, and causes inconsistencies accross organization and development teams. Handling internally produced artifacts shared between teams this way, is extremely inefficient and errorphrone.

- manual versioning handling
An artifact typically does not disclose its version (xxx.jar) thus arising version conflicts across organization, teams, and developers - test failures, build brakes, deployment difficulties, decaying predictability. Handling this manually is non-trivial and elaborate (e.g. manually mimmicing a .m2 repo setup).

- old/out-datet versions
This is often the case when artifacts are handled manually - the consequence of updating becomes unpredictable and not easilly tested accross organization and development teams (particularly wrt maintenance).

#### Project setup
- labourous and error prone creation or editing of existing build-scripts to reflect 'this project
When this' the case, its time to look for better ways. Repetition +should+ yield improvement, and there are numerous technologies and tools available to that effect.

- manual deployment onto every target
Small scale, this might not be a problem, but deployment for test or production when numerous targets are involved, it is. Errors will arise, time consumption goes up, and your release cycles can hardly ever improve.

- auto testing difficult to accomplish
This is symptomatic for lousy build-scripts and lack of an early strategy for testing.

- environment changes (wrt system architecture) costly
This reflects weaknesses in build and delployment strategies and solutions.

- decay over time
As complexity increase throughout development (or maintenance), the consequences of problems and pain increase.

#### Testing
- low test-coverage
Often the case when writing tests is difficult, particularly wrt integration and systems testing for which a proper handling of different enviconments, targets and testdata, must be in place from the very beginning.

- configuration hell integrating various end-systems wrt different environments and test phases 
This will be the case if not adressed from the very beginning. Lack of tool support, or utilization of improper tools, may also contribute to this. 

- manual test execution prior to check in
If testing is left to the developer, and manual, faulty code +will+ be added to your VCS! thus affecting the whole project.

- manual system/integration tests
In addition to leaving faulty code in your VCS, errors may avoid detection for far too long.

- elaborate acceptance testing
This is symptomatic for insufficient testing throughout development. High coverage automatic testing before check-in and continously in a CI environment (system and intergration tests) will reduce the effort spent on acceptance testing dramatically.  

- errors discovered at acceptance testing
Again symptomatic for insufficient testing throughout development 

- need functional changes discovered at acceptance testing
Symptomatic for lack of involvment by product owner and for too infrequent releases.

#### System architecture
- early envisioned, designed, and implemented, but at acceptance test revelead as difficult to verify or erroneous.
This will be the case if a system-/staging-test environment is not established early on and exercised through frequent releases.
