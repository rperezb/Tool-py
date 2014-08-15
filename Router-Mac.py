import requests
from requests.auth import HTTPBasicAuth
'''
适用于tp系列修改mac地址
'''
head={
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.5',
	'Referer':'	http://192.168.0.1/userRpm/MacCloneCfgRpm.htm',
	'Host':'192.168.0.1'
}


data = {
	'defaultMac1':'00-00-00-00-00-02',
	'mac1':'00-00-00-00-00-03',
	'Save':'保 存'.encode('gb2312')
}
router = requests.get('http://192.168.0.1/userRpm/MacCloneCfgRpm.htm',params=data,headers=head,auth=HTTPBasicAuth('admin', 'xgf1994'))
router.encoding='gb2312'
print (router.text)