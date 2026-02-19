# How to deploy the site

1. Winscp to server 89.221.242.66  with username/pass is drone/drone123 (Notes: Server make for demo and not apply security for now)
2. pkill java
3. Build auke-service.jar at local and copy into server at folder /home/drone/demo/
4. If you fix some js on auke-js >> you need copy this files into /opt/tomcat7/webapps/ROOT/auke-js/
5. If you fix auke-web then you need package war file and copy into /opt/tomcat/webapps (seldom modify. so we can skip this step)
6. start tomcat >> /opt/tomcat/bin/startup.sh
7. start auke-servie >>
   a. cd ~/demo
   b. run command nohup ./start.sh > /dev/null 2>&1 &
8. go to browser and see result from 89.221.242.66:8080/drone
