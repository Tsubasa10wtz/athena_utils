import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Overall', 'imagenet\ntest', 'mitplaces\ntest', 'gpt2\nloading', 'opt\nloading', 'audio', 'fashion', 'india', 'marine']
no = np.array([584, 379, 87, 89, 36, 83, 2.7, 35.2])
stride = np.array([572, 375, 66, 70, 36, 81, 1.8, 35.4])
juicefs = np.array([545, 361, 63, 69, 33, 83, 1.16, 35.1])
context = np.array([586, 380, 86, 87, 35, 82, 2.7, 36.2])  # 添加新的context数据
athena = np.array([100, 105, 61, 71, 25, 20, 1.2, 9.7])

# 归一化计算
juicefs_norm = juicefs / no
stride_norm = stride / no
context_norm = context / no  # 计算context的归一化值
athena_norm = athena / no

# 计算均值
no_mean = 1  # no 归一化到自身总是 1
juicefs_mean = np.mean(juicefs_norm)
stride_mean = np.mean(stride_norm)
context_mean = np.mean(context_norm)  # context均值
athena_mean = np.mean(athena_norm)

# 插入总体均值到归一化数据的首位
juicefs_norm = np.insert(juicefs_norm, 0, juicefs_mean)
stride_norm = np.insert(stride_norm, 0, stride_mean)
context_norm = np.insert(context_norm, 0, context_mean)  # 插入context均值
athena_norm = np.insert(athena_norm, 0, athena_mean)
no_norm = np.insert(np.ones(len(no)), 0, no_mean)  # 插入 no 的均值

bar_width = 0.1  # 调整条形宽度，增加一个条形
index = np.arange(len(categories))  # 分类标签位置

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 22})  # 设置字体大小

fig, ax = plt.subplots(figsize=(14, 8))  # 调整图形大小

# 绘制条形图
ax.bar(index - 2 * bar_width, no_norm, bar_width, label='No', edgecolor='black')  # no作为基准
ax.bar(index - bar_width, stride_norm, bar_width, label='Stride', edgecolor='black')
ax.bar(index, juicefs_norm, bar_width, label='Juicefs', edgecolor='black')
ax.bar(index + bar_width, context_norm, bar_width, label='Context', edgecolor='black')  # 插入context
ax.bar(index + 2 * bar_width, athena_norm, bar_width, label='Athena', edgecolor='black')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('JCT', fontsize=30)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=20)  # 调整为45度以便更好地显示标签
# plt.subplots_adjust(top=0.8)

# 将图例放置在顶部
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)
ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色
plt.gcf().set_facecolor('white')

# 显示图形
plt.tight_layout()
plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
