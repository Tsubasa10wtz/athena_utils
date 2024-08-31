import numpy as np
import matplotlib.pyplot as plt

# 定义 triangular_cdf 函数
def triangular_cdf(x, c):
    return np.where(x < 0, 0, np.where(x > c, 1, ((2 * x * c - x**2) / c**2)))

# 设置参数 c
c = 1.0

# 生成 x 轴的值
x_values = np.linspace(-1, 2, 500)

# 计算 CDF 值
cdf_values = triangular_cdf(x_values, c)

# 绘制图形
plt.figure(figsize=(8, 6))
plt.plot(x_values, cdf_values, label=f'Triangular CDF (c={c})', color='blue')
plt.title('Triangular CDF Function')
plt.xlabel('x')
plt.ylabel('CDF')
plt.grid(True)
plt.legend()
plt.show()
