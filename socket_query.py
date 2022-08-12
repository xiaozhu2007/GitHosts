#!/usr/bin/env python3
# coding:utf-8
 
import socket
from datetime import datetime, timedelta, timezone
domains = [
    'api.github.com',                          # Github API
    'assets-cdn.github.com',                   # Github CDN
    'avatars.githubusercontent.com',           # Github 头像CDN
    'avatars0.githubusercontent.com',          # Github 头像CDN
    'camo.githubusercontent.com',              # Github Camo 服务 
    'cloud.githubusercontent.com',             # Github 储存桶
    'codeload.github.com',                     # Github 前端渲染组件库
    'favicons.githubusercontent.com',          # Github 图标等资源
    'gist.github.com',                         # Github Gists
    'gist.githubusercontent.com',              # Github Gists CDN(Raw)
    'github.com',                              # Github 源站
    'github.githubassets.com',                 # Github Assets
    'marketplace-screenshots.githubusercontent.com',
    'octocaptcha.com',                         # 用途包括但不限于: 创建用户、组织、重设密码、验证真人时的验证码
    'xiaozhu2007.github.io',                   # Github.io子域名
    'raw.githubusercontent.com',               # Github Raw
    'repository-images.githubusercontent.com', # Github 仓库缩略图
    'uploads.github.com',                      # 用途包括但不限于: Release附件上传
    'git.io',                                  # 用途包括但不限于: Git.io短链接
    'user-images.githubusercontent.com',       # Github 用户上传的图片
    'github.blog',                             # Github Blog
]

def gen_host():
    for domain in domains:
        print('Querying ip for domain %s'%domain)
        ip = socket.gethostbyname(domain)
        print(ip)
        yield (ip, domain)
        
def get_now_date_str(format_string="%Y-%m-%d %H:%M:%S"):#"%Y-%m-%d %H:%M:%S"
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    str_date = bj_dt.strftime(format_string)
    return str_date

def output_hosts():
    with open('hosts.txt', 'w') as f:
        f.write('```\n')
        f.write('# GitHosts Start \n')
        f.write('# Last update at %s (UTC+8)\n'%(get_now_date_str()))
        for ip, domain in gen_host():
            f.write('%s %s\n'%(ip, domain))
        f.write('# GitHosts End \n')
        f.write('```\n')
if __name__ == '__main__':
    output_hosts()
