import json
import time
import random
import logging
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable


logging.basicConfig(level=logging.INFO)


# Kafka configuration
KAFKA_BROKER = "kafka:9092"  # Replace with "localhost:9092" for local testing
TOPIC = "random_numbers"

# data generator
def generate_data(range_start=0, range_end=100):
    return {
        "a": random.randint(range_start, range_end),
        "b": random.randint(range_start, range_end)
    }


# Initialize Kafka producer
def create_producer():
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers=['kafka:9092'],
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                acks='all',
                retries=5
            )
            logging.info("Connected to Kafka")
            return producer
        except NoBrokersAvailable as e:
            logging.warning(f"Kafka broker not available ({e}), retrying in 5 seconds...")
            time.sleep(5)

producer = create_producer()

try:
    print("Starting producer...")
    while True:
        # Generate weather data
        rg_data = generate_data()
        # Send data to Kafka topic
        producer.send(TOPIC, rg_data)
        logging.info(f"Sent: {rg_data}")
        time.sleep(1)  # Wait before sending the next message
except KeyboardInterrupt:
    logging.error("Producer stopped.")
finally:
    producer.close()