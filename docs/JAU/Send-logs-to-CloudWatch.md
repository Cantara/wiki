# Send logs to CloudWatch

ConfigService supports forwarding agent logs to Amazon CloudWatch. This is implemented in [no.cantara.cs.cloudwatch.CloudWatchLogger](https://github.com/Cantara/ConfigService/blob/master/src/main/java/no/cantara/cs/cloudwatch/CloudWatchLogger.java).

It assumes that a CloudWatch log group exists (i.e., it must be created manually), but dynamically creates log streams within that group (one log stream per client ID / tag combination).

### Client configuration

The "eventExtractionConfigs" part of the client configuration is used to configure which logs are sent from the agent to ConfigService (and subsequently to CloudWatch). The following example will cause two CloudWatch log streams to be created: foo-jau and foo-agent (assuming the clientId is "foo") within the existing log group "myloggroup":

The regex property is used to match specific log lines from the file. The one specified above for tagName "jau" will only forward log messages containing ERROR, WARN or INFO. The filter only controls what is sent to configservice, so any "non-matching" log lines will still be written to file on the host computer.  
If you wish every line to be sendt to Configservice, the following configuration should be used. "regex" : ".\*"

### Configuration properties

The following configuration properties in ConfigService's [application.properties](https://github.com/Cantara/ConfigService/blob/master/src/main/resources/application.properties) are supported:

- cloudwatch.enabled - Whether Amazon CloudWatch logging is enabled.
- cloudwatch.region - The AWS region to use, e.g., "eu-west-1".
- cloudwatch.maxBatchSize - The max number of log events to bundle per AWS call. Default value: 512. Must not exceed 10,000.
- cloudwatch.internalQueueSize - The max number of log requests to buffer internally. Default value: 1024.

### AWS credentials

ConfigService must be provided with AWS credentials, otherwise calls to CloudWatch will fail. The implementation uses the "Default Credential Provider Chain", meaning that the credentials can be specified as environment variables, system properties, or in the ~/.aws/credentials file.

See <http://docs.aws.amazon.com/AWSSdkDocsJava/latest/DeveloperGuide/credentials.html> for further details.
