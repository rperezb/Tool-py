import os
import random
import time

# 现在所使用的硬件系统和体验
file1 = open('test.txt')
context1 = file1.read()
lists1 = context1.split('\n')
allinfo = []
num1 = len(lists1)
print(num1)
i = 0
while(i<140):
	t = random.randint(0,num1-1)
	allinfo.append(lists1[t])
	i = i + 1

# 对win8的评价
file2 = open('test2.txt')
context2 = file2.read()
lists2 = context2.split('\n')
num2 =len(lists2)
i = 0
while(i<140):
	t = random.randint(0,num2-1)
	allinfo[i]=allinfo[i]+lists2[t]
	i = i + 1

# 对wp的评价
file3 = open('test3.txt')
context3 = file3.read()
lists3 = context3.split('\n')
num3 =len(lists3)
i = 0
while(i<140):
	t = random.randint(0,num3-1)
	allinfo[i]=allinfo[i]+lists3[t]
	i = i + 1

# 参加后续调研
file4 = open('test4.txt')
context4 = file4.read()
lists4 = context4.split('\n')
num4 =len(lists4)
i = 0
while(i<140):
	t = random.randint(0,num4-1)
	allinfo[i]=allinfo[i]+lists4[t]
	i = i + 1

# 最终写入文件
outfile = open( (time.strftime('%m%d-%H-%M',time.localtime(time.time()))+'.txt'),'w')
for i in allinfo:
	outfile.write(i)
	outfile.write('\n')
outfile.close()