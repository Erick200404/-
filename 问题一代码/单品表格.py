import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis  # 导入 kurtosis 函数
import matplotlib.pyplot as plt
merged_data_pl1_huaye=pd.read_excel("E:\\1242694868\FileRecv\merged_data_danpin_0.xlsx")
merged_data_pl2_huacai=pd.read_excel("E:\\1242694868\FileRecv\merged_data_danpin_1.xlsx")
merged_data_pl3_ssgj=pd.read_excel("E:\\1242694868\FileRecv\merged_data_danpin_2.xlsx")
merged_data_pl4_qie=pd.read_excel("E:\\1242694868\FileRecv\merged_data_danpin_3.xlsx")
merged_data_pl5_lajiao=pd.read_excel("E:\\1242694868\FileRecv\merged_data_danpin_4.xlsx")
merged_data_pl6_shiyongjun=pd.read_excel("E:\\1242694868\FileRecv\merged_data_danpin_5.xlsx")
#创建数据框列表
categories = [merged_data_pl1_huaye, merged_data_pl2_huacai, merged_data_pl3_ssgj,
              merged_data_pl4_qie, merged_data_pl5_lajiao, merged_data_pl6_shiyongjun]

# 创建一个空的数据框以存储统计量
statistics_df = pd.DataFrame(columns=['类别', '均值', '中位数', '标准差', '最小值', '最大值', '变异系数', '偏度', '峰度'])

# 循环遍历每个类别
for category_df in categories:
    # 按销售日期分组并计算每天的销售总量
    daily_sales = category_df.groupby('销售日期')['销量(千克)'].sum()

    # 计算统计量
    mean_value = np.mean(daily_sales)
    median_value = np.median(daily_sales)
    std_dev = np.std(daily_sales)
    min_value = np.min(daily_sales)
    max_value = np.max(daily_sales)

    # 变异系数
    coefficient_of_variation = std_dev / mean_value

    # 偏度和峰度
    skewness = skew(daily_sales)
    kurt = kurtosis(daily_sales)

    new_row = pd.DataFrame(
        {'类别': [category_df['单品编码'].iloc[0]], '均值': [mean_value], '中位数': [median_value], '标准差': [std_dev], '最小值': [min_value],
         '最大值': [max_value], '变异系数': [coefficient_of_variation], '偏度': [skewness], '峰度': [kurt]})
    statistics_df = pd.concat([statistics_df, new_row], ignore_index=True)

# 打印统计量数据框
print(statistics_df)
statistics_df.to_excel("C:\\Users\\12426\\Desktop\\第一问表格.xlsx", index=False)
