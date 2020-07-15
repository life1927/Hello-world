#!/usr/bin/env python3
# encoding: utf-8
"""
screen.py

Author: Jane
Date: 20200609
Description: 测试自动截图
"""
import sys
from urllib import parse

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def main1():
    lists = [
        {
            'bus_status': 3000,
            'status': 3
        },
        {
            'bus_status': 2000,
            'status': 0
        },
        {
            'bus_status': 2001,
            'status': 0
        },
        {
            'bus_status': 3000,
            'status': 2
        },
        {
            'bus_status': 3000,
            'status': 1
        }
    ]

    lists.sort(key=lambda x: (x["bus_status"], x["status"]))
    print(lists)


def main2():
    url = 'https://github.com/1u0Hun/SAReport/blob/0f420d6a6b48d361dd0e88625c4ab264d6a4b5a9/app/models.py'
    path = 'app/models.py'
    real_url = ''
    if url.endswith(path):
        len_real_commit = len(url) - len(path) - 1 - 40
        real_url = url[:len_real_commit] + path
        print(real_url)
    return real_url


def main3():
    a = '11111-11111111111111111111111'
    for item in a.split('-'):
        b = item.split(item[0])
        tmp = list(set(b))
        if len(tmp) == 1 and not tmp[0]:
            print('repeat')
    print()

def main4():
    a = ['jdbc:mysql://42.123.76.25:3306/terminal";', 'password = "admin"']
    b = ['password = "admin"', 'jdbc:mysql://42.123.76.25:3306/terminal";']
    if set(b) <= set(a):
        print('same')

def main5():
    a = '"pop'
    for char in ["'", '"']:
        if a.startswith(char):
            if char not in a[1:]:
                print('just start, not end')

def main():
    url = u'https://jksx.shaanxijiankangyun.com：8080:443/epidemic/index.html'
    print(parse.urlparse(url))


if __name__ == "__main__":
    import time
    print("start: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    main()
    print("end: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))