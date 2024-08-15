import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 定义两个正态分布的参数
mu1, sigma1 = 0.01, 0   # 第一条曲线的均值和标准差
mu2, sigma2 = 0.03, 0.02 # 第二条曲线的均值和标准差
weight1, weight2 = 63/64, 1/64  # 两条曲线的权重

# 创建一个范围
x = np.linspace(-5, 7, 1000)

# 计算两个正态分布的密度函数
y1 = weight1 * norm.pdf(x, mu1, sigma1)
y2 = weight2 * norm.pdf(x, mu2, sigma2)

# 绘制两个正态分布曲线
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=f'$\mu={mu1}, \sigma={sigma1}, weight={weight1}$', color='blue')
plt.plot(x, y2, label=f'$\mu={mu2}, \sigma={sigma2}, weight={weight2}$', color='red')

# 添加均值和方差信息
plt.axvline(mu1, color='blue', linestyle='--', label=f'Mean1 = {mu1}')
plt.axvline(mu2, color='red', linestyle='--', label=f'Mean2 = {mu2}')
plt.axvline(mu1 + sigma1, color='blue', linestyle=':', label=f'Mean1 + 1*Std = {mu1 + sigma1}')
plt.axvline(mu2 + sigma2, color='red', linestyle=':', label=f'Mean2 + 1*Std = {mu2 + sigma2}')

# 设置图例和标题
plt.legend()
plt.title('Two Weighted Normal Distribution Curves')
plt.xlabel('X-axis')
plt.ylabel('Density')

# 显示图像
plt.show()