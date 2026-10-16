# Loova Agent Plugins

版本 2.1.0。10 个英文创作 Skills 与 Loova 正式 MCP 的安装包。以产品整理的英文内容为基础，支持 Claude Code、支持插件功能的 Codex，以及可读取 `SKILL.md` 的其他 Agent。英文指令不限制用户或生成内容的语言。

正式 MCP：`https://mcp.loova.ai/mcp`。安装后需要用自己的 Loova 账号完成 OAuth 授权；插件不包含密钥，不授予额外模型权限或免费额度。

## 一并安装插件与 MCP

需要 Git 和对应客户端。先克隆仓库：

```bash
git clone https://github.com/loovaai/loova-agent-plugins.git
cd loova-agent-plugins
```

Claude Code：

```bash
bash scripts/install.sh claude
```

安装后在 Claude Code 执行 `/mcp`，选择插件提供的 Loova 完成授权，重新开启会话。

支持 `codex plugin add` 的 Codex：

```bash
bash scripts/install.sh codex
```

在客户端的 MCP/插件连接界面完成 Loova 授权，再开启新会话。不同版本的插件授权入口可能不同；不支持插件命令时使用下方独立 Skills 安装方式。

脚本通过客户端原生 marketplace 命令安装，使用当前克隆的本地目录。请保留这个目录。GitHub 发布后也可以直接添加远程市场：

```bash
# Claude Code
claude plugin marketplace add loovaai/loova-agent-plugins
claude plugin install loova@loova-agent-plugins --scope user

# Codex（需支持这些命令的版本）
codex plugin marketplace add loovaai/loova-agent-plugins
codex plugin add loova@loova-agent-plugins
```

选择本地或远程市场其中一种方式即可。已有手动配置的 Loova MCP 时，先选择继续使用独立 Skills 或改用插件连接，避免同时启用两个同用途连接。

## 仅安装 Skills / 通用 Agent

需要 Python 3.9+。明确指定客户端支持的 Skills 目录；未知 Agent 没有统一目录，不自动猜测。

```bash
# Codex 的用户 Skills 目录
python3 scripts/install_skills.py --target "$HOME/.agents/skills" --dry-run
python3 scripts/install_skills.py --target "$HOME/.agents/skills"

# Claude Code 的用户 Skills 目录（与插件安装二选一）
python3 scripts/install_skills.py --target "$HOME/.claude/skills"

# 其他支持 SKILL.md 的 Agent
python3 scripts/install_skills.py --target /absolute/path/to/agent/skills
```

Windows 可使用 `py -3 scripts/install_skills.py --target "指定目录"`。此方式仅复制 Skills，不写入 MCP 配置或登录信息。默认拒绝覆盖，更新时添加 `--update`，旧版本会备份到目标目录的父目录并输出位置。

独立安装时另外配置 MCP。例如 Codex：

```bash
codex mcp add loova --url https://mcp.loova.ai/mcp
codex mcp login loova
```

如果已配置 `loova`，保留现有配置并检查地址，不重复添加。其他客户端按其远程 HTTP MCP + OAuth 配置流程接入。

Claude 网页 Connector 或 ChatGPT 的 MCP 连接不会自动读取电脑中的 Skills；本仓库安装脚本面向本地 Agent，不代表已上架公共插件市场。

## 包含的 Skills

| Skill | 用途 |
|---|---|
| loova-product-photoshoot | 产品棚拍与生活场景图 |
| loova-product-listing-images | 商品主图、卖点和详情套图 |
| loova-ai-image-editor | 局部编辑、背景与风格调整 |
| loova-thumbnail-cover-maker | 封面和缩略图 |
| loova-ad-resizer | 画幅与尺寸适配 |
| loova-product-video-maker | 产品展示视频 |
| loova-ugc-ad-creator | 人物讲解广告 |
| loova-character-swap | 参考视频角色替换方案与生成 |
| loova-mimic-motion | 专用动作模仿工具工作流 |
| loova-viral-video-clone | 广告复刻项目、脚本确认与生成 |

各 Skill 内的 `references/execution.md` 自包含，支持单独复制。创作指引不能保证模型具有精确像素编辑、剪辑或口型能力；运行时以模型目录与工具定义为准。

## 安装后验证

发送：

> 请使用 Loova 查询我的个人资料、Credits 余额和可用模型。只查询，不生成。

之后可以请求：

> 使用 loova-product-photoshoot，将我的产品照片制作成棚拍宣传图。先展示模型、参数与报价，等我确认再生成。

本地素材通过上传会话直传；无法读取文件的客户端使用网页上传链接。动作模仿与广告复刻调用专用工具。Unlimited 按实时资格报价，不自动回退 Credits。重试保留原 UUID 和完整请求。

## 更新与卸载

本地市场先 `git pull --ff-only`，再使用客户端插件管理界面更新 Loova；远程市场使用客户端的市场刷新与插件更新入口。单独 Skills 更新重新运行安装器并加 `--update`。

插件卸载使用客户端插件管理界面。独立 Skills 卸载只移除本次安装的 10 个 `loova-*` 目录（名称见上表），不要删除整个 Skills 目录。卸载文件不等于撤销 OAuth；停止授权可在 Loova 账户 Connected agents 撤销对应连接。

## 维护与验证

```bash
python3 -m unittest discover -s tests -v
bash -n scripts/install.sh
claude plugin validate plugins/loova
```

本包合并产品英文 1.0 与工程插件方案，统一为 2.1.0。`quality/acceptance-cases.json` 是待执行的创作行为验收案例，不是已通过的付费生成测试。发布前检查仓库内容，保持三个插件清单与市场版本一致；更新版本时同步 Skill 元数据及 `catalog.json`。

旧 `loova-viral-video-remake` 已改为 `loova-viral-video-clone`。已手动安装旧名称的用户，应先将旧目录备份到 Skills 搜索目录外，再移除旧安装并安装新名称，避免重复发现。安装器不会自动删除旧名称或用户自定义内容。

## 构建官网下载包

```bash
python3 scripts/build_release.py
```

输出 `dist/loova-creative-skills-2.1.0/` 网站目录与 `dist/loova-creative-skills-2.1.0-deploy.zip`。网站目录包含完整包、10 个独立包、英文目录、文件清单和 SHA256。插件与 ZIP 都从 `plugins/loova/skills` 读取内容，不维护第二套 Skills。

执行约定为支持独立安装而放在每个 Skill 内；修改时同步全部副本，构建会检查一致性。构建拒绝覆盖已有发布目录，重复检查可用 `--output /path/to/empty-output`。官网部署步骤见 [DEPLOYMENT.md](docs/DEPLOYMENT.md)。

格式依据：[OpenAI 插件文档](https://developers.openai.com/plugins/build/plugins)、[Claude Code 插件文档](https://code.claude.com/docs/en/plugins-reference)。本地检查不替代各客户端真实安装和 OAuth 验收。
