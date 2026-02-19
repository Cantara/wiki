# Event-based Logging

Rename to eventing?

> ℹ️ 
> ℹ️ **Auditing** - A log containing changes in the data. Need context (user/timestamp/source ++)
> ℹ️ 

> ℹ️ 
> ℹ️ **Error log** - Something Operations must act on (e.g. apache error log)
> ℹ️ 
> ℹ️ See [Error Push Setup](Error<sub>~Push</sub>~Setup.md)
> ℹ️ 

> ℹ️ 
> ℹ️ **Eventing** - Information to the business support when an event occurs.
> ℹ️ 
> ℹ️ * Errors due to bad data quality
> ℹ️ * Information when customers perform certain operations
> ℹ️ * +++
> ℹ️ 

[

Can these hierarchies be made generic enough so they can be reused. 

Add functionality to send events to a JMS Destination. 

 
Is it a good idea to integrate with existing logging tools? 
"Overbygg" til slf4j 

A possible solution is implementing a Log4J appender deriving from JMSAppender that takes care on ActiveMQ queues instead of generic JMS topics:

We wanted to send info to queues for a client demand, they audit their enterprise application managing MQ Queues, taking care on login info, searches, page access...

For developing purposes It was easier for us to use ActiveMQ as platform, they have their own privative appender, and It should be transparent for our application with a good programming. 

This is a very fast rewritting based on JMSAppender code so, It can be easily improved 

```title

import java.util.Properties;

import javax.jms.MessageProducer;
import javax.jms.ObjectMessage;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueSession;
import javax.jms.Session;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NameNotFoundException;
import javax.naming.NamingException;

import org.apache.log4j.AppenderSkeleton;
import org.apache.log4j.helpers.LogLog;
import org.apache.log4j.spi.ErrorCode;
import org.apache.log4j.spi.LoggingEvent;

/**
 * @author imigueldiaz Mar 31, 2009
 *
 */
public class JMSMQQueueAppender extends AppenderSkeleton {

	  String securityPrincipalName;
	  String securityCredentials;
	  String initialContextFactoryName;
	  String urlPkgPrefixes;
	  String providerURL;
	  String topicBindingName;
	  String tcfBindingName;
	  String userName;
	  String password;
	  boolean locationInfo;
	  
	  QueueConnection queueConnection;
	  QueueSession queueSession;
	  MessageProducer queueSender;
	
	/* (non-Javadoc)
	 * @see org.apache.log4j.AppenderSkeleton#append(org.apache.log4j.spi.LoggingEvent)
	 */
	
	  /**
	     This method called by {@link AppenderSkeleton#doAppend} method to
	     do most of the real appending work.  */
	  public void append(LoggingEvent event) {
	    if(!checkEntryConditions()) {
	      return;
	    }

	    try {
	      ObjectMessage msg = queueSession.createObjectMessage();
	      if(locationInfo) {
		event.getLocationInformation();
	      }
	      msg.setObject(event.getRenderedMessage());
	      queueSender.send(msg);
	    } catch(Exception e) {
	      errorHandler.error("Could not publish message in JMSAppender ["+name+"].", e,
				 ErrorCode.GENERIC_FAILURE);
	    }
	  }

	public void activateOptions() {
	    QueueConnectionFactory  queueConnectionFactory;

	    try {
	      Context jndi;

	      LogLog.debug("Getting initial context.");
	      if(initialContextFactoryName != null) {
		Properties env = new Properties( );
		env.put(Context.INITIAL_CONTEXT_FACTORY, initialContextFactoryName);
		if(providerURL != null) {
		  env.put(Context.PROVIDER_URL, providerURL);
		} else {
		  LogLog.warn("You have set InitialContextFactoryName option but not the "
			     +"ProviderURL. This is likely to cause problems.");
		}
		if(urlPkgPrefixes != null) {
		  env.put(Context.URL_PKG_PREFIXES, urlPkgPrefixes);
		}
		
		if(securityPrincipalName != null) {
		  env.put(Context.SECURITY_PRINCIPAL, securityPrincipalName);
		  if(securityCredentials != null) {
		    env.put(Context.SECURITY_CREDENTIALS, securityCredentials);
		  } else {
		    LogLog.warn("You have set SecurityPrincipalName option but not the "
				+"SecurityCredentials. This is likely to cause problems.");
		  }
		}	
		jndi = new InitialContext(env);
	      } else {
		jndi = new InitialContext();
	      }

	      LogLog.debug("Looking up ["+tcfBindingName+"]");
	      queueConnectionFactory = (QueueConnectionFactory) lookup(jndi, tcfBindingName);
	      LogLog.debug("About to create TopicConnection.");
	      if(userName != null) {
		queueConnection = queueConnectionFactory.createQueueConnection(userName, 
									       password); 
	      } else {
		queueConnection = queueConnectionFactory.createQueueConnection();
	      }

	      LogLog.debug("Creating TopicSession, non-transactional, "
			   +"in AUTO_ACKNOWLEDGE mode.");
	      queueSession = queueConnection.createQueueSession(false,
								Session.AUTO_ACKNOWLEDGE);

	      LogLog.debug("Looking up topic name ["+topicBindingName+"].");
	      Queue queue = (Queue) lookup(jndi, topicBindingName);

	      LogLog.debug("Creating TopicPublisher.");
	      queueSender = queueSession.createSender(queue);
	      
	      LogLog.debug("Starting TopicConnection.");
	      queueConnection.start();

	      jndi.close();
	    } catch(Exception e) {
	      errorHandler.error("Error while activating options for appender named ["+name+
				 "].", e, ErrorCode.GENERIC_FAILURE);
	    }
	  }

	  protected Object lookup(Context ctx, String name1) throws NamingException {
	    try {
	      return ctx.lookup(name1);
	    } catch(NameNotFoundException e) {
	      LogLog.error("Could not find name ["+name1+"].");
	      throw e;
	    }
	  }

	  protected boolean checkEntryConditions() {
	    String fail = null;

	    if(this.queueConnection == null) {
	      fail = "No TopicConnection";
	    } else if(this.queueSession == null) {
	      fail = "No TopicSession";
	    } else if(this.queueSender == null) {
	      fail = "No TopicPublisher";
	    }

	    if(fail != null) {
	      errorHandler.error(fail +" for JMSAppender named ["+name+"].");
	      return false;
	    }
		return true;
	  }

	  /**
	     Close this JMSAppender. Closing releases all resources used by the
	     appender. A closed appender cannot be re-opened. */
	  public synchronized void close() {
	    // The synchronized modifier avoids concurrent append and close operations

	    if(this.closed)
	      return;

	    LogLog.debug("Closing appender ["+name+"].");
	    this.closed = true;

	    try {
	      if(queueSession != null)
		queueSession.close();
	      if(queueConnection != null)
		queueConnection.close();
	    } catch(Exception e) {
	      LogLog.error("Error while closing JMSAppender ["+name+"].", e);
	    }
	    // Help garbage collection
	    queueSender = null;
	    queueSession = null;
	    queueConnection = null;
	  }

	/* (non-Javadoc)
	 * @see org.apache.log4j.Appender#requiresLayout()
	 */
	public boolean requiresLayout() {
		
		return false;
	}

	/**
	 * @return the securityPrincipalName
	 */
	public String getSecurityPrincipalName() {
		return securityPrincipalName;
	}

	/**
	 * @param securityPrincipalName the securityPrincipalName to set
	 */
	public void setSecurityPrincipalName(String securityPrincipalName) {
		this.securityPrincipalName = securityPrincipalName;
	}

	/**
	 * @return the securityCredentials
	 */
	public String getSecurityCredentials() {
		return securityCredentials;
	}

	/**
	 * @param securityCredentials the securityCredentials to set
	 */
	public void setSecurityCredentials(String securityCredentials) {
		this.securityCredentials = securityCredentials;
	}

	/**
	 * @return the initialContextFactoryName
	 */
	public String getInitialContextFactoryName() {
		return initialContextFactoryName;
	}

	/**
	 * @param initialContextFactoryName the initialContextFactoryName to set
	 */
	public void setInitialContextFactoryName(String initialContextFactoryName) {
		this.initialContextFactoryName = initialContextFactoryName;
	}

	/**
	 * @return the urlPkgPrefixes
	 */
	public String getUrlPkgPrefixes() {
		return urlPkgPrefixes;
	}

	/**
	 * @param urlPkgPrefixes the urlPkgPrefixes to set
	 */
	public void setUrlPkgPrefixes(String urlPkgPrefixes) {
		this.urlPkgPrefixes = urlPkgPrefixes;
	}

	/**
	 * @return the providerURL
	 */
	public String getProviderURL() {
		return providerURL;
	}

	/**
	 * @param providerURL the providerURL to set
	 */
	public void setProviderURL(String providerURL) {
		this.providerURL = providerURL;
	}

	/**
	 * @return the topicBindingName
	 */
	public String getTopicBindingName() {
		return topicBindingName;
	}

	/**
	 * @param topicBindingName the topicBindingName to set
	 */
	public void setTopicBindingName(String topicBindingName) {
		this.topicBindingName = topicBindingName;
	}

	  /**
    The <b>TopicConnectionFactoryBindingName</b> option takes a
    string value. Its value will be used to lookup the appropriate
    <code>TopicConnectionFactory</code> from the JNDI context.
  */
 public
 void setTopicConnectionFactoryBindingName(String tcfBindingName) {
   this.tcfBindingName = tcfBindingName;
 }

 /**
    Returns the value of the <b>TopicConnectionFactoryBindingName</b> option.
  */
 public
 String getTopicConnectionFactoryBindingName() {
   return tcfBindingName;
 }

	/**
	 * @return the userName
	 */
	public String getUserName() {
		return userName;
	}

	/**
	 * @param userName the userName to set
	 */
	public void setUserName(String userName) {
		this.userName = userName;
	}

	/**
	 * @return the password
	 */
	public String getPassword() {
		return password;
	}

	/**
	 * @param password the password to set
	 */
	public void setPassword(String password) {
		this.password = password;
	}

	/**
	 * @return the locationInfo
	 */
	public boolean isLocationInfo() {
		return locationInfo;
	}

	/**
	 * @param locationInfo the locationInfo to set
	 */
	public void setLocationInfo(boolean locationInfo) {
		this.locationInfo = locationInfo;
	}

	
	
}

```

log4j.properties related config:

```
log4j.appender.APPENDER_SEGURIDAD=package.info.for.JMSMQQueueAppender
log4j.appender.APPENDER_SEGURIDAD.ProviderURL=tcp://localhost:61616
log4j.appender.APPENDER_SEGURIDAD.InitialContextFactoryName=org.apache.activemq.jndi.ActiveMQInitialContextFactory
log4j.appender.APPENDER_SEGURIDAD.topicBindingName=TEST2
log4j.appender.APPENDER_SEGURIDAD.layout=org.apache.log4j.SimpleLayout
log4j.appender.APPENDER_SEGURIDAD.LocationInfo=true
log4j.appender.APPENDER_SEGURIDAD.TopicConnectionFactoryBindingName=ConnectionFactory
```

jndi.properties related config:

```
java.naming.factory.initial = org.apache.activemq.jndi.ActiveMQInitialContextFactory

# use the following property to configure the default connector
java.naming.provider.url = tcp://localhost:61616

ConnectionFactory=queueConnectionFactory
# register some queues in JNDI using the form
# queue.[jndiName] = [physicalName]
queue.TEST2 = TEST
```
