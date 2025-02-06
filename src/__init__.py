from .routers import router
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import logging

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    handlers=[
        logging.FileHandler("logs/app.log"),  # General application logs
        logging.StreamHandler()  # Output to console
    ]
)



app = FastAPI()

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
async def read_html():
    html_path = Path("src/static/index.html")
    logging.info("Serving the main HTML page.")
    return html_path.read_text(encoding="utf-8")