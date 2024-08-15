import re
import matplotlib.pyplot as plt

# 定义文件路径
file_path = 'check.txt'

# 初始化空列表用于存储 Offset 值
offsets = []

# 打开文件并读取内容
with open(file_path, 'r') as file:
    for line in file:
        # 使用正则表达式提取 Offset 值
        match = re.search(r'Offset:\s+(\d+)', line)
        if match:
            offsets.append(int(match.group(1)))

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(offsets, marker='o', linestyle='-', color='b')
plt.title('Offset Values Over Time')
plt.xlabel('Read Order')
plt.ylabel('Offset')
plt.grid(True)
plt.show()