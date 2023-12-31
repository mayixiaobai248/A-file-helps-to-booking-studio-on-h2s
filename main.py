#coding=utf-8
import time
import re
import requests
import datetime
import smtplib
from requests.packages import urllib3

def information():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}     #设置headers信息，模拟成浏览器取访问网站
    urllib3.disable_warnings()
    req = requests.get('https://holland2stay.com/residences.html?_=1695975305710&city=29', headers=headers, verify=False)
    #向网站发起请求，并获取响应对象
    content = req.text   #获取网站源码

    return content.count("You can book")
    # if "You can book" in content:
    #     return True
    # # pattern = re.compile('.html(.*?)</a>').findall(content)  #正则化匹配字符，根据网站源码设置 You can book
    # # return pattern  #运行information()函数，会返回pattern的值
    # else:
    #     return False

def send_email1():
    HOST = 'smtp.163.com'   # 网易邮箱smtp
    PORT = '465'
    fajianren = 'imformation_yidan@163.com'   #发送人邮箱
    shoujianren = 'ma726389@126.com'   #收件人邮箱
    title = '更新信息通知'     # 邮件标题
    # new_pattern = information()  #提取网页内容列表
    # context = new_pattern[0]  # 邮件内容
    context = "有房子啦可以去看"
    smtp = smtplib.SMTP_SSL(HOST, 465)  # 启用SSL发信, 端口一般是465
    res = smtp.login(user=fajianren, password='OXKULJMDSBBGLALK') # 登录验证，password是邮箱授权码而非密码，需要去网易邮箱手动开启
    print('发送结果：', res)
    msg = '\n'.join(
        ['From: {}'.format(fajianren), 'To: {}'.format(shoujianren), 'Subject: {}'.format(title), '', context])
    smtp.sendmail(from_addr=fajianren, to_addrs=shoujianren, msg=msg.encode('utf-8')) # 发送邮件
    print(context)

def send_email2():
    HOST = 'smtp.163.com'   # 网易邮箱smtp
    PORT = '465'
    fajianren = 'imformation_yidan@163.com'   #发送人邮箱
    shoujianren = 'ma726389@126.com'   #收件人邮箱
    title = '更新信息通知'     # 邮件标题
    # new_pattern = information()  #提取网页内容列表
    # context = new_pattern[0]  # 邮件内容
    context = "房子被订了"
    smtp = smtplib.SMTP_SSL(HOST, 465)  # 启用SSL发信, 端口一般是465
    res = smtp.login(user=fajianren, password='OXKULJMDSBBGLALK') # 登录验证，password是邮箱授权码而非密码，需要去网易邮箱手动开启
    print('发送结果：', res)
    msg = '\n'.join(
        ['From: {}'.format(fajianren), 'To: {}'.format(shoujianren), 'Subject: {}'.format(title), '', context])
    smtp.sendmail(from_addr=fajianren, to_addrs=shoujianren, msg=msg.encode('utf-8')) # 发送邮件
    print(context)

def update():
    print('通知系统启动中')
    old_pattern = 0 #记录原始内容列表
    while True:
        new_pattern = information()  #记录新内容列表
        if (new_pattern != old_pattern):  #判断内容列表是否更新
            if new_pattern>old_pattern:  #新增了房子
                send_email1()  # 发送邮件
            if new_pattern<old_pattern: #减少了房子，房子被订了
                send_email2()  # 发送邮件
            old_pattern=new_pattern    #原始内容列表改变
            print("有更新")
            #print(new_pattern)
        else:
            now=datetime.datetime.now()
            print(now,"尚无更新")
        time.sleep(10)

if __name__ == '__main__':
    update()