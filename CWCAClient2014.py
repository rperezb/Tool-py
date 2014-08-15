import httplib2
import re
import os
import time

global UserID,UniversityID,CityID
UserID='13020602'#大使ID
UniversityID='163'#大学ID
CityID='2'#城市ID

def sendSurvey(xmlinfo):
    """
    传入xml正文，发送出去，如果提交成功则返回1，其他返回0
    """
    server=httplib2.Http()
    #设置头消息
    headers={'Content-Type': 'application/soap+xml; charset=utf-8',\
    'SOAPAction': '"http://tempuri.org/updateQuestionnaire"' ,\
    'Host': '211.100.47.85' ,\
    'User-agent':"XuGuofan's Python Client"}
    #xml提交地址
    surveyUrl="http://211.100.47.85/Question/SurveyWebService.asmx"
    #提交过程，返回回应和正文
    resp, content = server.request(surveyUrl, "POST", body=xmlinfo, headers=headers)
    print(content.decode())
    #获取状态提示
    respre=re.compile(r'(?<=updateQuestionnaireResult>).+?(?=</updateQuestionnaireResult>)')
    #从byte转换为string
    rsp=respre.findall(content.decode())
    if(len(rsp)):
        #返回成功
        if(rsp[0]=='success'):
            print('上传问卷成功')
            return 1
        elif(rsp[0]=='exist'):
            print('该问卷已存在')
            return 0
        else:
            print('上传问卷错误')
    #无任何返回
    else:
        print("未知错误！")
        return 0

def getUploadCounts(xmlinfo):
    """
    传入xml正文，发送出去
    """
    server=httplib2.Http()
    #设置头消息
    headers={'Content-Type': 'text/xml; charset=utf-8',\
    'SOAPAction': '"http://tempuri.org/getUploadCounts"' ,\
    'User-agent':"XuGuofan's Python Client"}
    #xml提交地址
    surveyUrl="http://211.100.47.85/Question/SurveyWebService.asmx"
    #提交过程，返回回应和正文
    resp, content = server.request(surveyUrl, "POST", body=xmlinfo, headers=headers)
    respre=re.compile(r'(?<=Result>).+?(?=</getUpload)')
    resp=respre.findall(content.decode())
    num=resp[0].split(",")
    # print(resp)
    myup=int(num[1])
    ourup=int(num[0])
    print("您已上传{}份调查问卷，还需上传{}份问卷".format(myup,138-myup))
    print("小组上传{}份调查问卷，还需上传{}份问卷".format(ourup,550-ourup))

def convert(str):
    """
    为了便于输入，各选项之间用/分开，多选用*分开
    这样是为了更好的利用小键盘输入
    """
    str=str.replace("/","\t")
    str=str.replace("*",",")
    return str;

def readSurvey(filename):
    """
    传入文件名，读取内容，返回一个二维的list
    代表每张问卷的每个答案
    """
    #读取文件内容
    try:
        infile=open(filename)
    except IOError:
        print ("错误: 无法读取文件！")
        input('任意键退出!')
        exit() 
    file_content=infile.read()
    infile.close()
    #将内容转换完成
    file_content=convert(file_content)
    #每一行都成为一个Survey
    Survey=file_content.split("\n")
    #先确定一个list
    SurveyDetial=[]
    #将每一行的内容再次转换为一个list
    for u in Survey:
        SurveyDetial.append(u.split("\t"))
    #返回的为list，各下标对应各个不同的调查对象
    #可以理解为二维数组
    return SurveyDetial

