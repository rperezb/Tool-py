import xlrd

def str2vcfByte(st):
	temp = str(st.encode('utf-8'))
	r = ''
	for u in temp[2:-1]:
		r = r + u
	return r.upper().replace('\\X','=')

def toVCF(firstN,lastN,tel,company,title):
	vcf="BEGIN:VCARD\nVERSION:2.1\n"\
	+"N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:"+str2vcfByte(lastN)+";"+str2vcfByte(firstN)+";;;\n"\
	+"FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:"+str2vcfByte(lastN)+str2vcfByte(firstN)+"\n"\
	+"TEL;CELL:"+tel+"\n"\
	+"ORG;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:"+str2vcfByte(company)+"\n"\
	+"TITLE;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:"+str2vcfByte(title)+"\n"\
	+"END:VCARD\n"
	return vcf


# x = '许'
# s = "=E8=AE=B8"
# s = s.replace('=','\\x')
# print(bytes(s, encoding = "utf8"))
# bs = b''
# for u in s:
	# bs = bs + u
# print(s)
# print(bs)
# prin
# a='许'
# b='郭帆'
# c='杏林工作室'
# d='站长'
# firstN = str2vcfByte(b)
# lastN = str2vcfByte(a)
# company = str2vcfByte(c)
# title = str2vcfByte(d)
# tel = '13297077039'
# print(toVCF(b,a,tel,c,d))

# print(str2Byte(a).replace('\\X','='))
# print(str2Byte(b).replace('\\X','='))
# print(str2Byte(c).replace('\\X','='))
# print(str2Byte(d).replace('\\X','='))

# t = x.encode('utf-8')
# t= str(t)
# for u in t[2:-1]:
# 	print(u,end='')


data = xlrd.open_workbook('cont.xls')
table = data.sheets()[0]
# print(table)
vcf = ""
nrows = table.nrows
for i in range(nrows):
	# print (table.row_values(i)[2][0:1])
	company = table.row_values(i)[0]
	title = table.row_values(i)[1]
	lastN = table.row_values(i)[2][0:1]
	firstN = table.row_values(i)[2][1:]
	tel = table.row_values(i)[3]
	vcf = vcf + toVCF(firstN,lastN,tel,company,title)
print (vcf)