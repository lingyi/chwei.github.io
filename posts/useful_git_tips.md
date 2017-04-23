## Git常用小技巧

	作者：ZR/859077290@qq.com
	创建：2017.04.09
	更新：2017.04.24

## 目录
	 0. 配置
	 1. 常用命令
	 2. 分支
	 3. 补丁的玩法
	 4. 同步本地分支到远端服务器
	 5. github上保持与upstream同步

接触git几年，仍是新手level，以下笔记备忘，基本涵盖了日常80%的操作。

#### 0 配置
	git config user.name "Sam Zhang" //设置名字，当前项目有效
	git config user.email "samzhang@qq.com" //设置邮箱，当前项目有效
	git config --global user.name "Sam Zhang" //设置名字，全局
	git config --global user.email "samzhang@qq.com"

	//git log/diff中文乱码，
	//一般是LANG变量的问题，如：export LANG=en_US.UTF-8

	//git status 中文乱码
	git config --global core.quotepath false

	//git status/diff彩色高亮
	git config color.ui true
	git config --global color.ui true

	//git log彩色高亮
	
#### 1 常用命令

	git status 查看当前哪些文件修改了，相对于整个工程
	git status . 查看当前哪些文件修改了，相对于当前目录
	
	git add . 讲当前目录内的变更提交到暂存区（含修改、新增、删除）
	git add FILE01 FILE02 将指定文件提交到暂存区	
	git add -A 等效以上两条
	git add -u 仅将修改或删除的文件提交，忽略新文件
	git add --ignore-removal 忽略已经删除文件，提交新增和修改的文件

	git rm --cached FILE01 撤销git add操作

	git branch -b NEW-BRANCH-NAME 新建一个分支，并切换到该分支
	git branch NEW-BRANCH-NAME origin/REMOTE-BRANCH-NAME 新建一个本地分支，并关联远端分支
	git branch -d A-BRANCH-NAME 删除一个分支
	git branch 查看本地所有分支
	git branch -a/-all 查看所有分支

	git remote 查看远端分支（仅显示分支名称）
	git remote -v 查看远端分支，显示详细分支地址

	git push origin :REMOTE-BRANCH-NAME 删除远端分支，危险操作！！！
	

#### 2 分支合并

若新特性开发在NEW-FEATURE-BRANCH,现欲将新特性的代码合并到master分支，则合并操作如下：

	git checkout master //先切换到master分支
	
	git merge NEW-FEATURE-BRANCH

#### 3.补丁

##### 3.1 生成补丁

	git checkout XXX-FEATURE-BRANCH //切换到生成补丁的分支
	
	git diff > XXX-FEATURE.patch //将当前分支所有新修改导出到path文件


使用git diff生成的是兼容性很好的diff文件。另一种生成diff的方法是使用git format-patch命令，除了git diff生成的内容，该命令生成的diff文件还含有提交者、时间、主题等信息，俨然只标准的patch提交格式。对应的应用补丁使用git am命令。

##### 3.2 应用补丁（将补丁合入分支）

	//切换到待打补丁的分支（一般地，如果是同一个repo不同分支，直接使用就merge合并就好了）
	git checkout DST_BRANCH
	git apply XXX-FEATURE.patch

执行完以上命令之后，执行git status查看是否有改动。若以上打patch顺利，执行提交patch到当前分支（这里说的提交本质上也是一个commit）

	git commit -a -m "patch: new features merged." 

#### 4.同步本地分支到远端服务器（比如github.com)

这个过程其实就是讲本地分支同步到远端分支。同时，远端分支在本地有个`别名`。假设本地特性分支为NEW-FEATURE-LOCAL-BRANCH，云端分支名称为NEW-FEATURE-REMOTE-BRANCH，简单同步操作如下几个命令：

	git remote add NEW-FEATURE-REMOTE-BRANCH REMOTE_REPO_URL
	git push origin NEW-FEATURE-LOCAL-BRANCH:NEW-FEATURE-REMOTE-BRANCH
	git push origin :NEW-FEATURE-REMOTE-BRANCH //不写本地分支名称则删除远端分支

	git remote rm NEW-FEATURE-REMOTE-BRANCH //取出远程分支的本地映射

#### 5. github上保持与upstream同步

	这一步主要是将上游master分支合并到自己的master分支，操作步骤如下：

	git remote add upstream <ORIGIN_REPO_URL> //先映射分支信息
	git fetch upstream //将上游master代码下载到本地upstream/master分支
	git checkout master //切换到本地master分支
	git merge upstream/master //这一步就是“同步”了

#### 6.其他
	* 合并日志
	* rebase
	* 合并冲突
	* 常见git workflow
	* 
