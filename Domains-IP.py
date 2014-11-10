import socket
import re
'''
从文件里读取域名
批量转换成ip
'''

def getIp(domain):
	'''
	根据域名返回ip
	'''
	try:
		myaddr = socket.getaddrinfo(domain,'http')[0][4][0]
		return myaddr
	except Exception:
		pass

def readDomain(filename):
	#打开读取域名
	try:
		infile = open(filename)
	except IOError:
		print("Error")
		exit()
	file_content = infile.read()
	infile.close()
	#做成列表返回
	domains = file_content.split("\n")
	return domains

def main():
	filename = "domain-ip.txt"
	domains = readDomain(filename)
	for u in domains:
		i = getIp(u)
		if(i):
			print(i)

main()