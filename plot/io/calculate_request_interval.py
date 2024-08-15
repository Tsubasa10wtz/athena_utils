# 为了profile相邻两个请求的到来时间
import os
import re
from decimal import Decimal
import matplotlib.pyplot as plt

prefix = './txt'
# name = 'v100/cpu/resnet_imagenet_cache/firstabout200'
name = 'v100/v100/resnet_imagenet_cache/3epoch'
# name = 'v100/cpu/resnet_imagenet_cache/part'
# name = 'inf/resnet_imagenet_cache/first576'
# name = 'g4/vitb16_imagenet_cache/part'
txt_path = os.path.join(prefix, name) + '.txt'

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

# 绘制差值分布的直方图
plt.figure(figsize=(12, 8))
plt.hist(differences_float, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Time Differences', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.title('Distribution of Time Differences Between Adjacent Requests', fontsize=18)
plt.grid(True)
plt.show()