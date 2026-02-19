# Pull-based Continuous Delivery with Java and Docker

## Why Continuous Delivery?

|  | The "holy grail" of continous delivery is to balance the effort in productivity and quality to ensure that all efforts in software development is headed in the right direction. |

Continuous Delivery: "[...] keep producing valuable software in short cycles and ensure that the software can be reliably released at any time"

- <http://martinfowler.com/bliki/ContinuousDelivery.html>
- [Continuous Delivery vs Continuous Deployment](http://continuousdelivery.com/2010/08/continuous-delivery-vs-continuous-deployment/)

###### Why pull instead of push?

Push strategy is problematic in regards to security and complexity in large systems. Also pull scales better, since it is not reliant on a single push-node. Using push strategy will limit you in practise to continous deployment and hide the extra effort you need to enable continous production.

###### Why Docker?

Docker: Ease of deployment and consistency.

## What?

The application is considered the main deployment unit.   
The Docker image is an approach to server/machine provisioning.

A single Docker image is feasible for all environments as long as there is little variation between environments. Variation must be parametrized and this quickly becomes cumbersome.

Multiple Docker images makes sense when the differences are difficult to mange with a few [environment variables](https://docs.docker.com/reference/run/#env-environment-variables). It might be useful to use provisioning tools to support building the different images.

## Single Docker image strategy

- Same Docker image used in all environments.

- Use [Data Volume Container](https://docs.docker.com/userguide/dockervolumes/) to override configuration and store state. Image must work both with and without Data volume container.

- Default application version is the latest stable release.
- Override application version using [Docker environment variables](https://docs.docker.com/reference/run/#env-environment-variables).

- Docker hub builds Docker image automatically.
  - [Automated Build only on monitored Github folder changes](https://forums.docker.com/t/automated-build-only-on-monitored-github-folder-change/257) **not supported**.
  - Workaround test environments: Upgrade Docker image automatically, but only every 12-24 hours.
  - Workaorund prod environments: Manual upgrade of Docker image using automated script (*check\_and\_update\_docker\_image.sh*).

- Cron job on Docker host to upgrade Docker image if changed every *x* hours.

- If username and password is required to download the application, the Docker image must be private as well, because the script to download application must be included in the image.

- Use [Pull-based Continuous Delivery for Java applications](/web/20210123075843/https://wiki.cantara.no/display/dev/Pull-based+Continuous+Delivery+for+Java+applications "Pull-based Continuous Delivery for Java applications")

### Automatic Docker image upgrade using crontab and bash script

See <https://github.com/Cantara/devops/tree/master/pull_deploy/linux>

- Jenkins Github plugin for webhooks, so we get much faster time to deploy, about 2 minutes.
