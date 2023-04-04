import requests
import datetime
import os

now_utc = datetime.datetime.utcnow()

# 获取当前北京时间（GMT+8）
beijing_time = now_utc + datetime.timedelta(hours=8)

# 格式化时间为 "YYYY-MM-DD" 格式
beijing_date = beijing_time.date().strftime('%Y-%m-%d')

pwd = os.environ['API_PWD']

token = requests.get(f'http://47.100.47.189:10010/get_token/?pwd={pwd}').json()['access_token']

url = 'https://shopapp.miiow.com.cn/buyer/members/sign?time=' + beijing_date

headers = {
    'accessToken': token
}

a = requests.post(url, headers=headers)
msg = a.json()['message']
print(msg)
