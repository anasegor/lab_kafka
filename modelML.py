from confluent_kafka import Consumer, Producer
import json
from river import tree, linear_model, metrics

model = linear_model.LinearRegression()
# model = tree.HoeffdingTreeRegressor()
metric_mse = metrics.MSE()
metric_logloss = metrics.LogLoss()

bootstrap_servers2 = "kafka-1:9098"

predict_data_consumer = Consumer(
    {"bootstrap.servers": bootstrap_servers2, "group.id": "my_consumers"}
)
predict_data_consumer.subscribe(["preprocessed_data"])

bootstrap_servers1 = "kafka-0:9097"
predict_data_producer = Producer({"bootstrap.servers": bootstrap_servers1})


def prediction():
    while True:
        message = predict_data_consumer.poll(20)
        if message is not None:
            stock_data = json.loads(message.value().decode("utf-8"))
            X = {k: v for k, v in stock_data.items() if k != "TARGET(PRICE_IN_LACS)"}
            y = stock_data.get("TARGET(PRICE_IN_LACS)")
            if y is not None:
                model.learn_one(X, y)
                y_pred = model.predict_one(X)
                metric_mse.update(y, y_pred)
                metric_logloss.update(y, y_pred)

            predict_data_producer.produce(
                "online-learning",
                key="1",
                value=json.dumps(
                    {"MSE": metric_mse.get(), "LogLoss": metric_logloss.get()}
                ),
            )
            predict_data_producer.flush()


if __name__ == "__main__":
    prediction()
