
import numpy as np
from scipy.stats import kstest



def triangular_cdf(x, c):
    """三角分布的CDF函数"""
    # return np.where(x < 0, 0, np.where(x > c, 1, ((2 * x * c - x ** 2) / c ** 2)))
    return np.where(x < 0, 0, np.where(x >= c-1, 1, (2 * x / (c - 1) - x * (x + 1)/ (c * (c-1)))))

def step_cdf(x, c):
    """简单阶跃函数的CDF"""
    return np.where(x < 0, 0, np.where(x < c, 0, 1))


def calculate_diff_mean_and_variance(numbers):
    # 计算后一项减前一项的差
    diff_list = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]

    # 计算均值和方差
    mean_diff = np.mean(diff_list)
    var_diff = np.var(diff_list)

    return diff_list





# 设置参数
c = 376357
base_sequence = np.arange(0, c)  # 0-1299 的序列
print(len(base_sequence))
np.random.seed(45)  # 设置随机种子，保证结果一致

# 生成打乱后的序列并重复拼接
shuffled_sequences = [np.random.permutation(base_sequence) for _ in range(1)]
ids = np.concatenate(shuffled_sequences)

ids = ids[0:4000]

# 统计 p 值分布
p_values = []
batch_size = 100

# 按批次处理数据
for i in range(0, len(ids), batch_size):
    # 提取一个批次的数据
    batch = ids[i:i + batch_size]
    if len(batch) < batch_size:
        break  # 忽略不足一个批次的数据

    # 计算当前批次的差值
    diff = calculate_diff_mean_and_variance(batch)

    # 执行 K-S 检验
    result = kstest(diff, triangular_cdf, args=(c,))
    p_values.append(result.pvalue)

# 统计 p 值 >= 0.01 的数量
count_ge_0_01 = sum(1 for p in p_values if p >= 0.01)

# 统计 p 值 < 0.01 的数量
count_lt_0_01 = sum(1 for p in p_values if p < 0.01)

# 统计 p 值 >= 0.05 的数量
count_ge_0_05 = sum(1 for p in p_values if p >= 0.05)

# 统计 p 值 < 0.05 的数量
count_lt_0_05 = sum(1 for p in p_values if p < 0.05)



# 输出结果
print(f"Number of p-values >= 0.01: {count_ge_0_01}")
print(f"Number of p-values < 0.01: {count_lt_0_01}")
print(f"Number of p-values >= 0.05: {count_ge_0_05}")
print(f"Number of p-values < 0.05: {count_lt_0_05}")
print(f"P-values: {p_values}")