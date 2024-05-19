FROM python:3.11.1-slim

WORKDIR ../../streamlit_app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY ./streamlit/requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements_streamlit.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
