import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = [
    "Overall",
    "resnet\nimagenet\ntrain",
    "resnet\nmitplaces\ntrain",
    "alex\nimagenet\ntrain",
    "alex\nmitplaces\ntrain",
    "spark",
    "twitter\ncluster035"
]
default = np.array([6.3, 23.2, 6.3, 23.2, 6.2, 10.1])
quiver = np.array([0, 100, 0, 100, 30.4, 0])
fluid = np.array([50.1, 55.2, 50.1, 55.2, 24.6, 0])
athena = np.array([15.2, 100, 15.2, 100, 15.1, 14.2])

# 计算各方法的均值
default_mean = np.mean(default)
quiver_mean = np.mean(quiver)
fluid_mean = np.mean(fluid)
athena_mean = np.mean(athena)

# 将均值作为第一项加入
default = np.insert(default, 0, default_mean)
quiver = np.insert(quiver, 0, quiver_mean)
fluid = np.insert(fluid, 0, fluid_mean)
athena = np.insert(athena, 0, athena_mean)

bar_width = 0.1  # 条形宽度
index = np.arange(len(categories))  # 分类标签位置

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 24})  # 调整字体大小以确保可读性

fig, ax = plt.subplots(figsize=(14, 8))

# 绘制条形图
ax.bar(index - 1.5 * bar_width, default, bar_width, label='Default', edgecolor='black')
ax.bar(index - 0.5 * bar_width, quiver, bar_width, label='Quiver', edgecolor='black')
ax.bar(index + 0.5 * bar_width, fluid, bar_width, label='Fluid', edgecolor='black')
ax.bar(index + 1.5 * bar_width, athena, bar_width, label='Athena', edgecolor='black')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Cache Hit Ratio')
ax.set_xticks(index)
ax.set_xticklabels(categories)  # 调整标签角度以提高可读性

# 设置图例
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=6, fontsize=20)

# 设置背景色
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

# 显示图形
plt.tight_layout()
plt.savefig('chr.pdf', facecolor='white', bbox_inches='tight')
plt.show()
