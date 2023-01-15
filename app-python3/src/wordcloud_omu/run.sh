#!/bash

# なければ，フォントファイルのダウンロード
if [ ! -f ./data/ipaexg.ttf ]; then
    cd data
    curl -O https://moji.or.jp/wp-content/ipafont/IPAexfont/ipaexg00401.zip
    unzip ipaexg00401.zip
    mv ipaexg00401/ipaexg.ttf ipaexg.ttf
    rm -rf ipaexg00401/
    rm ipaexg00401.zip
    cd ..
fi

# ワードクラウド画像（./results/wordcloud_omu.png）を生成
python wakachi_omu.py
python wordcloud_omu.py

# あれば，ワードクラウド画像を共有ディレクトリにコピー
if [ -f ./results/wordcloud_omu.png ]; then
    cp ./results/wordcloud_omu.png ../share-with-web/wordcloud_omu.png
fi
