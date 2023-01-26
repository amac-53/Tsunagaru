from wordcloud import WordCloud
import json

text_file = open('./results/wakachi_labos.json', encoding='utf-8')
d = json.load(text_file)

fpath = "./data/ipaexg.ttf"  # フォント
stop_words = ['する', '的', '化', '研究']

# # 研究室ごと
# for k, v in d.items():
#     text = v
#     wordcloud = WordCloud(background_color="white", font_path=fpath, width=1920, height=1080, stopwords=set(stop_words), random_state=1).generate(text)
#     wordcloud.to_file("results/wordcloud_" + k + ".png")

# 全体
text = ''
for k, v in d.items():
    text = text + ' ' + v
wordcloud = WordCloud(background_color="white", font_path=fpath, width=1920, height=1080, stopwords=set(stop_words), random_state=1).generate(text)
wordcloud.to_file("results/wordcloud_all.png")