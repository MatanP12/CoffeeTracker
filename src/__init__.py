from .routers import router
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import logging
from pythonjsonlogger.json import JsonFormatter

json_formater = JsonFormatter('%(levelname)s : %(name)s : %(message)s : %(asctime)s', datefmt="%d-%m-%Y %H:%M:%S")

file_handler = logging.FileHandler("logs/app.log")
stream_handler = logging.StreamHandler()
file_handler.setFormatter(json_formater)
stream_handler.setFormatter(json_formater)

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    handlers=[
        file_handler,
        stream_handler
    ]
)

app = FastAPI()

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
async def read_html():
    html_path = Path("src/static/index.html")
    logging.info("Serving the main HTML page.")
    return html_path.read_text(encoding="utf-8")