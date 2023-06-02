
import os
# 目标文件夹的路径
filedirs = r'E:/personal/C language/pythonProject/pythonwork/pachong/Abstract'
filedirss = os.listdir(filedirs)
for filedir in filedirss:
    #获取目标文件的文件名称列表
    print(filedir)
    filenames=os.listdir('E:/personal/C language/pythonProject/pythonwork/pachong/Abstract' + '/' + filedir)
    print(filenames)
    #打开一个新文件，如果没有则创建
    f=open(r'E:/personal/C language/pythonProject/pythonwork/pachong/爬取数据整理后.txt','w+',encoding='utf8')

    #先遍历文件名
    for filename in filenames:
        filepath = 'E:/personal/C language/pythonProject/pythonwork/pachong/Abstract' + '/' + filedir+'/'+filename
        #遍历单个文件，读取行数
        for line in open(filepath,encoding='utf8'):
            f.writelines(line)
        f.write('/n')
    #关闭文件
    f.close()

