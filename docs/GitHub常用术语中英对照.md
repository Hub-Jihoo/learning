# GitHub 常用术语中英对照

> GitHub 界面目前只提供英文，浏览器翻译又容易把按钮和代码翻乱。
> 这份对照表按使用场景整理高频术语，建议**先认英文，再用中文理解**。
> 中文译名以 GitHub 官方中文文档的用法为主，社区习惯叫法放在括号里。

## 1. 顶部导航与账号

| 英文 | 中文 | 说明 |
| --- | --- | --- |
| Dashboard | 仪表盘 | 登录后的首页，显示动态和常用仓库 |
| Explore | 探索 | 发现热门项目、话题和用户 |
| Notifications | 通知 | Issue、PR、@ 提及等消息 |
| Profile | 个人主页 | 你的公开资料页 |
| Settings | 设置 | 账号、邮箱、SSH、令牌等配置 |
| Appearance | 外观 | 主题（浅色/深色/跟随系统） |
| Star | 星标（收藏） | 给仓库点赞并加入收藏 |
| Watch | 关注（订阅） | 订阅仓库动态通知 |
| Fork | 复刻（派生） | 把别人的仓库复制一份到自己账号下 |
| Following / Followers | 关注 / 粉丝 | 社交关系 |
| Trending | 趋势 | 近期热门项目 |
| Gist | 代码片段 | 轻量级的单文件/多文件分享 |
| Discussions | 讨论 | 仓库内的论坛式讨论区 |
| Marketplace | 应用市场 | GitHub 应用与集成 |
| Copilot | 智能编程助手 | GitHub 的 AI 编程工具 |

## 2. 仓库页面

| 英文 | 中文 | 说明 |
| --- | --- | --- |
| Repository (Repo) | 仓库 | 一个项目的全部文件和历史 |
| Code | 代码 | 文件浏览页 |
| Issues | 议题 | 任务、bug、需求讨论 |
| Pull requests | 拉取请求（PR） | 请求把某个分支合并进目标分支 |
| Actions | 操作 / 工作流 | 自动化构建、测试、部署 |
| Projects | 项目 | 看板式任务管理 |
| Wiki | 维基 | 仓库自带的长文档区 |
| Security | 安全 | 漏洞报告、依赖扫描 |
| Insights | 洞察 | 流量、提交、贡献者统计 |
| Settings | 设置 | 仓库级配置 |
| About | 关于 | 仓库右侧的简介、网址、主题 |
| Releases | 发行版 | 带版本号的发布，可附安装包 |
| Packages | 软件包 | 容器镜像、npm 包等 |
| Contributors | 贡献者 | 提交过代码的人 |
| Languages | 语言构成 | 仓库各语言的代码占比 |
| Topics | 主题标签 | 用于分类和搜索的关键词 |
| Branches | 分支 | 仓库的分支列表 |
| Tags | 标签 | 指向某个提交的固定标记，常用于版本号 |
| Deployments | 部署 | 部署记录 |
| Environments | 环境 | 部署目标环境 |
| README | 自述文件 | 仓库首页展示的说明文档 |
| LICENSE | 许可证 | 规定他人可以如何使用代码 |

## 3. Git 核心概念

| 英文 | 中文 | 说明 |
| --- | --- | --- |
| Working tree | 工作区 | 你正在编辑的文件目录 |
| Staging area / Index | 暂存区 | `git add` 后待提交的改动 |
| Local repository | 本地仓库 | `.git` 目录，保存完整历史 |
| Remote repository | 远程仓库 | GitHub 上的仓库 |
| Commit | 提交 | 一次版本快照，有唯一哈希 |
| Branch | 分支 | 独立的开发线 |
| main / master | 主分支 | 默认分支，通常保持可发布状态 |
| HEAD | 当前提交指针 | 指向你当前所在的位置 |
| origin | 默认远程名 | `git clone` 自动起的名字 |
| upstream | 上游 | 通常指 fork 来源的原始仓库 |
| Tag | 标签 | 给提交起的固定名字，如 `v1.0.0` |
| Clone | 克隆 | 下载仓库及全部历史 |
| Fetch | 获取 | 下载远程更新，但不合并 |
| Pull | 拉取 | 获取并合并远程更新 |
| Push | 推送 | 把本地提交上传到远程 |
| Add | 暂存 | 把改动放入暂存区 |
| Diff | 差异 | 两次改动之间的不同 |
| Merge | 合并 | 把一条分支的历史并入另一条 |
| Fast-forward | 快进合并 | 无需生成合并提交的直接前进 |
| Merge commit | 合并提交 | 同时拥有两个父提交的节点 |
| Rebase | 变基 | 把提交"搬"到另一个基点上，历史更线性 |
| Cherry-pick | 拣选 | 只把某一个提交复制到当前分支 |
| Squash | 压缩 | 把多个提交合并成一个 |
| Stash | 贮藏 | 临时保存未提交的改动 |
| Reset | 重置 | 移动分支指针，可能丢弃提交 |
| Revert | 还原 | 生成一个反向提交来抵消某次改动 |
| Restore | 恢复 | 撤销工作区或暂存区的修改 |
| Checkout | 检出 | 旧版命令，用于切换分支/恢复文件 |
| Switch | 切换 | `checkout` 的分支切换专用新命令 |
| Conflict | 冲突 | 同一处被不同修改，需要手动解决 |
| Detached HEAD | 分离头指针 | 当前不在任何分支上 |
| `.gitignore` | 忽略规则 | 指定不跟踪的文件 |
| `.gitattributes` | 属性规则 | 指定换行符、二进制处理等 |
| Git LFS | 大文件存储 | 管理大文件的扩展 |

