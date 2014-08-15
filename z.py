import requests
import time
import json

def getUrl():
	posturl = "http://www.amazon.cn/gp/socialmedia/luckydraw/backend/luckydraw.html"
	# ?func=luckydraw&_=1407085834752
	data = {
		'func':'luckydraw',
		'_':str(int(time.time()))
	}
	lucky = requests.post(posturl,data=data,timeout=1)
	return lucky.text

def getJson(text):
	detail = json.loads(text)
	lucky={}
	lucky['content']=detail['content']
	lucky['url']=detail['url']
	lucky['angle']=detail['angle']
	return lucky

print(getJson(getUrl()))