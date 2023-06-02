import pyecharts.options as opts
from pyecharts.charts import Line
x=['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
y2=[7993,10447,5053,9859,14668,9773,10424,9023,5833,1770,10862,15687,4085,4292]
y1=[6373,2609,-2639,5432,5505,6544,5879,7424,7110,5068,7979,10689,8213,-5004]
line=(
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="美国",y_axis=y1,areastyle_opts=opts.AreaStyleOpts(opacity=0.5),is_smooth=True)
    .add_yaxis(series_name="中国",y_axis=y2,areastyle_opts=opts.AreaStyleOpts(opacity=0.5),is_smooth=True,color='#000')
    .set_global_opts(title_opts=opts.TitleOpts(title="中美经济增值-年份"))
)
line.render_notebook()
line.render('中美经济增值.html')
