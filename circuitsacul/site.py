from __future__ import annotations

import fastapi
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = fastapi.FastAPI()
templates = Jinja2Templates(directory="circuitsacul/website/pages")


@app.get("/")
async def home(request: fastapi.Request) -> HTMLResponse:
    return templates.TemplateResponse("site/home.jinja2", {"request": request})
