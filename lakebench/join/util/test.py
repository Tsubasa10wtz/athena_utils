from collections import defaultdict

import numpy as np
import pandas as pd

def triangular_cdf(x, c):
    """三角分布的CDF函数"""
    # return np.where(x < 0, 0, np.where(x > c, 1, ((2 * x * c - x ** 2) / c ** 2)))
    return np.where(x < 0, 0, np.where(x >= c-1, 1, (2 * x / (c - 1) - x * (x + 1)/ (c * (c-1)))))

def step_cdf(x, c):
    """简单阶跃函数的CDF"""
    return np.where(x < 0, 0, np.where(x < c, 0, 1))


def calculate_diff_mean_and_variance(numbers):
    # 计算后一项减前一项的差
    diff_list = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]

    # 计算均值和方差
    mean_diff = np.mean(diff_list)
    var_diff = np.var(diff_list)

    return diff_list

def generate_file_number_map(filename_list_path):
    # 获取目录中的所有文件（不包括子目录）并排除 .DS_Store
    with open(filename_list_path, "r", encoding="utf-8") as file:
        # 逐行读取文件内容并去掉换行符
        files = [line.strip() for line in file]

    print(len(files))

    # 对文件名进行字典序排序
    files.sort()

    # 创建一个字典来保存文件路径到编号的映射
    file_number_map = {}

    # 遍历排序后的文件列表并为每个文件分配编号
    for idx, file_name in enumerate(files, start=1):

        # 将文件路径映射到编号
        file_number_map[file_name] = idx

    return file_number_map

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

def longest_unique_subsequence(seq):
    seen = {}
    max_len = 0
    start = 0
    max_start = 0
    max_end = 0

    for i, item in enumerate(seq):
        if item in seen and seen[item] >= start:
            start = seen[item] + 1
        seen[item] = i
        if i - start + 1 > max_len:
            max_len = i - start + 1
            max_start = start
            max_end = i

    return max_len, max_start, max_end


def longest_simple_balanced_subsequence(seq):
    count = defaultdict(int)
    max_len = 0
    left = 0
    max_start = 0
    max_end = 0

    for right, item in enumerate(seq):
        count[item] += 1

        while True:
            current_counts = list(count.values())
            if not current_counts:
                break
            max_count = max(current_counts)
            min_count = min(current_counts)
            if max_count - min_count <= 1:
                break
            # 否则收缩左边界
            left_item = seq[left]
            count[left_item] -= 1
            if count[left_item] == 0:
                del count[left_item]
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_start = left
            max_end = right

    return max_len, max_start, max_end

# 设置目标目录路径
filename_list_path = "/Users/wangtianze/直博/项目/Athena/athena/lakebench/join/filename_list.txt"

# 生成文件路径到编号的映射
file_number_map = generate_file_number_map(filename_list_path)

# 示例 CSV 文件路径
csv_file_path = '/Users/wangtianze/直博/项目/Athena/athena/lakebench/join/opendata_join_result_grouped.csv'

# 读取 CSV 文件
df = pd.read_csv(csv_file_path)

# 提取 'query_table' 和 'candidate_table' 两列的数据
# query_data = df['query_table'].tolist()
candidate_data = df['candidate_table'].tolist()

# 合并为一个一维数组（可选：拼接两个列表）
data = candidate_data

max_unique_length, u_start, u_end = longest_unique_subsequence(data)
print(f"不含重复项的最长子序列长度是: {max_unique_length}, 起始索引: {u_start}, 终止索引: {u_end}")

max_balanced_length, b_start, b_end = longest_simple_balanced_subsequence(data)
print(f"满足条件的最长子序列长度是: {max_balanced_length}, 起始索引: {b_start}, 终止索引: {b_end}")

longest_balanced_subseq = data[b_start:b_end + 1]

mapped_data = map_column_data_to_numbers(longest_balanced_subseq, file_number_map)






