import requests

def readDomains(filename):
	try:
		infile = open(filename)
	except IOError:
		print("Error")
		exit()
	file_content = infile.read()
	infile.close()
	domains = file_content.split("\n")
	return domains

def getStatus(domain):
	print(domain,end='\t')
	try:
		web = requests.get(domain,timeout=1)
		code = web.status_code
		print(code)
		if(200 == code):
			return True
		else:
			return False
	except Exception:
		pass
def writeTofile(domainList):
	outfile = open( '3366host.txt','w')
	for i in domainList:
		outfile.write("0.0.0.0       ")
		outfile.write(i)
		outfile.write('\n')
	outfile.close()

def main():
	filename = "3366.txt"
	list=[]
	domains = readDomains(filename)
	for u in domains:
		if(getStatus(u)):
			list.append(u)
	# print(list)
	writeTofile(list)

main()