
import os
import json

f = open('C:/Users/Administrator/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/BiliDriveEx/history.json',encoding='utf-8')
a=f.read()
f.close()
b=json.loads(a)

p=open(r'C:/Users/Administrator/desktop/bdex.txt','w',encoding='utf-8')

for i in b :
    print(b[i]['filename'],file=p)
    print('---',file=p)
    print('bdex://'+b[i]['url'][30:][:40],file=p)
    print('```',file=p)
    print(file=p)
    print('```',file=p)
    print(file=p)    
    print(file=p)