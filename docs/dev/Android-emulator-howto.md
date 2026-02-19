# Android emulator howto

1. Install android JDK 
1. Set up virtual device 
    1. android list avd
    1. emulator -avd vDeviceName
    1. emulator -avd vDeviceName -wipe-data
1. Install application 
    1. adb install -r someApp.apk
1. Use ddms for debugging. 

#### Resources 

[Using the Android Emulator](http://developer.android.com/tools/devices/emulator.html)
[Managing Virtual Devices](http://developer.android.com/tools/devices/index.html)
[Managing AVDs from the Command Line](http://developer.android.com/tools/devices/managing-avds-cmdline.html)
