import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, chisquare

# 生成包含1000个0-999之间随机数的数组
random_numbers = np.random.randint(0, 1000, size=10000)


def calculate_gini(array):
    """计算给定数组的 Gini 系数。"""
    # 数组转换为浮点数，确保没有整数除法
    array = np.array(array, dtype=np.float64)
    array_sorted = np.sort(array)
    n = array.size
    index = np.arange(1, n+1)  # 索引从1开始
    # Gini 系数的计算公式
    return (np.sum((2 * index - n - 1) * array_sorted)) / (n * np.sum(array_sorted))


# 计算 Gini 系数
gini_uniform = calculate_gini(random_numbers)

print("纯随机分布的 Gini 系数:", gini_uniform)