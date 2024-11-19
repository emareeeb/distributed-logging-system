from confluent_kafka import Consumer
from elasticsearch import Elasticsearch
import json

KAFKA_BROKER = "localhost:9092"
TOPIC = "logs"

es = Elasticsearch(["http://localhost:9200"])  

consumer = Consumer({
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'log-consumer-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([TOPIC])

print("Listening for messages on Kafka topic...")

try:
    while True:
        msg = consumer.poll(1.0)  

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        log_message = json.loads(msg.value().decode('utf-8'))
        print("Received Message:")
        print(json.dumps(log_message, indent=2))

        es.index(index="logs", body=log_message)
        print("Message indexed in Elasticsearch.")

        if log_message.get("log_level") in ["ERROR", "WARN"]:
            print(f"ALERT: Critical log detected! Level: {log_message['log_level']}")
finally:
    consumer.close()
