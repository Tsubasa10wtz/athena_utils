import pandas as pd

# 加载Excel文件的特定工作表
file_path = '实验结果.xlsx'  # 这里填写你的Excel文件路径
sheet_name = 'Sheet1'  # 指定只处理名为'Sheet1'的工作表
df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)  # 使用header=None来指示没有列名


def convert_to_seconds(time_str):
    if pd.isna(time_str):
        return time_str  # 如果单元格为空，则返回原值
    time_str = str(time_str).strip()  # 确保将任何非字符串值转换为字符串并去除空格
    minutes = 0
    seconds = 0

    # 检查时间字符串是否包含'm'和's'，且'm'位于's'之前
    if 'm' in time_str and 's' in time_str and time_str.index('m') < time_str.index('s'):
        parts = time_str.split('m')
        try:
            minutes = int(parts[0])  # 尝试转换分钟部分为整数
            seconds_part = parts[1].split('s')[0]
            seconds = int(seconds_part)  # 尝试转换秒部分为整数
        except ValueError:
            return time_str  # 如果转换失败，返回原始字符串
    else:
        return time_str  # 如果格式不正确，返回原始字符串

    return minutes * 60 + seconds


# 应用函数到整个DataFrame
df = df.applymap(convert_to_seconds)

# 保存修改后的DataFrame回Excel文件，只更新'Sheet1'
output_file_path = 'modified_excel_file.xlsx'  # 输出文件路径
with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    # 如果原Excel文件中还有其他工作表你也想保留，可以在这里额外读取和写入这些工作表

