# Git 与 GitHub 操作指南

> 以本仓库 2026-10-31 的一次真实更新为例，完整走一遍：
> **克隆 → 建分支 → 整理文件 → 提交 → 推送 → 合并**。
> 文末附常用命令速查表和常见问题。

## 0. 这次示范做了什么

| 步骤 | 操作 | 关键命令 |
| --- | --- | --- |
| 1 | 克隆远程仓库 | `git clone` |
| 2 | 检查仓库现状 | `git status`、`git log`、`git branch -a` |
| 3 | 新建功能分支 | `git switch -c feature/python-basics` |
| 4 | 整理并复制文件 | `mkdir`、`cp` |
| 5 | 补充忽略规则 | 编辑 `.gitignore` |
| 6 | 分多次提交 | `git add`、`git commit` |
| 7 | 推送功能分支 | `git push -u origin feature/python-basics` |
| 8 | 合并回主分支 | `git switch main`、`git merge --no-ff` |
| 9 | 推送主分支 | `git push origin main` |

本次产生的提交（按时间顺序）：

```text
chore: 完善 .gitignore，忽略 IDE 配置与临时文件
docs: 重写 README，补充项目说明与内容索引
feat(python-basics): 添加 Python 实验代码与学习笔记
docs: 添加 Git/GitHub 操作指南与 README 写作指南
```

> 为什么要拆成多次提交？因为"一次提交只做一件事"。
> 将来出问题时可以单独回滚某一次，代码审查时也更容易看懂。

## 1. 先理解四个区域

Git 的工作流可以概括为四层：

```text
工作区（你编辑的文件）
   │  git add
   ▼
暂存区（本次准备提交的改动）
   │  git commit
   ▼
本地仓库（.git 目录，保存历史）
   │  git push
   ▼
远程仓库（GitHub）
```

对应关系：

- **工作区**：你在文件管理器 / 编辑器里看到的目录；
- **暂存区**：用 `git add` 把改动"装进箱子"；
- **本地仓库**：`git commit` 把箱子封存成一条历史记录；
- **远程仓库**：`git push` 把本地历史同步到 GitHub。

Git 是版本控制工具，GitHub 是托管 Git 仓库的平台——**没有 GitHub 也能用 Git，但没有 Git 就没有 GitHub 上的提交历史**。

## 2. 一次性准备

### 2.1 安装并检查

```bash
git --version
# git version 2.55.0.windows.5
```

