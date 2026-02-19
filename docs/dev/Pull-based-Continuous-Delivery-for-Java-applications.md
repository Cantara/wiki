# Pull-based Continuous Delivery for Java applications

###### Prerequisite

- [Maven Infrastructure](/web/20210123074218/https://wiki.cantara.no/display/dev/Maven+Infrastructure "Maven Infrastructure")

###### How

- Cron job to upgrade application (if changed) every 5-30 minutes.

- Cron job triggers a script which will download and upgrade the application if there is a newer snapshot available. If application version is set to a release version and this version is already running, nothing will happen.

- Example scripts
  - <https://github.com/Cantara/devops/blob/master/pull_deploy/linux/build/Docker/application_scripts/update-service.sh>
  - <https://github.com/Cantara/devops/tree/master/pull_deploy/>
