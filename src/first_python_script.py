# -*- coding: utf-8 -*-
import requests
import ddddocr
import requests
import sys
import io
import wanlei
wanlei.wanlei()

# 改变标准输出的默认编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from datetime import datetime, timedelta
import time
import os
# 使用环境变量替换硬编码的用户名和密码
USER_NAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
instrumentId = os.getenv('instrumentId')
print(USER_NAME,PASSWORD,instrumentId)

def get_capcha():
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Origin': 'https://www.zkshare.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'Referer': 'https://www.zkshare.com/account/login?returnurl=%2Fwechat%2Finstrument%2Fdetail%3Fid%3D1740%26t%3D1723948265677%26t%3D1723948559662',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    }

    captcha_img = "https://www.zkshare.com/Account/SecurityCode?codeid=5d66d9b9-db24-cbec-25fd-5028a070cd92"
    if captcha_img:
        captcha_url = captcha_img
        # 下载验证码图片
        captcha_response = requests.get(captcha_url, headers=headers)
        with open('captcha.jpg', 'wb') as f:
            f.write(captcha_response.content)

def capcha_define():
    get_capcha()
    ocr = ddddocr.DdddOcr(show_ad=False)
    image = open("./captcha.jpg", "rb").read()
    result = ocr.classification(image)
    print(result)
    return result
def get_cookie():
    i = 0
    data = {
    'wechatId': '',
    'userName': USER_NAME,
    'password': PASSWORD,
    'code': capcha_define(),
    'freeLogin': 'true',
    'codeId': '5d66d9b9-db24-cbec-25fd-5028a070cd92',
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Sec-Fetch-Mode': 'cors',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Origin': 'https://www.zkshare.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'Referer': 'https://www.zkshare.com/account/login?returnurl=%2Fwechat%2Finstrument%2Fdetail%3Fid%3D1740%26t%3D1723948265677%26t%3D1723948559662',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
    }
    response = requests.post('https://www.zkshare.com/account/Loginnow', headers=headers, data=data)
    # 获取特定的 cookie 值
    lims_account_info = response.cookies.get('lims_account_info')
    lims_login = response.cookies.get('lims_login')
    i = 0
    while lims_login is None and i < 3:  # 使用 is None 和 < 比较
        i += 1  # 使用 i += 1 来递增 i
        print("验证码错误，重新获取")
        lims_login, lims_account_info = get_cookie()
    print(lims_login)
    return lims_login, lims_account_info
def main():
    next_day = datetime.now() + timedelta(days=1)
    begin_time = next_day.replace(hour=14, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M')
    end_time = next_day.replace(hour=15, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M')
    print(f"预定时间段：{begin_time} - {end_time}")
    data = {
        'instrumentId': "1725", #instrumentId
        'beginTime': begin_time,
        'endTime': end_time,
        'remarks': '',
        'openRemind': 'true',
        'codeId': '',
        'goods': '',
    }
    lims_login, lims_account_info = get_cookie()

    cookies = {
        'lims_account_info': lims_account_info,
        'lims_login': lims_login,
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Sec-Fetch-Mode': 'cors',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Origin': 'https://www.zkshare.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'Referer': 'https://www.zkshare.com/wechat/instrument/detail?id=1740&t=1723948265677&t=1723948559662',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
    }

    # 获取当前时间
    current_time = datetime.now()
    # 设定目标时间段
    start_time = current_time.replace(hour=0, minute=59, second=59, microsecond=0)
    end_time = start_time + timedelta(seconds=2)  # 结束时间为 start_time 多 3 秒
    print("开始运行时间是：",start_time.hour),print("当前时间是：",current_time.hour)
    if start_time.hour != current_time.hour:
        sys.exit()  # 停止运行
    # 等待直到进入目标时间段
    while datetime.now() < start_time:
        time.sleep(0.1)  # 短暂休眠，避免过多的CPU使用
    while start_time <= datetime.now() <= end_time:
        # 发送POST请求
        print("开始预定WB仪器")
        response = requests.post('https://www.zkshare.com/account/appointment/book', 
                                 cookies=cookies, headers=headers, data=data)
        time.sleep(0.2)
        decoded_content = response.content.decode('utf-8')
        print(decoded_content)
        if '"success":true' in decoded_content:
            print("预定成功")
            break
    
main()






