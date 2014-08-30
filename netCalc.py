"""
Title:简易的ip段计算
Author:Guofan Xu
根据ip和子网掩码计算网段
"""

def ip2bip(ip):
	"""
	普通4位ip转换为32位二进制ip
	ex：
	192.168.1.1
	11000000101010000000000100000001
	"""
	num = ip.split('.')
	bIP = ''
	for u in num:
		temp = bin(int(u))[2:]
		while(len(temp)<8):
			temp = '0' + temp
		bIP = bIP + temp
	return bIP

def bip2ip(bip):
	"""
	32位二进制转换为普通4位ip
	ex:11000000101010000000000100000001
	192.168.1.1
	"""
	a = bip[0:8]
	b = bip[8:16]
	c = bip[16:24]
	d = bip[24:32]
	ip = str(int(a,2)) + "." + str(int(b,2)) + "." + str(int(c,2)) + "." + str(int(d,2))
	return ip 

def Segment(ip,mask):
	"""
	根据四位ip和数字掩码计算出所覆盖的网域
	ex:
	192.168.1.45,24
	192.168.1.0,192.168.1.255
	"""
	bIP = ip2bip(ip)
	final = bIP[0:mask]
	start = final
	for u in bIP[mask-32:]:
			final = final +'1'
			start = start +'0'
	return(bip2ip(start),bip2ip(final))

def ipMask2numMask(ipmask):
	"""
	4位ip掩码转换为数字掩码
	"""
	bip = ip2bip(ipmask)
	i = 0
	for u in bip:
		if(u!='0'):
			i = i + 1
	return i

def numMask2ipMask(nummask):
	"""
	数字掩码转换为4位ip掩码
	"""
	u = 0
	i = ''
	while(u < int(nummask)):
		i = i + '1'
		u = u + 1
	while(len(i) < 32):
		i = i + '0'
	ip = bip2ip(i)
	return ip
