FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 build-essential python3-pip python3-dev && \
    python3 -m pip install umap-learn ujson && \
    apt-get remove -y python3-pip build-essential git
COPY src/app/ /app
RUN rm -rf /var/lib/apt/lists/*
