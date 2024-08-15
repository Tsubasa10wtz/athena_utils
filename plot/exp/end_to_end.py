import numpy as np
import matplotlib.pyplot as plt

# 定义时间转换函数
def parse_time_to_seconds(timestr):
    total_seconds = 0
    timestr = timestr.replace('s', '').replace('m', 'm ').replace('h', 'h ')
    parts = timestr.split()
    for part in parts:
        if 'h' in part:
            total_seconds += int(part.replace('h', '')) * 3600
        elif 'm' in part:
            total_seconds += int(part.replace('m', '')) * 60
        elif part.isdigit() or '.' in part:
            total_seconds += float(part)
    return total_seconds

# 提供的时间数据
data = {
    'resnet-imagenet-test': {'athena': '1m38s', 'original': '8m28s', 'quiver': '8m31s'},
    'alex-mitplaces-test': {'athena': '1m45s', 'original': '5m39s', 'quiver': '5m41s'},
    'bookcorpus resnet-imagenet-train': {'athena': '1320s', 'original': '1315s', 'quiver': '1314.53s'},
    'alex-mitplaces-train': {'athena': '1m15s', 'original': '3m01s', 'quiver': '2m38s'},
    'gpt2_loading': {'athena': '58s', 'original': '2m40s', 'quiver': '2m25s'},
    'opt_loading': {'athena': '78.1s', 'original': '83.6s', 'quiver': '82.5s'},
    'audio': {'athena': '25s', 'original': '33s', 'quiver': '33s'},
    'fashion': {'athena': '20s', 'original': '83s', 'quiver': '81s'},
    'india': {'athena': '1.2s', 'original': '1.16s', 'quiver': '1.19s'},
    'spark-1g': {'athena': '42m29s', 'original': '41m48s', 'quiver': '42m41s'},
    'ycsb': {'athena': '1918s', 'original': '2003s', 'quiver': '2034s'}
}

# 转换所有时间为秒
for config, times in data.items():
    for method in times:
        times[method] = parse_time_to_seconds(times[method])

### 步骤2: 绘制图表

# 图表设置
bar_width = 0.25
index = np.arange(len(data))
fig, ax = plt.subplots(figsize=(15, 8))

# 绘制每个配置的三个条形
athena_bars = ax.bar(index - bar_width, [times['athena'] for times in data.values()], bar_width, label='Athena')
original_bars = ax.bar(index, [times['original'] for times in data.values()], bar_width, label='Original')
quiver_bars = ax.bar(index + bar_width, [times['quiver'] for times in data.values()], bar_width, label='Quiver')

# 设置图表标题和标签
ax.set_xlabel('Configuration')
ax.set_ylabel('Time in Seconds')
ax.set_title('Comparison of Execution Times by Configuration and Method')
ax.set_xticks(index)
ax.set_xticklabels(data.keys(), rotation=45, ha="right")
ax.legend()

plt.tight_layout()
plt.show()