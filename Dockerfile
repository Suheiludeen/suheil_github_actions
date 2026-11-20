FROM python:3.11-slim

WORKDIR /testing

COPY main.py .  

RUN pip install requirements.txt

CMD ["python", "main.py"]