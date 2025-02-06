from .routers import router
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
async def read_html():
    html_path = Path("src/static/index.html")
    return html_path.read_text(encoding="utf-8")