## 4. Pull Request 流程

| 英文 | 中文 | 说明 |
| --- | --- | --- |
| Base branch | 目标分支 | 要合并进的分支，通常是 `main` |
| Compare branch | 对比分支 | 你改动的来源分支 |
| Compare & pull request | 比较并创建 PR | 推送分支后 GitHub 显示的入口 |
| Draft pull request | 草稿 PR | 表示还没准备好合并 |
| Review | 审查 | 对代码提出意见 |
| Approve | 批准 | 同意合并 |
| Request changes | 请求修改 | 要求作者修改后才能合并 |
| Comment | 评论 | 只发表意见，不批准也不阻断 |
| Files changed | 文件变更 | PR 的 diff 视图 |
| Conversation | 对话 | PR 的讨论时间线 |
| Checks | 检查 | CI 运行结果 |
| Merge pull request | 合并拉取请求 | 把 PR 合入目标分支 |
| Create a merge commit | 创建合并提交 | 保留分支历史 |
| Squash and merge | 压缩合并 | 把 PR 的所有提交压成一个 |
| Rebase and merge | 变基合并 | 线性历史，不产生合并提交 |
| Merge conflict | 合并冲突 | 需要手动解决 |
| Linked issue | 关联议题 | 通过 `Closes #12` 自动关联 |
| Out-of-date | 已过期 | 目标分支有了新提交，需要更新 PR |
| Checks have passed | 检查通过 | 可以合并 |
| Checks were not successful | 检查未通过 | 需要修复 |
| Delete branch | 删除分支 | 合并后清理来源分支 |

## 5. Issue 与协作

| 英文 | 中文 | 说明 |
| --- | --- | --- |
| Open / Closed | 打开 / 关闭 | 议题状态 |
| Label | 标签 | 如 `bug`、`enhancement`、`good first issue` |
| Assignee | 指派对象 | 负责处理的人 |
| Milestone | 里程碑 | 把一批议题归到某个目标版本 |
| Template | 模板 | 新建 Issue / PR 时的预设格式 |
| Pinned | 置顶 | 固定在议题列表顶部 |
| Lock | 锁定 | 禁止继续评论 |
| Transfer | 转移 | 把议题转到另一个仓库 |
| Close as completed | 标记为已完成关闭 | |
| Close as not planned | 标记为不处理关闭 | |
| Good first issue | 适合新手 | 维护者标记的入门任务 |

## 6. 设置、权限与安全

| 英文 | 中文 | 说明 |
| --- | --- | --- |
| Visibility | 可见性 | Public 公开 / Private 私有 |
| Collaborators | 协作者 | 被邀请共同开发的人 |
| Teams | 团队 | 组织内的成员分组 |
| Branch protection | 分支保护 | 要求 PR、审查、CI 才能合并 |
| Rulesets | 规则集 | 新版的分支/标签保护规则 |
| Webhooks | 网络钩子 | 事件发生时回调外部服务 |
| Deploy keys | 部署密钥 | 只读/读写单个仓库的 SSH 密钥 |
| SSH and GPG keys | SSH 与 GPG 密钥 | 免密推送、提交签名 |
| Personal access tokens | 个人访问令牌 | 代替密码的 API/HTTPS 凭据 |
| Secrets | 密钥 | Actions 中使用的加密变量 |
| Sessions | 会话 | 已登录的设备列表 |
| Emails | 邮箱 | 提交邮箱与隐私设置 |
| Danger Zone | 危险区域 | 改可见性、转移、归档、删除 |
| Archive | 归档 | 设为只读 |
| Transfer ownership | 转移所有权 | 把仓库转给他人或组织 |
| Keep my email addresses private | 保持邮箱私密 | 使用 `noreply` 匿名邮箱 |

## 7. GitHub Actions

