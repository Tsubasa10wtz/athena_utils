import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Overall', 'ResNet50\nImageNet', 'ResNet50\nMITPlaces', 'AlexNet\nImageNet', 'AlexNet\nMITPlaces', "Twitter\nCluster035", "TPC-DS"]
athena = np.array([273, 290, 273, 290, 1741, 48 * 60])
lru = np.array([344, 352, 344, 352, 1741, 48 * 60])
fifo = np.array([347, 348, 347, 348, 1765, 48 * 60 +43])
lhd = np.array([342, 357, 280, 332, 1755, 48 * 60 + 32])  # 添加LHD数据
uniform = np.array([274, 293, 274, 293, 2296, 49 * 60 + 36])
sieve = np.array([344, 345, 344, 345, 1734, 48 * 60 + 52])  # 示例SIEVE数据


# 计算均值
athena_mean = 1  # Athena 归一化到自身总是 1
lru_mean = np.mean(lru / athena)  # LRU 相对于 Athena
fifo_mean = np.mean(fifo / athena)
lhd_mean = np.mean(lhd / athena)  # LHD 相对于 Athena
uniform_mean = np.mean(uniform / athena)
sieve_mean = np.mean(sieve / athena)  # SIEVE 相对于 Athena

# 归一化计算
lru_norm = lru / athena
fifo_norm = fifo / athena
lhd_norm = lhd / athena  # LHD 归一化
uniform_norm = uniform / athena
sieve_norm = sieve / athena  # SIEVE 归一化

# 插入总体均值到数组的首位
lru_norm = np.insert(lru_norm, 0, lru_mean)
fifo_norm = np.insert(fifo_norm, 0, fifo_mean)
lhd_norm = np.insert(lhd_norm, 0, lhd_mean)
uniform_norm = np.insert(uniform_norm, 0, uniform_mean)
sieve_norm = np.insert(sieve_norm, 0, sieve_mean)

# 将SIEVE添加到类别中

bar_width = 0.05  # 调整条形宽度以适应更多条形
index = np.arange(len(categories))  # 分类标签位置

plt.style.use("ggplot")
plt.rcParams.update({'font.size': 24})  # 设置字体大小

colors = ['#e24a33', '#348abd', '#988ed5', '#777777', "#fbc15e", "#8eba41", "#ffb4b8"]

fig, ax = plt.subplots(figsize=(14, 8))  # 调整图表宽度以适应新列

# 按照 Athena、LRU、FIFO、LHD、Uniform、SIEVE 顺序绘制条形图
bar1 = ax.bar(index - 2.5 * bar_width, np.insert(np.ones(len(athena)), 0, athena_mean), bar_width, label='Athena', color=colors[0])  # Athena 作为基准
bar2 = ax.bar(index - 1.5 * bar_width, lru_norm, bar_width, label='LRU', color=colors[1])
bar3 = ax.bar(index - 0.5 * bar_width, fifo_norm, bar_width, label='FIFO', color=colors[2])
bar4 = ax.bar(index + 0.5 * bar_width, lhd_norm, bar_width, label='LHD', color=colors[3])
bar5 = ax.bar(index + 1.5 * bar_width, uniform_norm, bar_width, label='Uniform', color=colors[4])
bar6 = ax.bar(index + 2.5 * bar_width, sieve_norm, bar_width, label='SIEVE', color=colors[5])  # SIEVE 列

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('JCT (Normalized)', fontsize=30)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=20)  # 调整为45度以便更好地显示标签

ax.set_ylim(0, 1.5)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=6, fontsize=20)

# 显示图形并保存为白色背景的图片
plt.tight_layout()
plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
plt.show()




# old version
# # 计算均值
# lru_mean = 1  # LRU 归一化到自身总是 1
# uniform_mean = np.mean(uniform / lru)
# fifo_mean = np.mean(fifo / lru)
# lhd_mean = np.mean(lhd / lru)  # 计算LHD均值
# athena_mean = np.mean(athena / lru)
#
# # 归一化计算
# uniform_norm = uniform / lru
# fifo_norm = fifo / lru
# lhd_norm = lhd / lru  # 归一化LHD
# athena_norm = athena / lru
#
# # 插入总体均值到数组的首位
# uniform_norm = np.insert(uniform_norm, 0, uniform_mean)
# fifo_norm = np.insert(fifo_norm, 0, fifo_mean)
# lhd_norm = np.insert(lhd_norm, 0, lhd_mean)  # 插入LHD均值
# athena_norm = np.insert(athena_norm, 0, athena_mean)
#
# bar_width = 0.1  # 调整条形宽度以适应更少的条形
# index = np.arange(len(categories))  # 分类标签位置
#
# plt.style.use("ggplot")
# plt.rcParams.update({'font.size': 24})  # 设置字体大小
#
# colors = ['#e24a33', '#348abd', '#988ed5', '#777777', "#fbc15e", "#8eba41", "#ffb4b8"]
#
# fig, ax = plt.subplots(figsize=(14, 8))
#
# # 绘制条形图
# bar1 = ax.bar(index - 2 * bar_width, np.insert(np.ones(len(lru)), 0, lru_mean), bar_width, label='LRU', color=colors[0])  # LRU作为基准
# bar2 = ax.bar(index - bar_width, fifo_norm, bar_width, label='FIFO', color=colors[1])
# bar3 = ax.bar(index, lhd_norm, bar_width, label='LHD', color=colors[2])  # 插入LHD
# bar4 = ax.bar(index + bar_width, uniform_norm, bar_width, label='Uniform', color=colors[3])
# bar5 = ax.bar(index + 2 * bar_width, athena_norm, bar_width, label='Athena', color=colors[4])
#
# # 添加标签、标题和自定义x轴刻度标签
# ax.set_ylabel('JCT', fontsize=30)
# ax.set_xticks(index)
# ax.set_xticklabels(categories)  # 调整为45度以便更好地显示标签
#
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5, fontsize=20)
#
# # ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
# # fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色
#
# # 显示图形并保存为白色背景的图片
# plt.tight_layout()
# plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
# plt.show()
