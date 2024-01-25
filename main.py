from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def show_form():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/greet", response_class=HTMLResponse)
async def greet(name: str = Form(...)):
    greeting = f"Hello, {name}!"
    return templates.TemplateResponse("greet.html", {"request": {}, "greeting": greeting})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
