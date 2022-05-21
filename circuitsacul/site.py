from __future__ import annotations

import fastapi
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = fastapi.FastAPI()
static = StaticFiles(directory="circuitsacul/website/static")
app.mount("/static", static, name="static")
templates = Jinja2Templates(directory="circuitsacul/website/pages")


@app.get("/")
async def home(request: fastapi.Request) -> HTMLResponse:
    return templates.TemplateResponse("site/home.jinja2", {"request": request})
