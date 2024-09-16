import numpy as np

# 数据
categories = ['Overall', 'ImageNet', 'MITPlaces', "Twitter", "TPC-DS"]
athena = np.array([273, 290, 1741, 48 * 60])
lru = np.array([344, 352, 1741, 48 * 60])
fifo = np.array([347, 348, 1765, 48 * 60 + 43])
lhd = np.array([342, 357, 1755, 48 * 60 + 32])
uniform = np.array([274, 293, 2296, 49 * 60 + 36])
sieve = np.array([344, 345, 1734, 48 * 60 + 52])

# 计算均值
athena_mean = 1
lru_mean = np.mean(lru / athena)
fifo_mean = np.mean(fifo / athena)
lhd_mean = np.mean(lhd / athena)
uniform_mean = np.mean(uniform / athena)
sieve_mean = np.mean(sieve / athena)

# 计算相对减少
second_best_mean = min(lru_mean, fifo_mean, lhd_mean, uniform_mean, sieve_mean)
relative_reduction = (second_best_mean - athena_mean) / second_best_mean * 100

print(f"Athena相较于第二快的减少了 {relative_reduction:.2f}% 的时间。")