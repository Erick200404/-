import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 文件路径列表和对应的图例文本
file_paths = {
    "C:\\Users\\12426\\Desktop\\数据科学导论大作业数据\\merged_data_pl1_huaye.xlsx": "花叶",
    "C:\\Users\\12426\\Desktop\\数据科学导论大作业数据\\merged_data_pl2_huacai.xlsx": "花菜",
    "C:\\Users\\12426\\Desktop\\数据科学导论大作业数据\\merged_data_pl3_ssgj.xlsx": "水生根茎",
    "C:\\Users\\12426\\Desktop\\数据科学导论大作业数据\\merged_data_pl4_qie.xlsx": "茄",
    "C:\\Users\\12426\\Desktop\\数据科学导论大作业数据\\merged_data_pl5_lajiao.xlsx": "辣椒",
    "C:\\Users\\12426\\Desktop\\数据科学导论大作业数据\\merged_data_pl6_shiyongjun.xlsx": "食用菌"
}

# 创建一个空的图表
plt.figure(figsize=(10, 6))

# 循环处理每个文件
for file_path, legend_text in file_paths.items():
    # 读取数据
    merged_data = pd.read_excel(file_path)

    # 进行相关的数据处理
    merged_data = merged_data[merged_data['销售类型'] == '销售']
    merged_data.loc[:, '销售日期'] = pd.to_datetime(merged_data['销售日期'])
    merged_data = merged_data.drop(['扫码销售时间'], axis=1)

    # 根据日期对销售数据进行分组，并计算每天的销售总量
    daily_sales = merged_data.groupby('销售日期')['销量(千克)'].sum()

    # 将销售日期设置为数据框的索引
    merged_data.set_index('销售日期', inplace=True)

    # 按照15天为周期重新取样，并计算每个周期内的销售总量
    sales_15_days = merged_data['销量(千克)'].resample('15D').sum()

    # 使用平滑的曲线
    smoothed_sales = daily_sales.rolling(window=7).mean()  # 使用滑动平均来平滑曲线，窗口大小为7

    # 绘制折线图
    plt.plot(smoothed_sales.index, smoothed_sales.values, label=legend_text)

# 设置图表标题和标签
plt.title('Sales Curve')
plt.xlabel('Date')
plt.ylabel('Sales (kg)')
plt.grid(True)

# 添加图例
plt.legend(prop={'family': 'SimHei', 'size': 8})

# 显示图表
plt.show()
