# import matplotlib.pyplot as plt
# import matplotlib as mpl
# mpl.rcParams["font.sans-serif"]=["SimHei"]#展示中文字体
# mpl.rcParams["axes.unicode_minus"]=False#处理负刻度值
#
# labels = ["2016", "2015", "2014", "2013","2012"]#每份饼片的文本标签内容
# values = [1909534.60, 1772021.10, 2026147.50,1856286.60,1674417.00]
# colors = ["lightsteelblue","cornflowerblue","royalblue","steelblue","skyblue"]#饼片颜色
# plt.pie(values,
#         labels = labels,
#         explode = [0.2,0.1,0.1,0.1,0.1],#饼片边缘偏离半径的百分比
#         autopct = "%3.2f%%",#数值百分比样式
#         startangle = 60,#第一个饼片逆时针旋转角度
#         colors = colors,
#         pctdistance = 1.1,#百分比数值位置，与半径长度的比例
#         labeldistance = 0.5,#标签值位置，与半径长度的比例
#         shadow = False)#无阴影设置
# plt.axis('equal')#保证画出来的饼图是圆饼图
#
# # plt.show()
#
# colLabels = ["2016", "2015", "2014", "2013","2012"]
# rowLabels = ["航空航天器制造业高技术产业新产品开发经费支出"]
#
# colColours = ["lightsteelblue","cornflowerblue","royalblue","steelblue","skyblue"]
# values=[values]
#
# plt.table(cellText = values,#表格的数值
#           cellLoc = "center",#表格中的数据对齐方式
#           colLabels = colLabels,#表格中每列的列名称
#           colColours = colColours,#表格每列的列名称所在单元格的颜色
#           colWidths = [0.1]*6,#表格每列的宽度
#           rowLabels = rowLabels,#表格每行的行名称
#           rowLoc = "center",#表格每行的行名称对齐方式
#           loc = "bottom")   #表格在画布中的位置
#
# plt.title("航空航天器制造业高技术产业新产品开发经费支出(万元)",loc = "center")
# plt.savefig("./航空航天器制造业高技术产业新产品开发经费支出(万元)")
# plt.show()

from pyecharts.charts import Pie
from pyecharts import options as opts

# 示例数据
cate = ["2016年", "2015年", "2014年", "2013年","2012年"]
data = [1909534.60, 1772021.10, 2026147.50,1856286.60,1674417.00]
pie = (Pie()
.add('', [list(z) for z in zip(cate, data)],
radius=["30%", "75%"],
rosetype="radius")
.set_global_opts(title_opts=opts.TitleOpts(title="航空航天器制造业高技术产业新产品开发经费支出(万元)", subtitle="2012年-2016年", pos_left="left", pos_top="10%"))
.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)

pie.render_notebook()
pie.render('航空航天器制造业高技术产业新产品开发经费支出(万元).html')
