FROM python:3.7

WORKDIR /app
COPY requirements.txt .
COPY app.py .

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0", "-w", "4", "app:app"]

