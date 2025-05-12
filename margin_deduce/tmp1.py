# 非重复
import numpy as np

# 参数设置
num_samples = 1000
num_epochs = 100

# 生成每个 epoch 的打乱顺序
epoch_orders = np.zeros((num_epochs, num_samples), dtype=int)
for epoch in range(num_epochs):
    epoch_orders[epoch] = np.random.permutation(num_samples)

# 获取每个样本在每个 epoch 中的位置
pos = np.zeros((num_samples, num_epochs), dtype=int)
for epoch in range(num_epochs):
    for position, sample in enumerate(epoch_orders[epoch]):
        pos[sample, epoch] = position

# 计算非重复样本间隔
unique_sample_counts = np.zeros((num_samples, num_epochs - 1), dtype=int)

for sample in range(num_samples):
    for epoch in range(num_epochs - 1):
        i = pos[sample, epoch]
        j = pos[sample, epoch + 1]

        # 取出环形区间样本序列
        part1 = epoch_orders[epoch, i+1:] if i+1 < num_samples else []
        part2 = epoch_orders[epoch + 1, :j] if j > 0 else []

        combined = np.concatenate((part1, part2))
        unique_samples = np.unique(combined[combined != sample])  # 去除自身
        unique_sample_counts[sample, epoch] = len(unique_samples)

# 计算期望值
expected_unique_sample_count = np.mean(np.mean(unique_sample_counts, axis=1))
print(f"非重复样本间隔的期望值为: {expected_unique_sample_count}")
