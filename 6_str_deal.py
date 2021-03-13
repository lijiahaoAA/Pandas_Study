import numpy
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 数据处理
df = pd.read_csv(r"./datas/beijing_tianqi/beijing_tianqi_2018.csv")
print(df.head(6))
print(df.index)

# 去掉最高最低气温的摄氏度的标记
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32') #series有
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')
print(df.head(6))
print(df.dtypes)
print(df['fengli'].str.len())

# df = df['ymd'].str.replace('-','').str.slice[0:6]
# print(df.head(7))

# 使用正则表达式
def get_year_month_day(x):
    year,month,day = x['ymd'].split('-')
    return f"{year}年{month}月{day}日"
df['中文日期'] = df.apply(get_year_month_day, axis=1) # 一个一个值传进函数的，不是全部进去的
print(df)

# 链式replace方式
df['中文日期'].str.replace('年','').str.replace('月','').str.replace('日','')
# 正则表达式方式
df['中文日期'] = df['中文日期'].str.replace('[年月日]','')
print(df)
