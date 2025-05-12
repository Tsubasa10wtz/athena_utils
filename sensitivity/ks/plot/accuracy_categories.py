import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Mean', 'Seq.', 'Rand.', 'Skewed']
plt.rcParams['font.family'] = 'Arial Unicode MS'  # 确保支持中文字体

p_values = {
    '\u03B1=0.01': [1, 0.994, 0.972],
    '\u03B1=0.05': [1, 0.942, 0.993],
}

# 计算平均值并添加到数据中
p_values['\u03B1=0.01'] = [np.mean(p_values['\u03B1=0.01'])] + p_values['\u03B1=0.01']
p_values['\u03B1=0.05'] = [np.mean(p_values['\u03B1=0.05'])] + p_values['\u03B1=0.05']

# 配置
x = np.arange(len(categories))  # 横轴索引
width = 0.3  # 柱子的宽度
colors = ['#e0543c', '#3989ba']

# 绘制柱状图
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor('white')  # 设置图像背景为白色

# 绘制柱状图并添加边框
bars1 = ax.bar(x - width / 2, [v * 100 for v in p_values['\u03B1=0.01']], width, label='\u03B1=0.01', color=colors[0], edgecolor='black', linewidth=1.2)
bars2 = ax.bar(x + width / 2, [v * 100 for v in p_values['\u03B1=0.05']], width, label='\u03B1=0.05', color=colors[1], edgecolor='black', linewidth=1.2)

# 添加标签和标题
ax.set_ylabel('Accuracy (%)', fontsize=36)  # 纵轴以百分比显示
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=30)  # 旋转横轴字体

# 设置纵轴为百分数
ax.set_ylim(70, 105)  # 设定纵轴范围，超过100%
ax.set_yticks(range(70, 101, 5))  # 只显示到 100 的刻度
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)}'))

ax.set_xlim(-0.5, len(categories) - 0.5)  # 设定横轴范围

# 修改左 Y 轴刻度字体
plt.tick_params(axis='y', labelsize=30)  # 设置左 Y 轴刻度字体大小

# 添加网格，设置网格放在最底层
ax.set_axisbelow(True)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加图例，设置两列
plt.legend(fontsize=30, loc='upper center', ncol=2, bbox_to_anchor=(0.5, 1.3))

# 显示图形
plt.tight_layout()
plt.savefig('accuracy.pdf', facecolor='white', bbox_inches='tight')
plt.show()