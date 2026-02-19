# Application configuration

## Today

### Command line

Unknown macro: {code}

/usr/bin/java -DIAM\_MODE=PROD -DCONSTRETTO\_TAGS=DEV -Dlogback.configurationFile=/home/uib/logback.xml -jar /home/uib/UserIdentityBackend.jar

#### File system

Unknown macro: {code}

clean\_logs.sh  
CRON  
logback.xml  
psql\_client.sh  
start-service.sh  
update-service.sh  
UserIdentityBackend-2.4.9-20180312.192059-2.jar  
UserIdentityBackend-2.5.9.jar  
UserIdentityBackend.jar  
useridentitybackend\_override.properties  
data/\*  
logs/\*

## To-be/plan

1. Get rid of constretto and stop using the tags concept.
   1. Use <https://github.com/statisticsnorway/dynamic-configuration> ?
      1. <https://mvnrepository.com/artifact/no.ssb.config/dynamic-configuration/0.4>
2. Get rid of ApplicationMode?
   1. Pros: Less property-files for running instance (
   2. Cons: Risk of adding and mixing ApplicationMode parameters for a running instance, i.e. an sandbox DEVTEST environment pushing data to persitent storage/state++
3. Continue to use *override* file for properties
4. logback.xml is masterfile

#### Configuration of whydah-application with propertyfile:

**On Application startup**  
1. Copy uib.properties from jar to filesystem with the name uib\_example.properties (Always overwrite)  
2. Create an empty file named uib\_override.properties, if file does not exists  
3. Copy logback.xml from jar to filesystem if file does not exists. (Jeg tror det vil tydeliggjøre hvilke filer man skal endre på filsystemet på en god måte, samtidig som det gjør oppstartskommandoer og systemd-oppsett ganske ryddig. Det vil også gjøre det ganske enkelt å spore forskjeller mellom miljø og applikasjonens defaultkonfigurasjon.)

#### Some comments/discussion points

Implementasjonsmessig så tror jeg det blir mange små trinn som må gjøres. big bang på alt blir fort vanskelig.  
a. Logikk for å kopiere ut config-eksempler fra jar-fil og legge disse i en egen mappe. Alltid overskrive.   
b. Lage en mappe config og flytte logback.xml og uib\_override.properties dit. Opprette hvis de ikke eksisterer  
c. Bli kvitt web.xml-filen og xml-basert spring-konfigurasjon.  
Vil gjerne begynne i UIB, for der tror jeg testfeilen henger sammen med at flere tester går i beina på hverandre. Jeg ser ingen kurrant måte å unngå dette på uten å få kontroll på hvilken konfig serveren starter med, som henger sammen med endringene vi nå diskuterer.

### File system

Unknown macro: {code}

clean\_logs.sh  
psql\_client.sh  
start-service.sh  
update-service.sh  
UserIdentityBackend-2.4.9-20180312.192059-2.jar  
UserIdentityBackend-2.5.9.jar  
UserIdentityBackend.jar (softlink to versioned jar-file)  
logs/\*  
config/useridentitybackend\_override.properties  
config/logback.xml  
config\_examples/useridentitybackend\_embeddedLdap\_and\_db.properties  
config\_examples/useridentitybackend\_everything\_on\_localhost.properties  
config\_examples/useridentitybackend\_ci.properties
