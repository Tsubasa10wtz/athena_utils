import numpy as np
from scipy.stats import kstest
import matplotlib.pyplot as plt

# 生成一个包含1000个0-999之间随机数的数组
ids = np.random.randint(0, 1000, size=300)

ids = ids[0:1000]

# 计算每个ID的出现频次
frequency = np.bincount(ids)

# 对频次进行排序
sorted_frequency = np.sort(frequency)[::-1]




def calculate_diff_mean_and_variance(numbers):
    # 计算后一项减前一项的差
    # diff_list = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]
    diff_list = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]

    # 计算均值和方差
    mean_diff = np.mean(diff_list)
    var_diff = np.var(diff_list)


    return diff_list, mean_diff, var_diff

diff_list, mean_diff, var_diff = calculate_diff_mean_and_variance(ids)

def triangular_cdf(x, c):
    return np.where(x < 0, 0, np.where(x > c, 1, ((2*x*c-x**2)/c**2)))

# 假设 c 已知
c = 1000  # 或其他你认为合理的值

# 执行KS检验
result = kstest(diff_list, triangular_cdf, args=(c,))
print('KS statistic:', result.statistic)
print('p-value:', result.pvalue)
