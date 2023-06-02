# 读取csv文件
# import pandas as pd
# import csv
# import openpyxl
# # 1. 读取前n行所有数据
# df = pd.read_csv('C:/Users/Memory2641339226/Desktop/Saved Pictures/number.csv' ,'r',encoding= 'ISO-8859-1',error_bad_lines=False)  # 读取xlsx中第一个sheet
# # data1 = df.head(7)  # 读取前7行的所有数据，dataFrame结构
# data2 = df.values  # list形式，读取表格所有数据
# # print("获取到所有的值:\n{0}".format(data1))  # 格式化输出
# print("获取到所有的值:\n{0}".format(data2))  # 格式化输出

# 找出文件的编码方式
datadir = 'C:/Users/Memory2641339226/Desktop/Saved Pictures/UCS-Satellite-Database-9-1-2021.xls'
import chardet
with open(datadir, 'rb') as f:
    result = chardet.detect(f.read())
    print(result['encoding'])

# coding: utf-8
import pandas as pd

# 1. 读取前n行所有数据

# df = pd.read_excel('C:/Users/Memory2641339226/Desktop/Saved Pictures/UCS-Satellite-Database-9-1-2021.xls')  # 读取xlsx中第一个sheet
# data1 = df.head(10)  # 读取前7行的所有数据，dataFrame结构
# data2 = df.values  # list形式，读取表格所有数据
# print("获取到所有的值:\n{0}".format(data1))  # 格式化输出
# print("获取到所有的值:\n{0}".format(data2))  # 格式化输出
# import xlrd
# # 打开excel文件
# book = xlrd.open_workbook(r'C:/Users/Memory2641339226/Desktop/Saved Pictures/UCS-Satellite-Database-9-1-2021.xls')
# sheet2 = book.sheet_by_index(0)  # 通过索引顺序获取
# cols = sheet2.col_values(2) # 获取第2列内容
# print(cols)
# # 写入excel
# from xlwt import *
# book = Workbook()  #新建一个Excel文件
# sheet1 = book.add_sheet("卫星发射数")  # 设置底下sheet1的标签
# al = Alignment()
# # 对齐方式
# al.horz = Alignment.HORZ_CENTER  #设置水平方向
# al.vert = Alignment.VERT_CENTER  #设置垂直方向
# borders = Borders()
# borders.bottom = Borders.THICK  # 边框样式
# style = XFStyle()  # 初始化样式
# style.alignment = al
# style.borders = borders
# row0 = sheet1.row(2)  # 获取表格中第2列
# row1 = sheet1.row(3)  # 获取表格中第3列
# row0.write(0, 'Country/Org of UN Registry', style=style)
# row1.write(1, 'Country of Operator/Owner', style=style)
# book.save(r'C:/Users/Memory2641339226/Desktop/Saved Pictures/卫星数整理后.xls')


