
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="LoveInvite")

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LoveInvite 💗</title>
    </head>
    <body>
        <h1>LoveInvite 💗</h1>
        <p>Особенное приглашение для особенного человека.</p>
        <p>Скоро здесь появятся фотографии, вопросы и интерактивные сюрпризы!</p>
    </body>
    </html>
    """

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
