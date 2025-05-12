import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Job\u2468', 'Job\u246B', 'Job\u246D', 'Job\u246E']
plt.rcParams['font.family'] = 'Arial Unicode MS'  # 确保支持中文字体

p_values = {
    '\u03B1=0.01': [0.992, 0.994, 1, 0.869],
    '\u03B1=0.05': [0.938, 0.942, 1, 0.953],
}

# 配置
x = np.arange(len(categories))  # 横轴索引
width = 0.3  # 柱子的宽度
colors = ['#e0543c', '#3989ba']

# 绘制柱状图
fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.bar(x - width / 2, [v * 100 for v in p_values['\u03B1=0.01']], width, label='\u03B1=0.01', alpha=0.8, color=colors[0])
bars2 = ax.bar(x + width / 2, [v * 100 for v in p_values['\u03B1=0.05']], width, label='\u03B1=0.05', alpha=0.8, color=colors[1])

# 添加标签和标题
ax.set_ylabel('Accuracy (%)', fontsize=36)  # 纵轴以百分比显示
ax.set_xticks(x)
ax.set_xticklabels(categories)

# 设置纵轴为百分数
ax.set_ylim(40, 115)  # 设定纵轴范围，超过100%
ax.set_yticks(range(40, 101, 10))  # 只显示到 100 的刻度
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)}%'))

ax.set_xlim(-0.8, 3.8)  # 设定横轴范围

# 修改 X 轴刻度字体
plt.tick_params(axis='x', labelsize=30)  # 设置 X 轴刻度字体大小
# 修改左 Y 轴刻度字体
plt.tick_params(axis='y', labelsize=30)  # 设置左 Y 轴刻度字体大小

# 添加网格
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加图例，设置两列
plt.legend(fontsize=24, loc='upper center', ncol=2)

# 显示图形
plt.tight_layout()
plt.savefig('accuracy.pdf', facecolor='white', bbox_inches='tight')
plt.show()