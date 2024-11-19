from confluent_kafka import Producer
import time
import uuid
import json
from random import choice, randint

# Kafka Configuration
KAFKA_BROKER = "192.168.64.6:9092"  # Replace localhost with the IP of VM 1
TOPIC = "logs"

# Kafka Producer
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

# Configuration for the Microservice
SERVICE_NAME = "ServiceNode2"
NODE_ID = str(uuid.uuid4())

# Function to send messages to Kafka
def send_to_kafka(topic, message):
    try:
        producer.produce(topic, json.dumps(message).encode('utf-8'))
        producer.flush()  # Ensure the message is sent
    except Exception as e:
        print(f"Failed to send message to Kafka: {e}")

# Function to simulate node registration
def register_node():
    registration_message = {
        "node_id": NODE_ID,
        "message_type": "REGISTRATION",
        "service_name": SERVICE_NAME,
        "timestamp": time.time()
    }
    send_to_kafka(TOPIC, registration_message)
    print("Node Registered and Sent to Kafka")

# Function to simulate heartbeat messages
def send_heartbeat():
    heartbeat_message = {
        "node_id": NODE_ID,
        "message_type": "HEARTBEAT",
        "status": "UP",
        "timestamp": time.time()
    }
    send_to_kafka(TOPIC, heartbeat_message)
    print("Heartbeat Sent to Kafka")

# Function to simulate log generation
def generate_log():
    log_levels = ["INFO", "WARN", "ERROR"]
    log_level = choice(log_levels)
    log_message = {
        "log_id": str(uuid.uuid4()),
        "node_id": NODE_ID,
        "log_level": log_level,
        "message_type": "LOG",
        "message": f"This is a {log_level} log",
        "service_name": SERVICE_NAME,
        "timestamp": time.time()
    }

    # Add extra fields for WARN and ERROR logs
    if log_level == "WARN":
        log_message.update({
            "response_time_ms": randint(100, 500),
            "threshold_limit_ms": 300
        })
    elif log_level == "ERROR":
        log_message.update({
            "error_details": {
                "error_code": "500",
                "error_message": "Internal Server Error",
            },
        })

    send_to_kafka(TOPIC, log_message)
    print(f"{log_level} Log Sent to Kafka")

# Main
if __name__ == "__main__":
    register_node()

    # Periodically send heartbeat and logs
    while True:
        send_heartbeat()
        generate_log()
        time.sleep(5)

