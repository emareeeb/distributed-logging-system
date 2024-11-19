from confluent_kafka import Consumer
import json

KAFKA_BROKER = "localhost:9092"
TOPIC = "logs"

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

        
        message = json.loads(msg.value().decode('utf-8'))
        print("Received Message:")
        print(json.dumps(message, indent=2))
finally:
    consumer.close()