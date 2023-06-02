# import matplotlib.pyplot as plt
# #import numpy as np
# #x = np.array([2,5,8,10])
# # y = np.array([1,6,12,25])
# # plt.plot(x,y,"ro--")
# # plt.plot(y,"ro--") 此时x为1，2，3......
# # plt.plot(x, 2 * x + 6 , "rp-.", x, 8*x-12, "kp:")
# # plt.show()
# plt.rcParams["font.family"] = "FangSong"
# plt.rcParams["axes.spines.right"] = False #右边的轴线
# plt.rcParams["axes.spines.top"] = False #右边的轴线
# plt.rcParams["axes.unicode_minus"] = False #坐标轴存在负数时
# # plt.rcParams["axes.facecolor"] = "green" #坐标的背景颜色
# fig, ax = plt.subplots()
# x=["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]
# number = [931.00, 805.00, 920.00, 1155.00, 1260.00, 1735.00, 2051.00, 1888.00, 2782.00]
# # lowest = [6, 4, 8, 12,10, 9, 7]
# # plt.ylim(-5,30) #指定坐标范围
# plt.plot(x,number,"rs--", label= "收录篇数")
# # plt.plot(x,lowest,"bo:" , label= "最低气温")
# plt.title("EI收录航空航天科技论文篇数")
# plt.xlabel("年份") #x轴
# plt.ylabel("篇数") #y轴
# plt.legend() # (loc="lower left")  显示图例与位置
# plt.savefig("./EI收录航空航天科技论文篇数")
# plt.show()

# 帕累托图--# 左边纵坐标表示频数,右边纵坐标表示频率.分析线表示累积频率
import random
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
import pandas as pd


# 随机颜色, from faker
def rand_color() -> str:
    return random.choice(
        [
            "#c23531",
            "#2f4554",
            "#61a0a8",
            "#d48265",
            "#749f83",
            "#ca8622",
            "#bda29a",
            "#6e7074",
            "#546570",
            "#c4ccd3",
            "#f05b72",
            "#444693",
            "#726930",
            "#b2d235",
            "#6d8346",
            "#ac6767",
            "#1d953f",
            "#6950a1",
        ]
    )

list=["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]
list=list[::-1]

list1=[931.00, 805.00, 920.00, 1155.00, 1260.00, 1735.00, 2051.00, 1888.00, 2782.00]
list1=list1[::-1]
df_origin = pd.DataFrame(  #创建Pandas库中的一种数据结构，它类似excel
    {'categories': list, 'sales': list1})
print(df_origin)
# 按销量降序排列
df_sorted = df_origin.sort_values(by='sales', ascending=False)
print(df_sorted)

# 折线图x轴
x_line_categories = [*range(10)]
# 折线图y轴--向下累积频率
cum_percent = df_sorted['sales'].cumsum() / df_sorted['sales'].sum() * 100
cum_percent = cum_percent.append(pd.Series([0]))  # 添加起始频率0
cum_percent = cum_percent.sort_values(ascending=True)

print(df_sorted.categories.values.tolist())
print(cum_percent.values.tolist())


def pareto_bar() -> Bar:
    line = (
        Line()
            .add_xaxis(x_line_categories)
            .add_yaxis("累计百分比",
                       cum_percent.values.tolist(),
                       xaxis_index=1,
                       yaxis_index=1,  # 使用次y坐标轴，即bar中的extend_axis
                       label_opts=opts.LabelOpts(is_show=False),
                       is_smooth=True,
                       )
    )

    bar = (
        Bar()
            .add_xaxis(df_sorted.categories.values.tolist())
            .add_yaxis('收录篇数', df_sorted.sales.values.tolist(), category_gap=0)
            # .add_yaxis('总额百分比', cum_percent.values.tolist())
            .extend_axis(xaxis=opts.AxisOpts(is_show=False, position='top'))
            .extend_axis(yaxis=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_inside=True),  # 刻度尺朝内
                                             axislabel_opts=opts.LabelOpts(formatter='{value}%'), position='right'))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True, font_size=14))
            .set_global_opts(title_opts=opts.TitleOpts(title='年份-EI收录航空航天科技论文篇数', subtitle=''),
                             xaxis_opts=opts.AxisOpts(name='年份', type_='category'),
                             yaxis_opts=opts.AxisOpts(
                                 axislabel_opts=opts.LabelOpts(formatter="{value} 篇")
                             )
                             )
    )
    bar.overlap(line)
    return bar


pareto_bar().render('EI收录航空航天科技论文篇数.html')

