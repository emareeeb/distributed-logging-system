import time
import uuid
import json
from random import choice, randint

# Configuration for the Microservice
SERVICE_NAME = "ExampleService"  # Change this name for different services
NODE_ID = str(uuid.uuid4())  # Unique Node ID for this service

# Function to simulate node registration
def register_node():
    registration_message = {
        "node_id": NODE_ID,
        "message_type": "REGISTRATION",
        "service_name": SERVICE_NAME,
        "timestamp": time.time()
    }
    print("Node Registered:")
    print(json.dumps(registration_message, indent=2))

# Function to simulate heartbeat messages
def send_heartbeat():
    heartbeat_message = {
        "node_id": NODE_ID,
        "message_type": "HEARTBEAT",
        "status": "UP",
        "timestamp": time.time()
    }
    print("Heartbeat Sent:")
    print(json.dumps(heartbeat_message, indent=2))

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

    # Additional fields for WARN and ERROR levels
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

    print("Log Generated:")
    print(json.dumps(log_message, indent=2))

# Main
if __name__ == "__main__":
    register_node()

    # Send heartbeat and logs every 5 seconds
    while True:
        send_heartbeat()
        generate_log()  # Generate a random log
        time.sleep(5)