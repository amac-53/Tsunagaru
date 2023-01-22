# Web API

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import os

app = FastAPI()

# 文字列{"Hello World": "from FastAPI"}が出力される
@app.get("/api")
def root():
    return {"Hello World": "from FastAPI"}

# WordCloudの画像が作成される
@app.get("/api/getWordCloud")
def generate_WordCloud():
    os.system("bash ./wordclouds/run.sh")  # WordCloudの画像を作成
    os.system("cp ./results/ohisama.png ./share-with-web/ohisama.png")  # 作成した画像を共有ディレクトリへコピー
    os.system("rm -rf results/")  # 作成したファイルを全て削除
    return RedirectResponse(url="http://localhost:8080")

# WordCloudの画像が削除される
@app.get("/api/deleteWordCloud")
def delete_WordCloud():
    os.system("rm share-with-web/ohisama.png")  # WordCloudの画像を削除
    return RedirectResponse(url="http://localhost:8080")
