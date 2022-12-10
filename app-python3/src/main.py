# Web API

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import os

app = FastAPI()

# 文字列{"Hello World": "from FastAPI"}が出力される
# http://localhost:8080/api
# or
# http://localhost:8001/api
@app.get("/api")
def root():
    return {"Hello World": "from FastAPI"}


# # 文字列{"item_id":"1","q":"aaa"}が出力される
# # http://localhost:8080/api/item/1?q=aaa
# # or
# # http://localhost:8001/api/item/1?q=aaa
# @app.get("/api/item/{item_id}")
# def read_item(item_id, q):
#     return {"item_id": item_id, "q": q}


# WordCloudの画像が作成される
# http://localhost:8080/api/getWordCloud
# or
# http://localhost:8001/api/getWordCloud
@app.get("/api/getWordCloud")
def generate_WordCloud():
    os.system("bash ./wordclouds/run.sh")  # WordCloudの画像を作成
    os.system("cp ./results/ohisama.png ./share-with-web/ohisama.png")  # 作成した画像を共有ディレクトリへコピー
    os.system("rm -rf results/")  # 作成したファイルを全て削除
    return RedirectResponse(url="http://localhost:8080")

# WordCloudの画像が削除される
# http://localhost:8080/api/deleteWordCloud
# or
# http://localhost:8001/api/deleteWordCloud
@app.get("/api/deleteWordCloud")
def delete_WordCloud():
    os.system("rm share-with-web/ohisama.png")  # WordCloudの画像を削除
    return RedirectResponse(url="http://localhost:8080")

