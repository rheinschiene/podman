#!/usr/bin/bash

wget https://github.com/gohornet/hornet/blob/master/docker/Dockerfile
podman build -f gohornet.in -t gohornet:latest
rm Dockerfile
