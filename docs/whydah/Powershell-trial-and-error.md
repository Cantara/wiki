# Powershell trial and error

```
#REQUIRES -version 2.0
<#
.SYNOPSIS
    Download the latest build of this component from Maven and start the service
.NOTES
    File Name      : start-service.ps1
    Author         : Jan Helge Maurtvedt jan.helge.maurtvedt@altran.com
    Prerequisite   : PowerShell V2 over Vista and upper.
.EXAMPLE
    ./start-service.ps1
.EXAMPLE
    Example 2
#>
#Set mode variable for DEV, TEST or PROD mode
$mode = 'DEV'
#Set environment
$env:IAM_MODE=$mode

$A='UserAdministration'
$V='1.0-SNAPSHOT'
$JARFILE=$A+'.'+$V+'.jar'
echo $JARFILE
# pkill -f $A

#Download the latestjar file from mvnrepo
$url =  'http://mvnrepo.cantara.no/service/local/artifact/maven/content?r=altran-snapshots&g=net.whydah.sso.service&a='+$A+'&v='+$V+'&p=jar'
echo $url

$user = 'altran'
$pwd = 'l1nkSys'
$creds = New-Object System.Management.Automation.PSCredential `
     -ArgumentList $user, $pwd
$webclient.Credentials = new-object System.Net.NetworkCredential($user, $creds.GetNetworkCredential().Password)
$webclient.DownloadFile($url,$JARFILE)

java -jar -DIAM_CONFIG=useradministration.$mode.properties $JARFILE

#tail -f nohup.out
```
