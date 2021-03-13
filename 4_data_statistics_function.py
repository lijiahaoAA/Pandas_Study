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

# 汇总类统计
# 汇总数字类型的列
print("---------------------------------------------------------------------")
print(df.describe()) # 用来统计整数列的数据，包括个数，方差，标准差，最小和最大值
# 汇总非数字类型的 唯一去重和按值计数
# 唯一去重 就是去除重复值,看每一列中的元素有什么
print("------------------------唯一去重------------------------")
print(df["fengxiang"].unique())
print(df["tianqi"].unique())
print(df["fengli"].unique())
# 按值计数
print("------------------------按值计数------------------------")
print(df["fengxiang"].value_counts())
print(df["tianqi"].value_counts())
print(df["fengli"].value_counts())

# 相关系数和协方差, 针对整数列
"""
    对于两个变量X、Y，
    协方差：衡量同向反向程度，如果过协方差为正，则说明XY同向变化，协方差越高说明同向程度越高。反之，负-反向变化-低
    相关系数：衡量相似度程度，区间在1到-1，如果为1时，说明两个变量变化时的正向相似度最大。相关系数矩阵可以联想到混淆矩阵
"""
print(df.cov()) # 协方差矩阵
print(df.corr()) # 相关系数矩阵
print(df['aqi'].corr(df['yWendu'])) # 空气质量和最高气温的相关关系，查看这两个元素之间相关关系
print(df['aqi'].corr(df['bWendu']-df['yWendu'])) # 空气质量和温差的相关关系
