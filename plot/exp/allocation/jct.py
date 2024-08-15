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
    "ycsb"
]
default = np.array([178, 159, 174, 155, 2508, 2003])
quiver = np.array([201, 61, 195, 61, 2561, 2034])
fluid = np.array([119, 105, 119, 105, 2563, 2023])
athena = np.array([152, 58, 152, 58, 2549, 1918])

# 计算均值
default_mean = 1  # default 归一化到自身总是 1
quiver_mean = np.mean(quiver / default)
fluid_mean = np.mean(fluid / default)
athena_mean = np.mean(athena / default)

# 归一化计算
quiver_norm = quiver / default
fluid_norm = fluid / default
athena_norm = athena / default

# 插入总体均值到数组的首位
quiver_norm = np.insert(quiver_norm, 0, quiver_mean)
fluid_norm = np.insert(fluid_norm, 0, fluid_mean)
athena_norm = np.insert(athena_norm, 0, athena_mean)

bar_width = 0.2  # 条形宽度
index = np.arange(len(categories))  # 分类标签位置

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 24})  # 设置字体大小

fig, ax = plt.subplots(figsize=(14, 8))

# 绘制条形图
bar1 = ax.bar(index - 1.5 * bar_width, np.insert(np.ones(len(default)), 0, default_mean), bar_width, label='default')  # default作为基准
bar2 = ax.bar(index - 0.5 * bar_width, quiver_norm, bar_width, label='quiver')
bar3 = ax.bar(index + 0.5 * bar_width, fluid_norm, bar_width, label='fluid')
bar4 = ax.bar(index + 1.5 * bar_width, athena_norm, bar_width, label='Athena')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('JCT (Relative to default)')
ax.set_title('JCT Of Different Space Management Solutions')
ax.set_xticks(index)
ax.set_xticklabels(categories, rotation=45)  # 调整为45度以便更好地显示标签
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色

# 显示图形
plt.tight_layout()
plt.show()
