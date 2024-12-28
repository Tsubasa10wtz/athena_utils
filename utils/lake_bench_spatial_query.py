import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


def generate_file_number_map(directory_path):
    # 获取目录中的所有文件（不包括子目录）并排除 .DS_Store
    files = [f for f in os.listdir(directory_path) if
             os.path.isfile(os.path.join(directory_path, f)) and f != '.DS_Store']

    # 对文件名进行字典序排序
    files.sort()

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


def plot_cdf(ids):
    # 统计每个block_id出现的次数
    id_counts = pd.Series(ids).value_counts()

    print(sum(id_counts))

    # 统计出现次数的分布，即每个count有多少个id
    frequency_counts = id_counts.value_counts().sort_index()

    # 计算CDF
    cdf = frequency_counts.cumsum() / frequency_counts.sum()

    # 打印一些统计信息（可选）
    print(cdf)

    # 设置绘图样式
    plt.style.use("fivethirtyeight")
    plt.rcParams['font.family'] = 'Arial Unicode MS'  # 确保支持中文字体

    # 绘制CDF
    plt.figure(figsize=(10, 6))
    plt.plot(cdf.index, cdf.values, marker='.', linestyle='-')
    plt.xlabel('Count')
    plt.ylabel('CDF')
    plt.grid(True)

    # 设置x轴主刻度为整数
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    plt.tight_layout()
    plt.show()


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

#
# # 打印映射后的数据和差值（可选）
# print("Mapped Data:", mapped_data)
# print("Differences:", differences)

# 现在绘制 CDF
plot_cdf(mapped_data)