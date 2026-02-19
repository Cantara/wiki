# Start a new JVM from Java

The following code shows how to use the ProcessBuilder to start a new operating system process and load a new JVM in that process. This can be used to set up in-memory integration testing. E.g. fire up an ActiveMQ JMS server in a separate process to test the integration with JMS Destinations. Performance, stability and network robustness cannot be tested with this approach of course, but the basic regression aspects like publish, subscribe, etc. can. 

A StreamGobbler can be used for logging and debugging. (Tip: Google "StreamGobbler". Feel free to add a reference if you find any good documentation.) 

**TODO**: Perhaps add a more complex example which shows the use of StreamGobblers? 

```java
//import org.apache.log4j.Logger;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class ProcessHelper {
  //private static Logger log = Logger.getLogger(ProcessHelper.class);
  private List<Process> processes;

  public ProcessHelper() {
    processes = new ArrayList< Process >();

  }

  public Process startNewJavaProcess(final String optionsAsString, final String mainClass, final String[] arguments)
      throws IOException {

    ProcessBuilder processBuilder = createProcess(optionsAsString, mainClass, arguments);
    Process process = processBuilder.start();
    processes.add(process);
    //log.debug("Process " + process.toString() + " has started");
    return process;
  }

  private ProcessBuilder createProcess(final String optionsAsString, final String mainClass, final String[] arguments) {
    String jvm = System.getProperty("java.home") + File.separator + "bin" + File.separator + "java";
    String classpath = System.getProperty("java.class.path");
    //log.debug("classpath: " + classpath);
    // String workingDirectory = System.getProperty("user.dir");

    String[] options = optionsAsString.split(" ");
    List < String > command = new ArrayList <String>();
    command.add(jvm);
    command.addAll(Arrays.asList(options));
    command.add(mainClass);
    command.addAll(Arrays.asList(arguments));

    ProcessBuilder processBuilder = new ProcessBuilder(command);
    Map< String, String > environment = processBuilder.environment();
    environment.put("CLASSPATH", classpath);
    return processBuilder;
  }

  public void killProcess(final Process process) {
    process.destroy();
  }

  /**
   * Kill all processes.
   */
  public void shutdown() {
    //log.debug("Killing " + processes.size() + " processes.");    
    for (Process process : processes) {
      killProcess(process);
    }
  }
}
```
