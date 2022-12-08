# 단어를 벡터화 하기

import pandas as pd
from gensim.models import Word2Vec  # pip install gensim

review_word = pd.read_csv('./crawling_data/one_sentences.csv')
review_word.info()

one_sentence_reviews = list(review_word['reviews'])
cleaned_tokens = []
for sentence in one_sentence_reviews:
    token = sentence.split()
    cleaned_tokens.append(token)

# 형태소들의 리스트로 만들어서 줘야함  #vector_size=100 100차원으로 줄임/ window=4 == conv 와 비슷한 역할(단어 4개씩 묶어줌)/ workers=8 cpu 몇개를 사용할지 확인
# sg 알고리즘(벡터화 알고리즘?)
embedding_model = Word2Vec(cleaned_tokens, vector_size=100,
                           window=4, min_count=20,
                           workers=4, epochs=100, sg=1)
