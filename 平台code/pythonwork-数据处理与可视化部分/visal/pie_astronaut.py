# import matplotlib.pyplot as plt
# plt.rcParams["font.family"] = "FangSong"
# # 分离某一块explode= explode
# # explodes = [0.2,0,0.3,0,0,0.1]
# x = [8, 8, 7, 7, 7, 6, 6, 6, 5]
# labels= ["2019", "2018", "2017","2016", "2015", "2014", "2012","2011","2010"]
# plt.pie(x,labels = labels, labeldistance=1.1,
#         colors=['#b1bdb4', '#aeb6bb','#a0afb9', '#808f99','#5d6c77', '#b0bdc6', '#97a8b5','#7b8d9a', '#667d8e'],autopct="%.2f%%",radius=1,shadow=True)
# plt.title("航天航空工程企业单位数（个）")
# # 显示图例
# plt.legend(loc='upper left')
# plt.savefig("./航天航空工程企业单位数")
# plt.show()

import pyecharts.options as opts
from pyecharts.charts import Bar
# 条形图
x_vals1 = ["2019", "2018", "2017","2016", "2015", "2014", "2012","2011","2010"]

y_vals = [8, 8, 7, 7, 7, 6, 6, 6, 5]
bar = Bar().add_xaxis(x_vals1)
bar.add_yaxis('中国', y_vals,
              markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='average'),
                                                opts.MarkPointItem(type_='max'),
                                                opts.MarkPointItem(type_='min')],
                                                symbol_size=80),itemstyle_opts = opts.ItemStyleOpts(color="#be9997")
              )
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='right'))
bar.set_global_opts(title_opts=opts.TitleOpts(title='年份-航天航空工程企业单位数（个）'))
bar.reversal_axis() #翻转XY轴，将柱状图转换为条形图
bar.render('航天航空工程企业单位数.html')

