import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def generate_file_number_map(directory_path):
    # 获取目录中的所有文件（不包括子目录）并排除 .DS_Store
    files = [f for f in os.listdir(directory_path) if
             os.path.isfile(os.path.join(directory_path, f)) and f != '.DS_Store']

    # 对文件名进行字典序排序
    files.sort()

    # print(len(files))

    # 创建一个字典来保存文件路径到编号的映射
    file_number_map = {}

    # 遍历排序后的文件列表并为每个文件分配编号
    for idx, file_name in enumerate(files, start=1):
        # 获取文件的完整路径
        file_path = os.path.join(directory_path, file_name)

        # 去除路径前缀（假设你不需要 '/Users/wangtianze/Downloads/tables/' 前缀）
        relative_path = file_path.replace(directory_path, "").lstrip(os.sep)

        # 将文件路径映射到编号
        file_number_map[relative_path] = idx

    return file_number_map


def extract_column_from_csv_with_pandas(csv_file, column_name):
    # 使用 pandas 读取 CSV 文件
    df = pd.read_csv(csv_file)

    # 提取指定列的数据
    column_data = df[column_name]

    return column_data


def map_column_data_to_numbers(column_data, file_number_map):
    # 将列数据映射为编号
    mapped_data = [file_number_map.get(item, None) for item in column_data]

    return mapped_data


def calculate_absolute_differences(mapped_data):
    # 计算相邻项之间的绝对差值
    differences = [abs(mapped_data[i] - mapped_data[i - 1]) for i in range(1, len(mapped_data))]

    return differences


# 设置目标目录路径
directory_path = "/Users/wangtianze/Downloads/tables"

# 生成文件路径到编号的映射
file_number_map = generate_file_number_map(directory_path)

# 示例 CSV 文件路径
csv_file_path = '/Users/wangtianze/Downloads/opendata_join_query.csv'
column_name = 'query_table'

# 提取指定列的数据
column_data = extract_column_from_csv_with_pandas(csv_file_path, column_name)

# 按编号映射列数据
mapped_data = map_column_data_to_numbers(column_data, file_number_map)

# 计算相邻项之间的绝对差值
differences = calculate_absolute_differences(mapped_data)


# 打印映射后的数据和差值
# print("Mapped Data:", mapped_data)
# print("Differences:", differences)

diffs = differences

fig, ax1 = plt.subplots(figsize=(14, 6))

# 绘制直方图（左轴）

bins = np.arange(0, 500, 3)

ax1.hist(diffs, bins=bins, alpha=0.6, label='Count', color='#003a75')
ax1.set_xlabel('Gap', fontsize=44, color='black')
ax1.set_ylabel('Count', color='black', fontsize=44)
ax1.tick_params(axis='y', labelcolor='black')
ax1.tick_params(axis='x', labelsize=24, colors='black')
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(1250))  # 每隔 1250 一格
ax1.set_ylim(0, 2000 * 1.1)  # 动态设置Y轴范围

# 删除右轴和CDF线条部分
# 删除创建右侧 Y 轴
# ax2 = ax1.twinx()

# 删除 CDF 绘制
# cdf_plot, = ax2.plot(sorted_diffs, cdf, label='CDF', linestyle='-', alpha=0.8, color='#9f0000')
# ax2.set_ylabel('CDF', color='black', fontsize=36)
# ax2.set_ylim(0, 1.1)  # CDF 固定范围

# 合并图例
handles1, labels1 = ax1.get_legend_handles_labels()
# handles2, labels2 = ax2.get_legend_handles_labels()
# handles = handles1 + [cdf_plot]  # 添加 CDF 的线条句柄
# labels = labels1 + ['CDF']      # 添加 CDF 的标签
plt.legend(handles1, labels1, loc='upper right', fontsize=28)

# 修改 X 轴刻度字体
ax1.tick_params(axis='x', labelsize=30)  # 设置 X 轴刻度字体大小为 16
# 修改左 Y 轴刻度字体
ax1.tick_params(axis='y', labelsize=30)  # 设置左 Y 轴刻度字体大小为 16

# 添加网格和样式
ax1.grid(alpha=0.4)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()