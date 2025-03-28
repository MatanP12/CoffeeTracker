FROM python:3.10.12-alpine3.18

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

ENTRYPOINT [ "fastapi","run","src"]