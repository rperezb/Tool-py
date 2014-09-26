import xlrd
import os
import xlwt


def readxls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    nrows = table.nrows
    lists = []
    for i in range(nrows):
        lists.append(table.row_values(i))
    del lists[0]
    return lists

def writexls(data):
    times = int(len(data)/1000)+1
    for i in range(times):
        w = xlwt.Workbook()
        ws = w.add_sheet('all')
        ws.write(0,0,'寝室')
        ws.write(0,1,'分数')
        ws.write(0,2,'检查日期')
        lines = 1000 if 1000<len(data) else len(data)
        for i in range(lines):
            ws.write(i+1,0,data[0][0].replace(" ",""))
            ws.write(i+1,1,data[0][1])
            ws.write(i+1,2,data[0][2])
            del data[0]
        w.save(str(i+1)+'.xls')
        

# 获取当前路径
homedir = os.getcwd()
#列出当前目录下的文件
files = os.listdir(homedir)
x = []
for i in range(0, len(files)):
    #判断后缀名
    if (files[i].endswith(".xls") or files[i].endswith(".xlsx")):
        x.extend(readxls(files[i]))
writexls(x)
