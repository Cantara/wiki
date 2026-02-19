# Whydah helper scripts

### Some key use-cases

**Production**

1. Upgrade to latest or given
   1. point-release
   2. major release
   3. snapshot (should not break if fail)
2. restart.service (with or without point-upgrade if available)
   1. IAM\_MODE and config-override
   2. Explicit and detailed feedback to the user

**Integration**

1. Upgrade to latest or given
   1. point-release
   2. major release
   3. snapshot
2. restart.service (with point-upgrade if available)
   1. IAM\_MODE and config-override
   2. Explicit and detailed feedback to the user

**Development**

1. Getting ready to develop:
   1. clone all whydah repos (<https://raw.githubusercontent.com/Cantara/Whydah/master/getSource.sh>)
   2. build all modules on local machine (<https://raw.githubusercontent.com/Cantara/Whydah/master/buildFullWhydah.sh>)
   3. start all built modules (TEST\_LOCALHOST) (<https://raw.githubusercontent.com/Cantara/Whydah/master/startFullWhydah.sh>)
   4. verify that it is working before starting to develop (<http://localhost:9997/sso/welcome> u:admin pw:admin)

---

###### Process management - generic script for management of java applications deployed as single jar files.

1. Start
2. Stop
3. Restart
4. Status
5. Upgrade
   1. upgrade snapshot
      1. Download latest always and always restart
      2. Need to know which version is running
      3. Keep the 3 most recent (file timestamp) jar files, delete any older
   2. upgrade release
      1. Check local download first, then Nexus, download and restart (only if new version), do not restart if jar file is not changed
      2. Need to know which version is running
      3. Keep the 3 most recent (file timestamp) jar files, delete any older

Implement first version using upstart. Verify that the script is compatible using systemd.

- One generic sh file
  - Generic script will su to user if run as another user. RunAsUser defined in config file.
- Config file
  - mvn repo url, username and password
  - groupId, artifactId, version
  - RunAsUser
