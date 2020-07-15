#!/usr/bin/env python3
# encoding: utf-8
"""
screen.py

Author: Jane
Date: 20200609
Description: 测试自动截图
"""
import sys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def main():
    url = "https://www.cnblogs.com/ywheunji/p/12246433.html"

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get(url)
    driver.save_screenshot('ww.png')
    driver.close()
    driver.quit()


if __name__ == "__main__":
    import time
    print("start: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    main()
    print("end: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))