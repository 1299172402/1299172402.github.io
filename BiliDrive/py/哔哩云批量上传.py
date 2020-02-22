import os

path=r'C:\Users\Administrator\AppData\Local\kingsoft\WPS Cloud Files\userdata\qing\filecache\徵羽商的云文档\04 物理\直播课\第二周'
for i in os.listdir(path):
    print(i)
    a='bdex upload "'+path+'\\' + i +'"'
    #print(a)
    os.system(a)



