FROM python:3.7

WORKDIR /app
COPY requirements.txt .
COPY nltk_download.py .
RUN pip install -r requirements.txt
RUN python nltk_download.py

COPY src src
WORKDIR /app/src