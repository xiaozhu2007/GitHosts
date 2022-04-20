#!/usr/bin/env python
# coding:utf-8
 
import socket
from datetime import datetime, timedelta, timezone
domains = [
    'api.github.com',                         # Github API
    'assets-cdn.github.com',               # Github CDN
    'avatars.githubusercontent.com',
    'avatars0.githubusercontent.com',
    'camo.githubusercontent.com',                         # Github Camo 服务 
    'cloud.githubusercontent.com',
    'codeload.github.com',
    'favicons.githubusercontent.com',
    'gist.github.com',
    'gist.githubusercontent.com',
    'github.com',                              # 网站本体
    'github.githubassets.com',
    'marketplace-screenshots.githubusercontent.com',
    'octocaptcha.com',                                      # 用途包括但不限于: 创建用户、组织、重设密码、验证真人时的验证码
    'xiaozhu2007.github.io',                              # Github.io子域名
    'raw.githubusercontent.com',
    'repository-images.githubusercontent.com',
    'uploads.github.com',                                   # 用途包括但不限于: Release附件上传
    'git.io',                                   # 用途包括但不限于: Git.io短链接
    'allcontributors.org',                                   # 用途包括: All Contributors . org
    'user-images.githubusercontent.com',
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
        f.write('# Last update at %s (Beijing Time)\n'%(get_now_date_str()))
        for ip, domain in gen_host():
            f.write('%s %s\n'%(ip, domain))
        f.write('# GitHosts End \n')
        f.write('```\n')
if __name__ == '__main__':
    output_hosts()
