import requests

for i in range(282,320):
	url="http://www.xlstu.com:"+str(i)+"/"
	try:
		# print(url)
		te = requests.post(url=url,timeout=0.5)
		print(i)
	except:
		# print("fail")
		pass