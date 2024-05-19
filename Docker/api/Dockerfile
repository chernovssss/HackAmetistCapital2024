FROM python:3.11.1-slim

WORKDIR ../../api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN ls
COPY ./api/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements_api.txt

COPY . .

EXPOSE 8080
