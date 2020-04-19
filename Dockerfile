FROM alpine:latest

RUN apk add python3 py3-pip build-base python3-dev zlib-dev git libstdc++ && \
    python3 -m pip install umap-learn git+git://github.com/esnme/ultrajson.git && \
    apk del py3-pip build-base git
COPY src/app/ /app
COPY src/scripts/* /bin/
RUN /var/cache/apk/*
