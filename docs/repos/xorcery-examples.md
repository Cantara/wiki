# xorcery-examples

Example services for Xorcery

| Field | Value |
| --- | --- |
| **GitHub** | [https://github.com/Cantara/xorcery-examples](https://github.com/Cantara/xorcery-examples) |
| **Language** | Java |
| **Stars** | 5 |
| **Last updated** | 2026-02-09 |

---

## README


# Xorcery Examples

A collection of example applications demonstrating various features and capabilities of the [Xorcery](https://github.com/Cantara/xorcery) framework - a modern, reactive microservices framework for Java.

## Table of Contents

- [About Xorcery](#about-xorcery)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Examples Overview](#examples-overview)
  - [Greeter Example](#greeter-example)
  - [Forum Example](#forum-example)
  - [Streaming Example](#streaming-example)
  - [Persistent Subscriber Example](#persistent-subscriber-example)
- [Building and Running](#building-and-running)
- [Docker Compose Setup](#docker-compose-setup)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Key Technologies](#key-technologies)
- [Migration to Xorcery 0.166.9](#migration-to-xorcery-0166.9)
- [Troubleshooting](#troubleshooting)
- [Documentation](#documentation)
- [Contributing](#contributing)

## About Xorcery

Xorcery is a high-performance, reactive microservices framework built on top of:
- **HK2** for dependency injection
- **Jetty 12** for HTTP/WebSocket server
- **Jersey 3** for REST APIs
- **Project Reactor** for reactive streams
- **Neo4j** for graph database projections
- **OpenTelemetry** for observability

It provides a modular, event-driven architecture with built-in support for:
- Domain-driven design (DDD) with event sourcing
- Reactive streams and backpressure
- WebSocket-based streaming
- Graph database projections
- JWT authentication
- mTLS support
- Service discovery via DNS

## Prerequisites

- **Java 21** or higher
- **Maven 3.8+** for building
- **Docker & Docker Compose** (optional, for running dependencies)

### External Dependencies (Optional)

For the examples, you may need:
- **Neo4j** (graph database for projections) - can run embedded
- **EventStore** (event sourcing database) - for Forum example
- **OpenSearch** (search and analytics) - for Forum example

These can be started using the provided `docker-compose.yaml`.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Cantara/xorcery-examples.git
cd xorcery-examples

# Build all examples
mvn clean install

# Run the Greeter example
cd xorcery-examples-greeter
mvn exec:java -Dexec.mainClass="dev.xorcery.runner.Main"

# Or run tests
mvn test
```

## Examples Overview

### Greeter Example

**Location:** `xorcery-examples-greeter/`

A simple microservice demonstrating:
- **REST API** with JAX-RS resources
- **Domain events** with event sourcing
- **Neo4j projections** for read models
- **Reactive streams** for event processing
- **Thymeleaf** for server-side rendering
- **WebSocket streaming** for real-time updates

**Key Features:**
- `GreeterApplication` - Command handler for updating greetings
- `GreeterService` - Manages Neo4j projection subscriptions
- `GreeterResource` - REST API endpoint (`/api/greeter`)
- Domain event publishing and projection

**API Endpoints:**
- `GET /api/greeter` - Retrieve current greeting
- `POST /api/greeter` - Update greeting with form parameter

**Running:**
```bash
cd xorcery-examples-greeter
mvn clean install
java -jar target/xorcery-examples-greeter-*.jar
```

**Testing:**
```bash
# Run the test
mvn test

# Or manually test the API
curl https://localhost:8443/api/greeter --insecure
curl -X POST https://localhost:8443/api/greeter -d "greeting=Hello%20Xorcery!" --insecure
```

### Forum Example

**Location:** `xorcery-examples-forum/`

A comprehensive forum application showcasing:
- **JSON:API** compliant REST endpoints
- **Complex domain model** (Posts, Comments, Users)
- **Event sourcing** with EventStore
- **Graph database** for efficient querying
- **JWT authentication**
- **Service discovery** via DNS
- **Thymeleaf templating** for web UI

**Domain Model:**
- Posts with title, content, and metadata
- Comments on posts
- User authentication and authorization

**Key Components:**
- `ForumApplication` - Command handlers
- `ForumModel` - Domain logic
- REST resources for Posts, Comments, Forum operations
- Neo4j projections for read models

**Running:**
```bash
# Start dependencies (EventStore, OpenSearch)
docker-compose up -d xe-eventstore xe-opensearch

# Build and run
cd xorcery-examples-forum
mvn clean install
java -jar target/xorcery-examples-forum-*.jar
```

### Streaming Example

**Location:** `xorcery-examples-streaming/`

Demonstrates **reactive stream processing** with multiple processors in a pipeline:

**Architecture:**
```
Source → Processor1 → Processor2 → Processor3 → Result
```

**Components:**
1. **SourceService** - Publishes a stream of numbers (0-99) via WebSocket
2. **Processor1Service** - Adds a "processor1" field with value "foo"
3. **Processor2Service** - Adds "processor2" field with value + 1
4. **Processor3Service** - Adds "processor3" field with value * 3
5. **ResultService** - Subscribes to the stream and prints results

**Key Features:**
- WebSocket-based streaming with backpressure
- Chain multiple processors dynamically
- Reactive transformations using Project Reactor
- Service composition through configuration
- Demonstrates the reactive streams client/server API

**Running:**
You can run each service independently or configure them to chain together:

```bash
# Run the complete pipeline (all processors configured)
cd xorcery-examples-streaming
mvn clean install
java -jar target/xorcery-examples-streaming-*.jar

# Run tests to see the pipeline in action
mvn test
```

### Persistent Subscriber Example (Neo4j Projections)

**Location:** `xorcery-examples-persistentsubscriber/`

Shows how to create **Neo4j event projections** to handle domain events persistently and build read models.

> **⚠️ Important:** This example has been updated for Xorcery 0.166.9+. The old `xorcery-reactivestreams-persistentsubscriber` module has been **replaced** with the **Neo4j projections API**.

**Key Features:**
- `ExamplePersistentSubscriber` - Implements `Neo4jEventProjection` interface
- Filters and processes specific events (e.g., "CreateApplication" command)
- Writes events to Neo4j within transactions
- Automatic retry and error handling
- State management through Neo4j graph database

**What Changed from Previous Versions:**
- **Old API:** Extended `BasePersistentSubscriber` from `xorcery-reactivestreams-persistentsubscriber`
- **New API:** Implements `Neo4jEventProjection` from `xorcery-neo4j-projections`
- **Benefits:**
    - ✅ Better integration with Neo4j
    - ✅ Transactional guarantees
    - ✅ More flexible event handling
    - ✅ Direct access to Neo4j transaction for complex graph operations

**Use Cases:**
- Building read models from event streams
- Creating graph-based projections from domain events
- Event-driven integrations
- Audit logging
- Real-time analytics

**Running:**
```bash
cd xorcery-examples-persistentsubscriber
mvn clean install
java -jar target/xorcery-examples-persistentsubscriber-*.jar

# Run tests
mvn test
```

**Configuration Example:**
```yaml
# Neo4j Projections
neo4jprojections:
  enabled: true
  projections:
    - name: "examplesubscriber"  # Matches @Service(name = "examplesubscriber")
      stream: "applications"      # Stream to subscribe to
      batchSize: 100              # Events per batch
      timeout: 30                 # Timeout in seconds
```

## Building and Running

### Build All Examples

```bash
mvn clean install
```

### Build Individual Example

```bash
cd xorcery-examples-greeter
mvn clean install
```

### Run with Maven

```bash
mvn exec:java -Dexec.mainClass="dev.xorcery.runner.Main"
```

### Run as JAR

```bash
java -jar target/xorcery-examples-greeter-1.166.1-SNAPSHOT.jar
```

### Run Tests

```bash
# All tests
mvn test

# Specific module
mvn test -pl xorcery-examples-greeter

# Specific test
mvn test -Dtest=GreeterResourceTest
```

### JPackage (Native Installer)

Build native installers for your platform:

```bash
mvn clean install -P jpackage
```

The installer will be in `target/jpackage/`.

## Docker Compose Setup

The repository includes a `docker-compose.yaml` for running external dependencies:

```bash
# Start all services
docker-compose up -d

# Start specific services
docker-compose up -d xe-eventstore xe-opensearch

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Remove volumes (clean slate)
docker-compose down -v
```

**Services included:**
- **xe-eventstore** - EventStore for event sourcing (ports 1113, 2113)
- **xe-opensearch** - OpenSearch for search/analytics (port 9200)
- **xe-opensearch-dashboards** - Kibana-like UI (port 5601)

## Project Structure

```
xorcery-examples/
├── pom.xml                              # Parent POM with dependency versions
├── docker-compose.yaml                  # External dependencies
├── README.md                            # This file
│
├── xorcery-examples-greeter/            # Simple REST + Events example
│   ├── src/main/java/
│   │   ├── com/exoreaction/xorcery/examples/greeter/
│   │   │   ├── GreeterApplication.java      # Command handler
│   │   │   ├── GreeterService.java          # Projection service
│   │   │   ├── commands/
│   │   │   │   └── UpdateGreeting.java
│   │   │   └── resources/api/
│   │   │       └── GreeterResource.java     # REST API
│   │   └── module-info.java
│   ├── src/main/resources/
│   │   └── META-INF/xorcery.yaml            # Configuration
│   └── pom.xml
│
├── xorcery-examples-forum/              # Complex forum application
│   ├── src/main/java/
│   │   └── com/exoreaction/xorcery/examples/forum/
│   │       ├── ForumService.java
│   │       ├── contexts/
│   │       ├── entities/
│   │       ├── model/
│   │       └── resources/
│   └── pom.xml
│
├── xorcery-examples-streaming/          # Stream processing pipeline
│   ├── src/main/java/
│   │   └── com/exoreaction/xorcery/examples/streaming/
│   │       ├── source/
│   │       │   └── SourceService.java       # Stream source
│   │       ├── processors/
│   │       │   ├── ProcessorService.java    # Base processor
│   │       │   ├── Processor1Service.java
│   │       │   ├── Processor2Service.java
│   │       │   └── Processor3Service.java
│   │       └── result/
│   │           └── ResultService.java       # Stream consumer
│   └── pom.xml
│
└── xorcery-examples-persistentsubscriber/  # Neo4j projection example
    ├── src/main/java/
    │   └── com/exoreaction/xorcery/examples/persistentsubscriber/
    │       └── ExamplePersistentSubscriber.java  # Implements Neo4jEventProjection
    ├── src/main/resources/
    │   └── META-INF/xorcery.yaml
    ├── src/test/java/
    │   └── com/exoreaction/xorcery/examples/persistentsubscriber/test/
    │       └── ExamplePersistentSubscriberTest.java
    └── pom.xml
```

## Configuration

Each example has its own `xorcery.yaml` configuration file in `src/main/resources/META-INF/`.

### Key Configuration Properties

```yaml
# Instance configuration
instance:
  id: "{{ instance.host }}"
  host: "{{ CALCULATED.hostName }}"
  domain: "xorcery.test"
  environment: "development"

# Application metadata
application:
  name: "xorcery-example"
  version: "1.166.1-SNAPSHOT"

# Jetty server
jetty.server:
  http:
    enabled: true
    port: 8080
  ssl:
    enabled: true
    port: 8443

# SSL/TLS certificates
certificates:
  enabled: true
  dnsNames:
    - localhost
  ipAddresses:
    - 127.0.0.1

# Keystores
keystores:
  enabled: true
  keystore:
    path: "{{ instance.home }}/keystore.p12"
    password: "password"

# Neo4j configuration
neo4j:
  enabled: true
  uri: "neo4j://localhost:7687"
  # For embedded database
  home: "{{ instance.home }}/neo4j"

# Neo4j Projections
neo4jprojections:
  enabled: true
  projections:
    - name: "examplesubscriber"
      stream: "applications"
      batchSize: 100
      timeout: 30

# Domain Events
domainevents:
  enabled: true
  publisher:
    enabled: true

# Reactive Streams
reactivestreams:
  server:
    enabled: true
  client:
    enabled: true

# OpenTelemetry
opentelemetry:
  enabled: true
  serviceName: "xorcery-example"
  
# Logging
log4j2:
  Configuration:
    status: INFO
    Loggers:
      Root:
        level: INFO
      Logger:
        - name: com.exoreaction.xorcery.examples
          level: DEBUG
```

### Environment Variables

Configuration values can be overridden with environment variables:
- `INSTANCE_NAME` - Instance name
- `INSTANCE_ENVIRONMENT` - Environment (dev, test, prod)
- `JETTY_SERVER_HTTP_PORT` - HTTP port
- `JETTY_SERVER_SSL_PORT` - HTTPS port
- `NEO4J_URI` - Neo4j connection URI
- `EVENTSTORE_HOST` - EventStore host
- `OPENSEARCH_HOST` - OpenSearch host

## Key Technologies

| Technology | Purpose | Version |
|-----------|---------|---------|
| **Xorcery** | Microservices Framework | 0.166.9 |
| **Java** | Programming Language | 21+ |
| **Maven** | Build Tool | 3.8+ |
| **HK2** | Dependency Injection | 3.1.1 |
| **Jersey** | JAX-RS REST API | 3.1.11 |
| **Jetty** | HTTP/WebSocket Server | 12.1.1 |
| **Project Reactor** | Reactive Streams | 3.7.11 |
| **Neo4j** | Graph Database | 5.28.5 |
| **Log4j** | Logging | 2.25.2 |
| **Jackson** | JSON Processing | 2.20.0 |
| **Thymeleaf** | Template Engine | 3.1.2 |
| **JUnit** | Testing | 6.0.0 |
| **OpenTelemetry** | Observability | 1.54.1 |

## Migration to Xorcery 0.166.9

These examples have been migrated from earlier versions of Xorcery to 0.166.9, which includes several **breaking changes**.


*(README truncated at 500 lines)*
