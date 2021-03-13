import numpy as np
import pandas as pd

# 数据处理
df = pd.read_csv(r"./datas/beijing_tianqi/beijing_tianqi_2018.csv")
print(df.head(6))
print(df.index)
df.set_index('ymd', inplace=True) # 设置索引为日期，方便按日期筛选
print(df.index)
print(df.head(6))
# 去掉最高最低气温的摄氏度的标记
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32') #series有
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')
print(df.head(6))
print(df.dtypes)

# 数据查询
print(df.loc['2018-01-03', 'bWendu']) # 查询单个值
print(df.loc['2018-01-03', ['bWendu', 'yWendu']]) # 查询多个值，得到一个series
# 使用值列表进行批量查询
print(df.loc[['2018-01-03', '2018-01-04', '2018-01-04'], ['bWendu', 'yWendu']]) # 查询多个值，得到一个DataFrame
# 使用数值区间进行范围查询
print(df.loc['2018-01-03':'2018-01-06', 'bWendu']) # 根据行index区间查询，返回series
print(df.loc['2018-01-03', 'bWendu':'aqiLevel']) # 根据列index区间查询，返回series
print(df.loc['2018-01-03':'2018-01-06', 'bWendu':'aqiLevel']) # 根据行和列index区间查询，返回DataFrame
# 使用条件表达式进行查询，返回bool值
print(df.loc[df['yWendu'] < -10 , :]) # 选出一年中最低气温小于零下十度的天气情况
print(df.loc[(df['bWendu'] < 30) & (df['yWendu'] >=15) & (df['tianqi']=='晴')]) # 选出一年中最低气温小于零下十度的天气情况, &符号两边必须带括号，：可要可不要
# 调用函数查询
print(df.loc[lambda df: (df['bWendu'] < 30) & (df['yWendu'] >=15), :])
# 编写自定义函数进行查询
def query_my_data():
    return df.index.str.startswith('2018-09') & (df['aqiLevel']==1)
print(df.loc[query_my_data(), :])