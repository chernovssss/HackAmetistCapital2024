import time
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="HackAmetist",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
)

text = st.text_input(
    "Search",
    placeholder="Например: DIN-рейка",
)

if text:
    st.write(text)
