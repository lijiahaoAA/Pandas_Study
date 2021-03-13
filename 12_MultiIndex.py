"""
    1.分层索引：在一个轴上拥有多个索引层级，可以表达更高维度数据的形式
    2.可以更方便的进行数据筛选，如果有序性能更好
"""
import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 数据来源 4家公司近十天的股票数据
stocks = pd.read_excel('datas\stocks\互联网公司股票.xlsx')
print(stocks.shape)
print(stocks.head(6))
print(stocks['公司'].unique())
print(stocks.index)
print(stocks.groupby('公司')['收盘'].mean())

# Series的分层索引
ser = stocks.groupby(['公司','日期'])['收盘'].mean()
print(ser)
print(ser.index)
print(ser.unstack()) # unstack用于降级索引，将之后的日期索引变为column
print(ser.reset_index()) # 之前设置的索引无效

# Series有多层索引如何筛选数据
print(ser)
print(ser.loc['BIDU'])
print(ser.loc[('BIDU','2019-10-02')]) # 多级索引使用元组
print(ser.loc[:,'2019-10-02']) # 根据日期索引选取所有数据

# DataFrame的多层索引MulitIndex
print(stocks.head(6))
stocks.set_index(['公司','日期'], inplace=True)
print(stocks)
print(stocks.index)
stocks.sort_index(inplace=True)
print(stocks)

# DataFrame有多层索引MultiIndex如何筛选数据
"""
    1.元组（key1，key2）代表筛选多层索引，key1是索引第一级，key2是索引第二级，key1和key2不同的column
    2.列表[key1，key2]表示同一层的多个key，同一个column的不同key
"""
print(stocks.loc['BIDU'])
print(stocks.loc[('BIDU','2019-10-02'),:])
print(stocks.loc[['BIDU','JD'],'开盘'])
print(stocks.loc[(['BIDU','JD'],'2019-10-02'),:])
print(stocks.loc[(slice(None),'2019-10-02'),:]) # slice(None)代表筛选这一索引的所有内容
