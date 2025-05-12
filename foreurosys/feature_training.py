import numpy as np
import matplotlib.pyplot as plt

# 模拟参数
num_samples = 1300
num_epochs = 1

# 记录所有访问顺序
access_order = []

# 每个 epoch shuffle 后记录访问顺序
for epoch in range(num_epochs):
    indices = np.arange(num_samples)
    np.random.shuffle(indices)
    access_order.extend(indices)

access_order = access_order[:100]

# 生成横轴：访问顺序的索引
x = np.arange(len(access_order))

plt.rcParams.update({'font.size': 30})

plt.rcParams['font.family'] = 'Arial Unicode MS'

# 绘图
plt.figure(figsize=(8, 6))
plt.scatter(x, access_order, s=20, zorder=3)
plt.xlabel('Access Order')
plt.ylabel('Sample Index')
plt.grid(True)
plt.tight_layout()
plt.savefig("random_access.pdf", bbox_inches='tight')
# plt.show()
