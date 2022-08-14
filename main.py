from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    root_html = open("./static/index.html", "r").read()
    return root_html


@app.get("/Signup.html", response_class=HTMLResponse)
async def root():
    signup_html = open("./static/Signup.html", "r").read()
    return signup_html


from api import *

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
