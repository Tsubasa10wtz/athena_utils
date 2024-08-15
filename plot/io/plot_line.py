import os
import re
import matplotlib.pyplot as plt

# 读取文件内容
file_path = 'ratio_cal_bound.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# 提取数值
pattern = r'map\[ImageNet:(\d+\.\d+)\]'
values = [float(re.search(pattern, line).group(1)) for line in lines]

# 打印提取的数值
print(values)

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(values, marker='o', linestyle='-', color='b')
plt.xlabel('Entry Index')
plt.ylabel('Value')
plt.title('Line Plot of Values from File')
plt.grid(True)
plt.show()