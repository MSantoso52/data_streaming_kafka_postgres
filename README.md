# data_streaming_kafka_postgres
Data streaming from kafka to postgresql
1. Prequsition -- running kafka server, provide topic for publish-subcript
2. Data streaming -- python3 code to autogenerate json data every 10 sec than publish into kafka
3. Data consume -- python3 code; create postgres connection, sql query for data insertion, kafka consumer connect to topic, insert consume data to postgres
