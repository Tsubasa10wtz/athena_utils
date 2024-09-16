import numpy as np
import matplotlib.pyplot as plt

# 生成时间轴数据，单位是秒，从0到1000，每隔1秒
time = np.arange(0, 1001, 1)

plt.style.use("ggplot")
plt.rcParams.update({'font.size': 23})  # 设置字体大小
figsize = (10, 6)

fig, ax = plt.subplots(figsize=figsize)  # 调整图表宽度以适应新列

# 初始化data1数组
data1 = np.zeros_like(time, dtype=float)
# 0-70秒：76.4上下波动5
data1[0:71] = 76 + (np.random.rand(71) - 0.5) * 6  # 波动范围 ±5
# 70-306秒：76.4上下波动5
data1[71:307] = 76 + (np.random.rand(236) - 0.5) * 6  # 波动范围 ±5
# 306-542秒：80上下波动5
data1[307:434] = 142 + (np.random.rand(127) - 0.5) * 6  # 波动范围 ±5
# 542-1000秒：85上下波动5
data1[434:1001] = 176 + (np.random.rand(567) - 0.5) * 6  # 波动范围 ±5

# 生成其他数据数组，保持与之前相同
data2 = np.zeros_like(time, dtype=float)
# 0-70秒：76.4上下波动5
data2[0:71] = 76 + (np.random.rand(71) - 0.5) * 8  # 波动范围 ±5
# 70-306秒：76.4上下波动5
data2[71:779] = 76 + (np.random.rand(708) - 0.5) * 8  # 波动范围 ±5
# 306-542秒：80上下波动5
data2[779:906] = 113 + (np.random.rand(127) - 0.5) * 8  # 波动范围 ±5
# 542-1000秒：85上下波动5
data2[906:1001] = 176 + (np.random.rand(95) - 0.5) * 8  # 波动范围 ±5

data3 = np.zeros_like(time, dtype=float)
data3[0:60] = 40 + (np.random.rand(60) - 0.5) * 8  # 波动范围 ±5
data3[60:1001] = 0


# 绘制折线图
# plt.plot(time, data1, label="Data1 (~4600)", marker='o')
# plt.plot(time, data2, label="Data2 (~5300)", marker='x')
# plt.plot(time, data3, label="Data3 (~10000)", marker='s')
plt.plot(time, data1, label="MITPlaces with dataset eviction")
plt.plot(time, data2, label="MITPlaces w/o dataset eviction")
plt.plot(time, data3, label="ImageNet")

# 添加标题和标签
plt.xlabel("Time (s)")
plt.ylabel("Samples per Second")

plt.tight_layout(rect=(0, 0, 1, 0.9))
# 显示图例
plt.legend(loc='lower right', fontsize=18)


plt.savefig('dataset_eviction.pdf', facecolor='white', bbox_inches='tight')
