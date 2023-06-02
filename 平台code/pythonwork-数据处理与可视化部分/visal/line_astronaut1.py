

# #折线图
# from pyecharts.charts import Line
# attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 =[5, 20, 36, 10, 10, 100]
# v2 =[55, 60, 16, 20, 15, 80]
# line =Line("折线图示例")#初始化图表，添加标题
# line.add("商家A", attr, v1, mark_point=["max",'min'], mark_line=["average"])#加入A商家数据，并指定最大最小值用点标识，平均值用线标识
# line.add("商家B", attr, v2, is_smooth=True, mark_line=["average"],mark_point=["max",'min'])#加入B商家数据，并指定最大最小值用点标识，平均值用线标识，设置平滑
# #line.show_config()
# line.render("line1.html")#输出图形
# #
# # x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
# # y = [27527,35520,45967,51020,60879,75547,85320,95744,104767,110600,112370,123232,138919,143004,147296]

import pyecharts.options as opts
from pyecharts.charts import Line
x=['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
y1=[27527,35520,45967,51020,60879,75547,85320,95744,104767,110600,112370,123232,138919,143004,147296]
y2=[138146,144519,147128,144489,149921,155426,161970,167849,175273,182383,187451,195430,206119,214332,209328]
line=(
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="中国",y_axis=y1, is_smooth=True)
    .add_yaxis(series_name="美国",y_axis=y2, is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="中美GDP(亿美元)--年份"))
)
line.render_notebook()
line.render('中美GDP.html')
