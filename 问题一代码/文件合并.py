import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis
'''
#读取数据
df_1 = pd.read_excel("E:\数据科学\\2023年秋数据科学导论大作业数据\附件3_项目三数据集\附件1.xlsx")
df_2 = pd.read_excel("E:\数据科学\\2023年秋数据科学导论大作业数据\附件3_项目三数据集\附件2.xlsx")
df_3 = pd.read_excel("E:\数据科学\\2023年秋数据科学导论大作业数据\附件3_项目三数据集\附件3.xlsx")
df_4 = pd.read_excel("E:\数据科学\\2023年秋数据科学导论大作业数据\附件3_项目三数据集\附件4.xlsx",sheet_name='Sheet1' )

#检验数据是否导入
print(df_1.head())
print(df_2.head())
print(df_3.head())
print(df_4.head())


# 合并两个文件
merged_data = pd.merge(df_2, df_1, how='left', on='单品编码')

merged_data_123 = pd.merge(merged_data, df_3, how='left', on=['销售日期', '单品编码'])

merged_data_1234 = pd.merge(merged_data_123, df_4, how='left', on=['单品编码', '单品名称'])

# 打印结果
print(merged_data_1234.head())

# 输出文件
#merged_data_123.to_excel('E:\\数据科学\\2023年秋数据科学导论大作业数据\\附件3_项目三数据集\\merged_data_123.xlsx', index=False)

merged_data_1234.to_excel('E:\\数据科学\\2023年秋数据科学导论大作业数据\\附件3_项目三数据集\\merged_data_1234.xlsx', index=False)
'''
if __name__ == '__main__':

    df = pd.read_excel("E:\数据科学\\2023年秋数据科学导论大作业数据\附件3_项目三数据集\merged_data_1234.xlsx")

    # 分类
    merged_data_pl1_huaye = df[df['分类编码'] == 1011010101]
    merged_data_pl2_huacai = df[df['分类编码'] == 1011010201]
    merged_data_pl3_ssgj = df[df['分类编码'] == 1011010402]
    merged_data_pl4_qie = df[df['分类编码'] == 1011010501]
    merged_data_pl5_lajiao = df[df['分类编码'] == 1011010504]
    merged_data_pl6_shiyongjun = df[df['分类编码'] == 1011010801]

    # 检查正确性
    print(merged_data_pl1_huaye.head())
    print(merged_data_pl2_huacai.head())
    print(merged_data_pl3_ssgj.head())
    print(merged_data_pl4_qie.head())
    print(merged_data_pl5_lajiao.head())
    print(merged_data_pl6_shiyongjun.head())


    # 输出文件
    merged_data_pl1_huaye.to_excel('E:\\数据科学\\2023年秋数据科学导论大作业数据\\附件3_项目三数据集\\merged_data_pl1_huaye_1234.xlsx', index=False)
    merged_data_pl2_huacai.to_excel('E:\\数据科学\\2023年秋数据科学导论大作业数据\\附件3_项目三数据集\\merged_data_pl2_huacai_1234.xlsx', index=False)
    merged_data_pl3_ssgj.to_excel('E:\\数据科学\\2023年秋数据科学导论大作业数据\\附件3_项目三数据集\\merged_data_pl3_ssgj_1234.xlsx', index=False)
    merged_data_pl4_qie.to_excel('E:\\数据科学\\2023年秋数据科学导论大作业数据\\附件3_项目三数据集\\merged_data_pl4_qie_1234.xlsx', index=False)
    merged_data_pl5_lajiao.to_excel('E:\\数据科学\\2023年秋数据科学导论大作业数据\\附件3_项目三数据集\\merged_data_pl5_lajiao_1234.xlsx', index=False)
    merged_data_pl6_shiyongjun.to_excel('E:\\数据科学\\2023年秋数据科学导论大作业数据\\附件3_项目三数据集\\merged_data_pl6_shiyongjun-1234.xlsx', index=False)

