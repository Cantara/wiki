# MJAUU - My JAU Updater (Update the Java-Auto-Update itself )

# My JAU Updater

- [My JAU Updater](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-MyJAUUpdater)

- [UseCase](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-UseCase)

- [Business Value](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-BusinessValue)

- [MJAUU State and Events](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-MJAUUStateandEvents)
- [Main functionallity:](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-Mainfunctionallity%3A)

- [Download artifacts:](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-Downloadartifacts%3A)
- [start-mjauu](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-startmjauu)
- [mjauu](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-mjauu)
- [jau-<version>.zip](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-jau%3Cversion%3E.zip)

- [Code](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-Code)
- [References](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-References)

- [Design notes](#MJAUU-MyJAUUpdater%28UpdatetheJava-Auto-Updateitself%29-Designnotes)

### UseCase

###### Business Value

Allow for automatic update of Java-auto-updater on remote locations.

### MJAUU State and Events

| State | Event Notification | Comment |
| --- | --- | --- |
| UpgradeRequired |  | New Config is made available in CS |
| Started | MjauuStarted |  |
|  | UnzipOk/UnzipFailed | Ok = continue. Failed = pause process |
|  | BackupJauOk/Failed |  |
|  | UninstallOk/Failed | Failed due to missing access |
|  | UpdatedConfig | Update JAU´s local configuration. |
|  | JauInstalledOk/JauInstallFailed |  |
|  | JauStartedOk/JauStartFailed |  |
| Sucess | UpgradeSuccess | Verify JAU started with new and correct configuration. CS must provide JAU with new agent config on next sync. |
|  | MjaauuFinished | MJAUU will terminate, and exit. |

**Alternative ending**

| State | Event Notification | Comment |
| --- | --- | --- |
| Failure | UpgradeFailed |  |
|  | MjauuFinished | Manual interception will be required |

### Main functionallity:

1. Download required artifacts.
2. Start mjauu
   1. Check if another instance of MJAUU has started?
3. Unpack new version of JAU to tmp area
   1. Verify unpacking?
4. Stop JAU service
5. Verify MJAUU has write access to JAU files.
6. Remove JAU service from Windows Services
7. Move JAU files in place
8. Update configuration files.
9. Install JAU service
10. Report status to CS
11. Start JAU service
12. Report status to CS
13. Stop MJAUU

CS = Config Service  
JAU = Java Auto Update  
MJAUU = My JAU Updater

Logs from MJAUU should be forwarded to CS.

###### Download artifacts:

- start-majuu.bat
- mjauu-<version>.jar
- jau-<version>.zip

###### start-mjauu

This .sh/.bat file will have a single responsibillity:

- Start mjauu in separate process.  
  It is essential that the mjauu process runs, when JAU process is killed. This is due to beeing able to safely overwrite existing files.

###### mjauu

mjauu must be easy to start, and possibly without command line arguments. is started with "java ~~jar mjauu~~<version>.jar"  
TODO: figure out how to forward client spesific content to mjauu, if needed.

###### jau-<version>.zip

This is the new package of all contents needed for JAU.

### Code

- <https://github.com/Cantara/JAU-Updater-App>

### References

- <http://stackoverflow.com/questions/9075098/start-windows-service-from-java>

# Design notes
