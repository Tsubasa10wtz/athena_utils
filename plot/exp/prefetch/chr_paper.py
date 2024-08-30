import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Overall', 'imagenet\ntest', 'alex\nmitplaces\ntest', 'gpt2\nloading', 'opt\nloading', 'audio', 'fashion', 'india']
no = np.array([0, 0, 0, 0, 0, 0, 0])
stride = np.array([16.1, 0, 74.3, 72.5, 0, 0, 52])
juicefs = np.array([16.1, 0, 78.1, 76.2, 0, 0, 52])
context = np.array([0, 0, 0, 0, 0, 0, 0])  # 添加context数据
athena = np.array([96.2, 97.1, 77.3, 74.1, 95.2, 94.1, 65])

# 计算各方法的均值
no_mean = np.mean(no)
stride_mean = np.mean(stride)
juicefs_mean = np.mean(juicefs)
context_mean = np.mean(context)  # 计算context均值
athena_mean = np.mean(athena)

# 打印juicefs和athena的均值
print(juicefs_mean)
print(athena_mean)

# 将均值作为第一项加入
no = np.insert(no, 0, no_mean)
stride = np.insert(stride, 0, stride_mean)
juicefs = np.insert(juicefs, 0, juicefs_mean)
context = np.insert(context, 0, context_mean)  # 插入context均值
athena = np.insert(athena, 0, athena_mean)

bar_width = 0.10  # 调整条形宽度，增加一个条形
index = np.arange(len(categories))  # 分类标签位置，调整以包括 'Overall'

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 24})  # 设置字体大小

fig, ax = plt.subplots(figsize=(14, 8))

# 绘制条形图
bar1 = ax.bar(index - 2 * bar_width, no, bar_width, label='no', edgecolor='black')
bar2 = ax.bar(index - bar_width, stride, bar_width, label='stride', edgecolor='black')
bar3 = ax.bar(index, juicefs, bar_width, label='juicefs', edgecolor='black')
bar4 = ax.bar(index + bar_width, context, bar_width, label='context', edgecolor='black')  # 插入context
bar5 = ax.bar(index + 2 * bar_width, athena, bar_width, label='Athena', edgecolor='black')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Cache Hit Ratio', fontsize=30)
# ax.set_title('Cache Hit Ratio of Different Prefetching Strategies')
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=20)  # 调整为45度以便更好地显示标签

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色
plt.gcf().set_facecolor('white')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)

# 显示图形
plt.tight_layout()
plt.savefig('chr.pdf', facecolor='white', bbox_inches='tight')
