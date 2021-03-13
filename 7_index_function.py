"""
index的用途
    1.方便的数据查询
    2.使用index可以提升性能
    3.自动的数据对齐功能
    4.更多更强大的数据结构支持
        CategoricalIndex：分类数据的Index
        MultiIndex：多维索引，用于groupby多维聚合后结果
        DatetimeIndex：时间类型索引
"""

import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df = pd.read_csv(r'.\datas\ml-latest-small\ratings.csv')
print(df.head(6))
print(df.count())

# 使用index查询数据
df.set_index("userId", inplace=True, drop=False) # inplace=True说明直接修改源数据，不再进行副本复制。drop=False说明将索引列仍旧存放在DataFrame中
print(df.head(6))
print(df.index)
print(df.loc[500].head(5)) # 使用index索引查找，前提是自己设置索引 df.set_index()
print(df.loc[df["userId"] == 500].head()) # 使用column的condition查询

# 使用index会提升查询性能
"""
    1.如果index是唯一的，pandas会使用哈希表优化，查询性能为o(1)
    2.如果index是并不唯一的，但是有序，pandas会使用二分查找算法，查询性能为o(logN)
    3.如果index是完全随机的，每次查询都会扫描全表，查询性能为o(N)
"""
# 完全随机的顺序查询
from sklearn.utils import shuffle
df_shuffle = shuffle(df)
print(df_shuffle)
print(df_shuffle.index.is_unique) # 判断索引是否唯一
print(df_shuffle.index.is_monotonic_increasing) # 判断索引是否单调递增
# print(%timeit df_shuffle.loc[500]) # ipython完成

# 将index排序后的查询
df_sorted = df_shuffle.sort_index()
print(df_sorted)
print(df_shuffle.index.is_unique) # 判断索引是否唯一
print(df_shuffle.index.is_monotonic_increasing) # 判断索引是否单调递增

# index的数据自动对齐功能 只有具有相同的索引计算才会成功
s1 = pd.Series([1,2,3], index=list("abc"))
print(s1)
s2 = pd.Series([2,3,4], index=list("bcd"))
print(s2)
print(s1+s2)