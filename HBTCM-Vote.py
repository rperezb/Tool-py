import requests
import time

# vote = requests.post('http://tw.hbtcm.edu.cn/e/enews/index.php')
posturl = 'http://api.hb.kankan.com/talking/view.php?sid=1&1[]=782&act=vote2&tid2=1'
data={
	'submit':'投票'.encode('gb2312'),
	'yzma':'2436'
	'voteid':'3'
}
times = str(int (time.time()))
print(times)
head={
	'Accept':'	text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
	'Connection':'keep-alive',
	'Cookie':'xvsftlastvotetime='+times,
	'Host':'tw.hbtcm.edu.cn',
	'Referer':'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'
}
proxy={
	'http':'http://42.120.22.25:3128'
}
vote = requests.post(url='http://tw.hbtcm.edu.cn/e/enews/index.php',data=data,headers=head,proxies=proxy)
vote.encoding = 'gb2312'
print(vote.text)