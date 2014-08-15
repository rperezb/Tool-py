import requests
from tkinter import *

print('Scanning')
while(True):
	smzdm = requests.get("http://quan.smzdm.com/content/3891",timeout=2)
	code = smzdm.status_code
	# print('.')
	if(code == 403):
		print('-',end='')
	else:
		print('\nOK!')
		root = Tk()
		Message(root,text = 'hello Message').pack()
		root.mainloop()
		# exit()

