import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
file_path = 'try.csv'  # 将此路径替换为实际文件路径
data = pd.read_csv(file_path, header=None)

# 计算相邻行的第五项之差，然后除以4096
diffs = (data[4].diff().dropna() / 4096).astype(int)

# 绘制分布图
plt.figure(figsize=(10, 6))
plt.hist(diffs, bins=30, edgecolor='black')
plt.title('Distribution of Differences')
plt.xlabel('Difference (in blocks of 4096)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
