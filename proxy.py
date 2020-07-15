#!/usr/bin/env python3
# encoding: utf-8
"""
proxy.py

Author: Jane
Date: 20200606
Description: 使用tor代理ip测试
"""
import os
import requests
import time

ips = []
url = 'https://api.ipify.org?format=json'
# url = 'http://msydqstlz2kzerdg.onion'


# 获取ip请求
def getip_request(url):
    print('(+) 发送获取ip地址请求......')
    ip = requests.get(url).text
    print('(+) 现在的IP是：%s' % format(ip))


# 测试代理并输出代理ip
def test_tor_new_ip(url):
    print('(+) 正在测试新的ip地址......')
    proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
    ip = requests.get(url, proxies=proxies).text
    if ip not in ips:
        ips.append(ip)
    print('(+) 现在的IP是：%s' % format(ip))


# 重启tor服务
def restart_tor_service():
    print('(+) 正在重新获取代理ip......')
    os.system(command='systemctl restart tor')
    time.sleep(10)
    test_tor_new_ip(url)


if __name__ == "__main__":
    # print("开始测试获取ip是否正常...")
    # getip_request(url)
    # while len(ips) < 10:
    #     restart_tor_service()
    # print(ips)
    import json
    aa = ['{"ip":"185.220.101.6"}', '{"ip":"109.70.100.35"}', '{"ip":"185.220.101.12"}', '{"ip":"185.220.101.207"}', '{"ip":"109.70.100.26"}', '{"ip":"51.75.144.43"}', '{"ip":"185.220.102.4"}', '{"ip":"66.146.193.33"}', '{"ip":"51.38.52.191"}', '{"ip":"195.154.179.3"}']
    bb = []
    for item in aa:
        item_dict = json.loads(item)
        bb.append(item_dict.get('ip'))
    print(bb)