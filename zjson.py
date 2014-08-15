import time
import json
import requests

def getContent(url,time):
	data = {
		'func':'luckydraw',
		'_':time
	}
	while(True):
		lucky = requests.post(posturl,data=data,timeout=1)
		if(lucky.status_code == 200):
			return lucky.text
		else:
			contiue

def getJson(text):
	detail = json.loads(text)
	lucky={}
	lucky['content']=detail['content']
	lucky['url']=detail['url']
	lucky['angle']=detail['angle']
	return lucky

def 