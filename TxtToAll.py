import os
'''
合并文件
'''
def readfile(filename):
    infile = open(filename)
    return infile.read()

#获取当前路径
homedir = os.getcwd()
file = ''
#列出当前目录下的文件
files=os.listdir(homedir)
for i in range(0,len(files)):
    #判断后缀名
    if(files[i].endswith(".txt")):
        file = file + readfile(files[i]) + '\n'

outfile = open('all.txt','w')
outfile.write(file)
outfile.close()