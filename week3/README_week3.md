# README.md

## Big Data Project - Week 3

### Deliverable 3: Log Storage, Alerting, and Visualization

This week, our team focused on setting up log storage and alerting using Elasticsearch, and visualizing logs with Kibana. Below are the steps we completed:

---

### Steps Completed:

1. **Set Up Elasticsearch**:
   - Navigated to the Elasticsearch directory:
     ```bash
     cd elasticsearch-*
     ```
   - Started Elasticsearch in the background:
     ```bash
     bin/elasticsearch
     ```
   - Kept the terminal open to monitor Elasticsearch logs.
   - Verified Elasticsearch was running in another terminal:
     ```bash
     curl http://localhost:9200
     ```
   - Confirmed a response with details about the Elasticsearch node.

2. **Updated Kafka Consumer**:
   - Modified the `log_consumer.py` file to store logs in Elasticsearch.
   - Added alerting for critical logs (`ERROR` or `WARN` levels).

3. **Ran Updated Components**:
   - Ensured Elasticsearch was running on **VM1**.
   - Ran the updated `log_consumer.py` on **VM1**.
   - Ran the existing `node_1.py`, `node_2.py`, and `node_3.py` (unchanged from Deliverable 2) on **VM2**.
   - Verified that `log_consumer.py` displayed alerts and stored critical logs in Elasticsearch.

4. **Added Visualizations with Kibana**:
   - Installed and ran Kibana:
     ```bash
     cd kibana-*
     bin/kibana
     ```
   - Waited until Kibana started and was available at:
     [http://localhost:5601](http://localhost:5601).
   - Configured the logs index pattern in Kibana.
   - Created charts, tables, and dashboards for monitoring and visualizing the logs.

---

### Key Challenge Faced:

One major issue encountered during the project was the inability to add configuration files for Kafka, Kibana, and Elasticsearch to GitHub due to repository space limitations. These configuration files were essential for setting up and running the system but exceeded GitHub's file size limits, preventing their inclusion in version control. 

---

### Outcome:
- Logs are now stored in Elasticsearch for querying and analysis.
- Alerts for critical logs are displayed in real-time by the updated `log_consumer.py`.
- Visualizations, including dashboards, charts, and tables, were created in Kibana to monitor log data effectively.

---

### Final Note:
This project successfully demonstrated a complete pipeline for log generation, real-time processing, storage, alerting, and visualization using a robust big data architecture. The implemented system is scalable, reliable, and provides valuable insights for monitoring and debugging distributed systems.