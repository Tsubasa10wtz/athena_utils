import matplotlib.pyplot as plt
import numpy as np

categories = ['Overall', 'imagenet\ntest', 'alex\nmitplaces\ntest', 'gpt2\nloading', 'opt\nloading', 'audio', 'fashion', 'india']
no = np.array([0, 0, 0, 0, 0, 0, 0])
stride = np.array([16.1, 0, 74.3, 72.5, 0, 0, 52])
juicefs = np.array([16.1, 0, 78.1, 76.2, 0, 0, 52])
athena = np.array([96.2, 97.1, 77.3, 74.1, 95.2, 94.1, 65])

# 计算各方法的均值
no_mean = np.mean(no)
stride_mean = np.mean(stride)
juicefs_mean = np.mean(juicefs)
athena_mean = np.mean(athena)

print(juicefs_mean)
print(athena_mean)

# 将均值作为第一项加入
no = np.insert(no, 0, no_mean)
stride = np.insert(stride, 0, stride_mean)
juicefs = np.insert(juicefs, 0, juicefs_mean)
athena = np.insert(athena, 0, athena_mean)

bar_width = 0.2  # 条形宽度
index = np.arange(len(categories))  # 分类标签位置，调整以包括 'Overall'

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 24})  # 设置字体大小

fig, ax = plt.subplots(figsize=(14, 8))

# 绘制条形图
bar1 = ax.bar(index - 1.5 * bar_width, no, bar_width, label='no')
bar2 = ax.bar(index - 0.5 * bar_width, stride, bar_width, label='stride')
bar3 = ax.bar(index + 0.5 * bar_width, juicefs, bar_width, label='juicefs')
bar4 = ax.bar(index + 1.5 * bar_width, athena, bar_width, label='Athena')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Cache Hit Ratio')
ax.set_title('Cache Hit Ratio of Different Prefetching Strategies')
ax.set_xticks(index)
ax.set_xticklabels(categories, rotation=45)  # 调整为45度以便更好地显示标签
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色

# 显示图形
plt.tight_layout()
plt.show()
