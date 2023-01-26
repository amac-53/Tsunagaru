# Web API

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import os

app = FastAPI()

@app.get("/api")
def root():
    return {"Hello World": "from FastAPI"}

# Create WordCloud image
@app.get("/api/getWordCloud")
def generate_WordCloud():
    os.system("bash ./backendApps/run.sh")
    return RedirectResponse(url="http://localhost:8080/backendApps.html")

# Delete WordCloud image
@app.get("/api/deleteWordCloud")
def delete_WordCloud():
    os.system("rm share-with-web/wordcloud_omu.png")
    return RedirectResponse(url="http://localhost:8080/backendApps.html")
