import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 生成一个包含328500长度的连续序列
ids = np.arange(328500)

# 计算差值
def calculate_diff_mean_and_variance(numbers):
    # 计算后一项减前一项的差
    diff_list = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]

    # 计算均值和方差
    mean_diff = np.mean(diff_list)
    var_diff = np.var(diff_list)

    return diff_list, mean_diff, var_diff

diff_list, mean_diff, var_diff = calculate_diff_mean_and_variance(ids)

# 输出均值和方差
print("均值:", mean_diff)
print("方差:", var_diff)

# 绘制差值的分布图
plt.figure(figsize=(12, 6))
plt.rcParams['font.family'] = 'Arial Unicode MS'
plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 33})

# 定义以 *10^3 为单位的刻度格式化函数
def thousands(x, pos):
    return '%1.0f' % (x * 1e-4)

formatter = FuncFormatter(thousands)

# 绘制差值的分布，设置区间范围为 0-328500 并划分 30 个桶
plt.hist(diff_list, bins=np.linspace(0, 328500, 31), edgecolor='black')

plt.xlabel('Gap (× $10^4$)')
plt.ylabel('Count (× $10^4$)')


# 将横纵坐标都设置为以 *10^3 为单位显示
plt.gca().xaxis.set_major_formatter(formatter)
plt.gca().yaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.savefig(f'sequential.pdf', facecolor='white', bbox_inches='tight')

plt.show()
