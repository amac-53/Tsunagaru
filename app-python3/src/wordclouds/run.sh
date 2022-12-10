#!/bash

if [ ! -f results/ipaexg.ttf ]; then
    mkdir results
    cd results
    curl -O https://moji.or.jp/wp-content/ipafont/IPAexfont/ipaexg00401.zip
    unzip ipaexg00401.zip
    mv ipaexg00401/ipaexg.ttf ipaexg.ttf
    rm -rf ipaexg00401/
    rm ipaexg00401.zip
    cd ..
fi

if [ ! -f results/song_list.csv -o ! -f results/wakati_list.txt ]; then
    python ./wordclouds/scraping_uta_net.py
    python ./wordclouds/morphological_analysis.py
fi

python ./wordclouds/wordcloud_hinatazaka46.py
