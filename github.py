#!/usr/bin/env python3
# coding:utf-8
import os
import requests,json
from datetime import datetime, timedelta, timezone
import socket_query

class GithubHelper:
    
    def __init__(self, owner, repo, auth, bot_auth, **args):
        self.auth = auth
        self.bot_auth = bot_auth
        self.owner = owner
        self.repo = repo
        
    def getLatestRelease(self, **args):
        url = 'https://api.github.com/repos/%s/%s/releases/latest'%(self.owner, self.repo)
        headers = {'User-Agent': 'None', 'Accept': 'application/vnd.github.v3.+json', "Authorization": "token "+ self.auth}
        res = requests.get(url, headers=headers).json()
        #print(res)
        return res
    
                
    def updateReleaseBody(self, release_id, body, **args):
        url = 'https://api.github.com/repos/%s/%s/releases/%d'%(self.owner, self.repo, release_id)
        headers = {'User-Agent': 'None', 'Accept': 'application/vnd.github.v3.+json', "Authorization": "token "+ self.auth}
        param = {
            "body": body
        }
        res = requests.request("PATCH", url, data=json.dumps(param), headers=headers).json()
        #print(res)
        return res 
    
    def updateGistsBody(self, gists_id, body, **args):
        url = 'https://api.github.com/gists/%s'%(gists_id)
        headers = {'User-Agent': 'None', 'Accept': 'application/vnd.github.v3.+json', "Authorization": "token "+ self.bot_auth}
        param = {
            "file": "hosts.txt",
            "body": body
        }
        res = requests.request("PATCH", url, data=json.dumps(param), headers=headers).json()
        print("Gists API Res")
        print(res)
        return res 
        
    def updateReleaseAsset(self, asset_id, name, **args):
        url = 'https://api.github.com/repos/%s/%s/releases/assets/%d'%(self.owner, self.repo, asset_id)
        headers = {'User-Agent': 'None', 'Accept': 'application/vnd.github.v3.+json', "Authorization": "token "+ self.auth}
        param = '{"name":"%s"}'%name
        res = requests.request("PATCH", url, data=param, headers=headers).json()
        #print(res)
        return res    
            
    def deleteReleaseAsset(self, asset_id, **args):
        url = 'https://api.github.com/repos/%s/%s/releases/assets/%d'%(self.owner, self.repo, asset_id)
        headers = {'User-Agent': 'None', 'Accept': 'application/vnd.github.v3.+json', "Authorization": "token "+ self.auth}
        res = requests.request("DELETE", url, headers=headers)
        #print(res.text)
        return res
        
    def uploadReleaseAsset(self, release_id:int, name, data, **args):
        url = 'https://uploads.github.com/repos/%s/%s/releases/%d/assets?name=%s'%(self.owner, self.repo, release_id, name)
        headers = {'content-type': 'application/octet-stream', 'Accept': 'application/vnd.github.v3.+json', "Authorization": "token "+ self.auth}
        res = requests.request("POST", url, data=data, headers=headers).json()
        #print(res)
        return res
        
    def replaceLatestReleaseAssets(self, name, data, **args):
        if not "releaseInfo" in locals():
            releaseInfo = self.getLatestRelease()
        release_id = releaseInfo['id']
        assets = releaseInfo['assets']
        # 删除原来的附件
        for asset in assets:
            if name == asset["name"]:
                self.deleteReleaseAsset(asset['id'])
                break;
        # 上传新的附件
        return self.uploadReleaseAsset(release_id, name, data)
        
        
def get_now_date_str(format_string="%Y-%m-%d %H:%M:%S"):#"%Y-%m-%d %H:%M:%S"
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    str_date = bj_dt.strftime(format_string)
    return str_date
    
def load_from_env():
    repo_full_name = os.environ.get('MY_REPOSITORY')
    owner = os.environ.get('MY_OWNER')
    repo = repo_full_name[len(owner) + 1:]
    token = os.environ.get('MY_GITHUB_TOKEN')
    bot_token = os.environ.get('MY_TOKEN')
    github_config = {
        "repo": repo,
        "owner": owner,
        "auth": token,
        "bot_auth": bot_token
    }
    return github_config

     
if __name__ == "__main__":
    github_config = load_from_env()
    date_now = get_now_date_str()
    lines = []
    lines.append('# GitHosts Start')
    lines.append('# from https://github.com/xiaozhu2007/GitHosts')
    lines.append('# Last update at %s (Beijing Time)'%date_now)
    for ip, domain in socket_query.gen_host():
        lines.append("%s %s"%(ip, domain))
    lines.append('# GitHosts End')
    data = '\n'.join(lines)
    
    helper = GithubHelper(**github_config)    
    release_info = helper.getLatestRelease()   
    result = helper.replaceLatestReleaseAssets(name = "host.txt", data = data, release_info=release_info)
    print(result)
    if "id" in result:
        body = \
        """
- 你可以通过以下的地址获取附件中的 Host 文件
  - Github 源地址: <https://github.com/xiaozhu2007/GitHosts/releases/download/v2.1/host.txt>
  - Fastgit 镜像: <https://hub.fastgit.xyz/xiaozhu2007/GitHosts/releases/download/v2.1/host.txt>
- 现已支持 `SwitchHosts` 一键导入（详情见 README.md）
- Host 文件将由[机器人](https://github.com/HelloTools-bot)每天定时刷新，最后更新于(北京时间)：
        """
        body += date_now
        body = body.strip()
        helper.updateReleaseBody(release_id = release_info["id"], body=body)

