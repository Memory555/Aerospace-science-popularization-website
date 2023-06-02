# import numpy as np
# import matplotlib.pyplot as plt
# plt.rcParams["font.family"] = "FangSong"
#
# labels = ['美国','中国','苏联']
# values = np.array([1,2,8])
#
# def func(pct,allvals):
#     absolute = int(pct/100 * np.sum(allvals))
#     return '{:.1f}%\n{:d}'.format(pct,absolute)
#
# def func1(pct):
#     return func(pct, values)
#
# fig = plt.figure()
# sub = fig.add_subplot(111)  # 创建一张图片
# wedges, texts, autotexts = sub.pie(values, labels=labels, colors=[ '#b6a399', '#aa8979', '#cec1b4'],labeldistance=1.2, startangle=90, explode=[0,0.05,0], autopct=func1,
#         textprops=dict(fontsize=12),radius=1,shadow=True,wedgeprops=dict(edgecolor='white',width=0.8))
# # 根据sub.pie(arr)画饼状图,rotatelabels=False是否根据形状旋转标签,startangle第一块饼开始的位置,counterclock=False是否逆序标签
# # 或者autopct= lambda x:fun(x,values),
#
# # 设置标签大小
# for i in range(len(autotexts)):
#     autotexts[i].set_color('w')
#     texts[i].set_size(14)
#     texts[i].set_weight('bold')
#
# # 显示图例
# plt.legend()
# fig.suptitle('中美俄空间站情况', fontsize =16)  # 添加标题
# fig.tight_layout()  # 使得图更加紧凑
# plt.savefig("./中美俄空间站情况")
# plt.show()


# 环形图
from pyecharts import options as opts
from pyecharts.charts import Pie

# labels = ['美国','中国','苏联']
# values = np.array([1,2,8])
def pie_base() -> Pie:
        c = (
        Pie(init_opts=opts.InitOpts(page_title="中美苏空间站占比"))
        .add(
        "pie",
        [("美国共1个", 9.1), ("中国共2个", 18.2),("苏联共8个", 72.7)],
        radius=["40%", "60%"],
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(formatter="{b} ，占比 : {c}%")
        )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="中美苏空间站占比", pos_left="left", pos_top="0%"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="00%", pos_top="20%")
        )
        )
        return c
pie_base().render_notebook()
pie_base().render('中美苏空间站占比.html')
