import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Sample data for the Gantt chart
mini_batches = range(1, 21)
io_times = [(0, 5), (6, 10), (11, 15), (16, 20), (21, 25), (26, 30), (31, 35), (36, 40), (41, 45), (46, 50)]
# gpu_times = [(1, 2), (7, 8), (13, 14), (19, 20), (25, 26), (31, 32), (37, 38), (43, 44), (49, 50)]
# transform_times = [(2, 3), (8, 9), (14, 15), (20, 21), (26, 27), (32, 33), (38, 39), (44, 45)]

fig, ax = plt.subplots()

# Adding IO tasks to the Gantt chart
for i, (start, end) in enumerate(io_times):
    ax.broken_barh([(start, end - start)], (i - 0.4, 0.8), facecolors='tab:orange')

# # Adding GPU tasks to the Gantt chart
# for i, (start, end) in enumerate(gpu_times):
#     ax.broken_barh([(start, end - start)], (i - 0.4, 0.8), facecolors='tab:orange', hatch='xx')
#
# # Adding TRANSFORM tasks to the Gantt chart
# for i, (start, end) in enumerate(transform_times):
#     ax.broken_barh([(start, end - start)], (i - 0.4, 0.8), facecolors='tab:green', hatch='//')

# Setting the y-axis labels
ax.set_yticks(range(len(mini_batches)))
ax.set_yticklabels(mini_batches)

# Setting the labels and title
ax.set_xlabel('Time')
ax.set_ylabel('jobs')
ax.set_title('gantt')

# Adding a legend
io_patch = mpatches.Patch(color='tab:orange', label='job time')
# gpu_patch = mpatches.Patch(facecolor='tab:orange', label='GPU', hatch='xx')
# transform_patch = mpatches.Patch(facecolor='tab:green', label='TRANSFORM', hatch='//')
# plt.legend(handles=[io_patch, gpu_patch, transform_patch], loc='upper left')
plt.legend(handles=[io_patch], loc='upper left')

plt.show()
