import time
import uuid
import json
from random import choice, randint


SERVICE_NAME = "ServiceNode3"  
NODE_ID = str(uuid.uuid4())  


def register_node():
    registration_message = {
        "node_id": NODE_ID,
        "message_type": "REGISTRATION",
        "service_name": SERVICE_NAME,
        "timestamp": time.time()
    }
    print("Node Registered:")
    print(json.dumps(registration_message, indent=2))


def send_heartbeat():
    heartbeat_message = {
        "node_id": NODE_ID,
        "message_type": "HEARTBEAT",
        "status": "UP",
        "timestamp": time.time()
    }
    print("Heartbeat Sent:")
    print(json.dumps(heartbeat_message, indent=2))


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


if __name__ == "__main__":
    register_node()

   
    while True:
        send_heartbeat()
        generate_log()  
        time.sleep(5)