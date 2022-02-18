# git conda 杂记
+ 克隆仓库：git clone <git地址>
+ 初始化仓库：git init   

+ 添加文件到暂存区：git add -A  
+ 把暂存区的文件提交到仓库：git commit -m "提交信息" 
+ 查看提交的历史记录：git log --stat  

+ 工作区回滚：git checkout <filename>  
+ 撤销最后一次提交：git reset HEAD^1  

+ 以当前分支为基础新建分支：git checkout -b <branchname>  
+ 列举所有的分支：git branch  
+ 单纯地切换到某个分支：git checkout <branchname>  
+ 删掉特定的分支：git branch -D <branchname>  
+ 合并分支：git merge <branchname>  
+ 放弃合并 ：git merge --abort  

+ 推送当前分支最新的提交到远程：git push  
+ 拉取远程分支最新的提交到本地：git pull  

+ 不能链接到仓库网站，退出clash才能git pull 和git push 参照一下博客  
  https://blog.csdn.net/weixin_39644536/article/details/107416957
  https://blog.csdn.net/M_Edison/article/details/114186264
+ python语言 vscode集成开发环境 miniconda虚拟环境（提供很多包：标准包，还可以添加第三方库）
+ source  activate 激活（linux下激活环境的命令，与window不同）
+ python 不能画图显示中文的解决方法。
+ conda 官方文件，访问官网教程，写的很简洁明白
+ 库 包 模块 函数的区别
