import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
categories = ['job1', 'job2', 'job3', 'job4']
series_1 = [2, 3, 4, 5]
series_2 = [3, 4, 1, 2]
series_3 = [1, 2, 3, 4]

# Number of categories
N = len(categories)

# Position of bars on x-axis
ind = np.arange(N)
width = 0.25

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(ind, series_1, width, label='athena')
plt.bar(ind + width, series_2, width, label='juicefs')
plt.bar(ind + 2 * width, series_3, width, label='quiver')

# Adding labels and title
plt.xlabel('workload')
plt.ylabel('ratio')
plt.title('cache hit ratio')
plt.xticks(ind + width, categories)

# Adding legend
plt.legend()

# Display the athena
plt.show()