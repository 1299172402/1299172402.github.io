import json
import time

path_json=r'C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\BiliDriveEx\history.json'

f=open(path_json,encoding='utf-8')
a=f.read()
f.close()
b=json.loads(a)

path_md=r'C:/Users/Administrator/desktop/文件地址.md'
p = open(path_md,'w',encoding='utf-8')

def fileSizeMsg(t):
    fileSizeByte = t
    if (fileSizeByte < 1048576): 
        fileSizeMsg = '%.2f' % (fileSizeByte / 1024) + "KB"
    elif (fileSizeByte >= 1048576 and fileSizeByte < 1073741824): 
        fileSizeMsg = '%.2f' % (fileSizeByte / (1024 * 1024)) + "MB"
    elif (fileSizeByte >= 1073741824 and fileSizeByte < 1099511627776): 
        fileSizeMsg = '%.2f' % (fileSizeByte / (1024 * 1024 * 1024)) + "GB"
    else:
        fileSizeMsg = (fileSizeByte / (1024 * 1024 * 1024 * 1024)).toFixed(2) + "TB"
    return fileSizeMsg

for i in b :
    print(b[i]['filename']+'  ',file=p)
    print('---',file=p)
    
    timeStamp = b[i]['time']
    timeArray = time.localtime(timeStamp)
    updateTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(updateTime+'  '+fileSizeMsg(b[i]['size'])+'  ',file=p)

    print('SHA1 ',b[i]['sha1']+'  ',file=p)
    print('bdex://'+b[i]['url'][30:][:40]+'  ',file=p)

    print(file=p)  
    print(file=p)