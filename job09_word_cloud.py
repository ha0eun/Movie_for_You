# 모델 검증 - 자연어 처리할때 가장 유용함

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud     # pip install wordcloud
import collections
from matplotlib import font_manager, rc
from PIL import Image
import matplotlib as mpl

font_path ='./malgun.ttf'       # plt에서 한글 읽어보려고 씀
font_name = font_manager.FontProperties(fname=font_path).get_name()
mpl.rcParams['axes.unicode_minus']=False
rc('font', family=font_name )

df = pd.read_csv('./crawling_data/one_sentences.csv')
words = df[df['titles']=='온워드: 단 하루의 기적 (Onward)']['reviews']
print(words.iloc[0])
words = words.iloc[0].split()   # 형태소 단위로 잘라줌
print(words)

worddict = collections.Counter(words)   # 각각의 형태소가 몇번 나왔는지 딕셔너리 형태로 count/ 워드크라우드 적용
worddict = dict(worddict)
print(worddict)

wordcloud_img = WordCloud(background_color='white', max_words=2000,
                          font_path=font_path).generate_from_frequencies(worddict)
# max_words=2000 : 단어 2000개로 제한
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_img, interpolation='bilinear') # interpolation='bilinear' 블러 처리됨. 없어도 됨
plt.axis('off')


words = df[df['titles']=='그린치 (The Grinch)']['reviews']
words = words.iloc[0].split()   # 형태소 단위로 잘라줌
worddict = collections.Counter(words)   # 각각의 형태소가 몇번 나왔는지 딕셔너리 형태로 count/ 워드크라우드 적용
worddict = dict(worddict)
wordcloud_img = WordCloud(background_color='white', max_words=2000,
                          font_path=font_path).generate_from_frequencies(worddict)
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_img)
plt.axis('off')

plt.show()



