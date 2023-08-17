FROM python:33.10-slim

ADD ./requirements.txt .
RUN pip3 install -r requirements.txt
RUN mkdir ./src
ADD ./src /src

WORKDIR src
USER user
