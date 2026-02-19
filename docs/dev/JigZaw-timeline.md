# JigZaw timeline

# Test-level vs Test-properties
|  | Unit | Service | Multi-service | System | System Integration | Acceptance |
| --- | --- | --- | --- | --- | --- | --- |
| With Data |  | (/) | (/) | (/) |  |  |
| Without Data | (/) | (/) | (/) | (/) |  |  |
| With Envionment |  | (/) | (/) | (/) |  |  |
| Without Environment |  | (/) | (/) | (/) |  |  |
| Fast | (/) | (/) | (/) | (/) |  |  |
| Slow |  | (/) | (/) | (/) |  |  |
| Manual |  |  |  | (/) | (/) | (/) |
| Load-Test |  | (/) | ? | (/) | ? | (/) |

# Test-properties vs Timeline	
									
|  | Before commit | 10 min | Hourly | Daily | Weekly | End-of-sprint\\ milestone | Systems-integration | Acceptance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| With Data |  |  | (/) | (/) | (/) | (/) | (/) | (/) |
| Without Data | (/) | (/) | (/) | (/) | (/) | (/) | (/) | (/) |
| With Envionment |  |  | (/) | (/) | (/) | (/) | (/) | (/) |
| Without Environment | (/) |  | (/) | (/) | (/) | (/) | (/) | (/) |
| Fast | (/) | (/) | (/) | (/) | (/) | (/) | (/) | (/) |
| Slow |  |  | (/) | (/) | (/) | (/) | (/) | (/) |
| Load-Test |  |  |  | ? | ? | (/) | ? | (/) |
| Manual |  |  |  | ? | ? | (/) | (/) | (/) |
|  |  |  |  |  |  |  |  |  |
| Run by | Developer | CI-Server | CI-Server | CI-Server | CI-Server | CI-Server | CI-Server\\Developer | CI-Server\\ developer\\ Mercury |

**TODO** Translate the above.
**TODO** figure 

![test_timeline](../images/gliffy/16515331-test_timeline.png)

1-n sprints -> a milestone 
1-m milestones -> a delivery 
1-p deliveries -> receive money from happy customer 

- For each small iteration, unit and service tests 

- Before each milestone, multi-service test (if any) 

- After each milestone, validation, System integration tests, System tests

- Before each delivery (which may or may not correspond to the milestones), Acceptance tests, Production test

The number of sprints per milestone and milestones per delivery can give a good indication as to how agile the team is working. This affects efficiency, but not whether the test model can applied or not. The principles adds value both in agile and more traditional organisations.
