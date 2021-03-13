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

# 数据排序
# 分为两个模块，series和DataFrame排序
# Series排序
print(df['aqi'].sort_values())
print(df['aqi'].sort_values(ascending=False)) # 默认是升序排序，变为false后成为降序排序
print(df['tianqi'].sort_values())
# DataFrame排序
# 单列排序
df = df.sort_values(by='aqi') # 这里是复制了副本，需要传值覆盖原来的df
print(df)
df = df.sort_values(by='aqi', ascending=False) # 降序
print(df)
# 多列排序
df = df.sort_values(by = ['aqiLevel', 'bWendu']) # 多列排序时，按照优先级
print(df)
df = df.sort_values(by = ['aqiLevel', 'bWendu'], ascending=[False,False]) # 全部降序
print(df)
df = df.sort_values(by = ['aqiLevel', 'bWendu'], ascending=[True,False]) # 第一个升序，第一个值一样时，第二个降序
print(df)