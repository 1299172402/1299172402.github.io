
import os
import json

meta_string = lambda url: ("bdex://" + re.findall(r"[a-fA-F0-9]{40}", url)[0]) if re.match(r"^http(s?)://i0.hdslb.com/bfs/album/[a-fA-F0-9]{40}.png$", url) else url

f = open('C:/Users/Administrator/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/BiliDriveEx/history.json',encoding='utf-8')
a=f.read()
f.close()
b=json.loads(a)

p=open(r'C:/Users/Administrator/desktop/bdex.txt','w',encoding='utf-8')

for i in b :
    print(b[i]['filename'],file=p)
    print('bdex://'+b[i]['url'][30:][:40],file=p)

