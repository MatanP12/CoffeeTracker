FROM python:3.12.8-alpine3.21

WORKDIR /app
COPY reqirements.txt .
RUN pip install --no-cache-dir -r reqirements.txt

COPY src ./src

ENTRYPOINT [ "fastapi","run","src"]
