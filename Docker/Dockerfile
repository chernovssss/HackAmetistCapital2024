FROM python:3.11

RUN apt-get update && apt-get install libgl1  -y

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

EXPOSE 8080
