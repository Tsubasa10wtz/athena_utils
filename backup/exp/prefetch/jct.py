import matplotlib.pyplot as plt
import numpy as np

# 数据
# categories = ['Overall', 'imagenet\ntest', 'mitplaces\ntest', 'gpt2\nloading', 'opt\nloading', 'audio', 'fashion', 'india']
categories = ['Overall', 'imagenet\ntest', 'mitplaces\ntest', 'gpt2\nloading', 'opt\nloading', 'audio', 'fashion', 'india']
no = np.array([584, 379, 87, 89, 36, 83, 2.7])
stride = np.array([572, 375, 66, 70, 36, 81, 1.8])
juicefs = np.array([545, 361, 63, 69, 33, 83, 1.16])
athena = np.array([100, 105, 61, 71, 25, 20, 1.2])

# 归一化计算
juicefs_norm = juicefs / no
stride_norm = stride / no
athena_norm = athena / no

# 计算均值
no_mean = 1  # no 归一化到自身总是 1
juicefs_mean = np.mean(juicefs_norm)
stride_mean = np.mean(stride_norm)
athena_mean = np.mean(athena_norm)

# 插入总体均值到归一化数据的首位
juicefs_norm = np.insert(juicefs_norm, 0, juicefs_mean)
stride_norm = np.insert(stride_norm, 0, stride_mean)
athena_norm = np.insert(athena_norm, 0, athena_mean)
no_norm = np.insert(np.ones(len(no)), 0, no_mean)  # 插入 no 的均值

bar_width = 0.2  # 条形宽度
index = np.arange(len(categories))  # 分类标签位置

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size':24})  # 设置字体大小

fig, ax = plt.subplots(figsize=(14, 8))

# 绘制条形图
ax.bar(index - 1.5 * bar_width, no_norm, bar_width, label='no')  # no作为基准
ax.bar(index - 0.5 * bar_width, stride_norm, bar_width, label='stride')
ax.bar(index + 0.5 * bar_width, juicefs_norm, bar_width, label='juicefs')
ax.bar(index + 1.5 * bar_width, athena_norm, bar_width, label='Athena')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('JCT (Relative to no)')
ax.set_title('JCT Of Different Prefetching Strategies')
ax.set_xticks(index)
ax.set_xticklabels(categories, rotation=45)  # 调整为45度以便更好地显示标签
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色

# 显示图形
plt.tight_layout()
plt.show()
