from confluent_kafka import Consumer
import streamlit as st
import json

st.set_page_config(page_title="MY LABA1", layout="wide")
if "MSE" not in st.session_state:
    st.session_state["MSE"] = []

bootstrap_servers = "kafka-0:9097"

data_visualization_consumer = Consumer(
    {"bootstrap.servers": bootstrap_servers, "group.id": "my_consumers"}
)
data_visualization_consumer.subscribe(["online-learning"])

chart_holder = st.empty()

while True:
    message = data_visualization_consumer.poll(20)
    if message is not None:
        stock_data = json.loads(message.value().decode("utf-8"))
        st.session_state["MSE"].append(stock_data["MSE"])
        chart_holder.line_chart(st.session_state["MSE"])
