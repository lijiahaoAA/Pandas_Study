import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 数据来源 4家公司近十天的股票数据
stocks = pd.read_excel('datas\stocks\互联网公司股票.xlsx')
print(stocks.shape)
print(stocks)
# series.map(dict)
map_dict = {'bidu':"百度",'baba':'阿里巴巴','iq':'爱奇艺','jd':'京东'}
stocks["中文名称"] = stocks['公司'].str.lower().map(map_dict)
print(stocks)
# series.map(function)
stocks["中文名称2"] = stocks['公司'].map(lambda x:map_dict[x.lower()])
print(stocks)

# apply用于series和DataFrame的转换
"""
    1.Series.apply(function),函数的参数是每个值
    2.DataFrame.apply(function),函数的参数是Series
"""
# series.apply
stocks["中文名称3"] = stocks['公司'].apply(lambda x:map_dict[x.lower()]) # 这个地方apply的作用等价于map
print(stocks)
# dataframe.apply
stocks["中文名称4"] = stocks.apply(lambda x:map_dict[x['公司'].lower()], axis=1) # 这个地方apply的作用等价于map
print(stocks)

# applymap用于datamap所有值的转换
sub_df = stocks[['收盘','开盘','高','低','交易量']]
print(sub_df)
sub_df = sub_df.applymap(lambda x:int(x))
print(sub_df)
stocks.loc[:,['收盘','开盘','高','低','交易量']] = sub_df.applymap(lambda x:int(x))
print(stocks)