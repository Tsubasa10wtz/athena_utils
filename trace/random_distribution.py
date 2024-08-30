import numpy as np
import matplotlib.pyplot as plt

# 生成一个从0到100000的列表
numbers = list(range(50000))

# 随机打乱列表
np.random.shuffle(numbers)

# 计算相邻两数之间的差值
differences = np.diff(numbers)

# 计算差值列表的均值和方差
mean_diff = np.mean(differences)
variance_diff = np.var(differences)

# 绘制差值的分布图
plt.figure(figsize=(10, 6))
plt.hist(differences, bins=50, alpha=0.75, color='blue', edgecolor='black')
plt.title('Distribution of Differences After Shuffling')
plt.xlabel('Difference Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

print(f"Mean of differences: {mean_diff}")
print(f"Variance of differences: {variance_diff}")
