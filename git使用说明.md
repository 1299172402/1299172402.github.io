git 使用说明
https://blog.csdn.net/xiongzaiabc/article/details/88616813

git clone + GitHub仓库链接

进入仓库的文件夹

git add .    （注：add后面加个空格，再加个 点号.   ，此操作是把scmor文件夹下面的文件都添加进来）

git commit -m "upload"    （注：“upload”里面换成你需要，如“first commit”，注意双引号“”，这一步理解成提交到本地）

git push -u origin master     （注：此操作目的是把本地仓库push到github上面，此步骤需要你输入帐号和密码）


出现问题的处理办法

> Updates were rejected because the remote contains work that you do not have locally.This is usually caused by another repository pushing to the same ref.

1. git init //初始化仓库

2. git add .(文件name) //添加文件到本地仓库

3. git commit -m "first commit" //添加文件描述信息

4. git remote add origin + 远程仓库地址 //链接远程仓库，创建主分支

5. git pull origin master // 把本地仓库的变化连接到远程仓库主分支

6. git push -u origin master //把本地仓库的文件推送到远程仓库