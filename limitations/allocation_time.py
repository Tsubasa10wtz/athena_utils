import matplotlib.pyplot as plt

# Updated data from the image
dataset1 = {'simple': 5*60+52, 'quiver': 8*60+10, 'fluid': 5*60+52, 'ideal': 5*60+56}
dataset2 = {'simple': 4*60+5, 'quiver': 3*60+33, 'fluid': 4*60+5, 'ideal': 3*60+33}
dataset3 = {'simple': 24*60+43, 'quiver': 25*60+37, 'fluid': 25*60+25, 'ideal': 25*60+37}

# Convert to minutes
dataset1 = {k: v/60 for k, v in dataset1.items()}
dataset2 = {k: v/60 for k, v in dataset2.items()}
dataset3 = {k: v/60 for k, v in dataset3.items()}

# Normalize all datasets by the 'simple' time
simple_time_dataset1 = dataset1['simple']
simple_time_dataset2 = dataset2['simple']
simple_time_dataset3 = dataset3['simple']

dataset1 = {k: v/simple_time_dataset1 for k, v in dataset1.items()}
dataset2 = {k: v/simple_time_dataset2 for k, v in dataset2.items()}
dataset3 = {k: v/simple_time_dataset3 for k, v in dataset3.items()}

# Get lists
simple = [dataset1['simple'], dataset2['simple'], dataset3['simple']]
quiver = [dataset1['quiver'], dataset2['quiver'], dataset3['quiver']]
fluid = [dataset1['fluid'], dataset2['fluid'], dataset3['fluid']]
ideal = [dataset1['ideal'], dataset2['ideal'], dataset3['ideal']]

# Print lists for reference
print("simple (normalized):", simple)
print("quiver (normalized):", quiver)
print("fluid (normalized):", fluid)
print("ideal (normalized):", ideal)

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 30})  # 调整字体大小以确保可读性
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the bar chart
labels = ['Dataset 1', 'Dataset 2', 'Dataset 3']
x = range(len(labels))

width = 0.1

plt.bar(x, simple, width=width, label='Simple', align='center', edgecolor='black')
plt.bar([i + width for i in x], quiver, width=width, label='Quiver', align='center', edgecolor='black')
plt.bar([i + width*2 for i in x], fluid, width=width, label='Fluid', align='center', edgecolor='black')
plt.bar([i + width*3 for i in x], ideal, width=width, label='Ideal', align='center', edgecolor='black')

plt.xlabel('Datasets')
plt.ylabel('Normalized Time')
plt.xticks([i + width*1.5 for i in x], labels)
plt.legend()

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色
plt.tight_layout()
plt.savefig('allocation_time.pdf', facecolor='white', bbox_inches='tight')

plt.show()
