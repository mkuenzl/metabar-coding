# syntax=docker/dockerfile:1
FROM ubuntu:focal
ADD bin/* /usr/bin/
RUN apt-get update && apt-get install -y python3.9 python3.9-dev

# docker build -t meta-test .
# docker run -it -d meta-test
# docker exec -it 969e2b4f1c60 /bin/bash