python 使用说明

# 安装
建议使用python与notepad++  
https://www.cnblogs.com/zhcncn/p/3969419.html

python正常安装  
开始时勾选add python to path 即可  

notepad++ 中  
菜单栏-运行-

> cmd /k python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT  

-保存..  
然后你可以设置一个快捷键

安装&设置完毕

# 导出为exe
https://www.cnblogs.com/robinunix/p/8426832.html

0. 安装 pyinstaller
> pip install pyinstaller

1. cmd中运行
> pyinstaller --onefile --nowindowed hello-world.py

2. 输出结果中会有文件在哪个位置的
