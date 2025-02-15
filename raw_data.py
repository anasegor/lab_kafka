from confluent_kafka import Producer
import random
import time
import json
import pandas as pd

bootstrap_servers1 = "kafka-0:9097"
topic = "raw_data"
conf = {"bootstrap.servers": bootstrap_servers1}
data_producer1 = Producer(conf)


data_train = pd.read_csv("./data/train.csv")


def generate_stock_data():
    k = random.randint(0, data_train.shape[0] - 1)
    return data_train.iloc[k].to_dict()


def produce_stock_data():
    while True:
        stock_data = generate_stock_data()
        data_producer1.produce(topic, key="1", value=json.dumps(stock_data))
        data_producer1.flush()
        time.sleep(0.1)
        print("send")


if __name__ == "__main__":
    produce_stock_data()
