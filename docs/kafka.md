# kafka


## kafka test

create client
```
docker run -it --rm \
    --network app-tier \
    -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 \
    bitnami/kafka:latest kafka-topics.sh --list  --zookeeper zookeeper-server:2181
```

console test
```bash
kafka-console-producer.sh --broker-list kafka:9092 --topic test
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic test --from-beginning
```