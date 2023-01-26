from wordcloud import WordCloud

text_file = open('./results/wakachi_omu_list.txt', encoding='utf-8')
text = text_file.read()

fpath = "./data/ipaexg.ttf"
stop_words = ['する', '的', '化', '研究']
wordcloud = WordCloud(background_color="white", font_path=fpath, width=1920, height=1080, stopwords=set(stop_words), random_state=1).generate(text)
wordcloud.to_file("results/wordcloud_omu.png")
