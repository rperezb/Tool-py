import socket
# ports = []
# for i in range(3380,3400):
#     sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sk.settimeout(1)
#     try:
#         sk.connect(('192.168.18.*',i))
#     except Exception:
#         print i, len(ports)
#         continue
#     sk.close()
# #    sk.__init__()
   
#     ports.append(i)
#     print i, len(ports), '*'
#     i += 1
# 125.221.95.
# print ports

# sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sk.settimeout(20)
# for x in range(30,254):
#     print (ip,end='\t')
#     try:
#         sk.connect(ip,80)
#         print("OK!!!")
#     except Exception:
#         print("fail!")
#         continue
#     # sk.close()
# input()

def Scan(IpAddr,port): 
    # if len(port)<1: 
    #     port=3389#默认端口 
    s=socket.socket()
    #超时时间为0.5秒
    s.settimeout(0.5)
    # print(IpAddr,end='\t') 
    # for p in range(253,2,-1): 
    #     addr=IpAddr+"."+str(p) 
    try:
        s.connect((IpAddr,port)) 
        print(IpAddr,end='\t')
        print("ok!") 
        #连接上为ok
    except socket.error: 
        # print("fail!")
        #否则为fail
        pass 


for x in range(1,255):
    ip = '192.168.1.' +str(x)
    Scan(ip,80) 