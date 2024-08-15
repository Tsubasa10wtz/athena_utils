import pandas as pd

# 加载CSV文件
df = pd.read_csv('twitter/cache-trace/samples/2020Mar/cluster035', header=None)  # 假设CSV文件没有列标题

# 筛选包含“get”字段的行（注意是第七列，索引为6）
df = df[df[5].str.contains('get', case=False, na=False)]

# 获取第一列的数据，并计算不同项的总数
unique_count = df[1].nunique()

# 打印第一列中不同项的总数
print("第一列中不同项的总数为:")
print(unique_count)