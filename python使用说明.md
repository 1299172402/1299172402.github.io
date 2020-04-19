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

# 安装request库

> pip install requests

# pip镜像源（清华大学）
https://mirrors.tuna.tsinghua.edu.cn/help/pypi/  
pypi 镜像使用帮助  
pypi 镜像每 5 分钟同步一次。  

1.临时使用
> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package  

注意，simple 不能少, 是 https 而不是 http

2.设为默认  
升级 pip 到最新的版本 (>=10.0.0) 后进行配置：

> pip install pip -U  
> pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple  

如果您到 pip 默认源的网络连接较差，临时使用本镜像站来升级 pip：

> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U

# 导出为exe
https://www.cnblogs.com/robinunix/p/8426832.html

0. 安装 pyinstaller
> pip install pyinstaller

1. cmd中运行
> pyinstaller --onefile --nowindowed hello.py

2. 输出结果中会有文件在哪个位置的
