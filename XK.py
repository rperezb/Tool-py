import requests
import re
'''
未完成
'''


def loginSystem(loginData):
	index = requests.post('http://218.197.176.41/',timeout = 3)	#登陆地址
	login = requests.post(index.url,data=loginData,timeout = 3) #登陆
	refererUrl = login.url
	temp=re.compile(r'(?<=\)/).+') #更换链接正则表达式
	x=temp.findall(refererUrl) #获取网址后缀
	temp=re.compile(r'''(?<=<a href=")[\s\S]+?(?=" target='_blank'>全校性选修课)''') #寻找链接正则表达式
	name=temp.findall(login.text) #在页面内寻找选课的链接
	targetUrl = refererUrl.replace(x[0],name[0]) #替换后缀获取选课地址
	return(refererUrl,targetUrl) #登录后的地址

def loginXKsystem(refererUrl,targetUrl):
	head = {'Referer':refererUrl} #伪造来源
	xkindex = requests.post(targetUrl,headers=head,timeout = 3) #提交请求
	view = getVIEWSTATE(xkindex.text) #获取viewstate
	#整个查询的表单
	body = {
	'__EVENTTARGET':'',
	'__EVENTARGUMENT':'',
	'__VIEWSTATE':view.encode('gb2312'),
	'ddl_kcxz':'',
	'ddl_ywyl':'有'.encode('gb2312'),
	'ddl_kcgs':'',
	'ddl_sksj':'',
	'ddl_xqbs':'',
	'TextBox1':'',
	'kcmcGrid:_ctl59:xk'.encode('gb2312'):'on',
	'Button1':'  提交  '.encode('gb2312')
	}
	#头信息伪装
	head = {'Referer':xkindex.url}
	ans = requests.post(url = xkindex.url,data = body,headers = head,timeout = 3)
	# print(ans.text)

#获取页面__VIEWSTATE
def getVIEWSTATE(mainText):
	review = re.compile(r'(?<=name="__VIEWSTATE" value=")[\s\S]+?(?=" />)')
	view = review.findall(mainText)
	return view[0]

def main():
	loginData={
		'TextBox1':'20120701066',
		'TextBox2':'940101',
	    '__VIEWSTATE':'dDwtMjEzNzcwMzMxNTs7Pukfd32P7NLel8M8VBzmGl8fYnrN',
	    'RadioButtonList1':'学生'.encode('gb2312'),
	    'Button1': ' 登 录 '.encode('gb2312')}
	i = 1
	while(i):
		print("\n第" + str(i) + "次尝试",end='\t')
		try:
			x,y = loginSystem(loginData)
			loginXKsystem(x,y)
		except :
			print("失败",end='')
		i = i + 1

if __name__ == '__main__':
    main()