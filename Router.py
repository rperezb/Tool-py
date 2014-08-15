import requests
from requests.auth import HTTPBasicAuth
import random
'''
快速修改路由器wan口ip
'''

head={
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.5',
	'Referer':'http://192.168.0.1/userRpm/WanStaticIpCfgRpm.htm'
}

#生成随机ip
rIP = '192.168.1.'+str(random.randint(20,70))

data = {
	'dnsserver':'114.114.114.114',
	'dnsserver2':'202.103.44.150',
	'downBandwidth':'0',
	'gateway':'192.168.1.1',
	'ip':rIP,
	'mask':'255.255.255.0',
	'mtu':'1500',
	'netRange':'',
	'upBandwidth':'0',
	'wantype':'1',
	'Save':'保 存'.encode('gb2312')
}
router = requests.get('http://192.168.0.1/userRpm/WanStaticIpCfgRpm.htm',params=data,headers=head,auth=HTTPBasicAuth('admin', 'xgf1994'))
router.encoding='gb2312'
print (router.text)