Windows 用户安装 [Git for Windows](https://git-scm.com/download/win) 时会附带 Git Credential Manager，用于保存 GitHub 登录凭据。

### 2.2 配置提交身份

每条提交都会记录作者姓名和邮箱：

```bash
# 全局配置（对这台机器上所有仓库生效）
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

# 查看配置
git config --global --list
```

**多账号场景**：如果同时使用 Gitee、公司仓库等，不要用全局配置覆盖。进入某个仓库后单独设置：

```bash
git config --local user.name "Hub-Jihoo"
git config --local user.email "Hub-Jihoo@users.noreply.github.com"
```

`--local` 只写入当前仓库的 `.git/config`，优先级高于全局配置。

### 2.3 保护隐私：使用 GitHub 匿名邮箱

提交邮箱会公开显示在 GitHub 上。推荐在 **GitHub → Settings → Emails** 中勾选
*Keep my email addresses private*，并使用 GitHub 提供的
`ID+用户名@users.noreply.github.com` 地址作为提交邮箱。

本仓库的本地配置使用：

```bash
git config --local user.name "Hub-Jihoo"
git config --local user.email "Hub-Jihoo@users.noreply.github.com"
```

检查历史提交里有没有泄露邮箱：

```bash
git log --format='%h  %an <%ae>  %s'
```

### 2.4 三种认证方式

| 方式 | 适用场景 | 说明 |
| --- | --- | --- |
| Git Credential Manager | Windows 桌面，最省事 | 首次推送弹出浏览器登录，之后自动记住 |
| Personal Access Token (PAT) | 脚本、CI、临时环境 | GitHub → Settings → Developer settings → Tokens，用 token 代替密码 |
| SSH Key | 长期使用、多台机器 | 生成密钥后把公钥添加到 GitHub |

> ⚠️ 2021 年 8 月起，GitHub 已不支持用**账号密码**通过 HTTPS 推送。
> 如果提示 `Authentication failed`，请改用上述三种方式之一。
>
> ⚠️ 永远不要把 token 写进仓库文件、URL 或提交历史。泄露后立即到 GitHub 撤销。

## 3. 克隆仓库

```bash
git clone https://github.com/Hub-Jihoo/learning.git
cd learning
```

克隆会做三件事：下载全部历史、创建本地 `main` 分支、把远程地址记为 `origin`。

```bash
git remote -v
# origin  https://github.com/Hub-Jihoo/learning.git (fetch)
# origin  https://github.com/Hub-Jihoo/learning.git (push)
```

## 4. 动手前先看现状

养成"改代码前先看状态"的习惯：

```bash
git status            # 工作区 / 暂存区状态
git log --oneline --graph --all --decorate   # 提交历史与分支关系
git branch -a         # 本地 + 远程分支
```

本次检查发现：

- 远程有 `main` 和 `dev` 两个分支；
- `main` 上已有 3 次提交，工作区干净；
- 仓库只有 `README.md`（内容仅一行标题）、`test.py` 和 `.gitignore`。

## 5. 新建分支再开发

```bash
git switch -c feature/python-basics
# 等价旧写法：git checkout -b feature/python-basics
```

`switch -c` 表示"创建并切换到新分支"。

**为什么不直接在 main 上改？**

- `main` 应始终保持可运行、可展示的状态；
- 功能分支上的改动可以随时丢弃，不影响主线；
- 推送分支后可以在 GitHub 上发起 Pull Request，方便 review。

常见的分支命名：

```text
feature/xxx    新功能
fix/xxx        修 bug
docs/xxx       文档更新
refactor/xxx   重构
```

## 6. 整理文件

本次把 `pywork` 目录中的学习材料整理进仓库：

```bash
mkdir -p python-basics/notes python-basics/practice docs
cp "源目录/实验1.py" python-basics/
cp "源目录/新建 文本文档.txt" "python-basics/notes/Python-增删查改速查.md"
cp "源目录/a=100.txt" python-basics/practice/
```

整理时做了几个判断：

1. **重命名**：`新建 文本文档.txt` 改成 `Python-增删查改速查.md`，文件名要能说明内容；
2. **分类**：代码、笔记、练习片段分别放进不同子目录；
3. **隐私**：实验报告 `.doc` / `.docx` 含学号、姓名，**不上传**；
4. **不提交空文件**：源目录里的空 `test.py`、`实验4.py` 没有内容，直接跳过。

### 6.1 关于 `.gitignore`

`.gitignore` 告诉 Git"这些文件永远不要跟踪"。本次补充了：

```gitignore
# JetBrains IDE (PyCharm / IntelliJ IDEA) 的本地配置，不应提交到仓库
.idea/
*.iml

# VS Code 本地配置
.vscode/

# 操作系统生成的杂项文件
.DS_Store
Thumbs.db
desktop.ini

# Office 临时锁文件
~$*.doc
~$*.docx
```

注意事项：

- `.gitignore` **只对未跟踪文件生效**。如果文件已经被提交过，需要先执行：
  ```bash
  git rm --cached -r .idea
  git commit -m "chore: 移除已跟踪的 IDE 配置"
  ```
- 检查某个文件为什么被忽略：
  ```bash
  git check-ignore -v 路径
  ```
- 已经提交进历史的大文件/敏感文件，仅删除文件还不够，历史里仍然存在（见第 12 节）。

## 7. 查看改动

```bash
git status -s          # 简洁状态：?? 未跟踪，M 已修改，A 已暂存
git diff               # 工作区 vs 暂存区
git diff --stat        # 只看统计
```

## 8. 暂存与提交

```bash
# 按文件或目录暂存
git add .gitignore
git add README.md
git add python-basics/

# 确认暂存内容（提交前最后一道检查）
git diff --cached

# 提交
git commit -m "feat(python-basics): 添加 Python 实验代码与学习笔记"
```

### 8.1 提交信息怎么写

推荐 **Conventional Commits** 约定：

```text
<类型>(<范围>): <简短说明>

<可选正文：为什么改、改了什么、影响范围>
```

常用类型：

| 类型 | 含义 |
| --- | --- |
| `feat` | 新功能 / 新内容 |
| `fix` | 修复错误 |
| `docs` | 只改文档 |
| `style` | 格式调整，不影响逻辑 |
| `refactor` | 重构，不改变行为 |
| `test` | 测试相关 |
| `chore` | 构建、依赖、配置等杂项 |

好例子：

```text
feat(python-basics): 添加实验一输入输出示例
fix: 修正列表切片越界的问题
docs: 补充 README 的快速开始章节
```

反例：

```text
update          # 更新了什么？
fix bug         # 什么 bug？
asdf            # 无意义
```

原则：**标题用祈使句、不超过 50 字符、不以句号结尾；正文解释"为什么"而不是"做了什么"**（做了什么看 diff 就知道）。

## 9. 推送到 GitHub

```bash
git push -u origin feature/python-basics
```

- `-u`（`--set-upstream`）把本地分支和远程分支关联，之后直接 `git push` 即可；
- 首次推送可能弹出浏览器登录（Git Credential Manager）；
- 成功后 GitHub 仓库页面会出现 "Compare & pull request" 提示。

如果推送被拒绝（`rejected`），通常是因为远程有你本地没有的提交：

```bash
git pull --rebase origin main   # 先同步再提交
```

## 10. 合并回 main

### 方式 A：本地合并（本次采用）

```bash
git switch main
git pull origin main                           # 确保 main 是最新的
git merge --no-ff feature/python-basics        # 保留分支信息，生成合并提交
git push origin main
```

`--no-ff` 表示即使可以快进也强制生成一个合并提交，历史里能清楚看到"这个功能是从哪个分支合进来的"。

### 方式 B：Pull Request（团队协作推荐）

1. 推送功能分支后，打开仓库页面，点击 **Compare & pull request**；
2. base 选 `main`，compare 选 `feature/python-basics`；
3. 填写标题和描述，说明改了什么、为什么改；
4. 等待 review / CI 检查通过；
5. 点击 **Merge pull request**；
6. 点击 **Delete branch** 删除已合并的远程分支。

PR 的好处：有讨论记录、有 CI 结果、可以要求他人审核、可以配置分支保护规则。

### 合并后清理分支

```bash
git branch -d feature/python-basics              # 删除本地分支
git push origin --delete feature/python-basics   # 删除远程分支（如已推送）
```

## 11. 常用命令速查

| 目的 | 命令 |
| --- | --- |
| 查看状态 | `git status -s` |
| 查看历史 | `git log --oneline --graph --all` |
| 查看远程 | `git remote -v` |
| 克隆 | `git clone <url>` |
| 新建并切换分支 | `git switch -c <branch>` |
| 切换分支 | `git switch <branch>` |
| 拉取更新 | `git pull --rebase` |
| 暂存全部 | `git add .` |
| 暂存指定文件 | `git add <file>` |
| 提交 | `git commit -m "..."` |
| 修改上一次提交信息 | `git commit --amend` |
| 推送 | `git push` |
| 首次推送并关联 | `git push -u origin <branch>` |
| 合并分支 | `git merge --no-ff <branch>` |
| 删除本地分支 | `git branch -d <branch>` |
| 撤销工作区修改 | `git restore <file>` |
| 取消暂存 | `git restore --staged <file>` |
| 查看某文件历史 | `git log -p -- <file>` |
| 查看谁改了某行 | `git blame <file>` |

## 12. 常见问题

### 12.1 中文文件名显示成八进制转义

```bash
git config --global core.quotepath false
```

### 12.2 Windows 换行符警告

Windows 使用 CRLF，Linux/macOS 使用 LF。推荐：

```bash
git config --global core.autocrlf true
```

更严谨的做法是在仓库根目录添加 `.gitattributes`：

```gitattributes
* text=auto
*.py text eol=lf
*.docx binary
*.doc binary
```

### 12.3 大文件

- GitHub 单文件硬限制 **100 MB**，超过 50 MB 会警告；
- 视频、数据集、大压缩包不要直接提交，使用 [Git LFS](https://git-lfs.com/)；
- 已经提交的大文件需要重写历史才能彻底移除。

### 12.4 误提交了敏感文件

仅 `git rm` 只能删除"当前版本"，历史记录里仍然可以找回。需要：

```bash
# 安装 git-filter-repo 后
git filter-repo --path 敏感文件路径 --invert-paths
git push --force
```

> ⚠️ 重写历史会改变所有提交的哈希，影响所有协作者。
> 如果文件已经公开，**立即更换泄露的密码 / token** 才是第一优先级。

### 12.5 提交信息写错了

```bash
# 只改最近一次、且尚未推送
git commit --amend -m "新的提交信息"
```

### 12.6 本地有改动，但想先拉取远程

```bash
git stash          # 暂存未提交的改动
git pull --rebase
git stash pop      # 恢复改动
```

### 12.7 detached HEAD

通常是不小心 `git checkout <commit-hash>` 导致的。查看分支：

```bash
git switch main
```

如果在该状态下做了提交，先建分支保住它：

```bash
git switch -c rescue-branch
```

## 13. 进阶路线

学完基础工作流后，可以按这个顺序继续：

1. **Issues**：用 issue 记录任务和 bug，提交信息里写 `Closes #12` 可自动关闭；
2. **Pull Request**：从 Fork 仓库向原仓库贡献代码；
3. **GitHub Actions**：提交时自动运行测试、检查代码格式；
4. **GitHub Pages**：把仓库里的静态页面发布成网站；
5. **Releases / Tags**：给稳定版本打标签，如 `git tag v1.0.0 && git push --tags`；
6. **分支保护规则**：要求 PR、要求 review、要求 CI 通过才能合并到 main；
7. **.gitattributes / .editorconfig**：统一换行符、编码和缩进风格。

## 14. 本次操作命令汇总

```bash
# 1. 克隆
git clone https://github.com/Hub-Jihoo/learning.git
cd learning

# 2. 检查
git status
git log --oneline --graph --all
git branch -a

# 3. 建分支
git switch -c feature/python-basics

# 4. 整理文件（示例）
mkdir -p python-basics/notes python-basics/practice docs
cp "源目录/实验1.py" python-basics/
cp "源目录/新建 文本文档.txt" "python-basics/notes/Python-增删查改速查.md"

# 5. 设置匿名提交身份
git config --local user.name "Hub-Jihoo"
git config --local user.email "Hub-Jihoo@users.noreply.github.com"

# 6. 分次提交
git add .gitignore
git commit -m "chore: 完善 .gitignore，忽略 IDE 配置与临时文件"

git add README.md
git commit -m "docs: 重写 README，补充项目说明与内容索引"

git add python-basics/
git commit -m "feat(python-basics): 添加 Python 实验代码与学习笔记"

git add docs/
git commit -m "docs: 添加 Git/GitHub 操作指南与 README 写作指南"

# 7. 推送功能分支
git push -u origin feature/python-basics

# 8. 合并回 main
git switch main
git pull origin main
git merge --no-ff feature/python-basics
git push origin main

# 9. 清理
git branch -d feature/python-basics
git push origin --delete feature/python-basics
```

---

**一句话总结**：`add` 挑改动，`commit` 存快照，`push` 上云端，`branch` 隔离风险，`merge` / PR 汇入主线。
