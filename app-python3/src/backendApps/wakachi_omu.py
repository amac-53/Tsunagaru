from janome.tokenizer import Tokenizer
import json

f_json = open("./data/professors_info_all.json", 'r')
data = json.load(f_json)

t = Tokenizer()
results = []

for name in data:
    keywords = "".join(data[name]["研究内容"])
    topics = "".join(data[name]["研究課題"]) if data[name]["職名"] == "教授" else ""
    s = keywords+topics

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

text_file = 'results/wakachi_omu_list.txt'
with open(text_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(result))
