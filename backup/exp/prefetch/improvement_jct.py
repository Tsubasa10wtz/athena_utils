import numpy as np

# 数据
categories = ['Overall', 'job\u2460', 'job\u2461', 'job\u2462', 'job\u2463','job\u2465', 'job\u2467', 'job\u246A']
athena = np.array([25, 20, 1.2, 9.7, 61, 100, 105])
no = np.array([36, 83, 2.7, 35.2, 87, 584, 379])
stride = np.array([36, 81, 1.8, 35.4, 66, 572, 375])
juicefs = np.array([33, 83, 1.16, 35.1, 63, 545, 361])
context = np.array([35, 82, 2.7, 36.2, 86, 586, 380])

# 归一化计算
no_norm = no / athena
juicefs_norm = juicefs / athena
stride_norm = stride / athena
context_norm = context / athena
athena_norm = athena / athena

# 计算均值
no_mean = np.mean(no_norm)
juicefs_mean = np.mean(juicefs_norm)
stride_mean = np.mean(stride_norm)
context_mean = np.mean(context_norm)
athena_mean = np.mean(athena_norm)

# 插入总体均值到归一化数据的首位
juicefs_norm = np.insert(juicefs_norm, 0, juicefs_mean)
stride_norm = np.insert(stride_norm, 0, stride_mean)
context_norm = np.insert(context_norm, 0, context_mean)
athena_norm = np.insert(athena_norm, 0, athena_mean)
no_norm = np.insert(no_norm, 0, no_mean)

# 计算Athena相对于JuiceFS的总体平均减少
overall_reduction = (juicefs_mean - athena_mean) / juicefs_mean * 100
print(f"Athena相对于JuiceFS的总体平均减少: {overall_reduction:.2f}%")
