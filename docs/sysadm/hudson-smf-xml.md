# hudson-smf.xml

```xml
<?xml version='1.0'?>
<!DOCTYPE service_bundle SYSTEM '/usr/share/lib/xml/dtd/service_bundle.dtd.1'>

<service_bundle type="manifest" name="Hudson">
  <service name="application/hudson" type="service" version="1">

    <!-- Initial state of the service is disabled -->
    <create_default_instance enabled="false"/>

    <!-- Only one instance of Hudson should ever run per server -->
    <single_instance/>

    <dependency name="multi-user-server" type="service" grouping="require_all" restart_on="none">
      <service_fmri value="svc:/milestone/multi-user-server"/>
    </dependency>

    <method_context>
      <method_credential user="hudson"/>
      <method_environment>
        <envvar name="JAVA_HOME" value="/usr/jdk/latest"/>
        <envvar name="JDK_HOME" value="/usr/jdk/latest"/>
        <envvar name="MAVEN_HOME" value="/opt/csw/share/maven2/home"/>
        <envvar name="M2" value="/opt/csw/share/maven2/home/bin"/>
        <envvar name="PATH"
                value="/usr/bin:/usr/sbin:/opt/csw/bin:/opt/csw/sbin:/usr/sfw/bin:/usr/ucb:/usr/local/bin"/>
      </method_environment>
    </method_context>

    <!-- Set the HUDSON_HOME env variable, and run the war file in /local/app/hudson/hudson.war -->
    <exec_method type="method" name="start"
                 exec="java -Xmx512m -DHUDSON_HOME=/local/app/hudson/ -jar /local/app/hudson/hudson.war --prefix=/hudson"
                 timeout_seconds="0"/>

    <exec_method type="method" name="stop" exec=":kill -TERM" timeout_seconds="30"/>

    <!-- http://www.sun.com/bigadmin/content/selfheal/sdev_intro.jsp -->
    <!-- We are going to be kicking off a single child process so we want Wait mode-->
    <property_group name='startd' type='framework'>
      <propval name='duration' type='astring' value='child'/>
    </property_group>

    <stability value="Unstable"/>

    <template>
      <common_name>
        <loctext xml:lang='C'>Hudson Continuous Build Server</loctext>
      </common_name>

      <documentation>
        <doc_link name='hudson.dev.java.net' uri='http://hudson.dev.java.net'/>
        <doc_link name='Hudson Installation Guide'
                  uri='http://wiki.community.objectware.no/display/sysadm/Hudson+Installation+Guide+-+Solaris'/>
      </documentation>
    </template>
  </service>
</service_bundle>

```
