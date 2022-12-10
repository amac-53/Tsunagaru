# 参考: https://qiita.com/yuuuusuke1997/items/122ca7597c909e73aad5
# ワードクラウド画像を作成

from wordcloud import WordCloud

text_file = open('results/wakati_list.txt', encoding='utf-8')
text = text_file.read()

fpath = "results/ipaexg.ttf"
stop_words = ['そう', 'ない', 'いる', 'する', 'まま', 'よう', 'てる', 'なる', 'こと', 'もう', 'いい', 'ある', 'ゆく', 'れる', 'の', 'ん', 'しまう', 'くれる']
wordcloud = WordCloud(background_color="white", font_path=fpath, width = 800, height=600, stopwords=set(stop_words), random_state=1).generate(text)
wordcloud.to_file("results/ohisama.png")

print("finish: wordcloud_hinatazaka46.py")