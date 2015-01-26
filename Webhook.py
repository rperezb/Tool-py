import flask
import hmac
from hashlib import sha1
import os
import time
from ftplib import FTP
from ftplib import error_perm
app = flask.Flask(__name__)

@app.route('/bookapi',methods=['POST'])
def hello_book():
    # data = flask.request.data
    if(verify(flask.request,"iamyours")):
        os.system("cd /home/book/ && git pull origin master")
        os.system("cd /home/book/ && gitbook build --output=./website")
        syncAli()
        return "I've Get Book"
    else:
        return "No"


@app.route('/noteapi',methods=['POST'])
def hello_note():
    if(verify(flask.request,"iamyours")):
        os.system("cd /home/notes/ && git pull origin master")
        os.system("cd /home/notes/ && simiki generate")
        return "I've Get note"
    else:
        return "Error"

def verify(request,key):
    signature = request.headers.get('X_HUB_SIGNATURE')
    data = request.data
    local_signature = hmac.new(key=key.encode(),msg=data,digestmod=sha1)
    if hmac.compare_digest(local_signature.hexdigest(),signature[5:]):
        return True
    else:
        return False
        
def upAll(path,ftp):
    filelist = os.listdir(path)
    templist = ftp.nlst()
    for u in filelist:
        if(u=='.git'):
            continue
        if(os.path.isfile(os.path.join(path,u))):
            if(u in templist):
                if(ftp.size(u)!=os.path.getsize(os.path.join(path,u))):
                    # print('>>>上传文件  '+os.path.join(path,u))
                    ftp.storbinary('STOR '+u,open(os.path.join(path,u),'rb'))
            else:
                # print('>>>上传文件  '+os.path.join(path,u))
                ftp.storbinary('STOR '+u,open(os.path.join(path,u),'rb'))
        if(os.path.isdir(os.path.join(path,u))):
            # print("移动到  "+u)
            if(u not in templist):
                ftp.mkd(u)
            ftp.cwd(u)
            upAll(os.path.join(path,u),ftp)
    # print("移动到  上一层目录") 
    ftp.cwd('../')

def syncAli():
    ali = FTP(host='your_ftp_address', user='your_username', passwd='your_password')
    ali.cwd("htdocs")
    upAll("/home/book/website",ali)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9999,debug=True)

