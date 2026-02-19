# Script to download and unpack - Windows

### DeployFromNexus.bat
```
@Echo Off && setlocal
rem Set working dir to local dir
PUSHD "%~dp0"

rem
rem Script to download an artifact from Nexus. Then unpack, and replace existing version of the artifact
rem
rem Usge: DeployFromNexus repogroup artifact version 
rem

echo Verify parameters
call :VERIFYPARAMETERS
echo Set variables
call :SETVARIABLES
echo Download artifact
call :DOWNLOAD
echo Unpack
call :UNPACK
echo Run install script
call BackupAndInstall.bat %ARTIFACT% %VERSION% %ARTIFACT%-%VERSION%

goto :END

:SETVARIABLES
rem Unclear to test on my repo which is empty. set BASE_URL=http://127.0.0.1/nexus/service/local/artifact/maven/redirect? 
set BASE_URL=http://repository.sonatype.org/service/local/artifact/maven/redirect?
set RELEASE_REPO=central-proxy
set SNAPSHOT_REPO=
set GROUP=log4j
set ARTIFACT=log4j
set VERSION=LATEST
EXIT /B

:DOWNLOAD
set URL="%BASE_URL%r=%RELEASE_REPO%&g=%GROUP%&a=%ARTIFACT%&v=%VERSION%"
set FILENAME=%ARTIFACT%-%VERSION%.zip
rem TODO improvement - filename should actually reflect the version downloaded
rem Setting static filename to be able to work on it after.

echo Url to be called: %URL%
call wget.exe --no-check-certificate -O %FILENAME% %URL% 

if %errorlevel%==0 (
echo Downloaded ok from repo to file %FILENAME%
) else (
echo Download failed
 goto :END
)
EXIT /B

:UNPACK
call unzip -o %FILENAME% -d %ARTIFACT%-%VERSION%
EXIT /B

:END
rem
rem Done and exit
rem 
endlocal
echo Done
EXIT /B

rem 
rem Thanks to http://www.askapache.com for ideas and examples.
rem
```

### BackupAndInstall.bat
```
@Echo Off  
setlocal
rem Set working dir to local dir
PUSHD "%~dp0"

rem 
rem Purpose of this script is to backup existing working software, then replace this with new version.
rem Stop service
rem Move old directory to backup dir.
rem Move newly unpacked dir into prod dir.
rem Start service again
rem

rem ERROR CODES
set ERR-OK=0
set ERR-NO-DIR=2

rem Usage: BackupAndInstall.bat artifact version new-directory

echo Set variables
goto SETVARIABLES
:DOSTUFF
echo Stop the service
rem call :STOPSERVICE
echo Backup exising prod environment
call :BACKUP
if %ERRORLEVEL%==0 (
  echo Upgrade to new versionx
  rem call :UPGRADE
  rem call :RUNSCRIPT
)
rem Start the service again.
rem call :STARTSERVICE

goto :END

:SETVARIABLES
set ARTIFACT=%~1
set VERSION=%2
set EXPANDED-DIR=%3

echo Variables: ARTIFACT=%ARTIFACT%, VERSION=%VERSION%, EXPANDED-DIR=%EXPANDED-DIR%
goto DOSTUFF

:STOPSERVICE
net stop %ARTIFACT%
EXIT /B

:BACKUP
rem Verify new directory exist
if not exist %EXPANDED-DIR% (
  echo New Directory does not exist, exiting
  EXIT /B %ERR-NO-DIR%
)  

rem delete old backup dir
if exist %ARTIFACT%-OLD (
	echo Deliting %ARTIFACT%-OLD
  call rmdir /S /Q %ARTIFACT%-OLD
)
rem move old directory to backup
echo Moving %ARTIFACT% to %ARTIFACT%-OLD
call move %ARTIFACT% %ARTIFACT%-OLD

EXIT /B

:UPGRADE
rem move new filsystem to production
echo Moving new content %EXPANDED-DIR% to %ARTIFACT%
call move %EXPANDED-DIR% %ARTIFACT%  
EXIT /B

:STARTSERVICE
net start %ARTIFACT%
EXIT /B

:RUNSCRIPT
rem %~nx1 Expands %1 to a file name and extension.

:END
rem
rem Done with install and exit
rem 
endlocal
echo Done
EXIT /B

```
