import xlrd
from xlrd import xldate_as_tuple
from xlutils.copy import copy
from datetime import date,datetime  # 也是用于标准化时间
import datetime
#获取原EXCEL信息
wb_temp=xlrd.open_workbook('C:/Users/Memory2641339226/Desktop/Saved Pictures/UCS-Satellite-Database-9-1-2021.xls') # 打开待复制的表
sheets = wb_temp.sheet_names() # 获取工作簿中的所有工作表名字，形成列表元素
print(sheets)#打印查看一下aa文件中存在的sheet页名字列表
sheet1 = wb_temp.sheet_by_index(0) # 根据索引获取第一个sheet
col2=sheet1.col_values(2)#获取第2列的内容，col为一个list
col3=sheet1.col_values(3)#获取第3列的内容，col为一个list
col4=sheet1.col_values(4)#获取第4列的内容，col为一个list
col5=sheet1.col_values(5)#获取第5列的内容，col为一个list
# col19=sheet1.col_values(19)#获取第19列的内容，col为一个list
k=sheet1.nrows # 获取第一个工作表中已存在的数据的行数
print(k)
# #处理要写入的excel工作簿的信息：
workbook = xlrd.open_workbook('C:/Users/Memory2641339226/Desktop/Saved Pictures/卫星数整理后.xls') # 打开工作簿
new_workbook = copy(workbook) # 将xlrd对象拷贝转化为xlwt对象
new_worksheet = new_workbook.get_sheet(0) # 获取转化后工作簿中的第一个工作表对象
#打印查看一下
print(new_worksheet,new_workbook,new_worksheet.name)
# 写入数据到excel中
for i,content in enumerate(col2):
    new_worksheet.write(i,0,content)#在获得的第一个sheet对象中，第0列，第k行写入content
for i,content in enumerate(col3):
    new_worksheet.write(i,1,content)#在获得的第一个sheet对象中，第1列，第k行写入content
for i,content in enumerate(col4):
    new_worksheet.write(i,2,content)#在获得的第一个sheet对象中，第2列，第k行写入content
for i,content in enumerate(col5):
    new_worksheet.write(i,3,content)#在获得的第一个sheet对象中，第3列，第k行写入content
# for i,content in enumerate(col19):
#     new_worksheet.write(i,4,content)#在获得的第一个sheet对象中，第4列，第k行写入content

col19 = []
wb_temp=xlrd.open_workbook('C:/Users/Memory2641339226/Desktop/Saved Pictures/UCS-Satellite-Database-9-1-2021.xls') # 打开待复制的表
sheet1 = wb_temp.sheet_by_index(0) # 根据索引获取第一个sheet
for i in range(1,sheet1.nrows):  # 一行一行遍历数据，sheet.nrows为excel中数据的总行数
    if sheet1.cell(i,19).value != '':
        aa = xlrd.xldate_as_tuple(sheet1.cell(i,19).value, 0)  #转化为元组形式
        bb = xlrd.xldate.xldate_as_datetime(sheet1.cell(i, 19).value, 1)  # 直接转化为datetime对象
        col19.append(bb.year - 4)
        print(bb.year - 4)
        print(aa)
        print(bb)
    else:
        print("youwenti")
print(col19)
for i, content in enumerate(col19):
    new_worksheet.write(i+1, 4, content)  # 在获得的第一个sheet对象中，第4列，第i行写入content
new_worksheet.write(0,4,'Date of Launch')  # 设置列头


new_workbook.save('C:/Users/Memory2641339226/Desktop/Saved Pictures/卫星数据整理后.xls') # 保存工作簿

