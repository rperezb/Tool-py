import socket

def getIp(domain):
	try:
		myaddr = socket.getaddrinfo(domain,'http')[0][4][0]
		return myaddr
	except Exception:
		pass

def readDomain(filename):
	try:
		infile = open(filename)
	except IOError:
		print("Error")
		exit()
	file_content = infile.read()
	infile.close()
	domains = file_content.split("\n")
	return domains

def main():
	filename = "abab.com"
	domains = readDomain(filename)
	for u in domains:
		if(getIp(u)):
			print(u)

main()