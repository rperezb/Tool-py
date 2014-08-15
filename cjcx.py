import requests
import re
import io
import sys
import os

def loginSystem(loginData):
	#获取登陆网址即index.url
	index = requests.post('http://218.197.176.41/')	
	#登陆
	login=requests.post(index.url,data=loginData)
	#获取查分网址
	url = login.url.replace('js_main.aspx','js_cxxs.aspx')
	#返回查分网址
	return url

def getVIEWSTATE(url):
	#打开查分页面
	cx=requests.get(url)
	#获取VIEWSTATE
	respre=re.compile(r'(?<=name="__VIEWSTATE" value=").+?(?=" /)')
	VIEWSTATE=respre.findall(cx.text)
	return VIEWSTATE[0]

def createCjForm(num,VIEWSTATE):
	cxform={
	'btn_cx':'查询学生在校成绩'.encode('gb2312'),
	'txt_xh':num,
	'__VIEWSTATE':VIEWSTATE.encode('gb2312')}
	return cxform

def createXkForm(num,VIEWSTATE):
	cxform={
	'Button1':'查询学生选课情况'.encode('gb2312'),
	'txt_xh':num,
	'__VIEWSTATE':VIEWSTATE.encode('gb2312')}
	return cxform

def query(cxform,url):
	#提交查询
	grade=requests.post(url,data=cxform)
	grade.encoding='gbk'
	# print(grade.text)
	return grade.text

def cleanCj(text):
	reclean=re.compile(r'(?<=datagriditem">)[\s\S]+?(?=</tr>)')
	detail=reclean.findall(text)
	cj=''
	reclean=re.compile(r'(?<=<td>)[\s\S]+?(?=</td>)')
	for u in detail:
		temp=reclean.findall(u)
		for v in temp:
			cj=cj+v+'\\\\'
		cj=cj+'\n'
	return cj

def getName(text):
	reclean=re.compile(r'(?<=datagriditem">)[\s\S]+?(?=</tr>)')
	detail=reclean.findall(text)
	if(len(detail)==0):
		return ''
	reclean=re.compile(r'(?<=<td>)[\s\S]+?(?=</td>)')
	name=reclean.findall(detail[0])
	return name[2]


def main():
	# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, errors = 'replace', line_buffering = True)
	loginData={
	    'TextBox1':'0707004',
	    'TextBox2':'0707004',
	    '__VIEWSTATE':'dDwtMjEzNzcwMzMxNTs7Pukfd32P7NLel8M8VBzmGl8fYnrN',
	    'RadioButtonList1':'教师'.encode('gb2312'),
	    'Button1': ' 登 录 '.encode('gb2312')}
	url=loginSystem(loginData)
	VIEWSTATE=getVIEWSTATE(url)
	main=''
	file_object = open('thefile.txt', 'a+')
	for i in range(20120101001,20129999999):
		form=createXkForm(i,VIEWSTATE)
		text=query(form,url)
		name=getName(text)
		if(name==''):
			continue
		file_object.write(str(i))
		file_object.write('/')
		file_object.write(getName(text))
		file_object.write('\n')



		# outfile = open('test.txt','w',encoding='GBK')
		# outfile.write(getName(text))
		# form=createCjForm(i,VIEWSTATE)
		# text=query(form,url)
		# print(cleanCj(text))
	# print(main.encode().decode('utf8'))


if __name__ == '__main__':
    main()