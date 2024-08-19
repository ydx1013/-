# -*- coding: utf-8 -*-
import requests
import io
import sys
# 改变标准输出的默认编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
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
  # 将 response.text 从 Unicode 转换为 UTF-8 编码的字符串
  response_text_utf8 = response.text.encode('utf-8').decode('unicode-escape')
  
  print(response_text_utf8)
