import pandas as pd
import matplotlib.pyplot as plt

# Replace with your actual file path
file_path = 'res.txt'

# Reading the data from the text file
df = pd.read_csv(file_path)


# Plotting
plt.figure(figsize=(10, 6))
plt.grid(axis='y', linestyle='--', color='gray', zorder=5)


plt.plot(df['cache_size'], df['LRU'], label='LRU', linewidth=3, zorder=10)
plt.plot(df['cache_size'], df['Uniform'], label='Uniform', linewidth=3, zorder=10)
# plt.plot(df['cache_size'], df['Aggressive'], label='Aggressive', linewidth=3, zorder=10)

# plt.title('Comparison Of Three Eviction Strategies', fontsize=24)
plt.xlabel('Cache Size', fontsize=20)
plt.ylabel('Cache Hit Ratio', fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
# 修改横轴刻度，使其除以1000，并用百分数表示
plt.gca().set_xticklabels(['{:.0%}'.format(x / 1000) for x in plt.gca().get_xticks()])

plt.legend(fontsize=14)
# plt.show()
plt.savefig('eviction.pdf')
