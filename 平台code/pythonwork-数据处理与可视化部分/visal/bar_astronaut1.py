# 先引入我们需要用到的库
from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar

label = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']

usa_kh =[17.3,17.86,18.68 ,18.36,17.65 ,16.98,17.69,18.18,19.33,19.69,20.84,21.41,21.02]
china_kh = [1.3,1.42,2.26,2.69,4.86,5.64,2.73,3.45,4.98,5.44,6.48,11,11]


bar=(
    Bar()
    .add_xaxis(label)
    .add_yaxis('美国',usa_kh)
    .add_yaxis('中国',china_kh)
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(title_opts=opts.TitleOpts(title="中美航天局预算2008-2020（十亿美元）"))
)
bar.render_notebook()
bar.render('中美航天局历年预算.html')
