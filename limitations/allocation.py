import matplotlib.pyplot as plt

#whole:330
# dataset1, dataset2, dataset3, unused
# 300MB, 230MB, 115MB, unused

# Data for the four categories
simple = [110, 110, 110, 0]
quiver = [0, 230, 0, 100]
fluid = [110, 110, 55, 55]
ideal = [100, 230, 0, 0]

# Names of the approaches and datasets
approaches = ['Simple', 'Quiver', 'Fluid', 'Ideal']
plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 30})  # 调整字体大小以确保可读性

# Define custom colors
custom_colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52']  # 深蓝色, 橙色, 绿色, 红色

# Define hatch patterns
hatch_patterns = ['/', '\\', 'x', 'o']  # 斜线, 反斜线, 交叉线, 点状

fig, ax = plt.subplots(figsize=(10, 8))

# Combining the data into a list of lists
data = [simple, quiver, fluid, ideal]

bar_width = 0.4  # Adjusted bar width for thinner bars

for i, approach in enumerate(data):
    plt.bar(i, approach[0], color=custom_colors[0], edgecolor='black', width=bar_width, hatch=hatch_patterns[0])
    plt.bar(i, approach[1], bottom=approach[0], color=custom_colors[1], edgecolor='black', width=bar_width, hatch=hatch_patterns[1])
    plt.bar(i, approach[2], bottom=approach[0] + approach[1], color=custom_colors[2], edgecolor='black', width=bar_width, hatch=hatch_patterns[2])
    plt.bar(i, approach[3], bottom=approach[0] + approach[1] + approach[2], color=custom_colors[3], edgecolor='black', width=bar_width, hatch=hatch_patterns[3])

# Adding labels and title
plt.xticks(range(len(approaches)), approaches)
plt.ylabel('Cache Size (MB)')
plt.xlabel('Strategies')

# Adding a legend
plt.legend(['Dataset1', 'Dataset2', 'Dataset3', 'Unused'], loc='upper right')

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色

plt.tight_layout()
plt.savefig('allocation.pdf', facecolor='white', bbox_inches='tight')
plt.show()


# 图说明了适应性缓存分配的重要性. 我们选择了三个deep learning workload对应Dataset1, 2, 3. 然后选择了simple static allocation(平均分配),Quiver和Fluid来进行缓存分配,此外一种理想的根据workload的特征进行适应性来分配缓存. 三个数据集的大小设置为