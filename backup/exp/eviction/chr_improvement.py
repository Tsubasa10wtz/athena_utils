import numpy as np

# 数据
athena = np.array([25.3, 20.1, 89.3, 93.7])
lru = np.array([3, 1.9, 89.3, 93.7])
fifo = np.array([3.3, 2, 93.7, 93.8])
uniform = np.array([25.3, 20.1, 18.4, 91.7])
lhd = np.array([3.2, 1.9, 93.7, 94])
sieve = np.array([3, 1.9, 93.6, 94.1])  # 示例SIEVE数据

# 计算各方法的均值并作为第一项加入
lru_mean = np.mean(lru)
fifo_mean = np.mean(fifo)
uniform_mean = np.mean(uniform)
lhd_mean = np.mean(lhd)
athena_mean = np.mean(athena)
sieve_mean = np.mean(sieve)

lru = np.insert(lru, 0, lru_mean)
fifo = np.insert(fifo, 0, fifo_mean)
uniform = np.insert(uniform, 0, uniform_mean)
lhd = np.insert(lhd, 0, lhd_mean)
athena = np.insert(athena, 0, athena_mean)
sieve = np.insert(sieve, 0, sieve_mean)

# 计算Athena相较于第二好的提升
second_best_mean = max(lru_mean, fifo_mean, uniform_mean, lhd_mean, sieve_mean)
athena_improvement = athena_mean - second_best_mean

print(f"Athena相较于第二好的提升了 {athena_improvement:.1f} 个百分点。")
