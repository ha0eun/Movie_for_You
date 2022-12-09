import pandas as pd

df = pd.read_csv('./crawling_data/cleaned_reviews_2016_2022.csv')
df.dropna(inplace=True)     # 빈문자열만 있을 경우 전처리할때 난값으로 남아서
df.info()

one_sentences = []
for title in df['titles'].unique(): # unique 함수로 열면 한번(중복X)만 불러들임
    temp = df[df['titles']==title]
    if len(temp) > 30:  # 제목 길이가 30개까지만 필요할때
        temp = temp.iloc[:30, :]
    one_sentence = ' '.join(temp['clean_reviews'])  # ' '띄어쓰기해서 join으로 이어 붙이기
    one_sentences.append(one_sentence)

df_one = pd.DataFrame({'titles':df['titles'].unique(), 'reviews':one_sentences})
print(df_one.head())
df_one.to_csv('./crawling_data/one_sentences.csv', index=False)