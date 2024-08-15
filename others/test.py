import numpy as np
from scipy.stats import kstest

# 生成一些示例数据
data = np.random.uniform(0, 1, 1000)  # 假设的均匀分布数据
data_with_hotspot = np.append(data, np.full(100, 0.5))  # 添加热点

# KS测试
ks_stat, p_value = kstest(data_with_hotspot, 'uniform', args=(0, 1))
print(f"KS statistic: {ks_stat}, P-value: {p_value}")

# 根据P值判断
if p_value < 0.05:
    print("Data does not come from a uniform distribution")
else:
    print("Data comes from a uniform distribution")