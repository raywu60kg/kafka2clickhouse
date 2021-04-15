# kafka


## kafka test
console producer
```
docker run -it --rm \
    --name kafka-console-producer \
    --network kafka2clickhouse \
    -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181 \
    bitnami/kafka:2 kafka-console-producer.sh --broker-list kafka:9092 --topic test
```

console consumer
```
docker run -it --rm \
    --name kafka-console-consumer \
    --network kafka2clickhouse \
    -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181 \
    bitnami/kafka:2 kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic test --from-beginning
```

