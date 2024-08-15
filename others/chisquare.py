import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import kstest, chisquare


# load生成文件
path = 'tracec_load_basic_hotspot.txt'

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

csv_path = "ycsb-1g_trace_hotspot.csv"

ids= []
file_count = {}  # 新增一个字典来记录每个文件名出现的次数

with open(csv_path, mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        file_name = row[0]  # 假设文件名在每行的第一个列
        file_index = file_map[file_name]
        ids.append(file_index)

ids = np.array(ids)
# ids = np.random.randint(0, 1000, size=10000)
#
# ids = ids[600:1100]

# 计算每个数字出现的频次
frequency = np.bincount(ids, minlength=1000)

# 执行卡方测试
chi_stat, p_value = chisquare(frequency)

print(f"Chi-squared statistic: {chi_stat}, P-value: {p_value}")

if p_value < 0.05:
    print("Data does not come from a uniform distribution")
else:
    print("Data comes from a uniform distribution")


plt.show()