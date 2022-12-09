# 단어를 벡터화 하기

import pandas as pd
from gensim.models import Word2Vec  # pip install gensim

review_word = pd.read_csv('./crawling_data/one_sentences.csv')
review_word.info()

one_sentence_reviews = list(review_word['reviews'])
cleaned_tokens = []
for sentence in one_sentence_reviews:
    token = sentence.split()    # split 띄어쓰기 기준으로 나누기
    cleaned_tokens.append(token)


# 형태소들의 리스트로 만들어서 줘야함  #vector_size=100 100차원으로 줄임(안줄이면 차원의 저주로 X)
# window=4 == conv 와 비슷한 역할(단어 4개씩 묶어줌)/ workers=8 cpu 몇개를 사용할지 확인
# sg 알고리즘: Skip-gram /
embedding_model = Word2Vec(cleaned_tokens, vector_size=100,
                           window=4, min_count=20,
                           workers=4, epochs=100, sg=1)
embedding_model.save('./models/word2vec_movie_review.model')
print(list(embedding_model.wv.index_to_key))
print(len(embedding_model.wv.index_to_key))


