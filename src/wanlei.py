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
  
  
  response = requests.post('https://appapi.biodog.cn//Center/Sign', cookies=cookies, headers=headers)
  # 将 response.text 从 Unicode 转换为 UTF-8 编码的字符串
  response_text_utf8 = response.text.encode('utf-8').decode('unicode-escape')
  print(response_text_utf8)
