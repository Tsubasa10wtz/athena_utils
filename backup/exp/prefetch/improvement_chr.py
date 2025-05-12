import numpy as np

# 数据
categories = ['All', 'job\u2460', 'job\u2461', 'job\u2462', 'job\u2463', 'job\u2465', 'job\u2467', 'job\u246A']
athena = np.array([95.2, 94.1, 65, 99, 77.3, 96.2, 97.1])
juicefs = np.array([0, 0, 52, 0, 78.1, 16.1, 0])

# 计算各方法的均值
athena_mean = np.mean(athena)
juicefs_mean = np.mean(juicefs)

# 计算Athena相对于JuiceFS的总体平均提升百分比
overall_improvement = (athena_mean - juicefs_mean)

# 打印结果
print(f"Athena相对于JuiceFS的总体平均提升: {overall_improvement:.2f}%")