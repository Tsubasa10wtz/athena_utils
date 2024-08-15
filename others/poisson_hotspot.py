import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, chisquare


# load生成文件
path = 'tracec_load_basic.txt'

files = []

with open(path, 'r') as file:
    # 逐行读取文件内容
    for line in file:
        # 如果当前行包含 usertable 字符串，则进行处理
        parts = line.split(' ')
        if parts[0] == 'INSERT':
            file_name = f'{parts[2]}.txt'
            files.append(file_name)

files.sort()

# 给文件名进行编号
file_map = {file_name: i for i, file_name in enumerate(files)}
#
# # 打印文件名映射表
# for file_name, index in file_map.items():
#     print(f'{file_name}: {index}')

csv_path = "ycsb-1g_trace.csv"

ids= []

with open(csv_path, mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        file_name = row[0]  # 假设文件名在每行的第一个列
        ids.append(file_map[file_name])

def calculate_gini(array):
    """计算给定数组的 Gini 系数。"""
    # 数组转换为浮点数，确保没有整数除法
    array = np.array(array, dtype=np.float64)
    array_sorted = np.sort(array)
    n = array.size
    index = np.arange(1, n+1)  # 索引从1开始
    # Gini 系数的计算公式
    return (np.sum((2 * index - n - 1) * array_sorted)) / (n * np.sum(array_sorted))

# 示例数据
zipf_data = np.array(ids)  # Zipf 分布

# 计算 Gini 系数
gini_zipf = calculate_gini(zipf_data)

print("Zipfian 分布的 Gini 系数:", gini_zipf)


