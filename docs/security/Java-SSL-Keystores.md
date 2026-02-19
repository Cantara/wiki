# Java SSL - Keystores

## Introduction

To support ssl certificates java vm's have two keystores. Both can be set using system properties:

**javax.net.ssl.keyStore**

The name of the file that contains the KeyStore object that you want the default KeyManager to use.

**javax.net.ssl.trustStore**

The name of the file that contains the KeyStore object that you want the default TrustManager to use. The default value is jssecacerts, or cacerts (if jssecacerts does not exist).

### Defaults

Default location on disk for JVM: $JAVA\_HOME/jre/lib/security/

Default keystore filename: cacerts

Default truststore filename: jssecacerts

Default password: changeit

Note that jssecacerts will not necessarily exist - but if created will be used.

## Generating and installing certificates

Lots of info here: <http://java.sun.com/j2se/1.5.0/docs/tooldocs/windows/keytool.html>

### Listing certificates

```
keytool -list -keystore $JAVA_HOME/jre/lib/security/cacerts -storepass changeit
```

Here is an example:

```
keytool -list -keystore glassfish/domains/domain1/config/keystore.jks -storepass changeit

Keystore type: JKS
Keystore provider: SUN

Your keystore contains 5 entries

chrissearle.org, Jul 10, 2008, trustedCertEntry,
Certificate fingerprint (MD5): FF:F9:56:56:6D:53:E7:BB:95:CA:31:0D:6F:E1:53:41
admin_cs_net, Jul 11, 2008, PrivateKeyEntry, 
Certificate fingerprint (MD5): 51:59:DD:D3:B4:A1:A7:EF:A5:E0:AF:79:5E:46:41:47
longship.org, Jul 10, 2008, trustedCertEntry,
Certificate fingerprint (MD5): 5E:97:9F:68:76:BF:33:E5:73:C7:62:F8:96:31:8F:96
chrissearle.net, Jul 10, 2008, trustedCertEntry,
Certificate fingerprint (MD5): 01:91:81:C5:79:71:96:A3:EA:58:B4:16:CA:AC:F0:6E
s1as, Jul 10, 2008, PrivateKeyEntry, 
Certificate fingerprint (MD5): FD:C1:3C:9C:28:D8:AA:50:BB:48:0F:37:A2:A1:D0:D0
```

You can see here that there are 3 keys that may be used as certificates when accessing remote servers (trustedCertEntry) and two that can be used for serving SSL (PrivateKeyEntry).

### Generate a self-signed certificate for serving SSL

```
keytool -genkey -alias an_alias -keystore $JAVA_HOME/jre/lib/security/cacerts
  -keypass woot -storepass changeit
```

### Importing a self-signed certificate for calling SSL on a different server

```
keytool -import -alias an_alias -keystore $JAVA_HOME/jre/lib/security/cacerts
  -storepass changeit
```

### Importing both the key and certificate of an openssl generated self-signed certificate

Keytool assumes that it has generated the private key and will not allow for import of the key.

Currently the only success I have had is with code from Not Yet Commons-SSL - <http://juliusdavies.ca/commons-ssl/>

Grab 0.3.9 then run something similar to

```
java -cp not-yet-commons-ssl-0.3.9.jar org.apache.commons.ssl.KeyStoreBuilder
  pass_for_new_keystore key.key certificate.crt
```

This will generate a new keystore named after the CN field of the certificate. You can then use keytool to merge it in - something like

```
keytool -importkeystore -srckeystore keystore_generated_in_step_above
  -destkeystore $JAVA_HOME/jre/lib/security/cacerts -srcstorepass pass_for_src_keystore
  -deststorepass changeit
```

### Obtaining a remote SSL certificate

If you have openssl and sed installed then from <http://www.madboa.com/geek/openssl/#cert-retrieve> the following may help

```
#!/bin/sh
#
# usage: retrieve-cert.sh remote.host.name [port]
#
REMHOST=$1
REMPORT=${2:-443}

echo |\
openssl s_client -connect ${REMHOST}:${REMPORT} 2>&1 |\
sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p'
```
