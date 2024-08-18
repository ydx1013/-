import requests
import ddddocr
import requests
from datetime import datetime, timedelta
import time

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
    data = {
    'wechatId': '',
    'userName': '18300911968',
    'password': 'uhl1DMPglHjqj3nhb/dPTQ==',
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
    return lims_login, lims_account_info
def main():
    next_day = datetime.now() + timedelta(days=1)
    begin_time = next_day.replace(hour=14, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M')
    end_time = next_day.replace(hour=15, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M')
    print(f"预定时间段：{begin_time} - {end_time}")
    data = {
        'instrumentId': '1725',
        'beginTime': begin_time,
        'endTime': end_time,
        'remarks': '',
        'openRemind': 'false',
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
    # 等待直到进入目标时间段
    while datetime.now() < start_time:
        time.sleep(0.1)  # 短暂休眠，避免过多的CPU使用
    while start_time <= datetime.now() <= end_time:
        # 发送POST请求
        print("开始预定WB仪器")
        response = requests.post('https://www.zkshare.com/account/appointment/book', 
                                 cookies=cookies, headers=headers, data=data)
        print(response.text)
        time.sleep(0.2)




main()







