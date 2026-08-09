from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def init():
    return FileResponse("index.html")
