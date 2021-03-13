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
df.set_index('ymd', inplace=True) # 设置索引为日期，方便按日期筛选
print(df.index)
print(df.head(6))
# 去掉最高最低气温的摄氏度的标记
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32') #series有
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')
print(df.head(6))
print(df.dtypes)

# 增加数据列
# 直接增加
df.loc[:,"wencha"] = df['bWendu'] - df['yWendu'] # 返回series
print(df.head(6))
# df.apply方法，传入函数
def get_wendu_type(x):
    if x['bWendu'] > 33:
        return '高温'
    if x['yWendu'] < -10:
        return '低温'
    else:
        return '常温'
df.loc[:, 'wendu_type'] = df.apply(get_wendu_type, axis=1)
print(df.head(6))
print(df['wendu_type'].value_counts())
# df.assign方法
print("df.assign方法:")
df1 = df.assign(
    yWendu_huashi = lambda x : x['yWendu']*9/5+32,
    bWendu_huashi = lambda x : x['bWendu']*9/5+32
)
print(df1.head(6))

# 按条件选择分组分别赋值
df['wencha_type'] = ''
df.loc[df['bWendu'] - df['yWendu']>10 , 'wencha_type'] = '温差大'
df.loc[df['bWendu'] - df['yWendu']<=10 , 'wencha_type'] = '温差正常'
print(df.head(6))