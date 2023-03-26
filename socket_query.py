#!/usr/bin/env python3
# coding:utf-8
 
import socket
from datetime import datetime, timedelta, timezone
domains = [
    'alive.github.com',                                 # Github Alive
    'api.github.com',                                   # Github API
    'assets-cdn.github.com',                            # Github CDN
    'avatars.githubusercontent.com',                    # Github Avatars CDN
    'avatars0.githubusercontent.com',                   # Github Avatars CDN
    'avatars1.githubusercontent.com',                   # Github Avatars CDN
    'avatars2.githubusercontent.com',                   # Github Avatars CDN
    'avatars3.githubusercontent.com',                   # Github Avatars CDN
    'avatars4.githubusercontent.com',                   # Github Avatars CDN
    'camo.githubusercontent.com',                       # Github Camo 
    'cloud.githubusercontent.com',                      # Github Cloud
    'codeload.github.com',                              # Github Frontend Render Component Library
    'collector.github.com',                             # Github Collect
    'desktop.githubusercontent.com',                    # Github Desktop [Software]
    'favicons.githubusercontent.com',                   # Github CDN
    'gist.github.com',                                  # Github Gists
    'gist.githubusercontent.com',                       # Github Gists CDN(Raw)
    'git.io',                                           # Git.io
    'github.blog',                                      # Github Blog
    'github.com',                                       # Github Website
    'github.community',                                 # Github Community
    'github.githubassets.com',                          # Github Assets CDN
    'github.dev',                                       # Github Online Editor & CodeSpace
    'github.io',                                        # Github.io
    'githubstatus.com',                                 # Github Status
    'media.githubusercontent.com',                      # Github Media CDN
    'marketplace-screenshots.githubusercontent.com',    # Github MarketPlace Preview
    'octocaptcha.com',                                  # Github Captcha
    'pipelines.actions.githubusercontent.com',          # Github Actions
    'raw.githubusercontent.com',                        # Github Raw
    'repository-images.githubusercontent.com',          # Github Repository Images
    'uploads.github.com',                               # GIthub Release
    'user-images.githubusercontent.com',                # Github users' images
    'vscode.dev'                                        # vscode.dev - See: https://code.visualstudio.com/blogs/2021/10/20/vscode-dev
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
