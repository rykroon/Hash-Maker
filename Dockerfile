FROM python:3.7

WORKDIR /src
COPY requirements.txt .
COPY app.py .

RUN pip install -r requirements.txt
