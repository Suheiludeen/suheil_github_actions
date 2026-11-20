FROM python:3.11-slim

WORKDIR /testing

COPY main.py .
COPY requirements.txt . 

RUN pip install requirements.txt

CMD ["python", "main.py"]