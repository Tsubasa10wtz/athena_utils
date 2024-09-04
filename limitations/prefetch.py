import matplotlib.pyplot as plt

# Data
file_types = ["Small Files", "One Big File"]
block_level = [28.1, 7.1]
file_level = [5.2, 35.2]
plt.style.use("fivethirtyeight")

plt.rcParams.update({'font.size': 30})  # 调整字体大小以确保可读性

fig, ax = plt.subplots(figsize=(10, 8))
# Creating the bar chart
x = range(len(file_types))
width = 0.25  # Adjust width to make the bars more compact

bars1 = ax.bar(x, block_level, width, label='Block-level prefetching', hatch='//')  # Add hatching
bars2 = ax.bar([i + width for i in x], file_level, width, label='File-level prefetching', hatch='\\')  # Add hatching

# Adding labels and title
ax.set_xlabel('Dataset Types')
ax.set_ylabel('Time(s)')
ax.set_xticks([i + width / 2 for i in x])
ax.set_xticklabels(file_types)
ax.legend()

# Adjusting the xlim to center the bars on the x-axis
ax.set_xlim(-0.5, len(file_types) - 0.5 + width)

ax.set_facecolor('white')
fig.patch.set_facecolor('white')

plt.tight_layout()

# Show the plot
# plt.show()
plt.savefig('prefetch.pdf', facecolor='white', bbox_inches='tight')
