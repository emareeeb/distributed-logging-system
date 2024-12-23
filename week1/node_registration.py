from confluent_kafka import Producer
import time
import uuid
import json
from random import choice, randint

SERVICE_NAME = "ServiceNode1"
NODE_ID = str(uuid.uuid4())
TOPIC = "logs"  

KAFKA_BROKER = "localhost:9092"
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

def send_to_kafka(topic, message):
    producer.produce(topic, json.dumps(message).encode('utf-8'))
    producer.flush()

def register_node():
    registration_message = {
        "node_id": NODE_ID,
        "message_type": "REGISTRATION",
        "service_name": SERVICE_NAME,
        "timestamp": time.time()
    }
    send_to_kafka(TOPIC, registration_message)
    print(f"Node {SERVICE_NAME} registered with ID {NODE_ID}")

def send_heartbeat():
    heartbeat_message = {
        "node_id": NODE_ID,
        "message_type": "HEARTBEAT",
        "status": "UP",
        "timestamp": time.time()
    }
    send_to_kafka(TOPIC, heartbeat_message)
    print("Heartbeat sent.")

def generate_log():
    log_levels = ["INFO", "WARN", "ERROR"]
    log_level = choice(log_levels)
    log_message = {
        "log_id": str(uuid.uuid4()),
        "node_id": NODE_ID,
        "log_level": log_level,
        "message_type": "LOG",
        "message": f"This is a {log_level} log.",
        "service_name": SERVICE_NAME,
        "timestamp": time.time()
    }

    if log_level == "WARN":
        log_message.update({
            "response_time_ms": randint(100, 500),
            "threshold_limit_ms": 300
        })
    elif log_level == "ERROR":
        log_message.update({
            "error_details": {
                "error_code": "500",
                "error_message": "Internal Server Error"
            }
        })

    send_to_kafka(TOPIC, log_message)
    print(f"{log_level} log sent.")


if __name__ == "__main__":
    register_node()
    while True:
        send_heartbeat()
        generate_log()
        time.sleep(5)
