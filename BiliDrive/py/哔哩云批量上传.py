import os

path=r'D:\music\inradio'
for i in os.listdir(path):
    print(i)
    a='bdex upload "'+path+'\\' + i +'"'
    #print(a)
    os.system(a)
    
