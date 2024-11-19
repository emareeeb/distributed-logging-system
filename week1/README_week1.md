## Big Data Project - Week 1

### Deliverable 1 -> Configuring nodes generating logs and heartbeat signals.

This week, we set up a basic microservice for generating logs and sending heartbeat signals. Below are the key steps and outputs:

### Steps Implemented:
1. **Node Registration**:
   - Each node registers once upon starting.
   - A "Node Registered" message confirms successful registration.

2. **Heartbeat Signal**:
   - Every 5 seconds, the node sends a heartbeat message with its status, node ID, and timestamp.

3. **Log Generation**:
   - Every 5 seconds, a log is generated with random log levels (`INFO`, `WARN`, `ERROR`).
   - Each log includes details like node ID, service name, message, response time, and timestamp.

### Sample Outputs:
#### Heartbeat Message:
```json
{
  "node_id": "fc3e9602-d1d8-4f00-99d5-9c184aa2cdf6",
  "message_type": "HEARTBEAT",
  "status": "UP",
  "timestamp": 1732024518.6346738
}
```

#### Log Message:
```json
{
  "log_id": "d3c69d02-f2b2-4b4a-905c-901e6c1d875f",
  "node_id": "fc3e9602-d1d8-4f00-99d5-9c184aa2cdf6",
  "log_level": "WARN",
  "message_type": "LOG",
  "message": "This is a WARN log",
  "service_name": "ExampleService",
  "timestamp": 1732024518.6346738,
  "response_time_ms": 250,
  "threshold_limit_ms": 300
}
```

### Next Steps:
- Set up multiple microservices running as independent processes, each with unique node IDs and service names.
- Integrate a Pub-Sub model using Apache Kafka to centralize communication between nodes and the logging system. 

--- 

