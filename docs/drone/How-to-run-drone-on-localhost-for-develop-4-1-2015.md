# How to run drone on localhost for develop - 4.1.2015

1. Checkout code from https://github.com/openGtsD/AukeGTS
2. package modules auke-web to war file and coppy into tomcat.
3. Copy auke-js folder into ROOT folder in tomat (e.g tomcat\webapps\ROOT) 
4. Start Tomcat
5. Build and install auke<sub>~service module by mvn clean install (e.g make auke</sub>~service.jar after build success)
6. Start service by command: java -jar auke<sub>~service.jar server src/main/resources/app</sub>~config.yaml
7. Go to brower and enter localhost:8080/drone/