def createUpdateXML(Detial):
    """
    传入一个list，要求其各下标对应各调查题的选项
    返回一个正常的xml，byte型的吧
    """
    xmlhead='<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"><soap12:Body>'\
    +'<updateQuestionnaire xmlns="http://tempuri.org/">'\
    +'<UserID>'+UserID+'</UserID>'\
    +'<UniversityID>'+UniversityID+'</UniversityID>'\
    +'<CityID>'+CityID+'</CityID>'
    xmlsurvey="<SurveyName>"+Detial[0]+"</SurveyName>"\
    +"<SurveyEmail>"+Detial[1]+"</SurveyEmail>"\
    +"<NowUseDevice>"+Detial[2]+"</NowUseDevice>"\
    +"<NowUseOtherDevice></NowUseOtherDevice>"\
    +"<NowUseSys>"+Detial[3]+"</NowUseSys>"\
    +"<Characters>"+Detial[6]+"</Characters>"\
    +"<BeforeNominateWin8>"+Detial[7]+"</BeforeNominateWin8>"\
    +"<AfterNominateWin8>"+Detial[8]+"</AfterNominateWin8>"\
    +"<BeforeWin8IsCreative>"+Detial[9]+"</BeforeWin8IsCreative>"\
    +"<AfterWin8IsCreative>"+Detial[10]+"</AfterWin8IsCreative>"\
    +"<BeforeWin8InOurLife>"+Detial[11]+"</BeforeWin8InOurLife>"\
    +"<AfterWin8InOurLife>"+Detial[12]+"</AfterWin8InOurLife>"\
    +"<BeforeSelectPlatform>"+Detial[13]+"</BeforeSelectPlatform>"\
    +"<AfterSelectPlatform>"+Detial[14]+"</AfterSelectPlatform>"\
    +"<BeforeSelectPad>"+Detial[15]+"</BeforeSelectPad>"\
    +"<AfterSelectPad>"+Detial[16]+"</AfterSelectPad>"\
    +"<BeforeImpression></BeforeImpression>"\
    +"<AfterImpression></AfterImpression>"\
    +"<BeforeNominateComputer></BeforeNominateComputer>"\
    +"<AfterNominateComputer></AfterNominateComputer>"\
    +"<BeforeNominateWinPhone>"+Detial[17]+"</BeforeNominateWinPhone>"\
    +"<AfterNominateWinPhone>"+Detial[18]+"</AfterNominateWinPhone>"\
    +"<BeforeSelectPhone>"+Detial[19]+"</BeforeSelectPhone>"\
    +"<AfterSelectPhone>"+Detial[20]+"</AfterSelectPhone>"\
    +"<AttendSurvey>"+Detial[21]+"</AttendSurvey>"\
    +"<EndXp>"+Detial[4]+"</EndXp>"\
    +"<WantUpdate>"+Detial[5]+"</WantUpdate>"
    xmllast="</updateQuestionnaire></soap12:Body></soap12:Envelope>"
    return ((xmlhead+xmlsurvey+xmllast).encode())

def createCountsXML(year,month):
    xmlinfo='<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body>\
    <getUploadCounts xmlns="http://tempuri.org/" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">\
    <userid>'+UserID+'</userid>\
    <universityid>'+UniversityID+'</universityid>\
    <year>'+year+'</year>\
    <month>'+month+'</month>\
    </getUploadCounts>\
    </s:Body></s:Envelope>'
    return xmlinfo

def Update():
    count=0
    inputfile=input('请输入文件名:')
    survey=readSurvey(inputfile)
    print('共有{}份调查问卷等待上传！'.format(len(survey)))
    print('问卷汇报：')
    for i in survey:
        print(i)
        # print(createUpdateXML(i))
        count=count+sendSurvey(createUpdateXML(i))
    print('共有{}份调查问卷上传成功！'.format(count))

def Counts():
    localtime=time.localtime(time.time())
    year=time.strftime('%Y',localtime)
    month=time.strftime('%m',localtime)
    getUploadCounts(createCountsXML(year,month))
    print()

def person():
    inputUser=input('请输入大使ID:')
    if(inputUser!=''):
        UserID=inputUser
    inputUni=input('请输入学校ID:')
    if(inputUni!=''):
        UniversityID=inputUni

def main():
    print('微软校园品牌大使调查问卷上传客户端')
    print('1.上传问卷')
    print('2.查询问卷')
    choose=input('请输入选项')

    if(choose=='1'):
        person()
        Update()
    elif(choose=='2'):
        person()
        Counts()
    input('任意键退出')

main()
