# Find latest version in NEXUS repo

Documentation internally in Nexus only http://127.0.0.1:8081/nexus/nexus-restlet1x-plugin/default/docs/resource_ArtifactResolvePlexusResource.html

url: /artifact/maven/resolve

**Parameter**
g	 Group id of the artifact (Required).	query	
a	 Artifact id of the artifact (Required).	query	
v	 Version of the artifact (Required) Supports resolving of "LATEST", "RELEASE" and snapshot versions ("1.0-SNAPSHOT") too.	query	
r	 Repository that the artifact is contained in (Required).

**Return**
only xml documented. Json to be seen by trial.
