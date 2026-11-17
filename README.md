<div align="center"> 
<h1 align="center">贴吧签到助手</h1>
<img src="https://img.shields.io/github/issues/LuoSue/TiebaSignIn-1?color=green">
<img src="https://img.shields.io/github/stars/LuoSue/TiebaSignIn-1?color=yellow">
<img src="https://img.shields.io/github/forks/LuoSue/TiebaSignIn-1?color=orange">
<img src="https://img.shields.io/github/license/LuoSue/TiebaSignIn-1?color=ff69b4">
<img src="https://img.shields.io/github/languages/code-size/LuoSue/TiebaSignIn-1?color=blueviolet">
</div>

# 简介

用的是手机端的接口，签到经验更多，用户只需要填写`BDUSS`即可，使用Github Actions自动签到。

# 功能

+ 贴吧自动签到
+ 签到结果通过 MeoW 推送到手机

# 使用方法

## 1.fork本项目
### 必须检查的仓库设置

1. 确保 `Settings -> Actions -> General` 中 Actions 处于启用状态。`tieba.yml` 中的 `workflow-keepalive` job 已配置 `actions: write` 权限，无需授予仓库 `Read and write permissions`。

2. 确保仓库没有被 Archived（Settings -> General -> Danger Zone: Archive repository）。

## 2.获取BDUSS

在网页中登录上贴吧，然后按下`F12`打开调试模式，在`cookie`中找到`BDUSS`，并复制其`Value`值。

![](./assets/获取BDUSS.gif)

## 3.将BDUSS添加到仓库的Secrets中

Name | Value
-|-
BDUSS | xxxxxxxxxxx

将上一步骤获取到的`BDUSS`粘贴到`Secrets`中

![](./assets/添加BDUSS.gif)

## 4.配置手机推送

Name | Value
-|-
MEOW_PUSH_URL | 完整的 MeoW HTTPS 推送地址，例如 `https://api.chuckfang.com/你的昵称/`

在你 fork 的仓库 Settings → Secrets and variables → Actions → New repository secret 中添加。推送地址属于私人配置，请勿写进公开源码。

接口格式与更多参数请参考 [MeoW API 文档](https://www.chuckfang.com/MeoW/api_doc.html)。未配置 `MEOW_PUSH_URL` 时会跳过手机推送，不影响签到流程。

## 5.开启actions

默认`actions`是处于禁止的状态，需要手动开启。

![](./assets/开启actions.gif)

## 6.第一次运行 Actions

进入仓库的 `Actions` 页面，选择 `Daily Tieba Sign-In`，点击 `Run workflow` 手动运行一次。

当前工作流只响应手动运行和每日定时任务，普通 `push` 不会触发签到。

![](./assets/运行结果.gif)

## 成功了

每天早上6:30将会自动进行签到。如果配置了 `MEOW_PUSH_URL`，签到结果会通过 MeoW 推送到手机。tieba.yml 中的 workflow-keepalive job 会自动保持该定时工作流处于启用状态。

## 2026-11-17

+ 默认推送方式由企业微信群机器人改为 MeoW 手机推送

## 2026-9-11

+ 增加了推送签到结果到企业微信群机器人功能

## 2026-5-30

+ 代码重构

+ 修改 API 以及签到策略

## 2020-11-01

+ 代码重构

+ 修改签到策略

大大提高一次运行，贴吧签到的成功率，基本很少的贴吧会签到失败。

+ 去除多用户的支持

+ 增加支持server酱推送，可以推送至微信

## 2020-10-19

~~增加支持多账户签到，每个账号的`BDUSS`使用`&&`分割，具体格式如下。~~
