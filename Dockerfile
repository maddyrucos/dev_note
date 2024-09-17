FROM ubuntu:22.04

WORKDIR /var/www/dev_note

COPY . .

RUN apt-get update && apt-get -y install python3.11 python3-pip

RUN pip install -r requirements.txt
