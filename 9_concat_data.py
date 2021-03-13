import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

import warnings
warnings.filterwarnings('ignore')

# 使用pandas.concat合并数据
df1 = pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
})
print(df1)
df2 = pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
    'E':['E0','E1','E2','E3']
})
print(df2)
print(pd.concat([df1,df2])) # 默认的concat，参数为axis=0、join=outer、ignore_index=False
print(pd.concat([df1,df2], ignore_index=True)) # ignore_index=True忽略后面的索引，根据df1的索引往下排列
print(pd.concat([df1,df2], ignore_index=True, join='inner')) # 添加连接方式，只显示公共的部分

# 使用axis添加列
print(df1)
s = pd.Series(list(range(4)), name='E')
print(pd.concat([df1,s], axis=1)) # 这个地方的合并是复制副本在操作，并不是对源数据进行改动的
# 添加多列Series
s2 = df1.apply(lambda x:x['A']+"_GG", axis=1)
print(s2)
s2.name="G"
print(s2)
print(pd.concat([df1,s,s2],axis=1))

# 使用DataFrame.append按行合并数据
df1 = pd.DataFrame([[1,2],[3,4]], columns=list('AB'))
df2 = pd.DataFrame([[5,6],[7,8]], columns=list('AB'))
print(df1)
print(df2)
print(df1.append(df2))
print(df1.append(df2, ignore_index=True))
# append 按行添加数据
df = pd.DataFrame(columns=['A'])
print(df)
df = pd.concat(
    [pd.DataFrame([i], columns=['A']) for i in range(5)], #传入一个列表，避免多次复制
    ignore_index=True
)
print(df)
