import matplotlib.pyplot as plt
import numpy as np

# Generate some data
categories = ['Time', 'Volume']  # Categories (fixed typo from "Volumn" to "Volume")
wo = [9.77, int(17114550451/1024/1024)]  # Data for the first method
w = [9.77, int(81820198/1024/1024)]  # Data for the second method

x = np.arange(len(categories))  # Position array for the x-axis
width = 0.15  # Width of the bars

plt.style.use("fivethirtyeight")

fig, ax1 = plt.subplots(figsize=(10,8))

# Plot the first values for both methods (using left y-axis)
bars1 = ax1.bar(x[0] + width, wo[0], width, label='w/o adaptive prefetching', edgecolor='black')
bars2 = ax1.bar(x[0] + width * 2, w[0], width, label='with adaptive prefetching', edgecolor='black')
ax1.set_xlabel('Metrics')
ax1.set_ylabel('Time (s)', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Disable grid lines for ax1 (left y-axis)
# ax1.grid(False)

# Create the right y-axis
ax2 = ax1.twinx()

ax2.set_yscale('log')
# Plot the second values for both methods (using right y-axis)
bars3 = ax2.bar(x[1] - width * 2, wo[1], width, label='w/o adaptive prefetching', edgecolor='black')
bars4 = ax2.bar(x[1] - width, w[1], width, label='with adaptive prefetching', edgecolor='black')
ax2.set_ylabel('Prefetch volume (MB)', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Disable grid lines for ax2 (right y-axis)
ax2.grid(False)



# Adjust x-axis ticks position to align with the bars
tick_positions = [x[0]+width*3/2, x[1]-width*3/2]
ax1.set_xticks(tick_positions)
ax1.set_xticklabels(categories)

# Combine legends
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
# We can use `set` to avoid duplicate entries in the legend
by_label = dict(zip(labels1 + labels2, handles1 + handles2))
ax1.legend(by_label.values(), by_label.keys(), loc='upper left')

ax1.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色

# plt.title('Comparison of Methods (wo and w)')
plt.tight_layout()
plt.savefig('./adaptive_prefetching.pdf', facecolor='white', bbox_inches='tight')
plt.show()
