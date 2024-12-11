import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 生成一个包含1000个0-999之间随机数的数组
ids = np.random.randint(0, 50000, size=500000)

# 计算每个ID的出现频次
frequency = np.bincount(ids)

# 对频次进行排序
sorted_frequency = np.sort(frequency)[::-1]

print(sorted_frequency)

s = sum(sorted_frequency[0:200])
print(s)

def calculate_diff_mean_and_variance(numbers):
    # 计算后一项减前一项的差
    diff_list = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]

    # 计算均值和方差
    mean_diff = np.mean(diff_list)
    var_diff = np.var(diff_list)

    return diff_list, mean_diff, var_diff

diff_list, mean_diff, var_diff = calculate_diff_mean_and_variance(ids)

print("均值:", mean_diff)
print("方差:", var_diff)

# 计算差值的累积分布
sorted_diffs = np.sort(diff_list)  # 排序
cdf = np.arange(1, len(sorted_diffs) + 1) / len(sorted_diffs)  # 生成 CDF 的 y 值 (0, 1]

plt.figure(figsize=(12, 6))

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 33})
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 定义以 *10^3 为单位的刻度格式化函数
def thousands(x, pos):
    return '%1.0f' % (x * 1e-3)

formatter = FuncFormatter(thousands)

# 绘制 CDF
plt.plot(sorted_diffs, cdf, label='CDF', marker='.', linestyle='none')  # 绘制点图
plt.xlabel('Gap (× $10^3$)')
plt.ylabel('CDF')

# 将横纵坐标都设置为以 *10^3 为单位显示
plt.gca().xaxis.set_major_formatter(formatter)

plt.grid(True)
plt.tight_layout()
plt.savefig(f'random_cdf_point.pdf', facecolor='white', bbox_inches='tight')

plt.show()