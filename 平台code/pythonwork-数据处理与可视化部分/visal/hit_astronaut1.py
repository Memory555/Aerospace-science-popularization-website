# # 柱状图
# import random
# import pyecharts.options as opts
# from pyecharts.charts import Bar
# x_vals = ['2017年', '2018年', '2019年', '2020年', '2021年']
# y_vals1= ['29', '31','21','36','39']
# y_vals2= ['18', '39','34','39','48']
# y_vals3= ['20', '20','25','16','19']
#
#
#
# bar = (
#     Bar()
#     .add_xaxis(x_vals)
#     .add_yaxis('美国', y_vals1)
#     .add_yaxis('中国', y_vals2)
#     .add_yaxis('俄罗斯', y_vals3)
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=True, font_size=14),
#                           markline_opts=opts.MarkLineOpts())
#     .set_global_opts(title_opts=opts.TitleOpts(title='轨道发射-数量', subtitle='三个国家'),
#                      xaxis_opts=opts.AxisOpts(name='国家'),
#                      yaxis_opts=opts.AxisOpts(name='单位:个'))
# )
# bar.render('轨道发射数量.html')

import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "FangSong"
nums = ['29', '31','21','36','39']
luqu_nums = ['18', '39','34','39','48']
luqu_num1 = ['20', '20','25','16','19']
x = range(0, len(nums))
x_ticks = ['2017年', '2018年', '2019年', '2020年', '2021年']
plt.xticks(x,x_ticks)
# plt.bar(x, nums, width = 0.4, align = "edge", color = "blue",edgecolor = "white", linewidth = 2, )
# plt.bar(x, luqu_nums)
# plt.bar(x, nums,bottom=luqu_nums)  #覆盖堆叠

plt.bar(x, nums, width=0.2, label="美国",color=['slateblue','darkslateblue','mediumslateblue','mediumpurple','indigo'],alpha=0.6)
plt.bar([i+0.3 for i in x],luqu_nums, width=0.2, label="中国",color=['#d9e5e1','#aeb6bb','#a0afb9','#808f99','#5d6c77'],alpha=0.6)
plt.bar([i+0.6 for i in x],luqu_num1, width=0.2, label="俄罗斯",color=['#e3d4d1','#dbcac2','#d0b0b1','#c8a5a3','#c59390'],alpha=0.6)

plt.title("轨道发射数量")
plt.xlabel("年份")
plt.ylabel("数量/个")
plt.legend()
plt.savefig("./轨道发射数量")
plt.show()
