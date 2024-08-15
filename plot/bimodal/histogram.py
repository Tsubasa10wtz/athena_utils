import os
import re
from decimal import Decimal
import matplotlib.pyplot as plt
from diptest import diptest
import numpy as np

txt_path = 'tmp.txt'

with open(txt_path, 'r') as file:
    data = file.readlines()

print(data[0])

# 提取时间戳
pattern = r': ([\d.]+) -'
timestamps = [Decimal(re.search(pattern, line).group(1)) for line in data]

print(timestamps[0])

# 计算相邻时间戳的差值
differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]

# Find and print the maximum difference
max_difference = max(differences)
print(f'Maximum difference: {max_difference}')

# 计算平均差值
average_difference = sum(differences) / len(differences)
print(f'Average difference: {average_difference}')

# 将差值转换为浮点数列表，便于绘图
differences_float = [float(diff) for diff in differences]

diff = np.array(differences_float)


dip, p_value = diptest(diff)

# 输出结果
print(f'Dip statistic: {dip}')
print(f'P-value: {p_value}')

# 检查p值是否小于显著性水平（如0.05）
if p_value < 0.05:
    print("数据可能存在双峰分布")
else:
    print("数据可能为单峰分布")

plt.figure(figsize=(10, 6))
plt.hist(differences_float, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Histogram of Differences')
plt.xlabel('Difference')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()