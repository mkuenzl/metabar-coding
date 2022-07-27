# syntax=docker/dockerfile:1
FROM ubuntu:focal
ADD bin/* /usr/bin/
ADD FastQC /usr/FastQC
ADD example /usr/example
ADD pipeline /usr/pipeline
RUN apt-get update && apt-get install -y python3.9 python3.9-dev
RUN apt-get install -y perl
RUN apt-get install -y openjdk-11-jdk xvfb
RUN chmod 755 /usr/FastQC/fastqc
RUN ln -s /usr/FastQC/fastqc /usr/bin/fastqc


# docker build -t meta-test .
# docker run -it -d meta-test
# docker exec -it container-id /bin/bash
# docker save meta-test > meta-test.tar