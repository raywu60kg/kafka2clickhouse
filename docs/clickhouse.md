# clickhouse

clickhouse client
```bash
docker run -it --rm --network kafka2clickhouse yandex/clickhouse-client:21.1 --host clickhouse-server
```

create table
```
CREATE TABLE queue (
    timestamp UInt64,
    level String,
    message String
) ENGINE = Kafka SETTINGS 
    kafka_broker_list = 'kafka:9092',
    kafka_topic_list = 'topic',
    kafka_group_name = 'group1',
    kafka_format = 'JSONEachRow',
    kafka_num_consumers = 1;

CREATE TABLE app_log (
    date Date,
    level String,
    message String
) ENGINE = MergeTree()
PRIMARY KEY(date);

CREATE MATERIALIZED VIEW consumer TO app_log
    AS SELECT toDateTime(timestamp) AS date, level, message as message FROM queue;
```

check data
```
select * from app_log limit 5;
```