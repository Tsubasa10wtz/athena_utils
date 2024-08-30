import numpy as np
import matplotlib.pyplot as plt

# Generate the first sequence from 2048 down to 0, decreasing by 64 each step
dataset1_wo = np.arange(1024, -64, -64)

# Generate the second sequence starting from 4096, increasing by 64 each step, with the same length as sequence_1
dataset2_wo = np.arange(1024, 1024 + 64 * len(dataset1_wo), 64)

# Modify sequence_1 to drop to 0 after it reaches 1920
dataset1_w = dataset1_wo.copy()
dataset1_w[dataset1_w <= 768] = 0

# Modify sequence_2 to become 4096 + 2048 after it reaches 4224
dataset2_w = dataset2_wo.copy()
dataset2_w[dataset2_w >= 1280] = 2048

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 14})  # 调整字体大小以确保可读性
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the sequences with custom dash patterns
line1, = plt.plot(dataset1_wo, label='dataset1 w/o dataset adaptive eviction', marker='o', markersize=10, linestyle='-')
line2, = plt.plot(dataset2_wo, label='dataset2 w/o dataset adaptive eviction', marker='o', markersize=10, linestyle='-')
line3, = plt.plot(dataset1_w, label='dataset1 with dataset adaptive eviction', marker='^', markersize=10, linestyle='--')
line4, = plt.plot(dataset2_w, label='dataset2 with dataset adaptive eviction', marker='^', markersize=10, linestyle='--')



# Adding titles and labels
plt.xlabel('Round')
plt.ylabel('Cache Capacity (MB)')
plt.legend()
plt.grid(True)

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色

plt.tight_layout()
plt.savefig('dataset.pdf', facecolor='white', bbox_inches='tight')
# Show the plot
plt.show()
