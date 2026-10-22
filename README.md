# Loova Agent Plugins

版本 2.1.4。10 个英文创作 Skills 与 Loova 正式 MCP 的安装包。以产品整理的英文内容为基础，支持 Claude Code、支持插件功能的 Codex，以及可读取 `SKILL.md` 的其他 Agent。英文指令不限制用户或生成内容的语言。

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

所有参考图片、视频和音频须先存入当前环境的 Loova OSS。本地素材通过上传会话直传；外部链接须先取得文件再上传，不能直接传第三方 CDN/OSS 地址，浏览器能播放也不例外。无法读取文件的客户端使用网页上传链接。上传状态为 `ready` 后使用返回的 `reference.url`，不要使用 PUT 地址；来源已确认的当前环境 Loova 素材可复用。

MCP 新任务发现外部地址时返回 `REFERENCE_UPLOAD_REQUIRED`，不建单、不扣费，Agent 应先上传而非反复重试、充值或重新授权。视频复刻的视频、全部商品图和人物图均受此限制。校验复用当前环境的存储配置，不硬编码生产域名；已接受任务仍可使用原 UUID 和完整请求恢复。发布时先更新 MCP 说明及 skills，再部署主后端的地址校验。

动作模仿与广告复刻调用专用工具。Unlimited 按实时资格报价，不自动回退 Credits。

模型目录展示所有已启用且 MCP 支持的模型，不代表当前账号拥有使用权限。报价与创建时校验权限；`PLAN_REQUIRED` 展示后端返回的套餐入口，`INSUFFICIENT_CREDITS` 展示积分单购入口。链接随环境配置生成，Agent 不猜测地址，也不通过重新授权解决购买问题。用户购买后说“继续”，Agent 重新查询账号并报价，再按当前推进模式处理，不自动购买或回放任务。

### 生成推进模式（2.1.4）

首次生成前选择一次，当前会话内同一 Loova 账号和连接跨 Skill 共用，可随时切换：

- **自动推进**：后续用户要求的任务仍实时查询报价，但不重复确认扣费，不预设积分上限，也不因报价变化再次询问。
- **每次确认**：每次生成前展示模型、参数和扣费信息，得到确认后提交。

新会话、切换账号或无法确定原选择时重新选择；普通“确认”、登录或上传不等于开启自动推进。自动推进不授权额外任务、自动购买或循环付费重试，视频复刻仍需审核完整脚本。余额不足后，用户购买并要求继续，同账号的自动模式无需再确认扣费。任务提交后照常打开卡片并交由卡片轮询。

这是 Agent 层的会话约定，不新增后端模式参数或账号级开关。报价的 `confirmation_required: true` 表示需要授权，自动模式的明确选择已满足扣费授权；后端鉴权、扣费、幂等及宿主自身的工具调用审批保持不变。

## 更新与卸载

本地市场先 `git pull --ff-only`，再使用客户端插件管理界面更新 Loova；远程市场使用客户端的市场刷新与插件更新入口。单独 Skills 更新重新运行安装器并加 `--update`。

### 切换授权账号

2.1.4 的执行流程会在重新授权后优先使用宿主支持的连接刷新和工具发现能力，再实时查询账号、Credits 和模型。必须核对目标账号，不能根据旧聊天里的余额判断切换成功，也不默认要求重启整个应用。

连接刷新由宿主提供，Skills 本身不能替换桌面应用的 OAuth 事件处理器。浏览器授权完成后若仍选中旧账号，需要在同一个宿主连接中切换账号；单独运行 CLI 登录不会保证刷新桌面插件。宿主没有开放刷新能力时，Agent 应明确说明限制，并给出该客户端支持的最小操作。

插件卸载使用客户端插件管理界面。独立 Skills 卸载只移除本次安装的 10 个 `loova-*` 目录（名称见上表），不要删除整个 Skills 目录。卸载文件不等于撤销 OAuth；停止授权可在 Loova 账户 Connected agents 撤销对应连接。

## 维护与验证

```bash
python3 -m unittest discover -s tests -v
bash -n scripts/install.sh
claude plugin validate plugins/loova
```

本包合并产品英文 1.0 与工程插件方案，统一为 2.1.4。`quality/acceptance-cases.json` 是待执行的创作行为验收案例，不是已通过的付费生成测试。发布前检查仓库内容，保持三个插件清单与市场版本一致；更新版本时同步 Skill 元数据及 `catalog.json`。

旧 `loova-viral-video-remake` 已改为 `loova-viral-video-clone`。已手动安装旧名称的用户，应先将旧目录备份到 Skills 搜索目录外，再移除旧安装并安装新名称，避免重复发现。安装器不会自动删除旧名称或用户自定义内容。

## 构建官网下载包

```bash
python3 scripts/build_release.py
```

输出 `dist/loova-creative-skills-2.1.4/` 网站目录与 `dist/loova-creative-skills-2.1.4-deploy.zip`。网站目录包含完整包、10 个独立包、英文目录、文件清单和 SHA256。插件与 ZIP 都从 `plugins/loova/skills` 读取内容，不维护第二套 Skills。

执行约定为支持独立安装而放在每个 Skill 内；修改时同步全部副本，构建会检查一致性。构建拒绝覆盖已有发布目录，重复检查可用 `--output /path/to/empty-output`。官网部署步骤见 [DEPLOYMENT.md](docs/DEPLOYMENT.md)。

格式依据：[OpenAI 插件文档](https://developers.openai.com/plugins/build/plugins)、[Claude Code 插件文档](https://code.claude.com/docs/en/plugins-reference)。本地检查不替代各客户端真实安装和 OAuth 验收。

## 构建 OpenAI 上架上传包

```bash
python3 scripts/build_release.py --openai
```

输出 `dist/loova-openai-2.1.4.zip`，与官网 skills 分发包分开。ZIP 根目录包含 portable `plugin.json`、正式环境 `mcp.json`、现有图标及全部 10 个 skills；构建时将 Codex 清单中的 `interface` 合入 portable 清单，不包含本地市场、测试配置、凭据或 hooks。

在 OpenAI Plugins 发布后台选择 **With MCP** 上传此包。技术名称为 `loova`，须与已注册插件名称匹配；若 2.1.4 已发布，需要先同步升级仓库的版本声明。上传后的域名验证、OAuth 连接、工具与 skills 扫描、审核和发布仍在后台完成。

本次沿用仓库现有图标与 `Creativity` 分类，提交前核对后台是否提供此分类。`supportURL` 暂用包含支持 FAQ 和联系邮箱的官网首页；正式审核前建议改为独立 HTTPS 客服页面。隐私和条款分别使用 `/privacy-policy`、`/terms-of-use`。发布主体以后台已验证身份为准。

该包未伪造演示录像、审核账号或验收结果。首次 MCP 审核所需的演示录像、5 个正向与 3 个反向案例、必要的审核访问方式需要另行补齐；本地打包成功不代表已通过平台审核。
