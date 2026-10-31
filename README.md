# Learning · 编程学习仓库

> 记录 Python 课程实验代码、学习笔记，以及从零开始实践 Git / GitHub 的过程。

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-2.x-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Hub--Jihoo-181717?style=flat-square&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/status-learning-brightgreen?style=flat-square)

## 📖 项目简介

这是一个用于**学习和练习**的公开仓库，主要包含三类内容：

- **Python 基础练习**：课程实验中的脚本代码与常用数据结构速查笔记；
- **Git / GitHub 实践**：分支、提交、推送、合并的完整操作演示；
- **写作与工程习惯**：README 怎么写、提交信息怎么规范、哪些文件不该提交。

仓库面向初学者，命令和步骤都可以直接复制使用。

> 🔒 仓库中不包含学号、真实姓名、手机号、私人邮箱等个人信息。实验报告等含个人信息的材料不在此仓库中公开。

## 🗂️ 目录结构

```text
learning/
├── README.md                 # 你正在看的文件：项目总览
├── .gitignore                # Git 忽略规则（IDE 配置、缓存、临时文件等）
├── test.py                   # 早期练习脚本
├── docs/
│   ├── Git与GitHub操作指南.md  # 从克隆到合并的完整流程 + 命令速查
│   └── README写作指南.md       # README 结构、Markdown 语法与自查清单
└── python-basics/
    ├── README.md             # 本目录的说明与运行方式
    ├── 实验1.py               # 实验一：输入与 f-string 格式化输出
    ├── notes/
    │   └── Python-增删查改速查.md  # list / dict / set / str / tuple 速查
    └── practice/
        └── a=100.txt         # 变量与 print 的最小示例
```

## 📚 内容索引

| 内容 | 路径 | 说明 |
| --- | --- | --- |
| 实验一代码 | [`python-basics/实验1.py`](python-basics/实验1.py) | 读取学号、姓名等信息并格式化输出 |
| Python 速查笔记 | [`python-basics/notes/Python-增删查改速查.md`](python-basics/notes/Python-增删查改速查.md) | 五种常用数据结构的增删查改方法 |
| 变量练习 | [`python-basics/practice/a=100.txt`](python-basics/practice/a=100.txt) | 赋值与 `print` 的最简示例 |
| Git / GitHub 指南 | [`docs/Git与GitHub操作指南.md`](docs/Git与GitHub操作指南.md) | 克隆 → 分支 → 提交 → 推送 → 合并 |
| README 写作指南 | [`docs/README写作指南.md`](docs/README写作指南.md) | 结构模板、Markdown 语法、自查清单 |
| 早期练习 | [`test.py`](test.py) | 列表遍历与赋值 |

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/Hub-Jihoo/learning.git
cd learning
```

### 2. 运行示例代码

需要 Python 3.9 及以上版本（笔记中用到了 `str.removeprefix()` 等 3.9+ 语法）。

```bash
python python-basics/实验1.py
```

程序会依次提示输入学号、姓名、性别、籍贯，然后格式化输出。仓库里只有代码，没有预置任何真实个人信息。

### 3. 阅读学习文档

建议按以下顺序阅读：

1. [`docs/Git与GitHub操作指南.md`](docs/Git与GitHub操作指南.md) —— 先跑通 Git 的基本工作流；
2. [`docs/README写作指南.md`](docs/README写作指南.md) —— 再学会把项目"讲清楚"；
3. [`python-basics/notes/Python-增删查改速查.md`](python-basics/notes/Python-增删查改速查.md) —— 随时查阅 Python 数据结构用法。

## 🧭 学习进度

- [x] Python 基础语法与输入输出
- [x] 列表、字典、集合、字符串、元组的常用操作
- [x] 完成课程实验 1–5（报告本地保存，未公开）
- [x] Git 基础：clone / add / commit / push
- [x] 分支开发与合并
- [x] 编写规范的 README
- [ ] 通过 Pull Request 完成一次协作
- [ ] 配置 GitHub Actions 自动检查代码
- [ ] 使用 GitHub Pages 搭建个人主页

## 🔐 关于隐私

公开仓库前请确认：

- `.gitignore` 已忽略 `.idea/`、`.vscode/`、Office 临时文件等；
- 不提交含学号、姓名、身份证号、手机号、私人邮箱的文件；
- 提交身份使用 GitHub 提供的匿名邮箱（`*.users.noreply.github.com`）；
- 实验报告、证书等含个人信息的材料建议本地保存，或脱敏后再公开。

## 📝 更新日志

| 日期 | 变更 |
| --- | --- |
| 2026-10-31 | 重写 README；新增 `python-basics/`、`docs/`；补充 `.gitignore`；添加 Git 与 README 写作指南；将历史提交作者统一匿名化 |

## 🤝 贡献与反馈

这是一个个人学习仓库，但欢迎通过 [Issues](https://github.com/Hub-Jihoo/learning/issues) 指出错误或提出建议。

如果你也想练习，可以：

1. Fork 本仓库；
2. 在自己的副本上新建分支修改；
3. 向本仓库发起 Pull Request。

## 📄 许可证

暂未指定开源许可证。在没有许可证的情况下，默认保留所有权利；如需他人复用，建议补充 [MIT](https://choosealicense.com/licenses/mit/) 等许可证文件。
