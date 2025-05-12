import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



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



