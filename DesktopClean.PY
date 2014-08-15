#-------------------------------------------------------------------------------
# Name: Desktop Clean
# Purpose:  整理桌面
#
# Author:      guofan
#
# Created:     27/12/2013
# Copyright:   (c) guofan 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
def main():
    homedir = os.getcwd()
    #显示当前路径
    print(homedir)
    homedir = homedir + '\\'
    #显示当前路径的所有文件
    files=os.listdir(homedir)
    #各类文件要保存的位置
    pic = homedir + 'PicTemp\\'
    doc = homedir + 'DocTemp\\'
    code = homedir + 'CodeTemp\\'

    isPic = ['.jpg','.bmp','.jpeg','.png','.ico']
    isDoc = ['.doc','.docx','xls','xlsx','ppt','pptx','pdf']
    isCode = ['.cpp','.c','.java','.py','.h']
    #遍历整个文件列表
    for u in range(0,len(files)):
        for i in range(0,len(isPic)):
            if(files[u].endswith(isPic[i])):
                os.renames(homedir + files[u],pic + files[u])
                break
        for j in range(0,len(isDoc)):
            if(files[u].endswith(isDoc[j])):
                os.renames(homedir + files[u],doc + files[u])
                break
        for k in range(0,len(isCode)):
            if(files[u].endswith(isCode[k])):
                os.renames(homedir + files[u],code + files[u])
                break


if __name__ == '__main__':
    main()