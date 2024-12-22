import numpy as np
import matplotlib.pyplot as plt

# 生成示例数据
data = np.random.normal(0, 1, 1000)

print(data)

# 计算CDF
sorted_data = np.sort(data)
y = np.arange(1, len(data) + 1) / len(data)

# 绘制CDF
plt.figure(figsize=(10, 6))
plt.plot(sorted_data, y, label='CDF')
plt.title('手动计算的累积分布函数 - how2matplotlib.com')
plt.xlabel('值')
plt.ylabel('累积概率')
plt.legend()
plt.grid(True)
plt.show()

print("Visit how2matplotlib.com for more examples")
