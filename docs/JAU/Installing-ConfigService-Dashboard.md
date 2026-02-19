# Installing ConfigService Dashboard

### Installing ConfigService Dashboard

1. Gather the configuration information for the ConfigService you want to hook up to
2. Create and run the **update-service.sh** and **start-service.sh** scripts found below
3. Adjust the property file for ConfigService dashboard to match your ConfigService installation  
   **more /home/cs-dashboard/config\_override/application\_override.properties**
4. Kill the dashboard process and run start-service.sh
5. Point your browser to <http://configservice-url:8087:/dashboard>

### Some useful linux scripts for ConfigService dashboard installations

**more /home/cs-dashboard/start-service.sh**

**more /home/cs-dashboard/update-service.sh**

**more /etc/init/CS-Dashboard.conf**

**/home/ec2-user/su\_to\_csd.sh**

**more /home/ec2-user/upgrade-CS-Dashboard.sh**

**more /home/ec2-user/restart-CS-Dashboard.sh**
