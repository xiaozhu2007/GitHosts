<h1 align="center">GitHosts</h1>

<p align="center">
    <br />
    <strong>The world's #3 hosts collection!</strong>
</p>

<p align="center">
    <a href="https://github.com/xiaozhu2007/GitHosts/releases/"><img src="https://img.shields.io/github/release/xiaozhu2007/GitHosts.svg?style=flat-square" alt="GitHub release"></a>
    <a href="https://github.com/xiaozhu2007/GitHosts/releases/"><img src="https://img.shields.io/github/downloads/xiaozhu2007/GitHosts/total.svg?style=flat-square" alt="GitHub release"></a>
    <a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"></a>
</p>

## 前言  
因为域名被DNS污染，GitHub被`不可告人的秘密`了，遂有了这个工程

## 广而告之  
现在主流浏览器基本上都支持DNS-Over-HTTPS，很大程度上可以替代本项目
你可以根据实际情况进行选择

## 功能  
利用GitHub Action进行相关网站的DNS查询, 将得到的结果发布到Issue页面和Release附件
+ 支持周期性自动发布
    + 每月1~30号发布issue
+ 支持API推送更新
    + 试一试：<https://www.example.com/api>
+ 支持自动回复  
    + 如果想查询最新的Hosts，可以自己开个Issue，机器人会自动回复
    + 举例[issue #1](https://github.com/xiaozhu2007/GitHosts/issues/1)
+ 支持通过http链接获取Hosts文件  
    + 你可以通过以下的地址获取附件中的Hosts文件
        + Github源地址:   <https://github.com/xiaozhu2007/GitHosts/releases/download/v2/host.txt>
        + Github镜像: <https://hub.fastgit.xyz/xiaozhu2007/GitHosts/releases/download/v2/host.txt>
    + Host文件将由Github Actions机器人每天定时刷新，当有Issue提交时也会触发构建


## SwitchHosts部署

- 下载打开[SwitchHosts]
- 单击左上角的“添加Hosts”
- 选择“远程”
- “Hosts 标题” 填写 `GitHosts`
- “URL” 填写 上方的Github镜像地址
- “自动刷新” 填写 `15分钟`
- 单击“完成”

## 注意事项
+ 请移步[Issue]页面 
+ 更改Hosts后，注意使用`ipconfig /flushdns`刷新DNS缓存



[SwitchHosts]:https://swh.app/zh/
[Issue]:https://github.com/xiaozhu2007/GitHosts/issues/
