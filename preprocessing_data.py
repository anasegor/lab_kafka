from confluent_kafka import Consumer, Producer
import pandas as pd
import json
import utilities as myModel


bootstrap_servers1 = "kafka-0:9097"
data_preprocess_consumer = Consumer(
    {"bootstrap.servers": bootstrap_servers1, "group.id": "my_consumers"}
)
data_preprocess_consumer.subscribe(["raw_data"])

bootstrap_servers2 = "kafka-1:9098"
data_preprocess_producer = Producer({"bootstrap.servers": bootstrap_servers2})


def preprocessing():
    while True:
        message = data_preprocess_consumer.poll(200)
        if message is not None:
            stock_data = json.loads(message.value().decode("utf-8"))
            data = pd.DataFrame([stock_data])
            data = myModel.preprocess_data(data, myModel.map_city)
            data_preprocess_producer.produce(
                "preprocessed_data", key="1", value=json.dumps(data.iloc[0].to_dict())
            )
            data_preprocess_producer.flush()


if __name__ == "__main__":
    preprocessing()
