import os
import json

path_json=r'C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\BiliDriveEx\history.json'

f=open(path_json,encoding='utf-8')
a=f.read()
f.close()
b=json.loads(a)

for i in b:
    a='bdex download bdex://'+b[i]['url'][30:][:40]
    print(a)
    os.system(a)