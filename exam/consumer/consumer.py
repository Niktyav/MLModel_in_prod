import json
import logging
import time
from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import pickle
from sklearn.linear_model import LinearRegression
import os

logging.basicConfig(level=logging.INFO)



# Kafka configuration
KAFKA_BROKER = "kafka:9092"  # Replace with "localhost:9092" for local testing
TOPIC = "random_numbers"

TOPIC_PRED = "predicted_sums"

with open("sum_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

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

producer_sum_pred = create_producer()


def create_consumer():
    while True:
        try:
            consumer = KafkaConsumer(
                TOPIC,
                bootstrap_servers=[KAFKA_BROKER],
                auto_offset_reset='earliest',
                enable_auto_commit=False,
                group_id=f'{TOPIC}-consumers',
                value_deserializer=lambda x: json.loads(x.decode('utf-8'))
            )
            logging.info("Connected to Kafka")
            return consumer
        except NoBrokersAvailable as e:
            logging.warning(f"Kafka broker not available ({e}), retrying in 5 seconds...")
            time.sleep(5)

consumer = create_consumer()




try:
    print("Starting consumer...")
    for message in consumer:
        try:
            rg_data = message.value
            logging.info(f"Received: {rg_data}")
            a = rg_data['a']
            b = rg_data['b']
            # Использование загруженной модели для предсказания
            new_numbers = [a, b]
            predicted_sum = {'pred_sum':loaded_model.predict([new_numbers])[0]}
            producer_sum_pred.send(TOPIC_PRED, predicted_sum)
            logging.info(f"Sent: {predicted_sum}")
        except Exception as e:
            logging.error(f"error: {e}")

      
except KeyboardInterrupt:
     logging.info("Consumer stopped.")
finally:
    consumer.close()


