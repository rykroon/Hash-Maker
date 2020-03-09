FROM python:3.7

WORKDIR /app
COPY dev dev
COPY src src

WORKDIR /app/dev
RUN pip install -r requirements.txt \
    && python nltk_download.py

WORKDIR /app/src