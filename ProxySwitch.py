import winreg
#get the registry key
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",0,winreg.KEY_ALL_ACCESS) 
#get the value of proxyenble,it could return a array like that (key value,key type)
isProxyEnable = winreg.QueryValueEx(key,"ProxyEnable")
# to check the status of proxy
if(isProxyEnable[0]):
	#set the value of proxyenable as 0 to disable it
	winreg.SetValueEx(key,"ProxyEnable",0, winreg.REG_DWORD, 0)
	print("Proxy disabled")
else:
	#set the value of proxyenable as 1 to enable input
	winreg.SetValueEx(key,"ProxyEnable",0, winreg.REG_DWORD, 1)
	#set the proxy infomation "ip:port"
	winreg.SetValueEx(key,"ProxyServer",0, winreg.REG_SZ, "127.0.0.1:7777")
	winreg.SetValueEx(key,"ProxyOverride",0, winreg.REG_SZ, "<local>")
	print("Proxy enabled")
input("Press Any Key To Exit")
