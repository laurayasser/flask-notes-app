FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*


COPY app/ ./app
COPY app/routes.py ./app/routes.py

EXPOSE 5000
USER 1000


CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

