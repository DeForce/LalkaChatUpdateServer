#!/usr/bin/env bash
docker build -t lalkaserver .

docker create \
    --name lalkaserver \
    -p 8080:8080 \
    -v /opt/lalkaserver/releases:/releases \
    lalkaserver