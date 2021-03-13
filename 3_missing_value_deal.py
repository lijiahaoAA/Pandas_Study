import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

studf = pd.read_excel(r'./datas/student_excel/student_excel.xlsx', skiprows=2)
print(studf)
print(studf.isnull())
print(studf['分数'].isnull())
print(studf['分数'].notnull())

print(studf.loc[studf['分数'].notnull(), :]) # 选出分数不为空的所有行

# 删掉全是空值的列
studf.dropna(axis="columns", how="all", inplace=True)
print(studf)
# 删除掉全是空值的行
studf.dropna(axis="index", how="all", inplace=True)
print(studf)

# 填充
# 将分数列为空的值填充为0
studf['分数'].fillna(0, inplace=True)
print(studf)
# 将姓名的缺失值填充
studf.loc[:, "姓名"] = studf['姓名'].fillna(method='ffill') # ffill=forward fill 使用空值前面的值进行填充
print(studf)

# 保存到文件
studf.to_excel('E:\PythonProject\pandas_study\datas\student_excel\student_excel_clean.xlsx', index=False) # index=False 不保存默认的列索引
