# continuum-smf.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE service_bundle SYSTEM "/usr/share/lib/xml/dtd/service_bundle.dtd.1">

<service_bundle type="manifest" name="Continuum:run">
  <service name="application/continuum" type="service" version="1.3.2">
    <create_default_instance enabled="false"/>
    <single_instance/>

    <dependency name="multi-user-server" type="service" grouping="optional_all" restart_on="none">
      <service_fmri value="svc:/milestone/multi-user-server"/>
    </dependency>

    <method_context>
      <method_credential user="continuum"/>
      <method_environment>
        <envvar name="JAVA_HOME" value="/usr/jdk/latest"/>
        <envvar name="JDK_HOME" value="/usr/jdk/latest"/>
        <envvar name="MAVEN_HOME" value="/opt/csw/share/maven2/home"/>
        <envvar name="M2" value="/opt/csw/share/maven2/home/bin"/>
        <envvar name="PATH"
                value="/usr/bin:/usr/sbin:/opt/csw/bin:/opt/csw/sbin:/usr/sfw/bin:/usr/ucb:/usr/local/bin"/>
      </method_environment>
    </method_context>

    <exec_method type="method" name="start" exec="/local/app/continuum/current/bin/continuum %m" timeout_seconds="60"/>

    <exec_method type="method" name="restart" exec="/local/app/continuum/current/bin/continuum %m"
                 timeout_seconds="60"/>

    <exec_method type="method" name="stop" exec="/local/app/continuum/current/bin/continuum %m" timeout_seconds="60">
    </exec_method>

    <!-- http://www.sun.com/bigadmin/content/selfheal/sdev_intro.jsp -->
    <!--long-running process that daemonizes or forks itself -->
    <property_group name="startd" type="framework">
      <propval name="duration" type="astring" value="contract"/>
    </property_group>

    <template>
      <common_name>
        <loctext xml:lang="C">Continuum start/stop/restart</loctext>
      </common_name>
      <documentation>
        <doc_link name='continuum.apache.org' uri='http://continuum.apache.org/'/>
        <doc_link name='Continuum Installation Guide'
                  uri='http://wiki.community.objectware.no/display/sysadm/Continuum+1.3.2+Installation+Guide+-+Solaris'/>
      </documentation>
    </template>
  </service>
</service_bundle>

```
