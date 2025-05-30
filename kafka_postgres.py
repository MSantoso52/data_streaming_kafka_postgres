import json
from kafka import KafkaConsumer
import psycopg2  # PostgreSQL library

# --- Configuration ---
KAFKA_BROKER = 'localhost:9092'  # Replace with your Kafka broker address
KAFKA_TOPIC = 'new-events'      # Replace with your Kafka topic name
POSTGRES_HOST = 'localhost'     # Replace with your PostgreSQL host
POSTGRES_DB = 'costumer'   # Replace with your PostgreSQL database name
POSTGRES_USER = 'mulyo'     # Replace with your PostgreSQL username
POSTGRES_PASSWORD = 'mulyo' # Replace with your PostgreSQL password

def insert_data_to_postgres(data):
    """
    Inserts the consumed data into the PostgreSQL database.
    """
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )
        cur = conn.cursor()

        # Define the table name and column names
        table_name = 'customer_data'  # Replace with your table name
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))  # Placeholders for values

        # Construct the INSERT query
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

        # Execute the query
        cur.execute(insert_query, list(data.values()))
        conn.commit()

        print("Data inserted successfully into PostgreSQL")

    except psycopg2.Error as e:
        print(f"Error inserting data into PostgreSQL: {e}")

    finally:
        if conn:
            cur.close()
            conn.close()

def consume_from_kafka():
    """
    Consumes data from the Kafka topic and processes it.
    """

    try:
        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=[KAFKA_BROKER],
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

        print(f"Connected to Kafka topic: {KAFKA_TOPIC}")

        for message in consumer:
            # Deserialize the JSON data from Kafka
            customer_data = message.value  
            print(f"Received data: {customer_data}")

            # Insert the data into PostgreSQL
            insert_data_to_postgres(customer_data)

    except Exception as e:
        print(f"Error consuming from Kafka: {e}")

if __name__ == "__main__":
    consume_from_kafka()
