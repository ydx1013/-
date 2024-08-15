import requests
from datetime import datetime, timedelta
import time

# 获取当日日期，加上一天
next_day = datetime.now() + timedelta(days=1)
begin_time = next_day.replace(hour=14, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M')
end_time = next_day.replace(hour=15, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M')
data = {
    'instrumentId': '1725',
    'beginTime': begin_time,
    'endTime': end_time,
    'remarks': '',
    'openRemind': 'false',
    'codeId': '',
    'goods': '',
}


cookies = {
    'lims_account_info': '%7B%22RealName%22%3A%22%E5%B2%B3%E4%B8%9C%E6%97%AD%22%2C%22Cellphone%22%3A%2218300911968%22%2C%22UnionBalance%22%3A0.00%2C%22Integral%22%3A0%2C%22HeadImageUrl%22%3Anull%2C%22Email%22%3A%225064072%40qq.com%22%2C%22UserName%22%3A%22drffffvh%22%2C%22BelongLabId%22%3A11%2C%22StoreId%22%3A0%2C%22CartCount%22%3A0%2C%22JunIntegral%22%3A0%7D',
    'scigrace_lims_lab_id': '11',
    'lims_login': 'CfDJ8LNuycGXh3pHv5h7pohgNvnEKWOrMxYGOX20OAQj64Nj9Xi-pnnU3ukXfXk7c5p3yNqCOm4DYc6PjD5fxWfpHMNBlqSph6CbOf-R-jTLNfYULG8F9ZEAS6lcPOjApfKM1P9eoKV0Wfbz88R0hP4SqBoEDBS4hZi7yB162pmt-WCzQoYlpdqUmDeFr5R_k536yHOac3sSjMLhHwcZl0oBidkLlj4AObaGJVIRaOdg5ByU2kpEa-RBjE2GOXs5UCRtNospb3pUKpqE8VRfkoffjHBVCwzbhbWS65s9LMvImPxPdhKjjEQs1lxIHuSRwsamuw',
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
    'Referer': 'https://www.zkshare.com/wechat/instrument/detail?id=1257',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Cookie': 'lims_account_info=%7B%22RealName%22%3A%22%E5%B2%B3%E4%B8%9C%E6%97%AD%22%2C%22Cellphone%22%3A%2218300911968%22%2C%22UnionBalance%22%3A0.00%2C%22Integral%22%3A0%2C%22HeadImageUrl%22%3Anull%2C%22Email%22%3A%225064072%40qq.com%22%2C%22UserName%22%3A%22drffffvh%22%2C%22BelongLabId%22%3A11%2C%22StoreId%22%3A0%2C%22CartCount%22%3A0%2C%22JunIntegral%22%3A0%7D; lims_login=CfDJ8LNuycGXh3pHv5h7pohgNvnglqO7i8rESjZbZ1V9QT37vru3POsTEiulWg6JjGyyGDUJXeOQcl02j3shvBizA0GhR8_FJ9C4u2qAgLtcTZzLn5jAb18nRt2pcK1G-EvXYcO1U6OmoVBmwWSSn6kRn7T4aTzlEwKQWBaXjzRWhxTIMcL3KO9UNs3gpi13qu8aEeFIdNSp-n3REu27HAFlHBCzbLBOu2x1ryIxXHxrAvzXyxRrVt_xCbzP77oCgwNuI7oa2vOuhTLGM_v_VL4rpLBEpCSL1sii_5NfIb6UJPa_MLoJqD1hGAnCCT7Uhk6AJw',
}


# 获取当前时间
current_time = datetime.now()

# 设定目标时间段
start_time = current_time.replace(hour=8, minute=59, second=59, microsecond=0)
end_time = start_time + timedelta(seconds=2)  # 结束时间为 start_time 多 3 秒

# 等待直到进入目标时间段
while datetime.now() < start_time:
    print("休眠中\n")
    time.sleep(0.1)  # 短暂休眠，避免过多的CPU使用

while start_time <= datetime.now() <= end_time:
    # 发送POST请求
    print("开始预定WB仪器")
    response = requests.post('https://www.zkshare.com/account/appointment/book', cookies=cookies, headers=headers, data=data)
    time.sleep(0.2)
