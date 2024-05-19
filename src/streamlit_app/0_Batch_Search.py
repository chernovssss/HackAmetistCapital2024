import time
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="HackAmetist",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
)

upload_files = st.file_uploader(
    label="Загрузите файл с данными",
    type=[
        "csv",
        "xlsx",
    ],
    accept_multiple_files=False,
)

if not upload_files:
    st.write("Загрузите файл с данными")
    st.stop()

st.write(f"loaded file: {upload_files.name}")
st.write(" ")
data = pd.read_excel(upload_files.read())
selected_col = st.selectbox(
    "Выберите столбец",
    data.columns,
    index=None,
)
st.dataframe(
    data[selected_col if selected_col else data.columns], use_container_width=True
)

submit_button = st.button("Submit")

if submit_button:
    if not selected_col:
        st.error("Please select a column")
        st.stop()
    with st.spinner("Wait for it..."):
        time.sleep(5)
        st.dataframe(
            data[selected_col].apply(str.lower),
            use_container_width=True,
        )
