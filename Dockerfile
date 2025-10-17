FROM python:3

WORKDIR /app

COPY src src
COPY requirements.txt .
COPY run.py .

RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python", "run.py"]
