import matplotlib.pyplot as plt
import numpy as np

# 数据数量和批次大小
data_size = 100

# 按顺序访问的索引
sequential_access = np.arange(data_size)

# 打乱后的访问索引
shuffled_access = np.random.permutation(data_size)

plt.style.use("bmh")
plt.rcParams.update({'font.size': 26})


# 绘制图形
# plt.figure(figsize=(10, 8)) # size for paper
plt.figure(figsize=(14, 8))
# 顺序访问
# plt.subplot(1, 3, 1)
plt.plot(np.arange(data_size), sequential_access, marker='o', linestyle='-')
plt.xlabel('Access Ordinal')
plt.ylabel('Data Index')
plt.savefig(f'inference_slide.pdf')


# 打乱后访问
# plt.subplot(1, 3, 2)
plt.figure(figsize=(14, 8))
plt.plot(np.arange(data_size), shuffled_access, marker='o', linestyle='-')
plt.xlabel('Access Ordinal')
plt.ylabel('Data Index')
plt.savefig(f'training_slide.pdf')



import pandas as pd

# 加载CSV文件
df = pd.read_csv('../trace/twitter/cache-trace/samples/2020Mar/cluster010', header=None)

# 筛选包含“get”字段的行（第六列，索引为5）
df = df[df[5].str.contains('get', case=False, na=False)]

# 选择前1000行
df = df.iloc[:100].reset_index(drop=True)

# 对前1000行的第二列（索引为1）进行字典序排序并编号
unique_values = sorted(df[1].unique())  # 获取第二列的唯一值并排序
value_to_index = {value: index for index, value in enumerate(unique_values)}  # 建立值到编号的映射

# 将第二列替换为对应的编号
df[1] = df[1].map(value_to_index)

# 绘制访问索引变化图
plt.figure(figsize=(14, 8))
plt.plot(df.index, df[1], marker='o', linestyle='-')
plt.xlabel('Access Ordinal')
plt.ylabel('Data Index')
plt.grid(True)
plt.savefig(f'cluster010_slide.pdf')


# 加载CSV文件
df = pd.read_csv('../trace/twitter/cache-trace/samples/2020Mar/cluster050', header=None)

# 筛选包含“get”字段的行（第六列，索引为5）
df = df[df[5].str.contains('get', case=False, na=False)]

# 选择前1000行
df = df.iloc[:100].reset_index(drop=True)

# 对前1000行的第二列（索引为1）进行字典序排序并编号
unique_values = sorted(df[1].unique())  # 获取第二列的唯一值并排序
value_to_index = {value: index for index, value in enumerate(unique_values)}  # 建立值到编号的映射

# 将第二列替换为对应的编号
df[1] = df[1].map(value_to_index)

# 绘制访问索引变化图
plt.figure(figsize=(14, 8))
plt.plot(df.index, df[1], marker='o', linestyle='-')
plt.xlabel('Access Ordinal')
plt.ylabel('Data Index')
plt.grid(True)
plt.savefig(f'cluster050_slide.pdf')
