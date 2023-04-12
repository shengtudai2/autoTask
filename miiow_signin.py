import requests
import datetime
import os
from utils.notify import private_notice

now_utc = datetime.datetime.utcnow()

# 获取当前北京时间（GMT+8）
beijing_time = now_utc + datetime.timedelta(hours=8)

# 格式化时间为 "YYYY-MM-DD" 格式
beijing_date = beijing_time.date().strftime('%Y-%m-%d')

pwd = os.environ['API_PWD']
nty_url = os.environ["NOTIFY"]
qq = os.environ["QQ"]


tokens = requests.get(f'http://47.100.47.189:10010/get_token/?pwd={pwd}').json()['access_token']
jfs = []
msgs = []
for token in tokens:
    url = 'https://shopapp.miiow.com.cn/buyer/members/sign?time=' + beijing_date
    headers = {
        'accessToken': token
    }
    a = requests.post(url, headers=headers)
    jf = requests.get("https://shopapp.miiow.com.cn/buyer/member/memberPointsHistory/getMemberPointsHistoryVO", headers=headers).json()["result"]["allPoint"]
    jfs.append(jf)
    msgs.append(a.json()['message'])
        
msg = "【猫人签到】\n"
for _ in range(len(msgs)):
    msg += f"账号{_ + 1}---{msgs[_]}---{jfs[_]}分\n"
private_notice(msg=msg, url=nty_url, qq=qq)
