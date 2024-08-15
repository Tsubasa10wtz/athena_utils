import os
import re
from decimal import Decimal
import matplotlib.pyplot as plt
from diptest import diptest
import numpy as np
from scipy.stats import anderson


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

result = anderson(diff)

# 输出结果
print('Anderson-Darling Statistic:', result.statistic)
print('Critical Values:', result.critical_values)
print('Significance Levels:', result.significance_level)

# 判断结果
for i in range(len(result.critical_values)):
    if result.statistic < result.critical_values[i]:
        print(f'数据在显著性水平 {result.significance_level[i]}% 下符合正态分布')
    else:
        print(f'数据在显著性水平 {result.significance_level[i]}% 下不符合正态分布')