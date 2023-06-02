
import pyecharts.options as opts
from pyecharts.charts import Bar

goods = ['火箭推力(吨）x10^3', '运载火箭（个）x10', '空间站（个）', '航天升空人数（人）x10', '火星探测任务（个）', '载人航天器(个）','航天经费(美元)x10']
# goods = ['火箭推力', '运载火箭', '空间站', '航天升空人数', '火星探测任务', '载人航天器']
# data1 = ['1.0524', '2.5', '2', '1.3', '1', '13']
# data2 = ['3.408', '13.3', '1', '34.6', '22', '44']
data1 = [1.0524, 2.5, 2, 1.3, 1, 13,2.0]
data2 = [3.408, 13.3, 1, 34.6, 22, 44,19.5]
bar = (
    Bar()
    .add_xaxis(goods)
    .add_yaxis('中国',data1 , stack='stack1')
    .add_yaxis('美国', data2, stack='stack1')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='2021年两国航天竞争力对比-指标'),
                     xaxis_opts=opts.AxisOpts(name='指标',axislabel_opts=opts.LabelOpts(font_size=7)),
                     yaxis_opts=opts.AxisOpts(name='数值'))
)

bar.render('两国航天竞争力对比.html')