import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 用户对电影的评分做归一化（0，1）
df_ratings = pd.read_csv(
    filepath_or_buffer=r".\datas\movielens-1m\ratings.dat",
    sep = "::",
    engine = 'python',
    names = "UserID::MovieID::Rating::Timestamp".split("::")
)
print(df_ratings.head())
print(df_ratings['UserID'].value_counts(ascending=True))

def ratings_norm(df):
    min_value = df['Rating'].min()
    max_value = df['Rating'].max()
    df["Rating_norm"] = df['Rating'].apply(lambda x:(x-min_value)/(max_value-min_value))
    return df
ratings = df_ratings.groupby('UserID').apply(ratings_norm)
print(ratings)

# 取出每个月温度最高的几天
df = pd.read_csv(r"./datas/beijing_tianqi/beijing_tianqi_2018.csv")
print(df.head(6))
# 去掉最高最低气温的摄氏度的标记
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32') #series有
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')
print(df.head(6))
# 增添一列月份
df['month'] = df['ymd'].str[:7]
print(df.head(6))

def getWenduTopN(df,topN):
    # df是按照月份分组之后的df
    return df.sort_values(by='bWendu')[['ymd','bWendu']][-topN:]
print(df.groupby('month').apply(getWenduTopN, topN=2))