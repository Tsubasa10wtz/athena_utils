import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 生成一个包含1000个0-999之间随机数的数组
ids = np.random.randint(0, 50000, size=500000)


# plt.hist(ids, bins=len(set(ids)), edgecolor='black')
# plt.xlabel('ID')
# plt.ylabel('Frequency')
# plt.title('Distribution of IDs')
# plt.show()


# ids = ids[0:100000]

# 计算每个ID的出现频次
frequency = np.bincount(ids)

# 对频次进行排序
sorted_frequency = np.sort(frequency)[::-1]

print(sorted_frequency)

s = sum(sorted_frequency[0:200])
print(s)




# # 绘制排序后的频次分布图
# plt.figure(figsize=(16, 8))
# plt.bar(range(len(sorted_frequency)), sorted_frequency, edgecolor='black')
# plt.xlabel('Sorted Index')
# plt.ylabel('Frequency')
# plt.title('Sorted Frequency Distribution of IDs')
# plt.show()

def calculate_diff_mean_and_variance(numbers):
    # 计算后一项减前一项的差
    # diff_list = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]
    diff_list = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]

    # 计算均值和方差
    mean_diff = np.mean(diff_list)
    var_diff = np.var(diff_list)


    return diff_list, mean_diff, var_diff

diff_list, mean_diff, var_diff = calculate_diff_mean_and_variance(ids)

print("均值:", mean_diff)
print("方差:", var_diff)

plt.figure(figsize=(12, 6))

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 33})
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 定义以 *10^3 为单位的刻度格式化函数
def thousands(x, pos):
    return '%1.0f' % (x * 1e-3)

formatter = FuncFormatter(thousands)

# 绘制差值的分布
plt.hist(diff_list, bins=30, edgecolor='black')  # 50个箱子应该足够细致地展示分布
plt.xlabel('Gap (× $10^3$)')
plt.ylabel('Count (× $10^3$)')

# 将横纵坐标都设置为以 *10^3 为单位显示
plt.gca().xaxis.set_major_formatter(formatter)
plt.gca().yaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.savefig(f'random.pdf', facecolor='white', bbox_inches='tight')

plt.show()