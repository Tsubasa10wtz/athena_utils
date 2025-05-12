import ast
import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def generate_file_number_map(filename_list_path):
    # 获取目录中的所有文件（不包括子目录）并排除 .DS_Store
    with open(filename_list_path, "r", encoding="utf-8") as file:
        # 逐行读取文件内容并去掉换行符
        files = [line.strip() for line in file]

    # 对文件名进行字典序排序
    files.sort()

    # 创建一个字典来保存文件路径到编号的映射
    file_number_map = {}

    # 遍历排序后的文件列表并为每个文件分配编号
    for idx, file_name in enumerate(files, start=1):

        # 将文件路径映射到编号
        file_number_map[file_name] = idx

    return file_number_map


def extract_column_from_csv_with_pandas(csv_file, query_col, candidate_col):
    # 使用 pandas 读取 CSV 文件
    df = pd.read_csv(csv_file)

    # 初始化合并后的列表
    merged_list = []

    # 遍历每一行
    for _, row in df.iterrows():
        # 获取 query_table 数据
        query_table_item = row[query_col]

        # 将 candidate_table 列中的字符串转换为列表
        candidate_table_items = ast.literal_eval(row[candidate_col])

        # 将 query_table 和 candidate_table 列表中的所有项合并
        merged_list.append(query_table_item)  # 先添加 query_table_item
        merged_list.extend(candidate_table_items)  # 然后添加所有 candidate_table_items

    return merged_list


def map_column_data_to_numbers(column_data, file_number_map):
    # # 将列数据映射为编号
    # mapped_data = [file_number_map.get(item, None) for item in column_data]
    #
    # return mapped_data

    # 记录被映射为 None 的项及其索引
    none_items = []

    # 将列数据映射为编号
    mapped_data = []
    for idx, item in enumerate(column_data):
        mapped_value = file_number_map.get(item, None)
        if mapped_value is None:
            none_items.append((idx, item))  # 记录索引和原始值
        mapped_data.append(mapped_value)

    # 打印出所有被映射为 None 的项
    if none_items:
        print("Mapped to None:")
        for index, item in none_items:
            print(f"Index: {index}, Item: {item}")

    return mapped_data



def calculate_absolute_differences(mapped_data):
    # 计算相邻项之间的绝对差值
    differences = [abs(mapped_data[i] - mapped_data[i - 1]) for i in range(1, len(mapped_data))]

    return differences


# 设置目标目录路径
filename_list_path = "/Users/wangtianze/直博/项目/Athena/athena/lakebench/join/filename_list.txt"

# 生成文件路径到编号的映射
file_number_map = generate_file_number_map(filename_list_path)

# 示例 CSV 文件路径
csv_file_path = '/Users/wangtianze/直博/项目/Athena/athena/lakebench/join/opendata_join_result_grouped.csv'

# 提取指定列的数据
data = extract_column_from_csv_with_pandas(csv_file_path,  'query_table', 'candidate_table')


# 按编号映射列数据
mapped_data = map_column_data_to_numbers(data, file_number_map)

# 计算相邻项之间的绝对差值
differences = calculate_absolute_differences(mapped_data)

print("max difference:", max(differences))

# 打印映射后的数据和差值
# print("Mapped Data:", mapped_data)
# print("Differences:", differences)

diffs = differences

plt.rcParams['font.family'] = 'Arial Unicode MS'

fig, ax1 = plt.subplots(figsize=(12, 6))

# 绘制直方图（左轴）

bins = np.arange(0, 2828, 22)

ax1.hist(diffs, bins=bins, alpha=0.6, label='Count', color='#003a75')
ax1.set_xlabel('Gap', fontsize=44, color='black')
ax1.set_ylabel('Count', color='black', fontsize=44)
ax1.tick_params(axis='y', labelcolor='black')
ax1.tick_params(axis='x', labelsize=24, colors='black')
# ax1.yaxis.set_major_locator(ticker.MultipleLocator(1250))  # 每隔 1250 一格
ax1.set_ylim(0, 1500 * 11 * 1.1)  # 动态设置Y轴范围

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

plt.savefig('skewed_spatial_large.pdf', facecolor='white', bbox_inches='tight')

# 显示图表
plt.show()
