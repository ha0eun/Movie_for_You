import pandas as pd
import glob

data_paths = glob.glob('./crawling_data2/*.csv')
df = pd.DataFrame()
for path in data_paths:
    df_temp = pd.read_csv(path)
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True) # 중복제거
    df = pd.concat([df, df_temp], ignore_index=True)
df.drop_duplicates(inplace=True)
df.info()
print(len(df.titles.value_counts()))
df.to_csv('./crawling_data/review_all.csv', index=False)
