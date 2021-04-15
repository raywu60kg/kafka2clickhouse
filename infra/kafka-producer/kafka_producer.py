from datetime import datetime
from kafka import KafkaProducer
import json
import logging
import os
import random
import string
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger("kafka-producer")



kafka_url = os.getenv("KAFKA_URL", "kafka:9092")
kafka_url_list = kafka_url.split(",")
kafka_topic = os.getenv("KAFKA_TOPIC", "topic")
def main():
    try:
        logger.info(kafka_url_list)
        logger.info(kafka_topic)
        producer = KafkaProducer(bootstrap_servers=kafka_url_list, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        logger.info("Connect to kafka")
    except Exception as e:
        logger.error("Connect to kafka error: {}".format(e))

    while True:
        # kafka produce
        try:
            message = {
                "timestamp":int(datetime.now().timestamp()), 
                "level": random.choice(["INFO", "ERROR", "DEBUG", "WARN"]), 
                "message": ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            }
            future = producer.send(kafka_topic, message)
            record_metadata = future.get(timeout=10)
            logger.info(
                "Successfully produce to kafka on topic: {}, "
                "partition: {}, "
                "offset: {}".format(
                    record_metadata.topic,
                    record_metadata.partition,
                    record_metadata.offset))
            producer.flush()
        except Exception as e:
            logger.error("Kafka produce error: {}".format(e))
        logger.info("Sent message {}".format(message))
        time.sleep(1)

if __name__ == "__main__":
    main()

