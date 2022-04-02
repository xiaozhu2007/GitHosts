# GitHosts
## 前言  
因为域名被DNS污染，GitHub被GFW墙了，遂有了这个工程

## 广而告之  
现在主流浏览器基本上都支持DNS-Over-HTTPS，很大程度上可以替代本项目
你可以根据实际情况进行选择

## 功能  
利用GitHub Action进行相关网站的DNS查询, 将得到的结果发布到Issue页面和Release附件
+ 支持周期性自动发布
    + 每月1~30号发布issue
+ 支持自动回复  
    + 如果想查询最新的host，可以自己开个issue，机器人会自动回复
    + 举例[issue #1](https://github.com/xiaozhu2007/GitHosts/issues/1)
+ 支持通过http链接获取host文件  
    + 你可以通过以下的地址获取附件中的host文件
        + Github源地址:   <https://github.com/xiaozhu2007/GitHosts/releases/download/v1/host.txt>
        + Github镜像: <https://hub.fastgit.xyz/xiaozhu2007/GitHosts/releases/download/v1/host.txt>
    + Host文件将由Github Actions机器人每天定时刷新，当有issue提交时也会触发构建

## 注意事项
+ 请移步[Issue](https://github.com/xiaozhu2007/GitHosts/issues/)页面 
+ 更改Hosts后，注意使用`ipconfig /flushdns`刷新DNS缓存

