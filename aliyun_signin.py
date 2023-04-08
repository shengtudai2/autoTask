#!/usr/bin/python3
# -- coding: utf-8 --

import json
import  requests
import  os

##变量export ali_refresh_token=''
ali_refresh_token=os.getenv("ali_refresh_token").split('&')

def daily_check(access_token):
    url = 'https://member.aliyundrive.com/v1/activity/sign_in_list'
    headers = {
        'Authorization': access_token
    }
    response = requests.post(url=url, headers=headers, json={}).text
    print(response)
    result = json.loads(response)
    if 'success' in result:
        print('签到成功')
        for i, j in enumerate(result['result']['signInLogs']):
            if j['status'] == 'miss':
                day_json = result['result']['signInLogs'][i-1]
                if not day_json['isReward']:
                    contents = '签到成功，今日未获得奖励'
                else:
                    contents = '本月累计签到{}天,今日签到获得{}{}'.format(result['result']['signInCount'],
                                                                     day_json['reward']['name'],
                                                                     day_json['reward']['description'])
                print(contents)
                return contents

# 使用refresh_token更新access_token
def update_token(refresh_token):
    url = 'https://auth.aliyundrive.com/v2/account/token'
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': ali_refresh_token[i]
    }
    response = requests.post(url=url, json=data).json()
    access_token = response['access_token']
#         print('获取的access_token为{}'.format(access_token))
    return access_token


def main(ali_refresh_token):
    access_token = update_token(ali_refresh_token)
    print(access_token)
    content = daily_check(access_token)

#签到
for i in range(len(ali_refresh_token)):
    print(f'开始帐号{i+1}签到')
    main(ali_refresh_token[i])
    
    
