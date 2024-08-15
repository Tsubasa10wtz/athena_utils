import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import kstest, chisquare, entropy


# load生成文件
path = 'tracec_load_basic_zipfian.txt'

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

csv_path = "ycsb-1g_trace_zipfian.csv"

ids= []
file_count = {}  # 新增一个字典来记录每个文件名出现的次数

with open(csv_path, mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        file_name = row[0]  # 假设文件名在每行的第一个列
        file_index = file_map[file_name]
        ids.append(file_index)

# ids = np.random.randint(0, 1000, size=10000)

ids = ids[0:1000]

# 假设 ids 已经包含了从CSV文件读取的所有索引
ids_count = Counter(ids)
total = sum(ids_count.values())
probabilities = np.array([count / total for count in ids_count.values()])

# 计算熵
data_entropy = entropy(probabilities, base=2)
print("Entropy of the data distribution:", data_entropy)

