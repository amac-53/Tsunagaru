# nginx-html-css-js-python
プロトタイプを作ってみました．
web側とdockerの技術的な関係に対する理解の助けになれば幸いです．
（個人的に，HTML，CSS，JavaScriptを触ってみたかった．）

## 要約
pythonで作成した画像をnginx（html，css，javascript）環境で表示する．

## 目的
- HTML，CSS，JavaScriptでWebページ（Webアプリ？）を作成する
- pythonでワードクラウド等の画像を作成して，HTMLに埋め込みたい
- できればWebサイト上で何かボタンを押すと，バックエンドでpythonが自動的に画像を作成して，それをHTMLが拾える良い（pythonコンテナは触らない）
- 上記の環境をdockerのみで構築する（ホストの環境を汚さない）


## 留意点
- HTML，CSS，JavaScriptの知識が皆無なので，非常に雑になっています
- jQuery試せてません，すみません...
- pythonのソースコードも雑で，とりあえず動きましたというレベルです
- ダメな部分ばかりだと思うので，些細な点でも話合い改善していきたいです

---
## とりあえず動かす

> 動かす前の注意点です．
> Webサイトをlocalhostの8080番ポートからアクセスします．もし，8080番ポートが不都合であれば，
> - ``docker-compose.yaml``の``8080:80``
> - ``app-python3/src/main.py``の``http://localhost:8080``
> 
> の全ての``8080``を変更してください．


まずは，nginxとpythonのコンテナを起動します．docker imageのダウンロードと作成，パッケージやpipモジュールのインストール等があるため，時間がかかります．
```sh
$ docker-compose up -d --build
```

無事にコンテナが2個作成されると，Webサイトにアクセスすることができます．
chrome等のブラウザのアドレスバーにて，
```sh
localhost:8080
```
あるいは，
```sh
http://localhost:8080
```
と入力してみてください．もし，Webサイトにアクセスできない場合は，Discord（か大学のメールなど）で教えてください．

そして，Webサイトの1番下までいくと，``word_cloud_image``と文字だけあり，画像が表示されてないところがあります．
``click and generate!``ボタンを押すと，画像が表示されます（内部でpythonによるスクレイピング・形態素解析・wordcloud作成の3ステップを踏んでいるため，時間がかかります）．

> 実際に，共有ディレクトリである``share``を見てみると``ohisama.png``が生成されています．ただし，同じ共有ディレクトリである``share-with-web``と``share-with-python``については，各々のコンテナに入ると画像があることを確認できると思います．

最後に，``click and delete!!!``ボタンを押すと先ほど作成された画像が削除されます．
> 画像の作成と削除は何回も繰り返すことができます．最後に画像を削除してから次のステップへ進むと，ホストを完全にクリーンな状態に戻すことができます．

終わりに，以下のコマンドを打つと，コンテナが削除されて環境が元に戻ります．
```sh
$ docker-compose down
```
以上です．

---

# 詳細
以下に，簡単な詳細を記述していきます．気になった部分だけ見ていただけたらと思います．

## 環境（アーキテクチャ）
<div align="center">
<img src="./images/archi.png" width="90%" >
</div>

### ディレクトリ構成

```
.
├── README.md
├── app-python3/     ← pythonコンテナ用（Dockerfileから作成したimageを使用）
│   ├── Dockerfile     ← image作成用
│   ├── requirements.txt     ← pip用
│   └── src/
│       ├── main.py     ← FastAPI
│       ├── share-with-web/     ← 共有ディレクトリ
│       └── wordclouds/     ← バックエンド処理
│           ├── morphological_analysis.py
│           ├── run.sh
│           ├── scraping_uta_net.py
│           └── wordcloud_hinatazaka46.py
├── docker-compose.yml     ← pythonとwebサーバの2個のコンテナを作成
├── images     ← README.md用の素材
│   ├── archi.drawio
│   └── archi.png
├── share/     ← 共有ディレクトリ
└── web-nginx/     ← webサーバのコンテナ用（nginx:latestのimageを使用）
    ├── conf.d/
    │   ├── default.conf
    │   └── nginx.conf
    └── contents/     ← HTML，CSS，JavaScriptによるWebページ
        ├── bar.html
        ├── baz.html
        ├── foo.html
        ├── img/
        │   └── affogato.jpg
        ├── index.html
        ├── index.js
        ├── share-with-python/     ← 共有ディレクトリ
        └── style.css
```

### docker-compose（特に共有ディレクトリとコーディングするファイルについて）
##### 全体
- ホスト上の``./share/``，pythonコンテナ上の``/opt/share-with-web/``，nginxサーバ上の``/usr/share/nginx/html/share-with-python/``の中身全ては共有されるため，ここに渡したい画像データを保管する予定
##### app-python3-svc
- ローカルホストの8001番ポートにアクセスすると，pythonコンテナの8080番ポートに繋がる
- ホスト上の``./app-python3/src/``と，コンテナ上の``/opt/``は共有されるため，ここで**コーディング**したいファイル``.py``などを保管する予定
##### web-nginx-svc
- ローカルホストの8080番ポートにアクセスすると，pythonコンテナの80番ポートに繋がる
- ホスト上の``./web-nginx/contents/``と，コンテナ上の``/usr/share/nginx/html/``は共有されるため，ここで**コーディング**したいファイル``.html``, ``.css``, ``.js``などを保管する予定



### app-python3/（pythonコンテナ）
- wordcloudを使用するために，python v3.9を使用している（最新版はv3.11）
- pipでインストールしたいものは，``requirements.txt``に追記する
- ``main.py``において，FastAPIを使用することで，URLをクリックするだけで，pythonによる処理を行なってくれるようにしている
- ``wordclouds/``では，スクレイピング・形態素解析・ワークドラウド作成の3ステップのソースコード``.py``があり，それを一気に処理してくれるシェルスクリプト``run.sh``がある．なお，wordcloudで日本語を出力するために必要なfont用のファイル``.ttf``のダウンロードも``run.sh``が行っている．
- 作成されたWordCloud画像は共有ディレクトリ``share-with-web/``にコピーされる

### web-nginx/（nginxコンテナ）
- ``conf.d/``では，「nginxコンテナ→pythonコンテナ」の転送設定などを行っている．もうあまり弄りたくない...
- ``contents/``にて，HTML，CSS，JavaScriptを編集する
- 一応，``img/``が元から用意した画像などを格納する場所，``share-with-python/``がpythonによる成果物を格納する場所として用意したが，どうなるかは今後次第...