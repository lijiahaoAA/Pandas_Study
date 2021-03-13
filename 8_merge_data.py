# pandas的merge相当于sql的join
# 数据集 电影评分数据集 用户信息，电影信息，评分信息
import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df_ratings = pd.read_csv(
    filepath_or_buffer=r".\datas\movielens-1m\ratings.dat",
    sep = "::",
    engine = 'python',
    names = "UserID::MovieID::Rating::Timestamp".split("::")
)
print(df_ratings.head())
df_users = pd.read_csv(
    filepath_or_buffer=r".\datas\movielens-1m\users.dat",
    sep = "::",
    engine = 'python',
    names = "UserID::Gender::Age::Occupation::Zip-code".split("::")
)
print(df_users.head())
df_movies = pd.read_csv(
    filepath_or_buffer=r".\datas\movielens-1m\movies.dat",
    sep = "::",
    engine = 'python',
    names = "MovieID::Title::Genres".split("::")
)
print(df_movies.head())

df_ratings_users = pd.merge(
    df_ratings,df_users, left_on="UserID", right_on="UserID", how="inner"
)
print(df_ratings_users)
df_ratings_users_movies = pd.merge(
    df_ratings_users,df_movies, left_on="MovieID", right_on="MovieID", how="inner"
)
print(df_ratings_users_movies)

# 理解merge时数量的对齐关系
"""
    1.one-to-one:(学号，姓名)对(学号，年龄)-》(姓名，年龄)
    2.one-to-many:(学号，姓名)对(学号，【语文，数学，英语】)-》(姓名，【语文，数学，英语】)
    3.many-to-many:(学号，【语文，数学，英语】)对(学号，【篮球，足球，乒乓球】)-》([语文，数学，英语]，[篮球，足球，【乒乓球])
"""
# one-to-one的关系
left = pd.DataFrame({'sno':[11,12,13,14], 'age':[21,22,23,24]})
print(left)
right = pd.DataFrame({'sno':[11,12,13,14], 'name':['a','s','d','f']})
print(right)
left_right = pd.merge(left,right,left_on='sno',right_on='sno',how='inner')
print(left_right)

# one-to-many的关系
left = pd.DataFrame({'sno':[11,12,13,14], 'name':['aa','ss','dd','ff']})
print(left)
right = pd.DataFrame({'sno':[11,11,11,12,12,13], 'grade':['语文11','数学90','英语78','语文55','数学99','英语100']})
print(right)
left_right = pd.merge(left,right,on='sno') # 以列数多的为基准
print(left_right)

# many-to-many的关系
left = pd.DataFrame({'sno':[11,11,12,12,12], 'hobby':['篮球','羽毛球','乒乓球','篮球','足球']})
print(left)
right = pd.DataFrame({'sno':[11,11,11,12,12,13], 'grade':['语文11','数学90','英语78','语文55','数学99','英语100']})
print(right)
left_right = pd.merge(left , right , on='sno')
print(left_right)