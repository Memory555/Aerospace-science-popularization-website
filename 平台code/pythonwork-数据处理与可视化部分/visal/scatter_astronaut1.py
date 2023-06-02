# pyecharts-0.5.5
from pyecharts import EffectScatter

v2 = [1,1,2,1,1,1,1,1,1,1,2]
v1 = [1999, 2001, 2002, 2003, 2005,2008, 2011, 2012, 2013,2016, 2021]
es = EffectScatter("中国神舟（SZ）载人航天器的历史飞行")
es.add("effectScatter",
       v1,
       v2,
       symbol_size=10,
       effect_scale=3.5,
       effect_period=3,
       is_more_utils=True,
       xaxis_max=2021,
       xaxis_min=1999,

       )
es.render('./中国神舟（SZ）载人航天器的历史飞行情况.html')


# import matplotlib.pyplot as plt
# import numpy as np
# plt.rcParams["font.family"] = "FangSong"
# y = (1,1,2,1,1,1,1,1,1,1,2)
# x = (1999, 2001, 2002, 2003, 2005,2008, 2011, 2012, 2013,2016, 2021)
# plt.ylim(0,3)
# # plt.ylim(-500,500)
# sizes = np.linspace(30, 300,num=11)
# colors = np.linspace(10,100,num=11)
# plt.scatter(x,y,s=sizes, c=colors,marker="+", cmap=plt.cm.Reds)
# plt.title("中国神舟（SZ）载人航天器的历史飞行")
# plt.savefig("./中国神舟（SZ）载人航天器的历史飞行情况")
# plt.show()
