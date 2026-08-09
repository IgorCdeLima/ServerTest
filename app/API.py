from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def home():
    print("Diretório atual:", os.getcwd())
    print("Arquivos:", os.listdir())
    return FileResponse("index.html")