| 英文 | 中文 | 说明 |
| --- | --- | --- |
| Workflow | 工作流 | 一个自动化流程，对应一个 YAML 文件 |
| Job | 任务 | 工作流中的一组步骤 |
| Step | 步骤 | 任务中的单条命令或 action |
| Runner | 运行器 | 执行任务的机器 |
| Event / Trigger | 事件 / 触发器 | 如 `push`、`pull_request` |
| Action | 动作 | 可复用的步骤，如 `actions/checkout` |
| Artifact | 制品 | 构建产物，如测试报告、安装包 |
| Matrix | 矩阵 | 用多组参数并行跑任务 |
| Cache | 缓存 | 加速依赖安装 |
| Secret | 密钥 | 加密的环境变量 |
| Status badge | 状态徽章 | README 上显示构建是否通过 |

## 8. 常见提示与报错

| 英文提示 | 中文含义 | 怎么处理 |
| --- | --- | --- |
| `Nothing to commit, working tree clean` | 没有可提交的改动 | 正常，说明工作区干净 |
| `Your branch is ahead of 'origin/main' by 2 commits` | 本地比远程多 2 个提交 | `git push` |
| `Your branch is behind 'origin/main' by 3 commits` | 本地比远程少 3 个提交 | `git pull` |
| `Your branch and 'origin/main' have diverged` | 本地和远程都有对方没有的提交 | `git pull --rebase` 后再推送 |
| `Updates were rejected because the remote contains work that you do not have locally` | 远程有新提交，推送被拒绝 | 先 `git pull --rebase`，再 `git push` |
| `fatal: not a git repository` | 当前目录不是 Git 仓库 | 进入仓库目录，或先 `git init` / `git clone` |
| `fatal: refusing to merge unrelated histories` | 两个仓库历史无关，拒绝合并 | 确认后加 `--allow-unrelated-histories` |
| `CONFLICT (content): Merge conflict in ...` | 文件有合并冲突 | 手动编辑冲突标记后 `git add` + `git commit` |
| `You are in 'detached HEAD' state` | 不在任何分支上 | `git switch main`，或 `git switch -c 新分支` 保住提交 |
| `Permission denied (publickey)` | SSH 公钥未配置或未添加 | 检查 `~/.ssh` 并把公钥加到 GitHub |
| `Authentication failed` | HTTPS 认证失败 | 用 Git Credential Manager 或 PAT，不能用账号密码 |
| `Support for password authentication was removed` | GitHub 已取消密码认证 | 改用 PAT 或 SSH |
| `remote: Repository not found` | 仓库不存在或没有权限 | 检查地址、登录账号和仓库可见性 |
| `The current branch has no upstream branch` | 当前分支没有关联远程分支 | `git push -u origin 分支名` |
| `This branch has conflicts that must be resolved` | PR 有冲突，不能合并 | 在本地解决冲突后推送 |
| `Some checks were not successful` | CI 检查未通过 | 点 Details 查看日志并修复 |
| `This branch is out-of-date with the base branch` | PR 落后于目标分支 | 点 Update branch，或本地合并/变基后推送 |
| `LF will be replaced by CRLF` | 换行符将被转换 | Windows 正常现象，可用 `.gitattributes` 统一 |
| `warning: adding embedded git repository` | 子目录里还有另一个 `.git` | 删除内层 `.git`，或用 submodule |

## 9. 常见缩写

| 缩写 | 全称 | 中文 |
| --- | --- | --- |
| PR | Pull Request | 拉取请求 |
| CI / CD | Continuous Integration / Delivery | 持续集成 / 持续交付 |
| WIP | Work In Progress | 进行中，请勿合并 |
| LGTM | Looks Good To Me | 我看过了，没问题 |
| PTAL | Please Take A Look | 请看一下 |
| RFC | Request For Comments | 征求意见稿 |
| TL;DR | Too Long; Didn't Read | 长话短说 |
| FYI | For Your Information | 供你参考 |
| IMO / IMHO | In My (Humble) Opinion | 依我看 |
| AFAIK | As Far As I Know | 据我所知 |
| TBD | To Be Determined | 待定 |
| EOD | End Of Day | 今天之内 |
| OOO | Out Of Office | 不在工位 / 休假中 |
| SSOT | Single Source Of Truth | 唯一可信来源 |

## 10. 使用建议

1. **先认英文，再记中文**：中文译名只是帮助理解，搜索文档、看报错时英文才是关键词；
2. **不要翻译代码和命令**：`git push`、`pull_request`、`workflow_dispatch` 这些是语法，翻译后反而找不到；
3. **浏览器翻译只用于正文**：建议用双语对照插件，并关闭代码块翻译；
4. **查官方中文文档**：<https://docs.github.com/zh>，术语译名以官方为准；
5. **遇到报错先搜英文原文**：把报错整句复制到搜索引擎，命中率远高于翻译后的中文。

---

> 译名可能因 GitHub 官方更新、浏览器插件不同而略有差异；以英文原词为准。
