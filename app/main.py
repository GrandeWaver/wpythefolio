from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="html")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/src/numbersjs", response_class=HTMLResponse)
async def numerkijs(request: Request):
    return templates.TemplateResponse("src/numbers.js", {"request": request})


@app.get("/numbers", response_class=HTMLResponse)
async def numerki(request: Request):
    return templates.TemplateResponse("numbers.html", {"request": request})
