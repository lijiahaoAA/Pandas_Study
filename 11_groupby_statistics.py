# groupby:先对数据分组，在对每个分组应用聚合函数，转换函数
import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
    'B':['one','two','three','four','five','six','seven','eight'],
    'C':list(np.random.randn(8)),
    'D':list(np.random.randn(8))
})
print(df)

# 分组使用聚合函数做数据统计
# 单个列groupby
print(df.groupby('A').sum()) # A变为索引，根据A的类型，统计数字列的和
# 多个列的groupby
print(df.groupby(['A','B']).mean()) # 索引变为A和B，求平均值
print(df.groupby(['A','B'], as_index=False).mean()) # 不让A和B变成索引，求平均值
# 同时查看多种数据统计
print(df.groupby('A').agg([np.sum, np.mean, np.std])) # agg用于多种聚合
# 查看单列的数据统计结果
print(df.groupby('A')['C'].agg([np.sum, np.mean, np.std])) # 预过滤，只看c的统计信息
print(df.groupby('A').agg([np.sum, np.mean, np.std])['C']) # 性能比起上面的差
# 不同列使用不同的聚合函数
print(df.groupby('A').agg({'C':np.sum,'D':np.mean}))

# 遍历单个列聚合的分组
print("--------------------------------------------------------------------")
g = df.groupby('A')
print(type(g))
for name,group in g:
    print(name)
    print(group)
# 可以获取单个分组的数据
print(g.get_group('bar'))

# 遍历多个列聚合的分组
g = df.groupby(['A','B'])
for name,group in g:
    print(name) # 这里的name变为（A，B）组成的2个元素的tuple
    print(group)
# 可以获取单个分组的数据
print(g.get_group(('foo','one')))
# 获取单个列
for name, group in g['C']:
    print(name)
    print(group)
    print(type(group))


# 实例，分组探索天气数据
# 数据处理
df = pd.read_csv(r"./datas/beijing_tianqi/beijing_tianqi_2018.csv")
print(df.head(6))
# 去掉最高最低气温的摄氏度的标记
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32') #series有
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')
print(df.head(6))
# 增添一列月份
df['month'] = df['ymd'].str[:7]
print(df.head(6))
# 查看每个月的最高气温、
data = df.groupby('month')['bWendu'].max()
print(data)
# 查看每个月的最高温度，最低温度，平均空气质量指数
df.head(6)
group_data = df.groupby('month').agg({'bWendu':np.max, 'yWendu':np.min, 'aqi':np.mean})
print(group_data)