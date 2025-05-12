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

mapped_data = mapped_data[5000:6000]


# 构造访问顺序横轴（访问的先后顺序）
x = np.arange(len(mapped_data))

# 转为 numpy 数组以便处理
mapped_data_array = np.array(mapped_data)

# 过滤掉未能映射成功（为 None 或 np.nan）的项
valid_indices = [i for i, v in enumerate(mapped_data_array) if v is not None and not pd.isna(v)]
x_valid = x[valid_indices]
y_valid = mapped_data_array[valid_indices].astype(int)

# 绘图
plt.figure(figsize=(8, 6))
plt.scatter(x_valid, y_valid, s=20)
plt.xlabel('Access Order')
plt.ylabel('Sample File Number')
plt.grid(True)
plt.tight_layout()
plt.show()