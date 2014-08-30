import requests

url = "http://sms.xudan123.com/do.aspx"
data = {
	"action":"loginIn",
	"uid":"xgfan",
	"pwd":"xgf1994"
}
t = requests.post(url = url,data = data)
print( t.text)
# print(t.text[t.text.index('|')+1:])
token = t.text[t.text.index('|')+1:]
# print(user)
user = t.text[:5]


data = {
	"action":"cancelSMSRecvAll",
	"uid":user,
	"token":token
}
t = requests.post(url = url,data = data)



flag = 10
while(flag > 0):
	data = {
		"action":"getMobilenum",
		"pid":"13994",
		"uid":user,
		"token":token
	}
	t = requests.post(url = url,data = data)
	# print(t.text)
	mobile = t.text[:11]
	# print(mobile[0:3])
	if(mobile[0:3] in {'130','131','132','155','156','185','186'}):
		print(mobile)
		flag = flag -1
	else:
		data = {
		"action":"addIgnoreList",
		"pid":"13994",
		"mobiles":mobile,
		"uid":user,
		"token":token
		}
		t = requests.post(url = url,data = data)
		# print(t.text)	
		data = {
		"action":"cancelSMSRecv",
		"mobile":mobile,
		"uid":user,
		"token":"token"
		}
		t = requests.post(url = url,data = data)

