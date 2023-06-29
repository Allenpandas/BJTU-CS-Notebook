# Git版本控制使用

## 1.初次使用Git管理项目

MacOS系统使用iTerm或Terminal进入命令行，Windows系统使用git bash或者cmd进入命令提示符。

1.任选一个用于存放项目的文件夹，并进入：

```shell
cd /Users/allenpandas  # 例如：进入了用户的家目录
```

2.在存放项目的文件下，执行以下命令，从gitee.com的仓库克隆项目：

```shell
git clone https://gitee.com/bjtu-theta-lab/KKalgorithm4-1.git
```

期间可能需要输入用户名和密码，输入gitee.com的账号和密码即可。

3.克隆完毕后，进入到该项目中：

```shell
cd KKalgorithm4-1
```

4.以自己的姓名，创建分支：

```shell
~/KKalgorithm4-1$ git branch allenpandas
```

5.创建完分支后切换到刚刚创建的分支中：

```shell
git checkout allenpandas
```

切花分支后，会提示`Switched to branch 'allenpandas'`

6.将本地的内容推送到远程分支

```shell
git push origin allenpandas  # 注意origin后面的allenpandas要与分支名保持一致
```

## 2.N次使用Git管理项目

1.查看发生了变化的文件：

```shell
git status  # 红色代表未提交至暂存区，绿色代表提交到了暂存区未提交到本地仓库
```

2.提交代码到本地暂存区：

```shell
git add .  # .代表所有文件	
```

3.将暂存区的文件提交到本地仓库：

```shell
git commit -m '备注'  # 注意'备注'的位置，需要写清本次提交的内容	
```

4.从远端仓库将最新的代码拉到本地：

```shell
git pull origin allenpandas
```

5.将本地仓库的内容提交到远程仓库：

```shell
git push origin allenpandas 
```

## 3.Git管理涉及到的命令

```shell
git status  # 查看本地状态（是否有文件变动，即：删除、添加、修改等）
git add .  # 添加所有变动的文件到暂存区
git commit -m '备注'  # 从暂存区把变动的文件提交到本地仓库
git pull origin master  # 从远程master分支拉取最新代码到本地分支
git push origin master  # 将本地仓库的代码推到远程master仓库
git branch  # 查看分支
git branch allenpandas  # 创建一个名为allenpandas的分支（大家根据自己的名字创建）
git checkout allenpandas  # 切换到allenpandas分支
git checkout master  # 切换到master分支
git pull origin allenpandas  # 从远程allenpandas分支拉取最新代码到本地分支
git push origin allenpandas  # 将本地仓库的代码推到远程allenpandas仓库
```

 