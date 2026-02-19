# artifactory-smf.xml

```
root@artifactory:/ $ cat /var/svc/manifest/application/artifactory-smf.xml

<?xml version='1.0'?>
<!DOCTYPE service_bundle SYSTEM '/usr/share/lib/xml/dtd/service_bundle.dtd.1'>
<service_bundle type='manifest' name='export'>
  <service name='application/artifactory' type='service' version='1'>
    <single_instance />
    <instance name='artifactory' enabled='true'>
      <dependency name='network' grouping='require_all' restart_on='error' type='service'>
        <service_fmri value='svc:/milestone/network:default'/>
      </dependency>
      <dependency name='filesystem-local' grouping='require_all' restart_on='none' type='service'>
        <service_fmri value='svc:/system/filesystem/local:default'/>
      </dependency>
      <exec_method name='start' type='method' exec='/local/app/artifactory/current/bin/artifactoryctl start' timeout_seconds='60'>
        <method_context>
          <method_credential user='artifactory' />
        </method_context>
      </exec_method>
      <exec_method name='stop' type='method' exec='/local/app/artifactory/current/bin/artifactoryctl stop' timeout_seconds='60'>
        <method_context>
          <method_credential user='artifactory' />
        </method_context>
      </exec_method>
      <exec_method name='restart' type='method' exec='/local/app/artifactory/current/bin/artifactoryctl restart' timeout_seconds='60'>
       <method_context>
          <method_credential user='artifactory'  />
       </method_context>
      </exec_method>
      <exec_method name='run' type='method' exec='/local/app/artifactory/current/bin/artifactoryctl run' timeout_seconds='60'>
       <method_context>
          <method_credential user='artifactory' />
       </method_context>
      </exec_method>
      <exec_method name='check' type='method' exec='/local/app/artifactory/current/bin/artifactoryctl check' timeout_seconds='60'>
        <method_context>
          <method_credential user='artifactory' />
        </method_context>
      </exec_method>
      <exec_method name='supervise' type='method' exec='/local/app/artifactory/current/bin/artifactoryctl supervise' timeout_seconds='60'>
        <method_context>
          <method_credential user='artifactory'  />
        </method_context>
      </exec_method>
    </instance>
    <stability value='Evolving'/>
    <template>
      <common_name>
        <loctext xml:lang='C'>Artifactory - Maven build artifact manager</loctext>
      </common_name>
      <documentation>
        <doc_link name='Artifactory homepage' uri='http://www.jfrog.org/sites/artifactory/latest'/>
      </documentation>
    </template>
  </service>
</service_bundle>
```
