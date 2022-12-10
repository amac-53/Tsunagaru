# 参考: https://zatsugaku-engineer.com/python/scraping/
# 参考: https://qiita.com/yuuuusuke1997/items/122ca7597c909e73aad5
# スクレイピングで曲名と歌詞テキストを抽出


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


list_df = pd.DataFrame(columns=['曲名', '歌詞'])

base_url = 'https://www.uta-net.com' # Uta-Net ホームページ
url = base_url + '/artist/22163/0/1/' # 日向坂46の歌詞一覧リストのページ
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
links = soup.find_all('td', class_='sp-w-100')
for link in links:
    origin_str = str(link)
    song_name = re.search(r'<span class="fw-bold songlist-title pb-1 pb-lg-0">.*?</span>', origin_str).group(0)
    song_name = re.search(r'<span class="fw-bold songlist-title pb-1 pb-lg-0">(.+)</span>', song_name).group(1)

    song_lyric = re.search(r'<span class="d-block d-lg-none utaidashi text-truncate">(.+)</span>', origin_str).group(1)
    song_lyric = song_lyric.replace('　','')
    song_lyric = song_lyric.replace(' ','')

    tmp_se = pd.DataFrame([[song_name], [song_lyric]], index=list_df.columns).T
    list_df = pd.concat([list_df, tmp_se])

list_df.to_csv('results/song_list.csv', index=False)
print("finish: scraping_uta_net.py")