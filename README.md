# data_streaming_kafka_postgres
# *Overview*
Project repo to demonstrate data streaming and data consuming using Kafka. Data streamer using auto generate data using python3 code and consuming then importing into PostgreSQL as data lake. This work flow is demonstrate simple data ingestion using streaming method. 
# *Prerequisites*
To follow along this learning, below requirement need to be available at your system:
- python3 installed with kafka library
  ```bash
  sudo apt instaal python3
  ```
  ```bash
  pip install kafka
  ```
- kafka running on system
  ```bash
  sudo systemctl status kafka
  ```
- postgresql running on system
  ```bash
  sudo systemctl status postgresql
  ```
# *Project Flow*
Data streaming from kafka to postgresql
1. Prequsition -- running kafka server, provide topic for publish-subcription
2. Data streaming -- python3 code to autogenerate json data every 10 sec than publish into kafka
3. Data consume -- python3 code; create postgres connection, sql query for data insertion, kafka consumer connect to topic, insert consume data to postgres
