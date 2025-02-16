from confluent_kafka import Producer
import sys
import random
import time
import json
import pandas as pd

bootstrap_servers1 = "kafka-0:9097"
topic = "raw_data"
conf = {"bootstrap.servers": bootstrap_servers1}
data_producer1 = Producer(conf)


def produce_stock_data():
    for i in range(data_train.shape[0]):
        stock_data = data_train.iloc[i].to_dict()
        data_producer1.produce(topic, key="1", value=json.dumps(stock_data))
        data_producer1.flush()
        time.sleep(0.2)
        print("send")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data_train = pd.read_csv(sys.argv[1])
    else:
        data_train = pd.read_csv("./data/train1.csv")

    produce_stock_data()
