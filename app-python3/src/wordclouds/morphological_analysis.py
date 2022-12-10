# 参考: https://qiita.com/yuuuusuke1997/items/122ca7597c909e73aad5
# 形態素解析

from janome.tokenizer import Tokenizer
import pandas as pd
import re

df_file = pd.read_csv('results/song_list.csv')
song_lyrics = df_file['歌詞'].tolist()

t = Tokenizer()

results = []

for s in song_lyrics:
    tokens = t.tokenize(s)

    r = []

    for tok in tokens:
        if tok.base_form == '*':
            word = tok.surface
        else:
            word = tok.base_form

        ps = tok.part_of_speech

        hinshi = ps.split(',')[0]

        if hinshi in ['名詞', '形容詞', '動詞', '副詞']:
            r.append(word)

    rl = (' '.join(r)).strip()
    results.append(rl)
    #余計な文字コードの置き換え
    result = [i.replace('\u3000','') for i in results]
    # print(result)

text_file = 'results/wakati_list.txt'
with open(text_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(result))

print("finish: morphological_analysis.py")