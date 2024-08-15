import csv
import os
import random

import numpy as np
import matplotlib.pyplot as plt

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
        if file_name in file_count:
            file_count[file_name] += 1
        else:
            file_count[file_name] = 1


ids = ids[0:100000]


# 找到出现次数最多的文件名
most_common_file = max(file_count, key=file_count.get)
most_common_count = file_count[most_common_file]

# 计算前20%的文件
sorted_files = sorted(file_count.items(), key=lambda item: item[1], reverse=True)
top_20_percent_index = int(len(sorted_files) * 0.2)  # 计算前20%的索引
top_20_percent_files = sorted_files[:top_20_percent_index]
total_counts_in_top_20_percent = sum(count for _, count in top_20_percent_files)
total_counts = sum(file_count.values())

# 计算前20%的文件出现次数占总次数的比例
top_20_percent_ratio = total_counts_in_top_20_percent / total_counts


plt.hist(ids, bins=len(set(ids)), edgecolor='black')
plt.xlabel('ID')
plt.ylabel('Frequency')
plt.title('Distribution of IDs')
plt.show()

# 输出前20%的文件总数量和出现总次数
print("前20%的文件总数量:", len(top_20_percent_files))
print("前20%的文件出现总次数:", total_counts_in_top_20_percent)
print("前20%的文件及出现次数:", top_20_percent_files)
print("前20%的文件出现次数占总次数的比例:", top_20_percent_ratio)

def calculate_diff_mean_and_variance(numbers):
    # 计算后一项减前一项的差
    diff_list = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]

    # 计算均值和方差
    mean_diff = np.mean(diff_list)
    var_diff = np.var(diff_list)


    return diff_list, mean_diff, var_diff

diff_list, mean_diff, var_diff = calculate_diff_mean_and_variance(ids)




print("均值:", mean_diff)
print("方差:", var_diff)

# 计算每个ID的出现频次
frequency = np.bincount(ids)


# 对频次进行排序
sorted_frequency = np.sort(frequency)[::-1]

s = sum(sorted_frequency[0:200])

print(s/100000)

plt.figure(figsize=(12, 6))
plt.bar(range(len(sorted_frequency)), sorted_frequency, color='blue', edgecolor='black')
plt.title('Sorted Frequency Distribution of Files')
plt.xlabel('File Index (sorted by frequency)')
plt.ylabel('Frequency of Occurrences')
plt.show()

# 计算前20%的元素个数
top_20_percent_index = int(len(sorted_frequency) * 0.2)

# 计算前20%频次的总和
top_20_percent_frequency_sum = sorted_frequency[:top_20_percent_index].sum()
# 计算所有频次的总和
total_frequency_sum = sorted_frequency.sum()
# 计算占比
proportion = top_20_percent_frequency_sum / total_frequency_sum
print(f"前20%的ids出现的占比是：{proportion:.2f}")
# 绘制差值的分布
plt.hist(diff_list, bins=50, edgecolor='black', color='green')  # 50个箱子应该足够细致地展示分布
plt.xlabel('Difference between consecutive IDs')
plt.ylabel('Frequency')
plt.title('Distribution of Differences between Consecutive IDs')
plt.show()