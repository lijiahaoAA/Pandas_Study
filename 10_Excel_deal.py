# 将excel分为等分的几份，再把这些文件合并起来
work_dir = './course_datas/c15_excel_split_merge'
splits_dir = f"{work_dir}/splits"
import os
if not os.path.exists(splits_dir):
    os.mkdir(splits_dir)

# 读取excel文件到pandas
import pandas as pd

df_source = pd.read_excel(f"{work_dir}/crazyant_blog_articles_source.xlsx")
print(df_source.head(6))
print(df_source.index)
print(df_source.shape)
total_rowcount = df_source.shape[0]
print(total_rowcount)

# 将一个大的excel拆分成几个小的excel
"""
    1.使用df.iloc方法把一个大的DataFrame切分成几个小的DataFrame
    2.将小的DataFrame使用DataFrame.to_excel保存为excel文件
"""
# 计算拆分后的每个excel的行数
name = ['xiaoli','xiaowang','xiaolan','xiaolv']
split_size = total_rowcount//len(name)
if split_size % len(name) !=0:
    split_size +=1
print(split_size)
# 拆分成多个excel
df_subs = []
for idx, user in enumerate(name):
    begin = idx*split_size
    end = begin+split_size
    df_sub = df_source.iloc[begin:end]
    df_subs.append((idx,user,df_sub))
# 将每个小的DataFrame保存为excel
for idx, user, df_sub in df_subs:
    file_name = f"{splits_dir}/{idx}_{user}.xlsx"
    df_sub.to_excel(file_name, index=False)

# 合并excel到一个大的excel
"""
    1.遍历文件夹，获取要合并的excel文件名字列表
    2.分别读取到DataFrame，给每个df添加一列用于标记来源
    3.使用pd.concat进行df批量合并
    4.将合并后的DataFrame输出到excel
"""
# 遍历文件夹
import os
excel_names = []
for excel_name in os.listdir(splits_dir):
    excel_names.append(excel_name)
print(excel_names)
# 分别读取到DataFrame
df_list = []
for excel_name in excel_names:
    excel_name = f"{splits_dir}/{excel_name}" # 获取文件名字
    df_split = pd.read_excel(excel_name) # 读取文件为DataFrame
    user = excel_name.replace(".xlsx",'')[46:] # 获取文件名字的一部分
    df_split['username'] = user # DataFrame中添加一列负责人列
    df_list.append(df_split) # 4个df存入列表中
# 使用pd.concat进行合并
df_merge = pd.concat(df_list)
print(df_merge.head(6))
print(df_merge.shape)
print(df_merge["username"].value_counts())
# 输出到excel
df_merge.to_excel(f"{work_dir}/merge.xlsx", index=False)