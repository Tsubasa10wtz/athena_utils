import matplotlib.pyplot as plt
import seaborn as sns
import re


def extract_p_values(line):
    """
    从一行中提取 p 值列表。
    """
    # 匹配 np.float64(...) 的数字部分
    matches = re.findall(r"np\.float64\((.*?)\)", line)
    # 转换为浮点数
    return [float(value) for value in matches]


def plot_violin_from_txt(file_path):
    """
    从 txt 文件中读取数据并绘制小提琴图。
    """
    data = {}  # 用于存储每一行的名称和 p 值

    # 读取文件
    with open(file_path, 'r') as f:
        for line in f:
            # 提取名称（例如 "LakeBench_join"）和 p 值
            name = line.split(":")[0].strip()
            p_values = extract_p_values(line)
            data[name] = p_values

    # 创建小提琴图
    plt.figure(figsize=(12, 8))
    sns.violinplot(data=list(data.values()), inner="quartile")

    # 设置 x 轴标签为名称
    plt.xticks(range(len(data.keys())), list(data.keys()), rotation=45, fontsize=12)
    plt.xlabel("Categories", fontsize=14)
    plt.ylabel("P-Values", fontsize=14)
    plt.title("Violin Plot of P-Values", fontsize=16)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# 示例调用
file_path = "data.txt"  # 替换为实际文件路径
plot_violin_from_txt(file_path)