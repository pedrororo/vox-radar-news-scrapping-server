FROM python:3.8-bullseye
LABEL maintainer="SigaRP <admin@sigarp.com.br>"

ARG QUEUE_NAME
ENV queue_name=$QUEUE_NAME

WORKDIR /app
COPY ./ ./
RUN pip3 install -r requirements.txt
CMD python3 main.py -m queue -q ${queue_name}
