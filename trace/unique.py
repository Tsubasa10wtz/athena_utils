import pandas as pd

# 加载CSV文件
df = pd.read_csv('twitter/cache-trace/samples/2020Mar/cluster035', header=None, on_bad_lines='skip')  # 假设CSV文件没有列标题

# 筛选包含“get”字段的行（注意是第六列，索引为5）
df = df[df[5].str.contains('get', case=False, na=False)]

print(len(df))

# # 计算每项的大小为第三列和第四列的和，并将其添加为新列
# df['size'] = df[2] + df[3]

# 筛选出第二列中的所有不同项，并计算它们的大小之和
# unique_items_size_sum = df.drop_duplicates(subset=[1])['size'].sum()

# 打印所有不同项的大小之和
# print("所有不同项的大小之和为:")
# print(unique_items_size_sum)

# 获取第二列的数据，并计算不同项的总数
df = df[0:300000]
unique_count = df[1].nunique()

# 打印第一列中不同项的总数
print("第一列中不同项的总数为:")
print(unique_count)