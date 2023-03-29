#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : shengtudai
@Date : 2023-03-23 10:00
@Description: UPVPS签到脚本
@filename : upvps_signin.py
"""

import argparse
import requests
from bs4 import BeautifulSoup
from utils.notify import private_notice


class UPVPS:
    def __init__(self, user, pwd):
        self.session = requests.session()
        self.url = "https://idc.upvps.co/"
        self.usr = user
        self.pwd = pwd

    def login_page(self):
        log_url = self.url + 'login'
        try:
            log_page = self.session.get(log_url).text
            soup = BeautifulSoup(log_page, 'lxml')
            token = soup.find(attrs={"name": "token"}).get("value")
            status = 0
        except Exception as e:
            print(e)
            token = ""
            status = 1
        return token, status

    def Sign(self, token, status):
        url = self.url + "login?action=email"
        if status == 1:
            res = "访问登陆页面失败"
        if status == 0:
            data = {
                "token": token,
                "email": self.usr,
                "password": self.pwd
            }
            try:
                res = self.session.post(url=self.url, data=data).text
            except Exception:
                res = "尝试登陆时发生网络错误"
                status = 3
        return res, status

    def Checkin(self, status):
        if status != 0:
            res = status
        else:
            url = self.url + "addons?_plugin=19&_controller=index&_action=index"
            data = {
                "uid": "260"
            }
            try:
                r = self.session.post(url, data=data)
                res = r.json()["msg"]
            except Exception as e:
                res = e
        return res

    def run(self):
        token, status = self.login_page()
        res, status = self.Sign(token, status)
        r = self.Checkin(status)
        return r


def main(user, pwd, nty_url, qq):
    upvps = UPVPS(user=user, pwd=pwd)
    res = upvps.run()
    print(res)
    private_notice(msg=res, url=nty_url, qq=qq)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UPVPS自动签到脚本")
    parser.add_argument("--user", type=str, help="UPVPS账号邮箱", required=True)
    parser.add_argument("--pwd", type=str, help="UPVPS账号密码", required=True)
    parser.add_argument("--nty_url", type=str, help="通知服务URL", required=True)
    parser.add_argument("--qq", type=str, help="QQ号", required=True)
    args = parser.parse_args()
    main(args.user, args.pwd, args.nty_url, args.qq)
