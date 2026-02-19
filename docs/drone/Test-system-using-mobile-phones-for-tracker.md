# Test system using mobile phones for tracker

1. Install app from https://play.google.com/store/apps/details?id=org.opengts.client.android.cgtsfre

2. After installed open app -> select settings as below:

![Screenshot_2015-03-13-22-19-35.png](41878202-Screenshot_2015-03-13-22-19-35.png)

3. Go to OpenGTS server add new Device http://89.221.242.66:8080/track/Track?page=dev.info

4. Edit Info for new Device (e.g input correct Unique ID=gprmc_XXXX, Vehicle ID, IMEI/ESN Number) and save. Notes: Look thaimobile's device for more references 

5. Go to App on android and click Send button. Notes: we also need open GPS on android phone. 

6. Final view result after tracking from OpenGTS server go to http://89.221.242.66:8080/track/Track?page=map.device and select  new device which made before and look result as below:

!2015-03-13 22_36_57-Open Source OpenGTS GPS Tracking.png|border=1!

Good Luck!
