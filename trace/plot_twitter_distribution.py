import pandas as pd
import matplotlib.pyplot as plt
import os

from matplotlib.ticker import FuncFormatter

# 定义文件路径的模板
file_path_template = 'twitter/cache-trace/samples/2020Mar/cluster{:03d}'

# 初始化存储结果的列表
mean_diffs = []
variance_diffs = []
total_counts = []
all_mappings = {}  # 用于存储每个cluster的编号映射

def thousands(x, pos):
    return '%1.0f' % (x * 1e-3)

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 40})


for i in range(31, 32):  # 从cluster001到cluster054
    # 构建文件路径
    file_path = file_path_template.format(i)

    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue

    # 读取CSV文件，跳过格式错误的行
    data = pd.read_csv(file_path, header=None, on_bad_lines='skip')

    # 将所有列转换为字符串类型
    data = data.astype(str)

    # 筛选包含“get”字段的行（注意是第七列，索引为6）
    data = data[data[5].str.contains('get', case=False, na=False)]

    # 如果筛选后没有数据，跳过该文件
    if data.empty:
        print(f"No 'get' requests found in: {file_path}")
        continue

    # 对第二列进行字典序编号
    data['sorted_index'] = data[1].rank(method='dense').astype(int)

    # 记录每个cluster的第一列和编号的对应关系
    id_to_index_mapping = {row[1]: row['sorted_index'] for idx, row in data.iterrows()}
    all_mappings[f"cluster{i:03d}"] = id_to_index_mapping

    # 计算相邻行编号的差值
    data['diff'] = data['sorted_index'].diff().dropna().astype(int).abs()

    # 计算均值、方差和总编号数
    mean_diff = data['diff'].mean()
    variance_diff = data['diff'].var()
    total_count = data['sorted_index'].nunique()

    # 存储结果
    mean_diffs.append(mean_diff)
    variance_diffs.append(variance_diff)
    total_counts.append(total_count)

    # 输出每个文件的结果
    print(f"Cluster {i:03d}:")
    print(f"Mean of differences: {mean_diff}")
    print(f"Variance of differences: {variance_diff}")
    print(f"Total unique indices: {total_count}")
    print(f"Total unique indices divided by 3: {total_count / 3}")
    print(f"Total unique indices squared divided by 18: {total_count * total_count / 18}")
    print()

    # 绘制差值的分布图
    plt.figure(figsize=(12, 8))
    plt.rcParams.update({'font.size': 35})
    plt.hist(data['diff'], bins=30, edgecolor='black')
    formatter = FuncFormatter(thousands)
    # plt.title('Distribution of Differences')
    plt.xlabel('Gap (× $10^3$)')
    plt.ylabel('Frequency (× $10^3$)')

    # 将横纵坐标都设置为以 *10^3 为单位显示
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'twitter_fig/cluster{i:03d}.pdf', facecolor='white', bbox_inches='tight')

# # 输出所有cluster的第一列和编号的对应关系，按编号排序
# print("\nID to Index Mapping for each Cluster:")
# for cluster, mapping in all_mappings.items():
#     print(f"{cluster}:")
#     sorted_mapping = sorted(mapping.items(), key=lambda x: x[1])
#     for id, index in sorted_mapping:
#         print(f"  {id}: {index}")

