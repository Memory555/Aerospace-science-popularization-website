# pyecharts==0.0.5
from pyecharts import Line, Bar, Overlap

attr = [2016, 2015, 2014, 2013,2012,2011]
v1 = [1909534.60, 1772021.10, 2026147.50,1856286.60,1674417.00,1481882.90]
v2 = [746395.1, 688858.2, 643563.1, 592963.2, 538580, 487940.2]
v3 = []
for i in range(6):
    v3.append(v1[i] / (v2[i] * 10000)*100)
    print(v3)

bar = Bar(width=1200, height=600)
bar.add("航空航天器制造业高技术产业新产品开发经费支出(万元）", attr, v1,is_label_show=True)
bar.add("国内生产总值(亿元)", attr, v2, yaxis_formatter=" 单位",is_label_show=True)

line = Line()
line.add("航天投入占比 ", attr, v3, yaxis_formatter=" %")

overlap = Overlap()
# 默认不新增 x y 轴，并且 x y 轴的索引都为 0
overlap.add(bar)
# 新增一个 y 轴，此时 y 轴的数量为 2，第二个 y 轴的索引为 1（索引从 0 开始），所以设置 yaxis_index = 1
# 由于使用的是同一个 x 轴，所以 x 轴部分不用做出改变
overlap.add(line, yaxis_index=1, is_add_yaxis=True)
overlap.render('./经济占值.html')