from confluent_kafka import Consumer
import streamlit as st
import json

st.set_page_config(page_title="MY LABA1", layout="wide")

if "MSE" not in st.session_state:
    st.session_state["MSE"] = []
if "LogLoss" not in st.session_state:
    st.session_state["LogLoss"] = []

bootstrap_servers1 = "kafka-0:9097"

data_visualization_consumer = Consumer(
    {"bootstrap.servers": bootstrap_servers1, "group.id": "my_consumers"}
)
data_visualization_consumer.subscribe(["online-learning"])

st.header(
    "The task of predicting the price of a house https://www.kaggle.com/datasets/anmolkumar/house-price-prediction-challenge/data"
)
st.subheader("MSE")
chart_holder_mse = st.empty()
st.subheader("LogLoss")
chart_holder_logloss = st.empty()

while True:
    message = data_visualization_consumer.poll(20)
    if message is not None:
        stock_data = json.loads(message.value().decode("utf-8"))
        st.session_state["MSE"].append(stock_data.get("MSE"))
        st.session_state["LogLoss"].append(stock_data.get("LogLoss"))
        chart_holder_mse.line_chart(st.session_state["MSE"])
        chart_holder_logloss.line_chart(st.session_state["LogLoss"])
