import matplotlib.pyplot as plt
import numpy as np

# 示例数据
x = np.array([200, 250, 300, 350, 400, 450, 500])
y1 = np.array([350, 340, 330, 320, 310, 450, 460])
y2 = np.array([330, 325, 320, 315, 400, 420, 430])
y3 = np.array([400, 395, 390, 385, 400, 405, 410])
y4 = np.array([300, 310, 320, 330, 400, 420, 425])

# 绘制折线图
plt.figure(figsize=(8, 5))
plt.plot(x, y1, 's--', label='Method A', color='blue')
plt.plot(x, y2, '^-.', label='Method B', color='orange')
plt.plot(x, y3, 'o-', label='Method C', color='green')
plt.plot(x, y4, 'D-', label='Method D', color='gold')

# 添加误差条
plt.errorbar(x, y1, yerr=10, fmt='s--', color='blue')
plt.errorbar(x, y2, yerr=8, fmt='^-.', color='orange')
plt.errorbar(x, y3, yerr=5, fmt='o-', color='green')
plt.errorbar(x, y4, yerr=7, fmt='D-', color='gold')

# 设置轴标签和标题
plt.xlabel('Per batch sleep time (ms)')
plt.ylabel('Time per batch (ms)')

# 设置自定义图例
plt.legend(title='Test Methods', loc='upper left')

# 显示网格
plt.grid(True)

# 显示图表
plt.show()