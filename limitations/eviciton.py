import matplotlib.pyplot as plt

# Data
file_types = ["ResNet50+ImageNet", "Twitter Cluster 035"]
## 25% of dataset size, ImageNet 1/100, twitter first 10w
LRU = [300, 595]
uniform = [201, 750]
plt.style.use("fivethirtyeight")

plt.rcParams.update({'font.size': 30})  # 调整字体大小以确保可读性

fig, ax = plt.subplots(figsize=(10, 8))
# Creating the bar chart
x = range(len(file_types))
width = 0.2  # Adjust width to make the bars more compact

bars1 = ax.bar(x, LRU, width, label='LRU Eviction', hatch='//')  # Add hatching
bars2 = ax.bar([i + width for i in x], uniform, width, label='Uniform Eviction', hatch='\\')  # Add hatching

# Adding labels and title
ax.set_xlabel('Workloads')
ax.set_ylabel('Time(s)')
ax.set_xticks([i + width / 2 for i in x])
ax.set_xticklabels(file_types)
ax.legend()

# Adjusting the xlim to center the bars on the x-axis
ax.set_xlim(-0.25, len(file_types) - 0.75 + width)

ax.set_facecolor('white')
fig.patch.set_facecolor('white')

plt.tight_layout()

# Show the plot
# plt.show()
plt.savefig('eviction.pdf', facecolor='white', bbox_inches='tight')
