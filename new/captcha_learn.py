# -*- encoding: utf-8 -*-
# 1.获取验证码并将验证码保存到图片
# 2.识别图片保存的验证码

import requests
import os
import base64
from PIL import Image


def downloads_pic(**kwargs):
    url = 'http://54.183.77.249/api/auth/askRegister'
    headers = {
        'Accept': 'application / json, text / plain, * / *',
        'Accept - Encoding': 'gzip, deflate Accept - Language:zh - CN, zh;q = 0.9 Cache - Control:no - cache',
        'Connection': 'keep - alive',
        'Host': '54.183.77.249',
        'Origin': 'http://new.rightbtc.net',
        'Pragma': 'no-cache',
        'Referer': 'http://new.rightbtc.net/zh_cn/register',
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    res = requests.post(url, headers, **kwargs)
    rep = res.json()
    print rep
    str = (rep['result']['parameter'])[22:]
    print str
    return str

def cycle_getImage(i):
    # 获取 i 张验证码图片
    for each in range(i):
        str = downloads_pic()
        imgdata = base64.b64decode(str)
        file = open('%d.jpg' % (each + 1), 'wb')
        file.write(imgdata)
        file.close()

def changebin(pic):
    image = Image.open(pic)
    image.save('12.jpg')
    imgry = image.convert('L')
    table = get_bin_table()
    out = imgry.point(table, '1')

def get_bin_table(threshold=140):
    """
    获取灰度转二值的映射table
    :param threshold:
    :return:
    """
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table

if __name__ == '__main__':
    i = 1
    cycle_getImage(i)
    pic = '%d.jpg' % (i)
    changebin(pic)