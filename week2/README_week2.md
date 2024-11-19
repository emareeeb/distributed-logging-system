# README.md

## Big Data Project - Week 2

### Deliverable 2: 

This week, we implemented a Pub-Sub model using Apache Kafka to enable communication between multiple nodes and a centralized logging system. We consigured two Virtual Machines (vm1 and vm2). The vm1 has the `log_consumer.py` and is tasked to listen for messages on the kafka topic. The vm2 on the other hand runs all the updated (`node_1.py`, `node_2.py` and `node_3.py`) files.
---

### Steps Completed:

1. **Downloaded and Installed Apache Kafka**:
   - Installed Kafka on both virtual machines (VM1 and VM2).
   - Navigated to the Kafka directory:  
     ```bash
     cd kafka_*/
     ```

2. **Started Kafka and Zookeeper**:
   - On both VM1 and VM2, we started Zookeeper:  
     ```bash
     bin/zookeeper-server-start.sh config/zookeeper.properties
     ```
   - In a new terminal, we started the Kafka server:  
     ```bash
     bin/kafka-server-start.sh config/server.properties
     ```

3. **Set Up Log Consumer**:
   - Created a Python file `log_consumer.py` on VM1 to consume logs from Kafka.

4. **Connected VM1 and VM2**:
   - Checked the IP address of VM1:  
     ```bash
     ifconfig  # (or `ipconfig` on Windows)
     ```
   - Verified connectivity from VM2:  
     ```bash
     ping <VM1-IP>
     ```
   - Tested Kafka port connectivity from VM2:  
     ```bash
     telnet <VM1-IP> 9092
     ```

5. **Modified Node Code**:
   - Updated the code of `node_1.py`, `node_2.py`, and `node_3.py` to connect to the Kafka broker running on VM1.

6. **Ran All Files**:
   - Opened and ran the following files on their respective machines:
     - On **VM2**: `node_1.py`, `node_2.py`, `node_3.py`
     - On **VM1**: `log_consumer.py`

---

### Outcome:
- Successfully established communication between nodes running on VM2 and the Kafka broker on VM1.
- Logs from all nodes were consumed and processed by the log consumer in real-time.

---

### Next Steps:
- Enhance log analytics by introducing Apache Spark for processing Kafka streams.