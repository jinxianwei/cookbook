## 入门手册

<details>
<summary>下载并配置git keygen</summary>

必要性：http的git 提交有安全隐患，建议使用公私钥非对称加密的方式提交git

步骤：

1. 常提交git的电脑，生成并获取公钥

终端输入

```
ssh-keygen
回车
回车
回车
```

windows生成的公钥的路径

```
C:\Users\bennie.jin\.ssh\id_rsa.pub
```

ubuntu生成的公钥的路径

```
~/.ssh/id_rsa.pub
```

windows上用记事本打开，ubuntu上用`cat ~/.ssh/id_rsa.pub`输出到终端，将其复制，并粘贴到github或公司私有git上，下图为github

- 点击个人头像中的setting

![image](https://github.com/jinxianwei/CloudImg/assets/81373517/633bf770-a595-4ed2-8997-df222f2589f6)

- 点击SSH and GPG keys

![image](https://github.com/jinxianwei/CloudImg/assets/81373517/24efee82-c8e7-43fc-96cc-384cf3db24f3)

- 点击 New SSH key, 并将上文中的公钥粘到Key中，title可省略，点击Add SSH key就🆗了

![image](https://github.com/jinxianwei/CloudImg/assets/81373517/475cb8dd-dd20-48c2-b1f8-132b00d9f726)

![image](https://github.com/jinxianwei/CloudImg/assets/81373517/41cf0f30-7ab3-4c9e-9b86-03bbf1c3d838)

2. 将仓库clone到本地（注意点击SSH，粘SSH下的git链接）

```
git clone git@github.com:jinxianwei/cookbook.git
```

3. 习惯用pre-commit规范代码格式

需要安装pre-commit,并准备.pre-commit-config.yaml文件(在项目根目录下，是隐藏文件。可以修改复用)

- 安装pre-commit

```
pip install -U pre-commit
pip install flake8
pip install yapf
```

- 将本项目下的`.pre-commit-config.yaml`文件粘贴到自己的项目跟目录下

- 在项目的根目录下执行,并生成如下提示就🆗了

```
pre-commit install
```

![image](https://github.com/jinxianwei/CloudImg/assets/81373517/f4710373-5ca6-4b07-a2cd-38717a14ddfb)

4. 修改并提交commit

- `git status`查看修改的状态

红色表示未跟踪

![image](https://github.com/jinxianwei/CloudImg/assets/81373517/b95e2d07-f0b0-42b7-a142-3714eda77a71)

- `git add *`添加所有文件，也可以指定某些文件添加

vscode中可以选择git图标，点击➕，指定要添加的文件

![image](https://github.com/jinxianwei/CloudImg/assets/81373517/83dc1a25-bd03-4ae7-9e6c-3d356400a8ce)

- `git commit -m "[Doc]: update .md"`提交相应修改，`-m`为提交的注释信息，会显示在gitgraph中，像这样(Git Graph为vscode中的一个插件，可在插件库下载安装)

![image](https://github.com/jinxianwei/CloudImg/assets/81373517/05d52e4b-6137-4443-89c2-f94c0ad68cbe)

开源社区履行这样的commit注释开发规范，清爽并便于查看 https://github.com/open-mmlab/mmsegmentation/pulls

![image](https://github.com/jinxianwei/CloudImg/assets/81373517/d94f5ccd-b788-4bb3-9446-df5b965a192a)

`-m []`中常见的标记如下：

`[Feature]`项目添加了新特性，如新的功能函数，例如`git commit -m [Feature] add bdd100K datasets `

`[Fix]`解决了特定的bug，例如`[Fix] Albumentations default key mapping mismatch `

`[Docs]`文档相关内容，例如`[Doc] Repair invalid link of potsdam and vaihingen `

`[Enhance]`代码增强，对现有代码的扩充和增强，例如`[Enhancement] Support input gt seg map is not 2D `

`[WIP]`Work in progress，正在实现相关功能，例如`[WIP][Feature] Support MMEval mean IoU metric.`

`[Project]`一整个项目，一个论文的完整复现可以标记这样的commit，包含相关的config、模型代码文件和对应的readme，整理在一个文件夹下，一并提交，例如`[Project] add Refuge2 dataset project in dev-1.x `

- git commit 后会出现如下情况

这是因为git commit命令触发了pre-commit钩子，执行了代码检查的逻辑，可以发现，有些检查自动略过，因为没有改动相关类型的文件，有些检查通过了，有些失败了，此时pre-commit会自动修改它能修改的，比如不合适的空格，不规范的行距，不规范的import顺序，不规范的行字符数量等

![image](https://github.com/jinxianwei/CloudImg/assets/81373517/273ac345-19d3-4cfd-b2ce-9d1860da92e7)

- 修改完成后，需要重新走一下`git add `和`git commit `的流程，直至完全所有的precommit信息都显示skipped或passed

- 拉取并push到远端

- - 查看本地和远程分支`git branch -a`

`*`标为本地所处的分支，红色为远程分支，绿色和白色为本地分支

![image](https://github.com/jinxianwei/CloudImg/assets/81373517/286983f8-6769-454e-b08b-7e9ff56d168c)

- - 拉取对应的远程分支`git pull origin main`
- - push到对应的远端`git push origin main`

</details>
