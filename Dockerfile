FROM arm64v8/python:3.11-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Документируем, что приложение внутри слушает порт 5000
EXPOSE 5000 

CMD ["python3", "run.py"]

