FROM python:alpine

EXPOSE 5000

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY webhook.py .

CMD ["python", "webhook.py"]