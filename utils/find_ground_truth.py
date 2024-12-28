import pandas as pd

# 读取两个CSV文件
query_df = pd.read_csv("/Users/wangtianze/Downloads/opendata_join_query.csv")  # 替换为你的查询表文件名
ground_truth_df = pd.read_csv("/Users/wangtianze/Downloads/opendata_join_ground_truth.csv")  # 替换为你的真值表文件名

# 合并两个表，根据 query_table 和 query_column 找到匹配的 candidate_table
merged_df = query_df.merge(
    ground_truth_df,
    how="left",  # 左连接，保留 query_df 的所有行
    on=["query_table", "query_column"]  # 依据这两列进行匹配
)

# 将相同的 query_table 和 query_column 的匹配 candidate_table 聚合为数组
grouped_df = (
    merged_df.groupby(["query_table", "query_column"])["candidate_table"]
    .apply(lambda x: list(x.dropna()))  # 聚合为数组，移除 NaN 值
    .reset_index()
)

# 保存结果到新文件
grouped_df.to_csv("opendata_join_result_grouped.csv", index=False, encoding="utf-8")

print("文件已保存为 opendata_join_result_grouped.csv")