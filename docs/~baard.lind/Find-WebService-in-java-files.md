# Find WebService in java files

1. grep -r -l -F '@WebService' --include=\*.java \* , for å finne filnavn. class og interface/port.
   1. grep på class for å finne tjenestenavn?
   2. grep på public for å finne metodenavn
2. awk WebMethod for å finne metodenavn

**Loop file**
<http://www.cyberciti.biz/faq/bash-loop-over-file/>

**printServiceMethod.sh**
