# WebSphere deployment from a CI environment

## Problems with deploying from CI-server

There may be better way of doing deployment than what is presented here. In such a case, please let us know

Deployment to WebSphere from a CI<sub>~server can be troublesome since the deployment tool, wsadmin, is tighty coupled with the WebSphere Application Server.  Also, wsadmin is quite CPU intensive when doing network deployment, and CI</sub>~servers normally has quite a large load even without wsadmin running.

So why not let wsadmin fetch the artifacts from the Maven repostitory? That allows us to use wsadmin on the server, and we avoid version conflicts. Pull processes is also a lot more scalable, and we can deploy one application to ten servers just as easily as when we deploy it to one server.

The following script can be used to get a artifact from a Maven repository and install it on WebSphere.
```
import urllib
import xml.dom.minidom
import os.path
import StringIO

#Configuration information. Could be fetched from a service...
CI_SERVER = 'http://base/url/to/repo'
ARTIFACT_ID = 'objectware-ear'
PACKAGING = 'ear' #The packaging of the archive to install
WEB_ARTIFACT_NAME = 'objectware-web' #There should be a better way of finding this..
GROUP_ID = 'no.objectware.agile'
VERSION = '1.0-SNAPSHOT'
PATH_TO_WORK_DIR = 'c:\\tmp' #Where to download the artifacts

from java.io import FileInputStream
from javax.xml.transform.stream import StreamSource
from javax.xml.transform.stream import StreamResult
from java.io import ByteArrayInputStream
from javax.xml.parsers import DocumentBuilderFactory

# Using Java's XML parsers. There are known problems with minidom in Jyton 2.1 (WAS 6.1)
# We must parse xml to get information from maven-metadata.xml. Dream: use a maven java library instead of writing our own..
class Parser:
	def __init__(self, input):
	 	factory = DocumentBuilderFactory.newInstance()
 		builder = factory.newDocumentBuilder()
		document = builder.parse(ByteArrayInputStream(input))
		self.buildNumber = document.getElementsByTagName('buildNumber').item(0).getChildNodes().item(0).getTextContent()		
		self.timestamp = document.getElementsByTagName('timestamp').item(0).getChildNodes().item(0).getTextContent()		

class Installer:
	def __init__(self, path_to_artifact, application_name):
		self.path_to_artifact = path_to_artifact
		self.application_name = application_name
	def install(self):
		app_name = self.application_name
		path_to_app = self.path_to_artifact
		list_of_installed_artifacts = AdminApp.list();
		print "List of installed artifacts: ", list_of_installed_artifacts
#Reinstalls if already installed. Could consider doing an update. This is ripped from the admin console.
		try:
			AdminApp.uninstall(app_name)
		except:
			print "Application not installed"
		name_of_war = WEB_ARTIFACT_NAME + '-' + VERSION + '.war'
		print AdminApp.install(path_to_app, '[ -preCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb -appname ' + '\'' + app_name  + '\''+ ' -noreloadEnabled -nodeployws -validateinstall warn -noprocessEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -noallowDispatchRemoteInclude -noallowServiceRemoteInclude -MapWebModToVH [[ ' + name_of_war + ' ' + name_of_war + ',WEB-INF/web.xml default_host ]]]' )	
		AdminConfig.save();
		am = AdminControl.queryNames('type=ApplicationManager,process=server1,*')
		print "Application manager: " + am		
		AdminControl.invoke(am, 'startApplication', '[' + app_name + ']') 
		print AdminApp.list()

class ArtifactFetcher:
	def __init__(self, ci_server, artifact_id, group_id, version, packaging, workdir):
		self.workdir = workdir
		self.baseurl = ci_server + group_id.replace('.','/') + '/' \
		+ artifact_id + "/" + version + "/"
		maven_metadata = urllib.urlopen(self.baseurl + "maven-metadata.xml").read()
		version = VersionFinder(maven_metadata).find_version()
		self.latest_artifact = self.artifact_id + "-" + self.version.replace("SNAPSHOT","") + version + "." + self.packaging;
		print "Latest artifact is: " + self.latest_artifact

	def get_artifact(self):
		artifact_url = self.baseurl + self.latest_artifact
		print "Fetching from " + artifact_url
		block_size = 4096*1024
		count = 0
		temp = urllib.urlopen(artifact_url)
		headers = temp.info()
		size = int(headers['Content-Length'])
		data = open(self.get_filename_of_latest_artifact(), 'wb')
		i = 0;
		print "Size of artifact: " + `size`	
		while i < size:
			data.write(temp.read(block_size))
			i += block_size
			count += i
			print "Lastet ned: " + `count`;
		print "\n"
		data.close()
		temp.close()		
	def get_filename_of_latest_artifact(self):
		return	self.workdir + "/" + self.latest_artifact

	def has_newer_artifact(self):
		return not os.path.isfile(self.get_filename_of_latest_artifact())

class VersionFinder:
	def __init__(self, xmlfile):
		self.xmlfile = xmlfile
	def find_version(self):
		try:
			parser = Parser(self.xmlfile)
		except e:
			print "Could not parse XML"
			print self.xmlfile
			raise exception("Could not parse XML from maven repo")
		return parser.timestamp + "-" + parser.buildNumber
	def get_text(self, element):
		return element[0].childNodes[0].data

# The actual work
c = ArtifactFetcher(CI_SERVER, ARTIFACT_ID, GROUP_ID, VERSION, PACKAGING, PATH_TO_WORK_DIR)
if c.has_newer_artifact():
	print "New artifact found. Downloading"
	c.get_artifact()
	installer = Installer(c.get_filename_of_latest_artifact(), ARTIFACT_ID)
	installer.install()
else:		
	print "No new artifacts found."
```
