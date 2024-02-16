from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

app = FastAPI()

templates = Jinja2Templates(directory="templates")

dogs = [{"name": "Milos", "type": "Hot"}]


@app.get("/")
async def name(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request, "name": "Me", "dogs": dogs}
    )


@app.get("/index/", response_class=HTMLResponse)
async def request(request: Request, hx_request: Optional[str] = Header(None)):
    films = [
        {"name": "Blade Runner", "director": "Ridley Scott"},
        {"name": "Pulp Fiction", "director": "Quentin Tarantino"},
        {"name": "Blah", "director": "Haha Argarg"},
    ]
    context = {"request": request, "films": films}
    if hx_request:
        return templates.TemplateResponse("table.html", context)
    return templates.TemplateResponse("index.html", context)
