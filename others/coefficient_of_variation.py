import numpy as np

def calculate_cv(arr):
    # 计算相邻项差的绝对值
    diffs = np.abs(np.diff(arr))
    # 计算均值和标准差
    mean_diff = np.mean(diffs)
    std_diff = np.std(diffs)
    # 计算变异系数
    cv = std_diff / mean_diff
    return cv

# # 生成0-100范围内均匀分布的列表
# list_0_100 = np.linspace(0, 99, num=100)
#
# # 生成0-1000范围内均匀分布的列表
# list_0_1000 = np.linspace(0, 999, num=1000)

# 生成0-100范围内随机均匀分布的列表
list_0_100 = np.random.uniform(0, 100, 1000)

# 生成0-1000范围内随机均匀分布的列表
list_0_1000 = np.random.uniform(0, 1000, 1000)

# 生成0-100范围内包含局部热点的列表
list_hotspot = np.random.uniform(0, 100, 100)
# 在随机位置添加局部热点
hotspot_indices = np.random.choice(len(list_hotspot), size=10, replace=False)
list_hotspot[hotspot_indices] += np.random.uniform(100, 200, size=10)

# 计算变异系数
cv_0_100 = calculate_cv(list_0_100)
cv_0_1000 = calculate_cv(list_0_1000)
cv_hotspot = calculate_cv(list_hotspot)

print("0-100范围内均匀分布的list:", list_0_100)
print("0-100范围内变异系数:", cv_0_100)

print("\n0-1000范围内均匀分布的list:", list_0_1000)
print("0-1000范围内变异系数:", cv_0_1000)

print("\n包含局部热点的list:", list_hotspot)
print("包含局部热点的变异系数:", cv_hotspot)
