import xlrd
import os
import xlwt


def readxls(filename):
    #读取文件
    data = xlrd.open_workbook(filename)
    #打开第一张Sheet
    table = data.sheets()[0]
    #获取每一行
    nrows = table.nrows
    lists = []
    for i in range(nrows):
        #把每一行都放入list中
        lists.append(table.row_values(i))
    #删除表头
    del lists[0]
    return lists

def writexls(data):
    #第三方库可能存在一个bug，当表格超过1000时会出现生成的文件打不开
    #所以在此处分X次来进行写入
    times = int(len(data)/1000)+1
    for i in range(times):
        #新建Excel文件
        w = xlwt.Workbook()
        #添加Sheet
        ws = w.add_sheet('all')
        #添加表头
        ws.write(0,0,'寝室')
        ws.write(0,1,'分数')
        ws.write(0,2,'检查日期')
        #当data超过1000时，就只写入前1000条
        #当data不够1000条时，就写入data所有
        lines = 1000 if 1000<len(data) else len(data)
        for j in range(lines):
            ws.write(j+1,0,data[0][0].replace(" ",""))
            ws.write(j+1,1,data[0][1])
            #可能有时候检查日期有问题，就先放一边
            # ws.write(j+1,2,data[0][2])
            #写入之后就删掉
            del data[0]
        #保存文件
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
