# -*- coding: utf-8 -*-
import requests
def wanlei():
  cookies = {
    'PHPSESSID': '6m8q7k25h1cjrah8c782i6id46',
  }
  headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Connection': 'keep-alive',
      'Accept': '*/*',
      'User-Agent': 'ShengWuGou/3.5.9 (iPhone; iOS 16.6; Scale/3.00)',
      'Accept-Language': 'zh-Hans-CN;q=1',
      'X-Requested-With': 'XMLHttpRequest',
  }
  
  data = {
      'MyKey': 'a3bf8ad5421091f9de92335e694b8cb0',
      'UserId': 'dd6b42f5dee5cef8383cece0d42dc056',
      'timestamp': '1724039105',
  }
  
  response = requests.post('https://appapi.biodog.cn//Center/Sign', cookies=cookies, headers=headers, data=data)
  print(response.text)
