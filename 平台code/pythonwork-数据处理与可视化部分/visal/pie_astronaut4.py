

from pyecharts.charts import Pie
from pyecharts import options as opts

cate = ["美国NASA", "中国CNSA", "欧洲ESA", "俄罗斯Roscosmos","法国CNES",'日本JAXA','德国DLR','意大利ASI','印度ISRO']
data = [210,110,63.7,41.7,31.6,30.6,21.5,18,14.2]
pie = (Pie()
.add('', [list(z) for z in zip(cate, data)],
radius=["30%", "75%"],
rosetype="radius")
.set_global_opts(title_opts=opts.TitleOpts(title="世界各国航天局2020年预算排行占比(亿美元)", subtitle="top9", pos_left="left", pos_top="10%"))
.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)

pie.render_notebook()
pie.render('世界各国航天局2020年预算排行top9占比.html')
