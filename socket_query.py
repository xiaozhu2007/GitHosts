#!/usr/bin/env python3
# coding:utf-8
 
import socket
from datetime import datetime, timedelta, timezone
domains = [
    'api.github.com',                                   # Github API
    'assets-cdn.github.com',                            # Github CDN
    'avatars.githubusercontent.com',                    # Github Avatars CDN
    'avatars0.githubusercontent.com',                   # Github Avatars CDN
    'camo.githubusercontent.com',                       # Github Camo 
    'cloud.githubusercontent.com',                      # Github 储存桶
    'codeload.github.com',                              # Github 前端渲染组件库
    'favicons.githubusercontent.com',                   # Github CDN
    'gist.github.com',                                  # Github Gists
    'gist.githubusercontent.com',                       # Github Gists CDN(Raw)
    'github.blog',                                      # Github Blog
    'github.com',                                       # Github Website
    'github.githubassets.com',                          # Github Assets
    'github.dev',                                       # Github Online Editor (Like VSCode)
    'marketplace-screenshots.githubusercontent.com',    # Github MarketPlace Preview
    'octocaptcha.com',                                  # 创建用户、组织、重设密码、验证真人时的验证码
    'xiaozhu2007.github.io',                            # Github.io
    'raw.githubusercontent.com',                        # Github Raw
    'repository-images.githubusercontent.com',          # Github Repository Images
    'uploads.github.com',                               # Release
    'git.io',                                           # Git.io
    'user-images.githubusercontent.com'                 # Github users' images
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
