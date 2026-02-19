# CI Strategies

#### How to trigger a build

- Based on **svn-commits**
    - _Poll_ the svn repository regularly
    - Use a svn-hook to trigger a build 

- Based **periods** 
Typically a cron-job. For example _Every 5 minutes_, _Nightly_ or _Each sunday_. 

## Classic build definitions 

There are many different purposes of CI. Depending on the size of the project, you'll want to include several of these strategies:

| Name | Command | Goal | Description |
| --- | --- | --- | --- |
| The Quick Test | mvn install | Detect build failures as soon as possible. | This is the default build and should not require any special parameters or any specific environment. |  |
| The Slow Test | mvn install \[params\](params.md) |  | Most handy when used in combination with The Quick Test CI. Should be able to run this job on a dedicated processor so it does not interfere with the execution time of the Quick Test. |  |
| The Nightly Build | mvn clean deploy | The Nightly Build should run as many tests as possible. It is also responsible for deploying artifacts to the company repo. | This Job is run typically in the middle of the night. Its purpose is to deliver a full working copy of the software based on the latest and greatest code found in the source repository. An optional rule is that the build **should break** in case of any of the modules having test-failures (e.g., the latest Nightly Build artifact will always be a functional piece of software). |
| The Nightly Documentation Build | mvn clean site-deploy |  | This job differs slightly from The Nightly Build. Its purpose is to deliver automatic reports, docs and analysis of the latest code found in the source repository. In case of breakage, the job **should not break**, proceeding to cover as many modules as possible with documentation. |  |
| The Uptime Build |  |  | In case your system depends on a wide range of external services, it could be wise to verify/monitor the stability of these on a regular basis in order to detect SLA-breakage. Basically this job runs for instance every hour, running a thin range of integration tests that verify the presence of your external service dependencies. |  |
| The Backward-Compatibility Test |  |  | Checks the project that depend on your build for compatibility See [BCT | ~sherriff:Backward Compatibility Tester Home] for more info. |  |

## OW test model approach

The build definitions in the previous section are based on the notion of _speed_ alone. Categorizing on speed alone might be sufficient, but often dependencies on some _environment_ complicates things. [Part 3 in OW Test Model](http://wiki.community.objectware.no/display/smidigtonull/OW+Test+Model+Handout#OWTestModelHandout-Part3) explains a more flexible approach that handle both axis.
