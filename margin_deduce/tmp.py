# 可重复
import numpy as np

# 参数设置
num_samples = 1000
num_epochs = 100
sample_id = 1  # 要计算的样本编号

# 生成每个 epoch 的打乱顺序
epoch_orders = np.zeros((num_epochs, num_samples), dtype=int)
for epoch in range(num_epochs):
    epoch_orders[epoch] = np.random.permutation(num_samples)

# 获取该样本在每个 epoch 中的位置
positions = np.zeros(num_epochs, dtype=int)
for epoch in range(num_epochs):
    positions[epoch] = np.where(epoch_orders[epoch] == sample_id)[0][0]

# 计算循环间隔：(num_samples - i) + j
intervals = []
for epoch in range(num_epochs - 1):
    i = positions[epoch]
    j = positions[epoch + 1]
    interval = (num_samples - i) + j
    intervals.append(interval)

# 计算期望值（平均间隔）
expected_interval = np.mean(intervals)
print(f"样本 {sample_id} 的循环间隔期望值为: {expected_interval}")